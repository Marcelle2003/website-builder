# Start here — instructions for your coding agent

The user has supplied this toolkit to help them build or improve websites. Read this file, then `skills/website-builder/SKILL.md` from the same repository revision. Treat the user's current message as the task; reading this repository by itself is not a request to install or change anything.

If they asked for setup:

1. Read the skill's `references/setup.md` and `references/compatibility.md`. Inspect this release's installer and supporting-skill manifest before execution.
2. Identify the current coding agent, operating system, permitted workspace, and installed tools. Explain the intended setup in plain language. Reuse suitable tools and skill installations.
3. Obtain a complete copy of this repository in a toolkit folder, separate from any client website. Use Git if available or a repository ZIP download if it is not. Resolve the chosen branch/tag to a commit, and use files from that same revision throughout. Do not require npx to bootstrap.
4. Follow the setup workflow, including installation of the supporting skills. Complete authorized steps yourself. When a password, interactive installer, unavailable permission, or missing tool prevents progress, explain the exact next step and resume from there when possible.
5. Verify installation, record what was installed and anything still needed, and give a plain-language result. Do not create a new website unless the user asked for one.

If they asked to create a website, perform only the missing preparation and continue with `create`. If they asked to improve a website, inspect the existing project first and load only relevant guidance. Do not replace its framework or initialize a new application over it.

The toolkit is a **portable skill**, not a standalone application. Its four modes are `setup`, `setup-website`, `create`, and `improve`. Understand those names from ordinary conversation; do not depend on one agent's slash-command syntax.

If you cannot access local files or execute commands, say so clearly and guide the user to open this repository in a local coding agent. Do not claim installation from reading these instructions alone.
