# Agent compatibility

Website Builder uses the shared Agent Skills format: a `website-builder` folder containing `SKILL.md`, YAML `name` and `description`, Markdown instructions, and supporting files. Keep these two fields present, the name lowercase with hyphens, and the folder name matching it. The core workflow does not depend on host-specific argument substitution, hooks, subagent types, or tool names.

The local installer needs Python 3.10+ and installs files for the **selected** agent. It does not install the agent application or sign the user in. Supporting skills can have additional tool requirements; inspect their relevant instructions before running them. PHP/WordPress tools serve the website, Node supports the selected asset build, and Python is only required for this toolkit installer. Installing instruction files does not install those runtimes. These locations describe local coding-agent sessions, not every hosted product with a similar name. Official documentation was checked on 2026-10-14; recheck it if an installed client behaves differently.

## Installation destinations

- **Codex:** user scope goes to `~/.agents/skills/website-builder/`; project scope goes to `<project>/.agents/skills/website-builder/`. Codex discovers repository skill roots up to the repository root. Mention `$website-builder` or select it from the skills UI; CLI and IDE documentation also describe `/skills`. [Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
- **Cursor:** user scope goes to `~/.cursor/skills/website-builder/`; project scope goes to `<project>/.cursor/skills/website-builder/`. Invoke `/website-builder` through Agent chat's skill picker. Cursor also discovers `.agents/skills/` and compatibility locations such as `.claude/skills/`, including personal equivalents. Install one selected copy rather than scattering duplicates across these roots. [Official Cursor skill documentation](https://cursor.com/docs/skills)
- **Claude Code:** user scope goes to `~/.claude/skills/website-builder/`; project scope goes to `<project>/.claude/skills/website-builder/`. Invoke `/website-builder`. Its documented local discovery does not include `.agents/skills/`; placing a copy there for Codex does not by itself install it for Claude Code. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills)

Here `~` means the current user's home directory; on Windows this is normally under `C:/Users/<name>`. The installer resolves it through Python, so the user need not create literal `~` folders. Native Windows and WSL homes are separate. Installing for another agent later is an explicit second selection, not an automatic side effect of setup.

## One skill, five modes

`setup`, `setup-website`, `create`, and `improve` are the four website modes. `review-skill` is a fifth mode for toolkit maintenance. These choices are interpreted by Website Builder's instructions; they are not five new slash commands. Supply the choice as ordinary text with the named skill:

```text
Codex:       $website-builder setup
Cursor:      /website-builder setup
Claude Code: /website-builder setup
```

The same pattern works with the other mode names and a short request, such as `/website-builder improve the mobile navigation` or `/website-builder review-skill for these projects`. A plain-language alternative is “Use the Website Builder skill in setup-website mode for this project.” If the skill is not discovered, resolve installation first; merely mentioning its name does not make missing files available. [Skill review](review-skill.md) defaults to a proposal; an existing request to apply and publish the selected improvements authorizes that workflow without repeated approval requests.

Claude Code supports `$ARGUMENTS` and positional substitution in its own skill bodies. Cursor's current skill documentation does not promise equivalent substitution. This toolkit therefore reads the user's mode and brief as conversational input rather than embedding those macros. Five separate picker entries would require separate skills or host-specific command definitions. [Claude arguments](https://code.claude.com/docs/en/skills#pass-arguments-to-skills), [Cursor invocation](https://cursor.com/docs/skills#how-skills-work)

## Persistent instructions for each website

During new-project preparation, generate a concise root `AGENTS.md` as the authoritative shared entry point for that website's project guidance. It should direct the agent to the installed Website Builder skill when relevant, identify the project brief and working commands, and preserve the owner's decisions. It remains subject to the user's current request and the host's instruction precedence. Keep detailed workflows in the skill instead of copying them into every project.

Codex discovers project instructions when a session starts; Cursor supports root and nested `AGENTS.md` files. Open the intended website project and check the effective instructions, including any overrides. [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Cursor project rules](https://cursor.com/docs/rules#agentsmd)

For a new project, also create a small sibling `CLAUDE.md` containing this literal import line:

```text
@AGENTS.md
```

In the actual file, the line must be outside quotes, backticks, and code fences. Add Claude-specific guidance below it only when needed. This keeps one shared source and avoids symlink portability problems. Existing projects require inspection and a compatible merge: preserve existing `AGENTS.md`, `CLAUDE.md`, and Cursor rules, resolve conflicts with the user's decisions, and avoid duplicate imports. Do not replace an established rules system or change global agent configuration merely to add Website Builder. [Claude's shared-file guidance](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools)

Claude Code **v2.1.277+** can read `AGENTS.md` directly under its default project-instruction setting. However, a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in the working directory or an ancestor suppresses that fallback; personal `~/.claude/CLAUDE.md` does not. Older versions, disabled support, or different settings can also prevent direct loading. The wrapper works when project `CLAUDE.md` loading is enabled; it cannot override exclusions or a managed-only setting. Verify the actual client rather than changing its settings automatically. [Claude AGENTS.md discovery](https://code.claude.com/docs/en/memory#agents-md)

Instruction loading and skill installation are separate checks. A project instruction can tell the agent to use Website Builder, but cannot make an absent skill available or install its dependencies. Loading the file does not authorize setup, and a discussion stays a discussion. Perform installations only when the user's task authorizes them. Keep imports local to the project; importing a personal skill path would tie the project to one computer and may require external-import approval.

The AI maintains `WEBSITE_BRIEF.md` as decisions, implementation, and verification change; the owner supplies direction and corrections rather than manually keeping this technical record. Follow [project-instruction maintenance and fresh-chat verification](project-instructions.md) to keep the brief and instructions consistent and confirm they load in the selected agent. Persistent instructions reduce repeated explanation, but they are model guidance, not a guarantee of compliance or an enforcement mechanism. [Claude instruction reliability](https://code.claude.com/docs/en/memory#write-effective-instructions)

## Local feedback across agents

Feedback uses ordinary project files, not a host-specific service. The AI creates and maintains `SKILL_FEEDBACK.md` after a meaningful verified observation, deduplicating notes and separating preferences from reusable defects. A shared local inbox is optional and requires the user's configuration or authorization: the project's untracked `.website-builder-local.json` may set `feedback_inbox` to an absolute directory path. Do not add global agent settings or inspect projects outside those the user designated. Recording needs no GitHub account and performs no automatic telemetry. Follow [feedback guidance](feedback.md).

An installed skill copy, a website project, and the toolkit source repository are distinct locations. Updating an installed skill does not modify existing website projects. Toolkit review works against the intended source checkout, with only reviewed, sanitized, approved improvements and history entering a public repository; raw notes are never automatically uploaded. See [review-skill](review-skill.md).

## Discovery and capabilities

After installing, check the host's actual skill inventory. Codex detects skill changes automatically; restart it if the update does not appear. Cursor discovers skills at startup and exposes them in Customize → Skills; start a fresh session or restart if necessary. Claude Code watches existing skill roots; `/reload-skills` discovers a newly created top-level root. Avoid repeatedly installing duplicates to fix a stale picker. [Codex discovery](https://learn.chatgpt.com/docs/build-skills), [Cursor discovery](https://cursor.com/docs/skills#viewing-skills), [Claude reload behavior](https://code.claude.com/docs/en/skills#edit-a-skill-during-a-session)

The workflow adapts to the host's available terminal, file, browser, research, image, and delegation tools. A portable skill does not guarantee those capabilities or their permissions. Use available equivalents, preserve each host's authorization rules, and identify a missing capability only when it blocks the requested outcome. In particular, a successful text build does not prove browser or visual verification occurred.

The selected WordPress, Tailwind, design, and optional animation skills are documented in [supporting skills](supporting-skills.md) and pinned in the manifest. Load relevant specialists through the host's discovered skill files; do not assume a host-specific tool or subagent API exists everywhere. Any upstream `allowed-tools` declarations remain subject to the current host's permissions. Inspect referenced helper scripts and use the local site's actual PHP/WordPress tools where needed. A WordPress block-theme specialist does not require converting the default hybrid PHP theme, and motion guidance does not require adding animation to every page.

Local personal installs do not automatically appear on other computers or in remote/cloud sessions. Install the selected files in the environment doing the work or follow that product's documented sharing mechanism. This repository supplies a local installer; it does not register a marketplace plugin or synchronize accounts. Keep supporting-skill provenance and license information with the installed resources.
