# Start here — instructions for your coding agent

The user has supplied this toolkit to help them build or improve WordPress websites. Read this file, then `skills/website-builder/SKILL.md` from the same repository revision. This WordPress workflow is developed on `wordpress-theme-builder`; do not silently fetch the default branch's older Astro/Wagtail workflow instead. Treat the user's current message as the task; reading this repository by itself is not a request to install or change anything.

If they asked for setup:

1. Read the skill's `references/setup.md` and `references/compatibility.md`. Inspect this release's installer and supporting-skill manifest before execution.
2. Identify the current coding agent, operating system, permitted workspace, and installed tools. Explain the intended setup in plain language. Reuse suitable tools and skill installations.
3. Obtain a complete copy of this repository in a toolkit folder, separate from any client website. Use Git if available or a repository ZIP download if it is not. Resolve the chosen branch/tag to a commit, and use files from that same revision throughout. Do not require npx to bootstrap.
4. Follow the setup workflow, including installation of the supporting skills. Complete authorized steps yourself. When a password, interactive installer, unavailable permission, or missing tool prevents progress, explain the exact next step and resume from there when possible.
5. Verify installation, record what was installed and anything still needed, and give a plain-language result. Do not create a new website unless the user asked for one.

If they asked to create a website, perform only the missing preparation and continue with `create`. If they asked to improve a website, inspect the existing project first and load only relevant guidance. Do not replace its framework or initialize a new application over it.

New projects default to conventional WordPress with a custom hybrid PHP theme and Tailwind CSS, targeting LAMP-compatible hosting. Use WordPress for editable content, the block editor where useful, and code components for distinctive layouts. Place durable business functionality in a companion plugin. Respect an explicit block-theme choice or existing architecture. Use CSS for simple motion and optional animation skills when coordinated sequences justify them; do not add Astro or a headless layer by default.

During website work, follow [feedback recording](skills/website-builder/references/feedback.md). The AI creates project-local `SKILL_FEEDBACK.md` only after the first meaningful verified observation, maintains and deduplicates it, and distinguishes client preferences from reusable defects. An optional shared local inbox needs the user's configured or authorized directory, recorded as an absolute directory path in `feedback_inbox` in the project's untracked `.website-builder-local.json`. Do not add global settings or scan projects the user has not designated. Local recording needs no GitHub authentication and sends no automatic telemetry.

If they asked to review the toolkit, follow [review-skill](skills/website-builder/references/review-skill.md) using only the designated projects or inbox. Default to a proposal. Existing authorization such as “apply and publish these” covers the corresponding edits, checks, version update, commit, and push without repeated approval requests. Locate the intended toolkit source repository rather than treating an installed skill copy as its source checkout. Public changes must be reviewed, sanitized, and approved; never automatically upload raw feedback notes.

The toolkit is a **portable skill**, not a standalone application. Its four website modes are `setup`, `setup-website`, `create`, and `improve`; `review-skill` is the fifth, for toolkit maintenance. Understand those names from ordinary conversation; they do not register five separate slash commands. Updating an installed skill does not edit existing website projects.

If you cannot access local files or execute commands, say so clearly and guide the user to open this repository in a local coding agent. Do not claim installation from reading these instructions alone.
