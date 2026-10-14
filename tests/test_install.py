"""Installer behaviour tests. All writes are isolated; no network or home installs."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import stat
import tempfile
import unittest
from unittest.mock import patch
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / "skills/website-builder/scripts/install.py"
spec = importlib.util.spec_from_file_location("installer", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text("---\nname: example\ndescription: A test\n---\nExample\n", encoding="utf-8")
        (self.source / "references").mkdir()
        (self.source / "references/guide.md").write_text("Required resource", encoding="utf-8")
        self.target = self.root / ".agents/skills/example"
        self.backups = self.root / ".agents/.website-builder-backups"
        self.provenance = {"version": "test"}

    def install(self, update=False):
        return installer.install_tree(self.source, self.target, self.provenance, update, self.backups)

    def test_agent_destinations_and_required_project(self):
        for agent, hidden in installer.AGENTS.items():
            with self.subTest(agent=agent):
                self.assertEqual(installer.destination_root(agent, "user", None, self.root), self.root / hidden / "skills")
                self.assertEqual(installer.destination_root(agent, "project", str(self.root)), self.root / hidden / "skills")
        with self.assertRaises(installer.InstallError):
            installer.destination_root("codex", "project", None)
        with self.assertRaises(installer.InstallError):
            installer.destination_root("codex", "project", str(self.root / "absent"))
        with self.assertRaises(installer.InstallError):
            installer.destination_root("codex", "user", str(self.root))

    def test_dry_run_has_no_writes_or_network(self):
        before = set(self.root.rglob("*"))
        with patch.object(installer, "urlopen") as network, contextlib.redirect_stdout(io.StringIO()):
            status = installer.main(["--agent", "claude", "--scope", "project", "--project", str(self.root), "--with-supporting", "--dry-run"])
        self.assertEqual(status, 0)
        network.assert_not_called()
        self.assertEqual(set(self.root.rglob("*")), before)

    def test_install_resources_and_repeat_without_change(self):
        self.assertIn("Installed", self.install())
        self.assertEqual((self.target / "references/guide.md").read_text(), "Required resource")
        receipt = json.loads((self.target / installer.RECEIPT).read_text())
        self.assertIn("references/guide.md", receipt["files"])
        before = (self.target / "SKILL.md").stat().st_mtime_ns
        self.assertIn("Already current", self.install())
        self.assertEqual((self.target / "SKILL.md").stat().st_mtime_ns, before)
        self.assertFalse(self.backups.exists())

    def test_conflict_preserves_user_file(self):
        self.install()
        (self.target / "custom.md").write_text("User's work")
        with self.assertRaises(installer.InstallError):
            self.install()
        self.assertEqual((self.target / "custom.md").read_text(), "User's work")

    def test_identical_install_from_another_tool_needs_no_receipt(self):
        shutil.copytree(self.source, self.target)
        self.assertIn("Already current", self.install())
        self.assertFalse((self.target / installer.RECEIPT).exists())

    def test_selected_project_alias_is_resolved_but_skill_links_rejected(self):
        alias = self.root / "alias"
        real_project = self.root / "real-project"
        real_project.mkdir()
        try:
            alias.symlink_to(real_project, target_is_directory=True)
        except OSError:
            self.skipTest("Host does not permit symlink creation")
        self.assertEqual(installer.destination_root("codex", "project", str(alias)), real_project / ".agents/skills")
        (real_project / ".agents").symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(installer.InstallError):
            installer.destination_root("codex", "project", str(real_project))

    def test_update_saves_recoverable_backup_outside_discovery(self):
        self.install()
        (self.target / "custom.md").write_text("Keep this")
        (self.source / "references/guide.md").write_text("New resource")
        self.assertIn("Backup:", self.install(update=True))
        backups = list(self.backups.iterdir())
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "custom.md").read_text(), "Keep this")
        self.assertEqual((backups[0] / "references/guide.md").read_text(), "Required resource")
        self.assertFalse(backups[0].is_relative_to(self.target.parent))
        self.assertEqual((self.target / "references/guide.md").read_text(), "New resource")

    def test_symlink_rejected_without_touching_destination(self):
        outside = self.root / "outside"
        outside.mkdir()
        link = self.source / "linked"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Host does not permit symlink creation")
        with self.assertRaises(installer.InstallError):
            self.install()
        self.assertFalse(self.target.exists())

    def test_lock_blocks_concurrent_install_and_cleans_up(self):
        skill_root = self.root / ".cursor/skills"
        with installer.install_lock(skill_root):
            with self.assertRaises(installer.InstallError):
                with installer.install_lock(skill_root):
                    self.fail("Second installer should not acquire lock")
        self.assertFalse((skill_root / ".website-builder-install.lock").exists())

    def test_manifest_rejects_unpinned_sources(self):
        manifest = self.root / "manifest.json"
        entry = self.entry()
        entry["revision"] = "main"
        manifest.write_text(json.dumps({"schema": 1, "skills": [entry]}))
        with self.assertRaises(installer.InstallError):
            installer.load_manifest(manifest)

    @staticmethod
    def entry():
        return {"name": "example", "repository": "https://github.com/example/repo", "revision": "a" * 40, "path": "skills/example", "license_path": "LICENSE"}

    def archive(self, extra=None):
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, "w") as z:
            z.writestr("repo-pin/LICENSE", "Upstream licence")
            z.writestr("repo-pin/skills/example/SKILL.md", (self.source / "SKILL.md").read_bytes())
            z.writestr("repo-pin/skills/example/references/guide.md", "A full folder")
            z.writestr("repo-pin/other/not-selected.txt", "Do not install")
            if extra:
                z.writestr(*extra)
        payload.seek(0)
        return payload

    def test_pinned_download_keeps_resources_licence_and_provenance(self):
        destination = self.root / "downloaded"
        with patch.object(installer, "urlopen", return_value=self.archive()) as network:
            installer.download_skill(self.entry(), destination)
        request = network.call_args.args[0]
        self.assertTrue(request.full_url.endswith("/zip/" + "a" * 40))
        self.assertEqual((destination / "references/guide.md").read_text(), "A full folder")
        self.assertEqual((destination / "UPSTREAM-LICENSE").read_text(), "Upstream licence")
        self.assertEqual(json.loads((destination / "UPSTREAM-SOURCE.json").read_text())["revision"], "a" * 40)
        self.assertFalse((destination / "not-selected.txt").exists())

    def test_archive_traversal_is_rejected(self):
        with patch.object(installer, "urlopen", return_value=self.archive(("repo-pin/skills/example/../../escaped", "bad"))):
            with self.assertRaises(installer.InstallError):
                installer.download_skill(self.entry(), self.root / "downloaded")
        self.assertFalse((self.root / "escaped").exists())

    def test_archive_symlink_is_rejected(self):
        member = zipfile.ZipInfo("repo-pin/skills/example/link")
        member.create_system = 3
        member.external_attr = (stat.S_IFLNK | 0o777) << 16
        with patch.object(installer, "urlopen", return_value=self.archive((member, "../../outside"))):
            with self.assertRaises(installer.InstallError):
                installer.download_skill(self.entry(), self.root / "downloaded")

    def test_archive_size_limit(self):
        with patch.object(installer, "MAX_DOWNLOAD", 5), patch.object(installer, "urlopen", return_value=io.BytesIO(b"123456")):
            with self.assertRaises(installer.InstallError):
                installer.download_skill(self.entry(), self.root / "downloaded")


if __name__ == "__main__":
    unittest.main()
