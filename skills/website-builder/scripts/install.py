#!/usr/bin/env python3
"""Install Website Builder and pinned supporting skills; Python 3.10+, stdlib only."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tempfile
from urllib.request import Request, urlopen
import uuid
import zipfile

SKILL = Path(__file__).resolve().parents[1]
RECEIPT = ".website-builder-install.json"
AGENTS = {"codex": ".agents", "cursor": ".cursor", "claude": ".claude"}
MAX_DOWNLOAD = 64 * 1024 * 1024
MAX_EXPANDED = 256 * 1024 * 1024


class InstallError(Exception):
    """A recoverable installation failure with a user-facing explanation."""


def reject_symlink_path(path: Path) -> None:
    for part in (path, *path.parents):
        if part.is_symlink():
            raise InstallError(f"Refusing to replace or write through a symlink: {part}")


def destination_root(agent: str, scope: str, project: str | None, home: Path | None = None) -> Path:
    if scope == "project":
        if not project:
            raise InstallError("Project scope requires --project with an existing website folder.")
        base = Path(project).expanduser().resolve()
        if not base.is_dir():
            raise InstallError(f"Project folder does not exist: {base}")
    else:
        if project:
            raise InstallError("--project can only be used with --scope project.")
        base = (home or Path.home()).resolve()
    root = base / AGENTS[agent] / "skills"
    reject_symlink_path(root)
    return root


def safe_relative(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if (not value or path.is_absolute() or ".." in path.parts
            or "\\" in value or ":" in value or path == PurePosixPath(".")):
        raise InstallError(f"Unsafe archive or manifest path: {value!r}")
    return path


def load_manifest(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != 1 or not isinstance(data.get("skills"), list):
        raise InstallError("Unsupported supporting-skills manifest format.")
    names = {"website-builder"}
    for item in data["skills"]:
        name = item.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
            raise InstallError(f"Invalid or duplicate skill name: {name!r}")
        names.add(name)
        if not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", item.get("repository", "")):
            raise InstallError(f"Unsupported repository for {name}.")
        if not re.fullmatch(r"[0-9a-f]{40}", item.get("revision", "")):
            raise InstallError(f"{name} must use a full pinned commit SHA.")
        safe_relative(item["path"])
        safe_relative(item["license_path"])
        if not isinstance(item.get("default", True), bool):
            raise InstallError(f"Invalid default selection for {name}.")
        if not isinstance(item.get("requires", []), list) or not all(
                isinstance(dependency, str) for dependency in item.get("requires", [])):
            raise InstallError(f"Invalid dependencies for {name}.")
    # Validate the complete graph, including optional skills not selected this run.
    select_supporting(data["skills"], False, [item["name"] for item in data["skills"]])
    return data["skills"]


def select_supporting(entries: list[dict], defaults: bool, requested: list[str]) -> list[dict]:
    """Resolve explicit choices and their dependencies without installing every skill."""
    by_name = {item["name"]: item for item in entries}
    selected = []
    visited = set()
    visiting = set()

    def visit(name: str) -> None:
        if name not in by_name:
            raise InstallError(f"Unknown supporting skill: {name}. See supporting-skills.json for available names.")
        if name in visiting:
            raise InstallError(f"Supporting-skill dependency cycle includes {name}.")
        if name in visited:
            return
        visiting.add(name)
        for dependency in by_name[name].get("requires", []):
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
        selected.append(by_name[name])

    for name in [*(item["name"] for item in entries if defaults and item.get("default", True)), *requested]:
        visit(name)
    return selected


def ignored(directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name in {"__pycache__", ".git", RECEIPT}
            or name.endswith((".pyc", ".pyo"))}


def snapshot(folder: Path) -> dict[str, str]:
    result = {}
    for entry in sorted(folder.rglob("*")):
        if entry.is_symlink():
            raise InstallError(f"Skill contains a symlink; inspect it manually: {entry}")
        if entry.is_file():
            result[entry.relative_to(folder).as_posix()] = hashlib.sha256(entry.read_bytes()).hexdigest()
        elif not entry.is_dir():
            raise InstallError(f"Skill contains a non-regular file: {entry}")
    return result


def payload_snapshot(folder: Path) -> dict[str, str]:
    """Compare content, not our receipt or Python's generated cache files."""
    return {name: digest for name, digest in snapshot(folder).items()
            if name != RECEIPT and "__pycache__" not in PurePosixPath(name).parts
            and not name.endswith((".pyc", ".pyo"))}


def validate_skill_name(folder: Path, expected: str) -> None:
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match or not re.search(r"^name:\s*[\"']?" + re.escape(expected) + r"[\"']?\s*$", match[1], re.M):
        raise InstallError(f"SKILL.md does not declare the expected name: {expected}")


def download_skill(item: dict, destination: Path, archive_cache: dict | None = None) -> None:
    repo = item["repository"].removeprefix("https://github.com/")
    url = f"https://codeload.github.com/{repo}/zip/{item['revision']}"
    payload = archive_cache.get(url) if archive_cache is not None else None
    if payload is None:
        request = Request(url, headers={"User-Agent": "website-builder-installer/0.4"})
        with urlopen(request, timeout=60) as response:
            payload = response.read(MAX_DOWNLOAD + 1)
    if len(payload) > MAX_DOWNLOAD:
        raise InstallError(f"Archive exceeds download limit: {repo}")
    if archive_cache is not None:
        archive_cache[url] = payload
    prefix = safe_relative(item["path"])
    license_path = safe_relative(item["license_path"])
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if sum(entry.file_size for entry in archive.infolist()) > MAX_EXPANDED:
            raise InstallError(f"Archive exceeds expanded-size limit: {repo}")
        seen = set()
        roots = set()
        license_data = None
        for entry in archive.infolist():
            full = safe_relative(entry.filename.rstrip("/"))
            roots.add(full.parts[0])
            if len(roots) != 1:
                raise InstallError("Archive has more than one root directory.")
            if len(full.parts) < 2 or entry.is_dir():
                continue
            relative = PurePosixPath(*full.parts[1:])
            if relative != license_path and not relative.is_relative_to(prefix):
                continue
            file_type = stat.S_IFMT(entry.external_attr >> 16)
            if file_type not in (0, stat.S_IFREG):
                raise InstallError(f"Unsupported archive member: {entry.filename}")
            content = archive.read(entry)
            if relative == license_path:
                license_data = content
            if relative.is_relative_to(prefix):
                within = relative.relative_to(prefix)
                safe_relative(str(within))
                # Detect case-colliding names before writing on Windows/macOS.
                key = str(within).casefold()
                if key in seen:
                    raise InstallError(f"Duplicate archive path: {within}")
                seen.add(key)
                target = destination.joinpath(*within.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
        if license_data is None:
            raise InstallError(f"Upstream licence file was not found for {item['name']}.")
        if not (destination / "SKILL.md").is_file():
            raise InstallError(f"Pinned skill folder was not found for {item['name']}.")
        (destination / "UPSTREAM-LICENSE").write_bytes(license_data)
        (destination / "UPSTREAM-SOURCE.json").write_text(json.dumps(item, indent=2) + "\n", encoding="utf-8")
        validate_skill_name(destination, item["name"])


def install_tree(source: Path, target: Path, provenance: dict, update: bool, backup_root: Path) -> str:
    reject_symlink_path(target)
    reject_symlink_path(backup_root)
    snapshot(source)  # Reject links before copying, including links outside the source tree.
    validate_skill_name(source, target.name)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".website-builder-stage-", dir=target.parent.parent) as temporary:
        staged = Path(temporary) / target.name
        shutil.copytree(source, staged, ignore=ignored)
        receipt = {"schema": 1, "source": provenance, "files": snapshot(staged)}
        (staged / RECEIPT).write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        if target.exists():
            if target.is_dir() and payload_snapshot(target) == payload_snapshot(staged):
                return f"Already current: {target}"
            if not update:
                raise InstallError(f"Existing files differ at {target}. Review them; use --update only for an intentional update. Nothing at this destination was replaced.")
            backup_root.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup = backup_root / f"{target.name}-{stamp}-{uuid.uuid4().hex[:8]}"
            target.rename(backup)
            try:
                staged.rename(target)
            except BaseException:
                backup.rename(target)
                raise
            return f"Updated: {target}\nBackup: {backup}"
        staged.rename(target)
        return f"Installed: {target}"


@contextmanager
def install_lock(root: Path):
    root.mkdir(parents=True, exist_ok=True)
    lock = root / ".website-builder-install.lock"
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise InstallError(f"Another installation may be running. If an earlier process stopped, inspect and remove this stale lock before retrying: {lock}") from error
    try:
        with os.fdopen(descriptor, "w") as stream:
            stream.write(f"pid={os.getpid()}\n")
        yield
    finally:
        lock.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=AGENTS, required=True)
    parser.add_argument("--scope", choices=("user", "project"), required=True)
    parser.add_argument("--project", help="Existing website folder; required for project scope")
    parser.add_argument("--with-supporting", action="store_true", help="Install the default pinned WordPress, Tailwind, and design guidance")
    parser.add_argument("--supporting", nargs="+", default=[], metavar="NAME", help="Also install named supporting skills and their dependencies; see supporting-skills.json")
    parser.add_argument("--dry-run", action="store_true", help="Show destinations without writes or network requests")
    parser.add_argument("--update", action="store_true", help="Back up and replace differing existing skills")
    args = parser.parse_args(argv)
    try:
        root = destination_root(args.agent, args.scope, args.project)
        manifest = load_manifest(SKILL / "supporting-skills.json") if args.with_supporting or args.supporting else []
        supporting = select_supporting(manifest, args.with_supporting, args.supporting)
        version = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
        print(f"Website Builder {version}; agent={args.agent}; scope={args.scope}")
        for name in ["website-builder", *(entry["name"] for entry in supporting)]:
            print(f"Destination: {root / name}")
        if args.dry_run:
            print("Dry run only. No files changed and no downloads performed.")
            return 0
        backup_root = root.parent / ".website-builder-backups"
        archive_cache = {}  # One bounded download per pinned repository in this run.
        with install_lock(root):
            print(install_tree(SKILL, root / "website-builder", {"name": "website-builder", "version": version}, args.update, backup_root))
            for entry in supporting:
                with tempfile.TemporaryDirectory(prefix="website-builder-download-") as temporary:
                    source = Path(temporary) / entry["name"]
                    download_skill(entry, source, archive_cache)
                    print(install_tree(source, root / entry["name"], entry, args.update, backup_root))
                if entry.get("runtime"):
                    print(f"Additional runtime required for {entry['name']}: {json.dumps(entry['runtime'])}")
        print("Skill files are ready. Follow references/setup.md to verify required runtimes and agent discovery.")
        return 0
    except (InstallError, OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        print("Completed destinations remain installed. Resolve the cause and rerun the same pinned selection.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
