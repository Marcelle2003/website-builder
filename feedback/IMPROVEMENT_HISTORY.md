# Website Builder improvement history

This is the public record of approved, reusable toolkit changes. Keep raw project observations, client details, and local inbox configuration outside this repository. See [feedback recording](../skills/website-builder/references/feedback.md) and [skill review](../skills/website-builder/references/review-skill.md) for the workflow.

## v0.4.2 branch — Runtime safeguards and observable verification

**Problem:** Nested local runtimes can contaminate authored-component detection, and sandbox visibility can be mistaken for a stopped database. Successful extraction, editor fallback saves, dispatched downloads and technically running animations can also be overstated as verified outcomes.

**Approved change:** Separate authored-component feature evidence from runtime inventory while retaining workspace build manifests and sibling components. Check host runtime visibility before restarting services. Verify extracted WordPress core and scope recovery to affected core files. Record visual editing separately from code saves, and file delivery separately from clicks. Make requested motion demos noticeable and provide their location/trigger. Retain v0.4.1's general scroll/hover direction and optional interaction transitions, adding form-step transitions explicitly. These are reusable workflow clarifications; uncertain browser/extractor causes remain unresolved. No upstream detector, runtime dependency or website implementation changes.

**Verification:** All 20 offline installer tests, skill format validation, local resource links and diff checks passed on Linux. Isolated v0.4.1-to-v0.4.2 upgrades into all three supported agent destinations preserved old-version backups and fixture briefs; repeat installation was unchanged. Manual scenario review covered scoped triage, host visibility, incomplete extraction, editor/download uncertainty and motion scope. It was not an independent agent or live website test. See [validation scope](../VALIDATION.md). This is a branch update, not a tagged release.

## v0.4.1 branch — Scroll and hover movement defaults

**Problem:** A broad request to add movement did not explicitly establish scroll animation and hover/focus feedback as the starting direction.

**Approved change:** Add those defaults with selective use, plus optional entrance sequences, disclosures, action feedback, content transitions, and navigation feedback. Preserve narrow requests and explicit static designs. Specify touch behaviour, reduced-motion visibility, normal scrolling, and creative justification for heavier effects. Add corresponding browser verification guidance. Supporting skill versions and runtime dependencies are unchanged.

**Verification:** All 20 offline installer tests, skill format validation, local Markdown resource-link checks, and diff checks passed on Linux. A manual instruction walkthrough covered a broad movement request, an FAQ-only fix, a static-design exception, and touch/reduced-motion use. This was an instruction review, not an independent agent test or an executed website animation. Version 0.4.1 is a branch update, not a tagged release.

## v0.4.0 branch — Custom WordPress theme workflow

**Problem:** Teams maintaining conventional WordPress sites need AI-assisted creative development without a new CMS or a headless deployment. Bespoke motion and layouts also need a clear editing model and relevant specialist guidance.

**Approved change:** Default new projects to custom hybrid WordPress themes with Tailwind on LAMP-compatible hosting, retaining existing architectures when improving a site. Add intentional, browser-verified motion design and optional GSAP guidance. Replace the default Astro/Wagtail supporting pack with selected official WordPress skills, Tailwind, and frontend-design; provide explicit optional selections with dependency resolution and source-archive reuse. Pin reviewed sources, preserve their licenses, and document observed upstream caveats. Retain all five modes, AI-maintained project instructions/brief, and local feedback. Publish this work on `wordpress-theme-builder`; it is not a tagged release or a change to `main`.

**Verification:** All 20 offline installer tests, skill validation, resource-link checks, and diff checks passed locally. A temporary live install and unchanged repeat covered all 15 supporting skills plus Website Builder; installation paths for all three agents and a recoverable v0.3.0 upgrade were checked on Linux. Independent workflow and implementation reviews covered environment reuse, narrow improvements, hybrid detection, and installer behaviour. No full WordPress site, animation, or physical Mac setup was executed. See [validation scope](../VALIDATION.md) for precise evidence and limitations.

## v0.3.0 — Evidence-based skill improvements

**Problem:** Website work can expose useful improvements to the toolkit, but those observations need continuity, evidence, and a distinction between a site's preferences and reusable guidance.

**Approved change:** Add AI-maintained local `SKILL_FEEDBACK.md` records with stable IDs, provenance, deduplication, and review status. Support an optional user-designated local inbox. Add `review-skill` to evaluate the actual source and propose narrow changes; apply and publish within the user's authorization. Keep observations separate from the website brief and public release history. Route this workflow through project instruction templates and the existing website modes.

**Verification:** The 14 offline installer tests, skill validation, and resource-link checks passed on Linux. Isolated upgrades from v0.2.0 into the Codex, Claude Code, and Cursor project destinations copied the new resources, preserved recoverable backups and project notes/configuration/inbox contents, and left repeat installs unchanged. An independent synthetic scenario exercised deduplication, evidence uncertainty, an unavailable inbox, project-specific preferences, and a read-only review that correctly proposed no source change. See [validation scope](../VALIDATION.md) for the scope and limitations. Published versions and CI results are independently visible in [GitHub releases](https://github.com/Marcelle2003/website-builder/releases) and [workflow runs](https://github.com/Marcelle2003/website-builder/actions).

## v0.2.0 — Project continuity

**Problem:** Ordinary requests in later chats need the website's architecture, decisions, skill routing, and verification commands without requiring the owner to repeat the original setup instructions.

**Approved change:** Generate concise project-specific `AGENTS.md` instructions with a `CLAUDE.md` compatibility import, preserve existing rules, and have the AI maintain `WEBSITE_BRIEF.md` from conversations. Distinguish accepted decisions from assumptions and proposals.

**Verification:** Installer tests and resource checks passed. Temporary new/existing project scenarios preserved owner content and existing instructions. A separate read-only Codex session found the workflow through project instructions without an explicit skill invocation. Claude/Cursor application loading was not exercised. See [validation scope](../VALIDATION.md) and the [v0.2.0 release](https://github.com/Marcelle2003/website-builder/releases/tag/v0.2.0).
