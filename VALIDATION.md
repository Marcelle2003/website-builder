# Validation scope

Release v0.1.0 includes deterministic, offline installer tests for:

- Selected-agent user/project destinations and required project arguments.
- Dry-run behaviour without writes or network requests.
- Complete resource copies and unchanged repeat installation.
- Conflict refusal that preserves local edits.
- Intentional updates with recoverable backups outside skill discovery.
- Concurrent installer locks.
- Full revision pins, archive limits, traversal and symlink rejection.
- Pinned-download extraction, upstream licence preservation, and provenance.

Run `python3 -m unittest discover -s tests -v` from the repository root. GitHub Actions runs the same suite on Linux, macOS, and Windows with Python 3.10 and 3.13. Consult the [actual workflow runs](https://github.com/Marcelle2003/website-builder/actions) for results; a configured job is not evidence that it passed.

On 2026-10-14, all 14 installer tests passed locally on Linux. The core skill validator and local Markdown resource-link checks passed. A live download/install of all three pinned support folders into an isolated temporary project succeeded, followed by an unchanged repeat install. Independent scenario review covered a nontechnical Mac/Claude setup and a scoped menu/FAQ improvement request; it was a workflow review, not execution on a Mac. See [supporting skills](skills/website-builder/references/supporting-skills.md) for the source review's scope and limitations.

These checks do **not** constitute a complete first-run setup on a physical Mac, an end-to-end installation inside all three coding-agent applications, or proof of every framework example. The toolkit itself was authored on Linux. Browser and CMS verification of a generated website belongs to that website's run and must be recorded separately.
