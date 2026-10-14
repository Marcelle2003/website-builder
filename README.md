# Website Builder

Turn your ideas into a website with your coding agent. Create a new site, improve an existing one, and edit its content through Wagtail.

Website Builder gives **Cursor, Claude Code, and Codex** a shared workflow for **Astro, Tailwind CSS, and Wagtail**. You direct the look, content, and purpose. Your agent handles the technical work and shows you the result.

## Start here

Open your coding agent in a folder where it can work, and paste:

> Read https://github.com/Marcelle2003/website-builder and follow START_HERE.md to set up Website Builder for this coding agent. Install what you can, check that it works, and guide me through anything that needs my help. I am not technical.

You do not need to install Node, npx, Python, or Git before asking. The agent checks what is available and guides or performs the missing setup. It needs access to files, a terminal, and the internet; an ordinary chat without those tools cannot do the installation. Administrator prompts may need your help.

If the agent cannot read the URL, use GitHub's **Code → Download ZIP**, extract the folder, open it in your coding agent, and ask it to read `START_HERE.md`.

## Four things you can ask for

- **Setup:** “Set up Website Builder on this computer.” Installs the skill, its supporting framework skills, and the necessary development tools.
- **Setup website:** “Prepare a new website called Willow Studio.” Creates and connects an Astro frontend, Tailwind styling, and a Wagtail content editor.
- **Create:** “Create a warm, playful website for my ceramics studio. Here are my photos and some references I like.” Develops the content, design, pages, and interactions with you.
- **Improve:** “The mobile menu opens abruptly. Make it smooth, and keep the existing design.” Inspects and improves the relevant parts of your site.

These are four modes of one skill, not four automatically registered slash commands. Ordinary language works. See [agent-specific installation and invocation](skills/website-builder/references/compatibility.md).

Each website belongs in its **own project folder**, separate from this toolkit. Your agent keeps a short project brief so another agent can pick up the work later.

## What the workflow covers

- A homepage that explains the business, audience, and next step.
- A considered visual direction, useful imagery, responsive layouts, and consistent colours and typography.
- Restrained motion for menus, FAQs, controls, galleries, and navigation when it helps the experience.
- Accessible interactions, reduced-motion support, and mobile verification.
- Fast Astro pages, purposeful client-side interactivity, and reusable Tailwind design tokens.
- Wagtail editing for routine content, including a verified path from publishing an edit to seeing it on the website.

It preserves existing project choices when improving a site. A visual change does not authorize changing accounts, permissions, payment flows, or business rules. New sites use the full three-part stack by default; you can request a simpler frontend-only site.

## Installation details for agents

Read [START_HERE.md](START_HERE.md), then the [setup workflow](skills/website-builder/references/setup.md). The included Python installer needs Python 3.10 or newer, uses the standard library, and does not require npx. It installs complete skill folders for the selected agent. Supporting skills are fetched at the reviewed commits in [the manifest](skills/website-builder/supporting-skills.json).

Preview an installation from the repository folder:

```sh
python3 skills/website-builder/scripts/install.py --agent codex --scope user --with-supporting --dry-run
```

Use `cursor` or `claude` for those agents. On Windows, use a verified Python command such as `py -3`. Remove `--dry-run` after inspecting the plan. Re-running skips identical files; different existing files require an intentional `--update`, which preserves a backup. Project installation uses `--scope project --project /path/to/website`.

Setup does not publish a website or create paid hosting accounts. Deployment can be a later request.

## Versions and maintenance

The first release is **v0.1.0**. For a fixed version, give your agent the release/tag URL instead of the default branch. To update, ask it to inspect the new release and update the installed toolkit. Supporting skills are not silently advanced to their latest upstream versions.

[Supporting skill sources and review notes](skills/website-builder/references/supporting-skills.md) explain the selected dependencies. Official framework documentation and the actual project's installed versions take precedence over outdated skill advice.

## Validation

Run the installer tests with Python's built-in test runner:

```sh
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the installer tests on Linux, macOS, and Windows. These checks exercise installation behaviour; they do not certify every coding-agent version or a full first-time Mac setup. See [validation scope](VALIDATION.md).

Original toolkit content is [MIT licensed](LICENSE). Downloaded supporting skills retain their own licences and attribution.
