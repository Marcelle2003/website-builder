# Setup

Use this reference when the user wants to prepare their computer and agent for website work. Complete authorized setup where tools permit. Explain the roles simply: WordPress runs on PHP and a database; Tailwind turns theme styles into CSS; Git saves version history; skills give the agent specialist instructions. Python is only needed for this toolkit's installer helper, not for the WordPress website.

Setup prepares tools and installs this toolkit. Creating a WordPress site or database, building a theme, adding demonstration content, and designing pages belong to `setup-website` or `create`. If several modes were requested together, continue to the next requested mode after setup. The four website modes are `setup`, `setup-website`, `create`, and `improve`; `review-skill` is a separate toolkit maintenance mode. They are choices within one skill, not automatically registered slash commands.

## Inspect before installing

1. Identify the current agent, operating system, CPU architecture, shell, actual user home, and writable locations. Work in the environment that will run the website. Windows and WSL have separate tools and home folders; do not mix them.
2. Find an existing local WordPress environment first, including app-managed PHP/database tools and its site shell. Resolve executable paths and versions for available PHP, WordPress CLI, Node/package manager, Git, and Python. Check Composer only if the chosen project or verification tools use it. Include usable runtimes exposed by the agent application; a missing PATH entry is not a missing installation.
3. If a site exists, read its runtime constraints, theme/plugin dependencies, lockfiles, and setup notes. Preserve its environment and editing model. Setup does not authorize replacing Flatsome, converting a block theme, or migrating an Astro/Wagtail or other website to WordPress.
4. Consult current official requirements below. Reuse maintained, compatible installations and install only missing tools needed for the requested workflow. Prefer the user's existing environment or package manager.
5. State the selected agent and destination briefly. Default to **user scope for the current agent**, so the toolkit is reusable across projects. Respect a requested project scope or another agent. If the agent cannot be established, ask that one question while continuing independent inspection. Do not install into every agent's directories.

Useful checks, adapted to the shell and executable paths actually found:

```text
php --version
wp --info
node --version
npm --version
git --version
python3 --version
```

Run only applicable checks. Use the local WordPress application's site shell or explicit bundled executable where required. On Windows, `py -3 --version` or `python --version` may locate Python; an application-store alias without an interpreter is not a working installation. On macOS/Linux, prefer the discovered `python3` executable over assuming `python` means Python 3.

## Choose a compatible local environment

The default hosting target is conventional WordPress on **LAMP**: Linux, Apache, MySQL/MariaDB, and PHP. A designer's Mac or Windows computer does not need to become a Linux server. Reuse its working WordPress environment; otherwise select a maintained local option compatible with the intended host. The [WordPress local-development guide](https://developer.wordpress.org/themes/getting-started/tools-and-setup/) lists options including Local, MAMP, XAMPP, and `@wordpress/env`. Check the selected option's current platform support and prerequisites before using it. Containers are one option, not a requirement; do not install Docker or WSL solely because a generic guide assumes them.

Select the smallest workable toolchain and record actual versions and the date checked:

- **WordPress/PHP/database:** use maintained versions compatible with the intended host and required plugins. Check [WordPress requirements](https://wordpress.org/about/requirements/) and [PHP support](https://www.php.net/supported-versions.php), rather than treating WordPress's legacy minimum as the preferred installation. A local app may supply PHP, the database, and web server together; do not install duplicate system services. Note any differences from the hosting target and verify affected features there before deployment.
- **WP-CLI:** reuse an environment's supplied CLI or follow [official installation instructions](https://make.wordpress.org/cli/handbook/guides/installing/) when useful for setup and verification. It runs against the selected WordPress installation and PHP runtime. Inspect `wp --info` and use the actual site path; a CLI being present does not prove a website or database is ready. Some operations can use the WordPress admin if the CLI is unavailable.
- **Tailwind and JavaScript tooling:** keep a single package manager and project-local build dependencies. For a new project, select a maintained Node LTS compatible with its chosen tools; check [Node releases](https://nodejs.org/en/about/previous-releases) and the [Tailwind CLI](https://tailwindcss.com/docs/installation/tailwind-cli). A standalone Tailwind CLI is an alternative for a CSS-only workflow, but it does not supply a JavaScript bundler. Compiled theme assets can run on conventional PHP hosting without a Node server. Preserve an existing Tailwind version unless a change is in scope.
- **Composer:** use it when the chosen PHP dependencies or checks require it. It is not required just to create a basic WordPress theme or install these skill files. Keep development packages local to the project. [Composer installation](https://getcomposer.org/doc/00-intro.md)
- **Toolkit installer:** Python **3.10 or newer**, using its standard library. It needs no Node, npm, npx, Git, Composer, or pip packages. Supporting skills are fetched over HTTPS from pinned revisions. Copying their files does not install their separate tools or execute their scripts.
- **Git:** prepare supported Git for website version history. Its absence does not prevent extracting the toolkit ZIP or running the helper. GitHub CLI, a GitHub account, and hosting credentials are not setup prerequisites. [Git installation](https://git-scm.com/install/)

## Install missing tools with minimal disruption

Use an existing trusted package manager or the selected tool's official installer for the detected OS and architecture. Check the package version and destination before installing; avoid broad system upgrades or replacing working defaults.

- **macOS:** reuse a working local WordPress app, version manager, or Homebrew installation where appropriate. Do not add Homebrew solely to run the toolkit. Choose Apple Silicon or Intel packages correctly. Git may require Apple's Command Line Tools and a system dialog; the full Xcode application is unnecessary.
- **Windows:** preserve the existing environment and shell. Use a trusted package manager or official installer. Use `npm.cmd` if PowerShell blocks its script shim; do not weaken machine-wide execution policy or require WSL.
- **Linux:** reuse compatible distribution packages or a user-managed runtime. Avoid replacing distribution Python, using `sudo pip`, or starting competing web/database services. Check ports and data directories before selecting a service.

Use official downloads such as [Node](https://nodejs.org/en/download), [Python](https://www.python.org/downloads/), and the selected WordPress environment's documentation. Never pipe an uninspected remote script into a shell. If a documented standalone installer is appropriate, download the selected version, inspect it and its destination, verify published integrity information where available, and run the local file within the authorized scope.

Let the agent execute ordinary supported installation steps. Ask the person to act only for genuinely manual operations such as an OS password prompt, agent sign-in, or an installer dialog outside the available tools. Give one concrete action, where to do it, and what success looks like. Continue independent work while waiting. After a PATH-changing installation, use the known executable or refresh the current process; request an application restart only when necessary.

## Install Website Builder and supporting skills

Resolve `scripts/install.py` relative to this skill folder. From an extracted repository root, its path is `skills/website-builder/scripts/install.py`. Read its `--help` and review the bundled `supporting-skills.json` before running it. The manifest, not a remembered skill catalogue, defines the reviewed sources and pinned revisions for this release.

For full setup, include `--with-supporting` for the reviewed core selection. Use `--supporting NAME [NAME ...]` for optional specialists actually needed by the project, using names in the manifest; it can be combined with the core selection and resolves declared dependencies. Do not install every optional skill by default. Pass `--agent` and `--scope` explicitly, even when using the default choice. With `--scope project`, pass the actual absolute project path using `--project`; do not guess a website folder that does not exist yet. Use the interpreter discovered above. For example, from the extracted repository root on macOS/Linux, when Codex is the selected agent:

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

The installed skill is separate from the toolkit source checkout. Updating it does not edit existing website projects or publish source changes. Adopt updated project instructions and feedback conventions only in the website projects the user asks to continue; preserve their existing decisions and rules.

Missing `npx` does not block any of these installer steps. If website tooling later needs package execution, use the installed package manager's supported execution command or project scripts. Do not install a second Node distribution just to obtain `npx` when a usable supported environment already exists.

## Prepare only relevant supporting tools

Read [supporting skills](supporting-skills.md) for the selected WordPress, Tailwind, design, and optional motion skills and their limitations. The manifest is the source of exact names and revisions. An instruction file does not grant permission to run a script, install a plugin, connect to production, or change architecture. Load specialist instructions only for the relevant task.

For local WordPress setup, check that the selected PHP runtime and WP-CLI can run together. Composer-based standards checks, block-development packages, browser automation, and GSAP packages belong to the project only when needed. Do not preinstall every tool mentioned by every supporting skill. Website preparation will test a real WordPress site; setup-only verification must not create one as a hidden test.

## Cognito Forms connection

Include the official [Cognito Forms MCP connector](cognito-forms.md#connect-the-agent) in full setup. Check the current agent’s connection and guide missing sign-in/organization authorization. This is an account connection, separate from installing supporting-skill folders; do not add an invented package to the installer manifest. Record actual readiness and continue independent setup if sign-in is pending.

## Local feedback and toolkit maintenance

Feedback recording needs no additional runtime, GitHub authentication, or global agent configuration. During later website work, the AI creates project-local `SKILL_FEEDBACK.md` after its first meaningful verified observation and maintains it according to [feedback.md](feedback.md), combining duplicates and separating client preferences from reusable defects. Setup alone does not require an empty feedback log, and notes are not sent as telemetry.

Leave a shared local inbox unconfigured unless the user supplies or authorizes its directory. When requested, record `feedback_inbox` as an absolute directory path in the relevant project's untracked `.website-builder-local.json`, keeping that machine-specific file out of version control. This is a local directory, not an upload endpoint. Do not scan other repositories to discover feedback or add settings to a global agent configuration. A missing inbox does not block local project notes.

For toolkit improvements, [review-skill](review-skill.md) uses only user-designated projects or the authorized inbox and defaults to a reviewable proposal. If the user has already authorized applying and publishing those improvements, proceed with the corresponding edits, verification, version update, commit, and push without asking for the same approval again. Work in the intended source checkout. Only reviewed, sanitized, approved improvements and their history enter the public repository; raw notes are never automatically uploaded.

## Verify and resume

Verify the result rather than assuming a successful installer window finished setup:

- Check the selected runtime executables in the environment the agent will use. Confirm Python can import `ssl`; run PHP/WP-CLI and Node/package-manager checks where selected. A local app installation can be ready before a site exists; label database/site checks as pending `setup-website` instead of claiming they passed.
- Check installer exit status and summary. Verify the core `SKILL.md`, referenced resources, licenses/provenance, and requested supporting skill folders at the reported destination. Distinguish complete installation from a partial download or skipped conflict.
- Confirm `website-builder` appears in the selected agent's skill picker or available-skill inventory. If discovery is stale, use its supported reload/restart path from [compatibility](compatibility.md). Invoke a harmless request such as “Use Website Builder to explain its four website modes and review-skill mode without changing files.” If the inventory cannot be inspected, state discovery as unverified.

Keep a compact checkpoint in the conversation or an existing status record: agent/scope, local WordPress environment choice, executable paths and versions, installed skills, verified checks, and the exact pending step. Do not record credentials. On resume, inspect reality and repeat only incomplete or failed steps. A failed support download need not undo a working core installation; retry the original pinned selection after resolving the cause. Do not disable TLS verification to bypass certificate errors.

Finish with what is ready, anything pending, and the next useful mode. Distinguish skill discovery, tool availability, and a running website. For a setup-only request, suggest `setup-website`; do not silently start building a site.
