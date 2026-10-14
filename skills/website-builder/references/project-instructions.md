# Persistent project instructions and the website brief

Use this when creating a website, adopting Website Builder into an existing project, or changing its architecture. Instructions belong to each website project, not just the toolkit repository. The user should be able to continue ordinary conversation in later chats without repeatedly naming the skill.

## Create the shared instructions

For every new website, write a concise project-root `AGENTS.md` adapted from [the template](../assets/AGENTS.md.template). Generate it from inspected files and verified decisions; do not leave authoring placeholders or assume the default stack was actually installed. Include:

- Actual frontend/backend directories, installed framework versions or the authoritative manifests, and the responsibility of each part.
- How content reaches the frontend, what editors can change, and the real publish/refresh path.
- A direction to read `WEBSITE_BRIEF.md` before website work and to load the installed `website-builder` skill for relevant implementation tasks, with framework skills loaded only as needed.
- A direction to maintain local skill feedback when meaningful evidence arises, using [feedback tracking](feedback.md). Keep the brief's site decisions separate from reusable workflow observations; do not put private inbox paths in shared instructions.
- Verified run, build, and relevant check commands with their working directories. Reference a run guide for lengthy or OS-specific details; do not invent commands or label an unrun command verified.
- Project-specific design/business constraints and how to verify the affected flows. Keep evolving creative decisions in the brief instead of copying them into multiple instruction files.

Keep skill references portable: use the skill names and the host's discovered installation paths at runtime, not the author's home directory. Project instructions do not install missing skills. If a skill is absent, report that and use available project guidance for independent work; follow authorized setup when it is needed. Do not run installation merely because a fresh chat reads `AGENTS.md`.

Read the skill's relevant workflow instructions; do not expand its entire contents, supporting skills, or the whole brief into `AGENTS.md`. A small routing rule and concrete project facts are enough. Record future architecture/command changes in the same file as part of the authorized work.

## Add Claude Code compatibility

For a new project, add a sibling `CLAUDE.md` from [the import template](../assets/CLAUDE.md.template). It contains a literal `@AGENTS.md` line outside backticks and code fences. This imports the shared instructions instead of creating a second copy that can drift. Do not use a symlink or import a machine-specific absolute skill path.

For an existing project, inspect the effective instructions first: parent and nested `AGENTS.md`/overrides, `CLAUDE.md`/local files, `.claude/CLAUDE.md`, and existing Cursor rules as relevant. Preserve their scope and unrelated instructions. Add an import only where it is missing; use a relative path from the actual importing file (for example `@../AGENTS.md` from `.claude/CLAUDE.md`). Do not create a second competing Claude file or duplicate a working import. Preserve symlinks already managed by the owner; inspect their targets rather than replacing them.

Current Claude Code can read `AGENTS.md` directly in some configurations, but the import also supports sessions that do not. See [compatibility](compatibility.md) for documented loading differences. No global settings change or extra Cursor rule is needed for a new project using this arrangement. Inspect existing rules for conflicts rather than deleting or overriding them wholesale.

When adopting an existing site, add only missing relevant guidance during authorized project work. A review or discussion alone does not authorize file edits. Do not reconstruct the project or rewrite existing instruction files simply to match the templates.

## The AI maintains the brief

Create `WEBSITE_BRIEF.md` from information already supplied and observed. The owner need not understand Markdown or maintain it manually. Explain that it is the site's shared notes and that they can correct it through normal conversation or edit it themselves.

Update it as material decisions settle during authorized work and before a handoff: purpose, audience, scope, accepted visual direction, content sources, implemented behaviour, deferred requests, and actual verification. Read existing notes and preserve the owner's edits. Use the latest clear user decision when direction changes, recording a short superseded note only if it helps explain current work.

Separate confirmed decisions, agent assumptions, and open questions. An AI suggestion is not a user-approved decision; a discussed feature is not implemented functionality. Do not rewrite the brief after every message, store a transcript, or require approval for routine note-taking already in scope. Ask only when a conflicting or missing decision materially affects the work. Respect explicit instructions to discuss without changing files.

Keep technical commands/architecture in `AGENTS.md` and the run guide; keep the brief focused on this site's intent and current state. Exclude secrets and unnecessary personal information. On later tasks, read both before asking the owner to repeat context.

## Preserve local feedback across sessions

During authorized website work, the AI maintains `SKILL_FEEDBACK.md` for confirmed workflow issues, following [feedback tracking](feedback.md). Create it only when useful evidence exists, keep it out of routine commits, and retain records across skill updates. The owner can ask “Review the Website Builder feedback” to use the [review-skill maintenance mode](review-skill.md). A review alone produces proposals; changes to the reusable skill follow the user's authorized scope.

When preparing or adopting a website, include this routing in its project instructions and arrange the local ignore rules as described in feedback tracking. Preserve existing project rules and tracked files. Do not create a central inbox or change global agent instructions unless the user requests that configuration.

## Verify a fresh chat

After creating or materially changing the project instructions:

1. Check actual manifests, paths, commands, and the brief. Resolve stale references, duplicated imports, and conflicts with effective parent/nested rules. Confirm installed skills are discoverable in the environment that will do the work.
2. Where the host supports an isolated fresh-context agent/session within the authorized task, start it in the website project without copying the old conversation. Do not create a separate user-owned chat or contact another chat unless the user requested it. Ask: “Without changing files, explain this website's stack, where its decisions are recorded, which workflow you would use for a homepage change, and how you would verify that change.”
3. Compare the answer against the project. It should find the shared instructions and brief, use Website Builder when relevant, preserve existing constraints, and identify real commands. Use host context/instruction diagnostics when available; merely repeating the skill name is not evidence of loading.
4. If an isolated session or diagnostics are unavailable, perform the static checks, provide that harmless prompt for a later new chat, and report **fresh-chat loading unverified**. Keep independent website work moving; do not claim the test passed or demand that the owner repeat commands in every prompt.

Instructions improve continuity but cannot guarantee perfect compliance. Verify loading after changing agent, machine, workspace root, or instruction configuration. Test the installed target agent; a subagent that explicitly reads a file is a useful scenario review, not proof that every product auto-loads it.
