# Setup

Use this reference when the user wants to prepare their computer and agent for website work. Complete the authorized setup yourself where tools permit. Explain results in ordinary language: Node runs the website tools; Python runs the content manager; Git saves version history; skills give the agent specialist instructions.

Setup prepares tools and installs this toolkit. Creating project folders, installing Astro or Wagtail project packages, generating a website, starting databases, and designing pages belong to `setup-website` or `create`. If the user requested several modes together, finish setup and continue to the next requested mode.

## Inspect before installing

1. Identify the current agent, operating system, CPU architecture, shell, actual user home, and writable locations. Work in the environment that will run the website. A Windows host and its WSL environment have separate tools and home folders; do not mix them.
2. Find existing Node, npm or another project package manager, Python, Git, and uv before choosing installers. Include usable runtimes exposed by the agent application. Resolve executable paths as well as versions so a stale PATH does not look like a missing tool.
3. If a website already exists, read its runtime constraints, lockfiles, and setup notes first. Preserve its package manager and environment. A setup request does not authorize a framework migration.
4. Recheck the official requirements below. Reuse maintained, compatible installations. Install only missing or incompatible tools, using the user's existing version manager or package manager where practical.
5. State the selected agent and destination briefly. Default to **user scope for the current agent**, so the recipient can reuse the toolkit across projects. Respect a requested project scope or another agent. If the current agent cannot be established, ask that one question while continuing independent runtime inspection. Do not install into every agent's directories.

Useful checks, adapted to the shell and executable paths you actually found:

```text
node --version
npm --version
git --version
uv --version
python3 --version
```

On Windows, check `py -3 --version` and `python --version` as available. An application-store alias or launcher without an installed interpreter is not a working Python. On macOS/Linux, prefer the discovered `python3` executable over assuming `python` means Python 3. Run only applicable checks; missing commands are information, not a reason to repeatedly retry the same command.

## Choose compatible versions

Consult the live official pages when installing. Record the selected versions and the date checked. The observations here were checked on **2026-10-14** and are a baseline, not permanent pins.

- **Toolkit installer:** Python **3.10 or newer**, using the standard library. It needs no Node, npm, npx, Git, uv, or pip packages. Supporting skills are fetched over HTTPS from pinned revisions. Installing their files does not install their separate runtime dependencies.
- **Astro:** the current install guide requires Node **22.12.0 or newer** and excludes odd-numbered releases. For a fresh installation choose a currently supported Node LTS meeting Astro's requirement; reuse an existing compatible supported LTS. Node's release page currently lists 24 and 22 as LTS. Check the chosen Astro release if an existing project pins an older version. [Astro prerequisites](https://docs.astro.build/en/install-and-setup/#prerequisites), [Node releases](https://nodejs.org/en/about/previous-releases)
- **Wagtail:** select Python, Wagtail, and Django together using the compatibility matrix. The current Wagtail 8.0 row permits Python 3.10–3.14 and Django 5.2, 6.0, or 6.1; Django and other chosen dependencies can narrow that range. Prefer a maintained Python release inside the full intersection. Do not install an unsupported newest Python just because it is newest. Wagtail project packages will live in an isolated environment during `setup-website`. [Wagtail compatibility](https://docs.wagtail.org/en/stable/releases/upgrading.html#compatible-django-python-versions), [Wagtail first-site guide](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
- **Tailwind:** follows the frontend project's dependencies. Current Astro supports Tailwind 4 through `@tailwindcss/vite`; it does not need a global Tailwind installation. Preserve an existing Tailwind setup unless changing it is requested. [Astro Tailwind guide](https://docs.astro.build/en/guides/styling/#tailwind)
- **Official Wagtail supporting skill:** its reviewed stub loads workflow instructions through `wt`, supplied by `wagtail-cli`. This toolkit pins CLI **0.4.0**, which requires Python **3.12+**. That minimum is separate from the toolkit installer's Python 3.10 requirement and from a website's Wagtail compatibility range. Prepare this isolated tool during full setup; the procedure is below. [Pinned Wagtail skill](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/skills/wagtail/SKILL.md), [CLI release metadata](https://pypi.org/pypi/wagtail-cli/0.4.0/json)
- **uv:** prefer an existing working installation for Python environment management. If it is absent, use a suitable documented install method, or use Python's `venv` and pip when that meets the project workflow. uv is not required to install the skills. [uv installation](https://docs.astral.sh/uv/getting-started/installation/)
- **Git:** use a supported package supplied for the host platform. Its absence does not block extracting the toolkit ZIP or running its installer; prepare it for website version history before handing off. GitHub CLI, a GitHub account, Docker, a database server, and deployment accounts are not prerequisites for this setup. [Git installation](https://git-scm.com/install/)

## Install missing tools with minimal disruption

Prefer a documented package through a package manager already present, or the official runtime's installer/download for the detected OS and architecture. Check what the selected package actually installs; a package called `node` may be a different major version from the one selected. Avoid broad system upgrades or replacing a working default interpreter.

- **macOS:** reuse an existing version manager or Homebrew installation where appropriate. Do not add Homebrew solely to run this toolkit. Official Node and Python installers are valid alternatives; choose Apple Silicon or Intel correctly. If Git needs Apple's Command Line Tools, explain that macOS may present a system installation dialog. Do not install the full Xcode application for this workflow.
- **Windows:** use the user's existing environment and shell. An available trusted package manager or official installer can supply the selected runtimes. Use `npm.cmd` if PowerShell blocks the npm script shim; call a virtual environment's Python executable directly when activation is blocked. Do not weaken machine-wide execution policy or require WSL merely to complete setup.
- **Linux:** reuse the distribution's package manager or the user's runtime manager, checking versions against the requirements. If system packages are too old, prefer a user-scoped compatible runtime. Do not replace distribution Python, run `sudo pip`, or bypass externally managed Python protections. Some distributions package `venv` separately; install that component only if needed.

Use [Node downloads](https://nodejs.org/en/download), [Python downloads](https://www.python.org/downloads/), [Git installation](https://git-scm.com/install/), and [uv installation](https://docs.astral.sh/uv/getting-started/installation/) as the source for platform instructions. Never pipe an uninspected remote script into a shell. If a documented standalone script is the appropriate route, download the selected version, inspect it and its destination, verify published integrity information where available, then run the local file within the authorized scope.

Let the agent execute ordinary installation steps when authorized and supported. Ask the person to act only for genuinely manual operations such as an OS password prompt, signing in to their chosen agent, or an installer dialog the agent cannot control. Give one concrete action, where to do it, and what success looks like. Continue independent work while waiting. After a PATH-changing installation, use the known executable path or refresh the current process; request an application restart only when it is actually needed.

## Install Website Builder and supporting skills

Resolve `scripts/install.py` relative to this skill folder. From an extracted repository root, its path is `skills/website-builder/scripts/install.py`. Read its `--help` and review the bundled `supporting-skills.json` before running it. The manifest, not a remembered skill catalogue, defines the reviewed sources and pinned revisions for this release.

For full setup, include `--with-supporting` by default. Pass `--agent` and `--scope` explicitly, even when using the default choice. With `--scope project`, pass the actual absolute project path using `--project`; do not guess a website folder that does not exist yet. Use the interpreter discovered above. For example, from the extracted repository root on macOS/Linux, when Codex is the selected agent:

```sh
python3 skills/website-builder/scripts/install.py --agent codex --scope user --with-supporting --dry-run
python3 skills/website-builder/scripts/install.py --agent codex --scope user --with-supporting
```

For a Windows user who selected Claude Code, the equivalent commands with a working Python launcher are:

```powershell
py -3 skills/website-builder/scripts/install.py --agent claude --scope user --with-supporting --dry-run
py -3 skills/website-builder/scripts/install.py --agent claude --scope user --with-supporting
```

Use `--agent cursor` for Cursor. For project scope, change to `--scope project --project "ABSOLUTE_PROJECT_PATH"` with the real path substituted. Quote paths containing spaces and use the host shell's argument rules. These are command templates; do not execute examples for an agent the user did not select.

Inspect the dry-run plan, then execute the same selection without `--dry-run`. The dry-run is a planning check, not proof that downloads or final writes will succeed. The installer copies local core files and downloads supporting skill folders; it does not install runtime programs, agent applications, or website packages. Keep those stages distinct in progress reports.

Identical existing skill contents are left alone. A differing destination requires review: do not delete it to force installation. For an authorized toolkit update, use `--update`; the installer saves a backup outside the discovery root before replacement. Preserve custom modifications and report the actual backup path. Use the pinned manifest as shipped; changing a revision or fetching an unrelated specialist skill is separate work, not a network-error workaround.

Missing `npx` does not block any of these installer steps. If website tooling later needs package execution, use the installed package manager's supported execution command or project scripts. Do not install a second Node distribution just to obtain `npx` when a usable supported environment already exists.

## Prepare the Wagtail supporting skill's CLI

When full setup includes the manifest's official `wagtail` skill, also prepare its runtime. Read the manifest's `runtime` pin and inspect any existing `wt` installation before changing it. The reviewed selection is `wagtail-cli==0.4.0`; do not silently replace a different installation the user already relies on.

Use a compatible Python 3.12+ interpreter and an isolated tool environment:

```sh
uv tool install wagtail-cli==0.4.0
wt --help
wt skills get core
wt skills list
```

If uv would select an older interpreter, add `--python` with the discovered compatible interpreter's path or a supported managed Python version. Install a managed Python only when needed for this tool, without replacing system Python. An existing equivalent isolated package manager is acceptable. This tool environment does not add Wagtail or Django to the website's environment. If a `wt` command already exists, resolve which executable you are testing. [uv tool isolation and Python selection](https://docs.astral.sh/uv/guides/tools/)

If the installed executable directory is missing from PATH, use its actual path for the current session. For a durable fix, apply `uv tool update-shell` only to the appropriate user shell configuration and explain that a new terminal may be needed. Do not change unrelated shell settings.

If uv cannot be installed but a compatible Python is available, create a dedicated user tool environment with that interpreter's `-m venv`, then run the environment's Python with `-m pip install wagtail-cli==0.4.0`. Keep it separate from website environments. The helper will be at `<environment>/bin/wt` on macOS/Linux or `<environment>/Scripts/wt.exe` on Windows. Verify it using that full path and record the path in the setup checkpoint. Use the full path in subsequent agent commands, or prepend its directory to the current agent shell's PATH; do not overwrite system PATH or require activation. An existing isolated pipx installation is another suitable route. Reuse one working approach rather than installing the helper twice.

The CLI is currently alpha. Its API operations target Wagtail's v3 admin API, not the public v2 content API. Do not point those operations at a v2 endpoint, enable an API, request production credentials, or upgrade an existing site during setup. The skill and documentation commands above need no project API credentials; loading them verifies the helper without connecting to a CMS. Treat an unavailable CLI as an incomplete Wagtail helper setup, not a reason to block unrelated frontend work. [Pinned CLI documentation](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/README.md)

Preserve the supporting manifest's license provenance: the stub declares MIT, while its repository/runtime license is BSD-3-Clause. Retain both notices rather than relabeling the entire upstream source with one license.

## Verify and resume

Verify the actual result rather than assuming a successful installer window finished setup:

- Run the selected Node and package manager, Git, and Python version checks from the environment the agent will use. Confirm Python can import `ssl`, `sqlite3`, and `venv`. Where uv is selected, check `uv --version`. If virtual-environment creation needs testing, use an isolated temporary directory and the resulting Python executable; do not create a website as a test.
- Check installer exit status and read its summary. Verify the core `SKILL.md`, referenced resources, and requested supporting skill folders exist at the reported destination. Distinguish complete installation from a partial download or a skipped conflict.
- If the official Wagtail supporting skill was included, verify its selected CLI version and the successful `wt --help`, `wt skills get core`, and `wt skills list` checks. File installation alone does not make this stub ready to use.
- Confirm `website-builder` appears in the selected agent's skill picker or available-skill inventory. If discovery is stale, use that agent's supported reload/restart path from [compatibility.md](compatibility.md). Then invoke a harmless request such as “Use Website Builder to explain the four modes without changing files.” If you cannot inspect the host's inventory, state discovery as unverified instead of claiming it worked.

Keep a compact checkpoint in the conversation or the project's existing status record: chosen agent/scope, executable paths and versions, installed skills, verification completed, and the exact pending step. Do not record credentials. When setup resumes, inspect reality and repeat only incomplete or failed steps. A failed support download need not undo a working core installation; retry the original pinned selection after resolving the reported cause. Do not disable TLS verification to get past a certificate error.

Finish with what is ready, anything still pending, and the next useful mode. Say whether the website runtimes and skill discovery were both verified. For a setup-only request, the next step is `setup-website`; do not silently start building a site.
