---
name: website-builder
description: Creates and improves custom WordPress themes with Tailwind CSS for nontechnical users. Use for Website Builder setup, preparing or refining a WordPress website, and reviewing recorded feedback about the Website Builder workflow.
---

# Website Builder

Let the user direct the creative work. Translate their business, audience, references, and feedback into a working website, using specialist skills for framework details. Ask about the visitor's experience rather than making the user choose technical architecture.

## Choose the requested mode

Read only the relevant workflow, plus the shared guidance needed for the change:

- **setup** — prepare this computer and install skills: [setup](references/setup.md) and [compatibility](references/compatibility.md).
- **setup-website** — prepare WordPress and a custom theme project: [project setup](references/setup-website.md).
- **create** — turn a brief into a website: [creation](references/create.md).
- **improve** — inspect and refine an existing site: [improvement](references/improve.md).
- **review-skill** — review recorded Website Builder feedback and propose reusable improvements: [skill review](references/review-skill.md). Apply or publish changes only within the user's authorization.

Mode names may appear in ordinary conversation. A request for discussion or a plan stays a discussion or a plan. A creation request in an empty folder includes necessary project preparation. An improvement request begins with the existing project, not scaffolding.

## Shared working approach

- Read project instructions and existing changes first. Continue from the user's decisions; preserve their business rules and requested scope. Visual/text work alone does not authorize account, permission, payment, or publishing changes.
- Load the relevant installed framework skills from [supporting skills](references/supporting-skills.md). Skills are files to discover and read; do not assume one agent has another agent's skill-calling API. Read referenced resources as needed. Compare technical advice against the installed versions and official docs. Never run a supporting script merely because its skill was loaded.
- Create concise, project-specific `AGENTS.md` instructions and a `CLAUDE.md` compatibility import for every new website, following [project instructions](references/project-instructions.md). Preserve and merge existing guidance when adopting a project; update instructions when architecture or verified commands change. These files direct future chats to this workflow without requiring repeated skill commands.
- The AI creates and maintains `WEBSITE_BRIEF.md` using [the brief template](assets/WEBSITE_BRIEF.md); the user is not expected to fill out a form. Record settled decisions from conversation, keep proposals and assumptions distinct, and update meaningful changes before handing work back. Read it on subsequent tasks instead of asking settled questions again. Preserve user edits and never store credentials there.
- During authorized Website Builder work, record meaningful verified workflow problems in a local `SKILL_FEEDBACK.md`, following [feedback tracking](references/feedback.md). The AI maintains it; distinguish site preferences from reusable issues and merge duplicate evidence. Keep it local by default. Observing a problem does not authorize changing or publishing the skill.
- Use [design and motion guidance](references/design-and-motion.md) to develop layout, content, imagery, and movement together. Inspect reference interactions in a real browser when available; screenshots alone do not establish how they move. Use [verification](references/verification.md) for affected flows, including WordPress editing and the rendered site.
- Show an actual local preview when browser tools exist. Give concrete, small choices when feedback would change direction. Continue independent work while waiting; do not repeatedly ask permission for steps already authorized.
- End with what changed, where to view it, what was checked, and any actual limitation. Distinguish implemented behaviour from a proposed feature. A build pass is not proof that a browser interaction works.

## Default architecture

For new websites, use conventional WordPress on LAMP-compatible hosting with a custom hybrid theme: PHP templates and reusable components for distinctive layouts, Tailwind for styling, and WordPress editing controls for routine content. Use the block editor where it helps authors. Keep content types and business functionality that must survive a theme change in a companion plugin. The theme owns presentation. Astro and a headless CMS are not required.

Use CSS for simple movement and consider GSAP for coordinated timelines or scroll choreography when the design needs it. Animation is a design decision, not a reason to choose a theme type. Both hybrid and block themes can support expressive websites. Respect explicit requests for block themes and preserve an existing site's architecture; loading a supporting block-theme skill does not authorize converting it. Website Builder owns this hybrid architecture workflow rather than assuming an upstream skill supplies it.

Keep everyday text, imagery, and appropriate ordering editable in WordPress. Explain which structural changes are handled through AI or code, without promising an unbuilt visual layout editor. Do not impose a reference site's colours, font, imagery, motion intensity, industry, or account model on another website.
