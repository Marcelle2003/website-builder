# Agent compatibility

Website Builder uses the shared Agent Skills format: a `website-builder` folder containing `SKILL.md`, YAML `name` and `description`, Markdown instructions, and supporting files. Keep these two fields present, the name lowercase with hyphens, and the folder name matching it. The core workflow does not depend on host-specific argument substitution, hooks, subagent types, or tool names.

The local installer needs Python 3.10+ and installs files for the **selected** agent. It does not install the agent application or sign the user in. Supporting skills can have additional runtime requirements; the official Wagtail helper requires its separate CLI and Python 3.12+. These locations describe local coding-agent sessions, not every hosted product with a similar name. Official documentation was checked on 2026-10-14; recheck it if an installed client behaves differently.

## Installation destinations

- **Codex:** user scope goes to `~/.agents/skills/website-builder/`; project scope goes to `<project>/.agents/skills/website-builder/`. Codex discovers repository skill roots up to the repository root. Mention `$website-builder` or select it from the skills UI; CLI and IDE documentation also describe `/skills`. [Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
- **Cursor:** user scope goes to `~/.cursor/skills/website-builder/`; project scope goes to `<project>/.cursor/skills/website-builder/`. Invoke `/website-builder` through Agent chat's skill picker. Cursor also discovers `.agents/skills/` and compatibility locations such as `.claude/skills/`, including personal equivalents. Install one selected copy rather than scattering duplicates across these roots. [Official Cursor skill documentation](https://cursor.com/docs/skills)
- **Claude Code:** user scope goes to `~/.claude/skills/website-builder/`; project scope goes to `<project>/.claude/skills/website-builder/`. Invoke `/website-builder`. Its documented local discovery does not include `.agents/skills/`; placing a copy there for Codex does not by itself install it for Claude Code. [Official Claude Code skill documentation](https://code.claude.com/docs/en/skills)

Here `~` means the current user's home directory; on Windows this is normally under `C:/Users/<name>`. The installer resolves it through Python, so the user need not create literal `~` folders. Native Windows and WSL homes are separate. Installing for another agent later is an explicit second selection, not an automatic side effect of setup.

## One skill, four modes

`setup`, `setup-website`, `create`, and `improve` are choices interpreted by Website Builder's instructions. They are not four new slash commands. Supply the choice as ordinary text with the named skill:

```text
Codex:       $website-builder setup
Cursor:      /website-builder setup
Claude Code: /website-builder setup
```

The same pattern works with the other mode names and a short request, such as `/website-builder improve the mobile navigation`. A plain-language alternative is “Use the Website Builder skill in setup-website mode for this project.” If the skill is not discovered, resolve installation first; merely mentioning its name does not make missing files available.

Claude Code supports `$ARGUMENTS` and positional substitution in its own skill bodies. Cursor's current skill documentation does not promise equivalent substitution. This toolkit therefore reads the user's mode and brief as conversational input rather than embedding those macros. Four separate picker entries would require separate skills or host-specific command definitions. [Claude arguments](https://code.claude.com/docs/en/skills#pass-arguments-to-skills), [Cursor invocation](https://cursor.com/docs/skills#how-skills-work)

## Discovery and capabilities

After installing, check the host's actual skill inventory. Codex detects skill changes automatically; restart it if the update does not appear. Cursor discovers skills at startup and exposes them in Customize → Skills; start a fresh session or restart if necessary. Claude Code watches existing skill roots; `/reload-skills` discovers a newly created top-level root. Avoid repeatedly installing duplicates to fix a stale picker. [Codex discovery](https://learn.chatgpt.com/docs/build-skills), [Cursor discovery](https://cursor.com/docs/skills#viewing-skills), [Claude reload behavior](https://code.claude.com/docs/en/skills#edit-a-skill-during-a-session)

The workflow adapts to the host's available terminal, file, browser, research, image, and delegation tools. A portable skill does not guarantee those capabilities or their permissions. Use available equivalents, preserve each host's authorization rules, and identify a missing capability only when it blocks the requested outcome. In particular, a successful text build does not prove browser or visual verification occurred.

The official `wagtail` supporting skill is a small index that retrieves its working instructions from `wt skills get core`. Follow [setup.md](setup.md) to prepare the pinned `wagtail-cli` runtime in isolation. Its host-specific `allowed-tools` frontmatter does not grant universal permissions; use the current agent's normal terminal controls. The alpha CLI's API client targets Wagtail v3, so an existing v2 content API must continue using its appropriate integration. Reading the helper's documentation does not require enabling v3 or upgrading a website. [Pinned Wagtail helper](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/skills/wagtail/SKILL.md)

Local personal installs do not automatically appear on other computers or in remote/cloud sessions. Install the selected files in the environment doing the work or follow that product's documented sharing mechanism. This repository supplies a local installer; it does not register a marketplace plugin or synchronize accounts. Keep supporting-skill provenance and license information with the installed resources.
