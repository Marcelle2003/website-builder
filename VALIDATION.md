# Validation scope

Release v0.2.0 retains deterministic, offline installer tests for:

- Selected-agent user/project destinations and required project arguments.
- Dry-run behaviour without writes or network requests.
- Complete resource copies and unchanged repeat installation.
- Conflict refusal that preserves local edits.
- Intentional updates with recoverable backups outside skill discovery.
- Concurrent installer locks.
- Full revision pins, archive limits, traversal and symlink rejection.
- Pinned-download extraction, upstream licence preservation, and provenance.

Run `python3 -m unittest discover -s tests -v` from the repository root. GitHub Actions runs the same suite on Linux, macOS, and Windows with Python 3.10 and 3.13. Consult the [actual workflow runs](https://github.com/Marcelle2003/website-builder/actions) for results; a configured job is not evidence that it passed.

For v0.1.0 on 2026-10-14, all 14 installer tests passed locally on Linux and all six CI jobs passed. The core skill validator and local Markdown resource-link checks passed. A live download/install of all three pinned support folders into an isolated temporary project succeeded, followed by an unchanged repeat install. Independent scenario review covered a nontechnical Mac/Claude setup and a scoped menu/FAQ improvement request; it was a workflow review, not execution on a Mac. See [supporting skills](skills/website-builder/references/supporting-skills.md) for the source review's scope and limitations.

For v0.2.0 on the same date:

- All 14 local installer tests, skill validation, and resource-link checks passed. An isolated upgrade from the original release installed both instruction templates and the new workflow reference while preserving a recoverable v0.1.0 backup.
- An independent agent applied the workflow to two temporary website fixtures. It created instructions for a new project, preserved existing project rules and an existing `.claude/CLAUDE.md` import in the other, kept the owner's brief text, and recorded a proposed workshops page as undecided. It correctly distinguished manifest-declared commands from commands verified by execution.
- A separate, ephemeral Codex CLI 0.161.0 session ran read-only in the new fixture, without this conversation or an explicit skill invocation. A plain-language question led it to load `AGENTS.md`, the brief, and the installed Website Builder skill; it selected the improve workflow and identified the real scope, commands, and unverified runtime checks. No website files were changed by that session.
- Fresh-session loading was exercised in Codex only. Claude/Cursor loading follows their documented mechanisms but was not executed in their applications during this release check. The fixtures were documentation tests, not running Astro/Wagtail websites.

These checks do **not** constitute a complete first-run setup on a physical Mac, an end-to-end installation inside all three coding-agent applications, or proof of every framework example. The toolkit itself was authored on Linux. Browser and CMS verification of a generated website belongs to that website's run and must be recorded separately.
