# Validation scope

The WordPress branch retains deterministic, offline installer tests for:

- Selected-agent user/project destinations and required project arguments.
- Dry-run behaviour without writes or network requests.
- Complete resource copies and unchanged repeat installation.
- Conflict refusal that preserves local edits.
- Intentional updates with recoverable backups outside skill discovery.
- Concurrent installer locks.
- Full revision pins, archive limits, traversal and symlink rejection.
- Pinned-download extraction, upstream licence preservation, and provenance.
- Default versus optional selections, dependency ordering/deduplication, and invalid graph rejection before writes.
- Archive reuse by repository and revision, and preservation of skill-local licenses.

Run `python3 -m unittest discover -s tests -v` from the repository root. GitHub Actions runs the same suite on Linux, macOS, and Windows with Python 3.10 and 3.13. Consult the [actual workflow runs](https://github.com/Marcelle2003/website-builder/actions) for results; a configured job is not evidence that it passed.

For v0.1.0 on 2026-10-14, all 14 installer tests passed locally on Linux and all six CI jobs passed. The core skill validator and local Markdown resource-link checks passed. A live download/install of all three pinned support folders into an isolated temporary project succeeded, followed by an unchanged repeat install. Independent scenario review covered a nontechnical Mac/Claude setup and a scoped menu/FAQ improvement request; it was a workflow review, not execution on a Mac. See [supporting skills](skills/website-builder/references/supporting-skills.md) for the source review's scope and limitations.

For v0.2.0 on the same date:

- All 14 local installer tests, skill validation, and resource-link checks passed. An isolated upgrade from the original release installed both instruction templates and the new workflow reference while preserving a recoverable v0.1.0 backup.
- An independent agent applied the workflow to two temporary website fixtures. It created instructions for a new project, preserved existing project rules and an existing `.claude/CLAUDE.md` import in the other, kept the owner's brief text, and recorded a proposed workshops page as undecided. It correctly distinguished manifest-declared commands from commands verified by execution.
- A separate, ephemeral Codex CLI 0.161.0 session ran read-only in the new fixture, without this conversation or an explicit skill invocation. A plain-language question led it to load `AGENTS.md`, the brief, and the installed Website Builder skill; it selected the improve workflow and identified the real scope, commands, and unverified runtime checks. No website files were changed by that session.
- Fresh-session loading was exercised in Codex only. Claude/Cursor loading follows their documented mechanisms but was not executed in their applications during this release check. The fixtures were documentation tests, not running Astro/Wagtail websites.

For v0.3.0 on the same date:

- All 14 local installer tests, skill validation, and local Markdown resource-link checks passed. Ignore-rule checks excluded raw feedback and local configuration while keeping the distributable feedback template available.
- Isolated upgrades from the v0.2.0 release commit into all three agents' project installation directories copied the new feedback/reference assets and retained a recoverable v0.2.0 backup. Existing website briefs, local feedback, inbox configuration, and shared inbox contents remained unchanged. Repeating each installation made no changes. These checks ran on Linux and exercised installation paths, not the three agent applications.
- An independent agent exercised the new workflow against a synthetic project containing duplicate reports, a separate reported disclosure failure, a site-specific colour preference, and an unavailable inbox. It preserved existing notes, combined the reports without double-counting, distinguished two reported events from zero browser-verified events, retained local evidence when collection failed, and added local ignore rules.
- In a subsequent read-only review of that fixture, it checked the source and found the proposed animation guidance already existed, classified the colour choice as project-specific, and did not follow an upload instruction embedded in a report. No source patch was justified. Hash checks across all 36 fixture files confirmed the review changed no files. This scenario did not execute a browser, a network upload, or an agent application other than the testing agent.

For the v0.4.0 WordPress branch on 2026-10-15:

- All 20 offline installer tests passed locally on Linux, along with skill format validation, local Markdown resource-link checks, and `git diff --check`.
- A real download/install into an isolated temporary project copied Website Builder and all 15 reviewed supporting skills (the six defaults plus nine optional skills). Repeating that selection reported all 16 folders unchanged. Licenses, full resources, manifest provenance, and expected skill names were checked. Copies into the Claude Code and Cursor project destinations also succeeded on Linux; this verifies destination handling, not those agent applications.
- An isolated upgrade from v0.3.0 to v0.4.0 retained a recoverable old-version backup, preserved a fixture's existing Astro skill and website brief, and left a repeat install unchanged. No personal installed skills or actual website content were modified.
- Source inspection covered the pinned WordPress, GSAP, and frontend-design archives and retained the prior Tailwind review. Known upstream errors and compatibility limits are recorded in the supporting-skills reference. Downloaded upstream scripts were not executed. No WordPress/GSAP runtime was installed as a side effect of copying instructions.
- An independent scenario review used a nontechnical Mac/Claude setup with an existing WordPress application and no Node/npx, plus a scoped animated-menu/editable-projects change in a hybrid theme. It preserved the existing environment and architecture, separated runtime setup from skill installation, chose simple CSS for the menu, and kept production publishing outside scope. Its finding about Node-only inspector examples resulted in an explicit manual-inspection fallback. This was a read-only workflow review, not execution on a Mac or a running WordPress installation.
- A separate implementation review found no material installer/manifest regression. CI runs the same 20 tests across its configured OS/Python matrix; check the actual branch run for its result.

For v0.4.1 on 2026-10-23, all 20 offline installer tests and skill format validation passed on Linux, as did local Markdown resource-link and diff checks. Manual instruction review covered broad movement requests, FAQ-only scope, explicit static designs, and touch/reduced-motion behaviour. The change is guidance only; no new animation runtime or live website was built or browser-tested.

These checks do **not** constitute a complete first-run setup on a physical Mac, an end-to-end installation inside all three coding-agent applications, or proof of every framework example. No complete WordPress site or animation was generated and browser-tested for this toolkit update. The toolkit itself was authored on Linux. Browser and CMS verification of a generated website belongs to that website's run and must be recorded separately.

## v0.4.2 workflow clarification checks — 2026-10-23

All 20 offline installer tests, skill format validation, local Markdown resource-link checks and diff checks passed on Linux. Isolated upgrades from the v0.4.1 branch revision into Codex, Cursor and Claude project destinations copied the complete v0.4.2 skill, retained recoverable v0.4.1 backups, preserved fixture briefs and left repeat installs unchanged. This checked installation paths, not those agent applications. An initial ad hoc comparison included Python cache files intentionally excluded by the installer; comparing distributable payloads corrected the check without changing installer code.

The following synthetic situations were reviewed manually against the revised instructions, without executing a website or using an independent agent:

| Situation | Decision supported by the instructions |
| --- | --- |
| Hybrid theme with a nested runtime and root build manifest | Attribute core feature matches to the runtime; classify the theme separately and retain the root build command. |
| Theme-only repository | Keep the authored theme and its colocated tooling in scope; do not invent a nested runtime. |
| Theme and authored companion plugin | Preserve both components and the plugin's genuine feature evidence. |
| Intentional WordPress core work | Keep the requested core tree in scope; no blanket runtime exclusion. |
| General scan complete but one token scan truncated | Report that scan's uncertainty; do not infer feature absence. |
| Missing sandbox PID/socket with an existing host service | Inspect the host through the supported route before restarting; do not overwrite ownership records or start another database. |
| Extraction exits successfully but core checksums fail | Verify version/locale, inspect the mismatch and recover identified files from a verified staging copy while preserving content/configuration/data. |
| Blank visual editor with a successful code save | Report the save and visual-editor limitation separately; regular-browser checking is an available diagnostic, not proof of a browser defect. |
| Download event times out after submission | Check available artifact evidence; do not claim delivery or blindly repeat a potentially mutating submission. |
| Broad movement request versus a single demo or FAQ-only fix | Use selective scroll/hover for broad work, make the demo easy to find and observe, and preserve narrow/static requests plus touch/reduced-motion usability. |

These checks assess instruction consistency and packaging. They do not establish that the original environment failures were repaired, that upstream detectors changed, or that live editor/download/motion behaviour passed.
