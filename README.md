# Website Builder

Turn your ideas into a custom WordPress website with your coding agent. Create a new theme, improve an existing site, and edit routine content in WordPress.

Website Builder gives **Cursor, Claude Code, and Codex** a shared workflow for **WordPress, PHP, and Tailwind CSS** on conventional LAMP-compatible hosting. You direct the look, content, and purpose. Your agent handles the technical work and shows you the result. This branch develops the WordPress workflow; the previous Astro/Wagtail toolkit remains in its earlier revisions.

## Start here

Open your coding agent in a folder where it can work, and paste:

> Read https://github.com/Marcelle2003/website-builder/tree/wordpress-theme-builder and follow START_HERE.md from that branch to set up Website Builder for this coding agent. Install what you can, check that it works, and guide me through anything that needs my help. I am not technical.

You do not need to install Node, npx, Python, or Git before asking. The agent checks what is available and guides or performs the missing setup. It needs access to files, a terminal, and the internet; an ordinary chat without those tools cannot do the installation. Administrator prompts may need your help.

If the agent cannot read the URL, select the **wordpress-theme-builder** branch, use GitHub's **Code → Download ZIP**, extract the folder, open it in your coding agent, and ask it to read `START_HERE.md`.

## Four website modes and a review mode

- **Setup:** “Set up Website Builder on this computer.” Installs the skill, its supporting framework skills, and the necessary development tools.
- **Setup website:** “Prepare a new website called Willow Studio.” Prepares local WordPress, a custom theme, Tailwind styling, and the project's editing model.
- **Create:** “Create a warm, playful website for my ceramics studio. Here are my photos and some references I like.” Develops the content, design, pages, and interactions with you.
- **Improve:** “The mobile menu opens abruptly. Make it smooth, and keep the existing design.” Inspects and improves the relevant parts of your site.
- **Review skill:** “Review the Website Builder feedback from these projects.” Uses the local notes you designate to propose improvements to the toolkit. It proposes changes by default; it applies and publishes them when you authorize that work.

These are five modes of one skill, not five automatically registered slash commands. Ordinary language works. See [agent-specific installation and invocation](skills/website-builder/references/compatibility.md).

Each website belongs in its **own project folder**, separate from this toolkit.

## Continue in ordinary conversation

You normally do not need to repeat the skill command in every message. When preparing a new website, the agent writes project-specific `AGENTS.md` instructions and a small `CLAUDE.md` compatibility file so later chats can find the workflow, architecture, and verification commands. Existing project instructions are preserved and merged. Setup checks fresh-chat loading when the agent has the necessary tools and reports when it could not verify it.

The agent also **creates and keeps `WEBSITE_BRIEF.md` updated** from your conversations. You explain what you want, review the preview, and change your mind as needed; you do not have to complete or maintain a technical document. It records accepted decisions, separates assumptions and ideas from confirmed choices, and tracks what is complete or still pending. You can correct it in conversation or edit it yourself.

Project instructions help the next chat resume work. Skills must still be available in that agent's environment, and loading behaviour depends on the agent and its settings. See [project continuity](skills/website-builder/references/project-instructions.md) for the workflow and [compatibility](skills/website-builder/references/compatibility.md) for agent details.

## Learn from real project work

When the agent first verifies a meaningful observation about the toolkit, it creates `SKILL_FEEDBACK.md` in that website project. The AI maintains the notes and combines duplicates. It keeps your design preferences separate from reusable workflow defects, so one client's taste does not become a rule for every website. You do not have to maintain this log yourself.

Feedback recording is local: it needs no GitHub sign-in and sends no automatic telemetry. If you want a shared local inbox, authorize its directory and let the agent configure the project's untracked `.website-builder-local.json` with `feedback_inbox` set to that directory's absolute path. This is optional; no global agent settings are added, and the agent does not search unrelated projects for notes. See [feedback recording](skills/website-builder/references/feedback.md).

Use `review-skill` when you want to turn those observations into a reviewable proposal. Only reviewed, sanitized, approved improvements and their [history](feedback/IMPROVEMENT_HISTORY.md) belong in the public toolkit repository; raw project notes are never automatically uploaded. If you already asked the agent to “apply and publish these,” it carries out the authorized edits, checks, version update, commit, and push without asking for the same approval again. See [skill review](skills/website-builder/references/review-skill.md).

## What the workflow covers

- A homepage that explains the business, audience, and next step.
- A considered visual direction, useful imagery, responsive layouts, and consistent colours and typography.
- Intentional motion, from refined menus and FAQs to coordinated typography and scroll sequences when the creative direction calls for them.
- Accessible interactions, reduced-motion support, and mobile verification.
- Custom WordPress templates, purposeful JavaScript, and reusable Tailwind design tokens aligned with editor styles.
- WordPress editing for routine content, including a verified path from saving an edit to seeing it on the website.

New sites default to a **custom hybrid theme**: PHP templates and reusable components shape distinctive layouts, while WordPress provides content controls and the block editor where useful. Durable content types and business features belong in a companion plugin. AI or a developer handles structural design changes; the theme does not automatically include a drag-and-drop builder.

Block themes can be equally expressive and remain an option when the team wants to edit entire layouts visually. The workflow preserves explicit choices and existing architecture, including existing builders. A visual change does not authorize a framework migration or changes to accounts, permissions, payment flows, or business rules. Astro and headless WordPress are not needed for the default workflow.

CSS handles simple movement. GSAP is optional for coordinated animation and scroll choreography, with mobile and reduced-motion alternatives. The agent inspects reference interactions in a browser where available, rather than treating a screenshot as evidence of animation. Setup and reusable components save time; distinctive design still benefits from iteration with you.

## Forms, attribution and favicon

Website Builder includes [Cognito Forms MCP setup and form-building guidance](skills/website-builder/references/cognito-forms.md). Connecting it requires the owner’s Cognito sign-in and organization access; copying skill files does not authenticate it. New website preparation includes reusable tracking scripts with first-visit attribution, 90-day storage and the standard hidden form fields, visible only when both names are ADMIN. The agent also [asks for a favicon](skills/website-builder/references/site-icon.md), allows an explicit skip, and verifies the configured icon. Existing websites adopt these changes only within requested project work.

## Installation details for agents

Read [START_HERE.md](START_HERE.md), then the [setup workflow](skills/website-builder/references/setup.md). The included Python installer needs Python 3.10 or newer, uses the standard library, and does not require npx. It installs complete skill folders for the selected agent. Supporting skills are fetched at the reviewed commits in [the manifest](skills/website-builder/supporting-skills.json).

The supporting set combines selected official WordPress skills, Tailwind guidance, and frontend design guidance. Specialized block development, environment, performance, and animation skills are installed when relevant. Website Builder supplies the hybrid-theme workflow and coordinates these specialists; it does not load every skill for every task. See [supporting skills](skills/website-builder/references/supporting-skills.md) for the exact sources, selection, and review notes.

Preview an installation from the repository folder:

```sh
python3 skills/website-builder/scripts/install.py --agent codex --scope user --with-supporting --dry-run
```

Use `cursor` or `claude` for those agents. On Windows, use a verified Python command such as `py -3`. Remove `--dry-run` after inspecting the plan. Re-running skips identical files; different existing files require an intentional `--update`, which preserves a backup. Project installation uses `--scope project --project /path/to/website`.

Setup does not publish a website or create paid hosting accounts. Deployment can be a later request.

## Versions and maintenance

This branch targets **v0.5.0** and is not a published release. Use the branch URL above for the WordPress workflow, or an exact commit URL for a fixed revision. To update, ask your agent to inspect the chosen revision and update the installed toolkit. Supporting skills are not silently advanced to their latest upstream versions.

The installed skill is a working copy for your agent, separate from the toolkit's source repository. Reviewing or publishing a toolkit improvement requires the intended source checkout; editing an installed copy does not update GitHub.

Updating the skill does not automatically edit existing website projects. Ask the agent to adopt the updated project-instruction and feedback workflow in the website you want to continue; it will preserve existing rules and decisions.

[Supporting skill sources and review notes](skills/website-builder/references/supporting-skills.md) explain the selected dependencies. Official framework documentation and the actual project's installed versions take precedence over outdated skill advice.

## Validation

Run the installer tests with Python 3.10+ and the tracking-script tests with Node 22+:

```sh
python3 -m unittest discover -s tests -v
node --test tests/tracking.test.cjs
```

GitHub Actions runs the installer and tracking-script tests on Linux, macOS, and Windows. These checks exercise installation behaviour and isolated script logic; they do not certify every coding-agent version or a full first-time Mac setup. See [validation scope](VALIDATION.md).

Original toolkit content is [MIT licensed](LICENSE). Downloaded supporting skills retain their own licences and attribution.
