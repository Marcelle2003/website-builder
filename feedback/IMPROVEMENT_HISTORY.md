# Website Builder improvement history

This is the public record of approved, reusable toolkit changes. Keep raw project observations, client details, and local inbox configuration outside this repository. See [feedback recording](../skills/website-builder/references/feedback.md) and [skill review](../skills/website-builder/references/review-skill.md) for the workflow.

## v0.3.0 — Evidence-based skill improvements

**Problem:** Website work can expose useful improvements to the toolkit, but those observations need continuity, evidence, and a distinction between a site's preferences and reusable guidance.

**Approved change:** Add AI-maintained local `SKILL_FEEDBACK.md` records with stable IDs, provenance, deduplication, and review status. Support an optional user-designated local inbox. Add `review-skill` to evaluate the actual source and propose narrow changes; apply and publish within the user's authorization. Keep observations separate from the website brief and public release history. Route this workflow through project instruction templates and the existing website modes.

**Verification:** The 14 offline installer tests, skill validation, and resource-link checks passed on Linux. Isolated upgrades from v0.2.0 into the Codex, Claude Code, and Cursor project destinations copied the new resources, preserved recoverable backups and project notes/configuration/inbox contents, and left repeat installs unchanged. An independent synthetic scenario exercised deduplication, evidence uncertainty, an unavailable inbox, project-specific preferences, and a read-only review that correctly proposed no source change. See [validation scope](../VALIDATION.md) for the scope and limitations. Published versions and CI results are independently visible in [GitHub releases](https://github.com/Marcelle2003/website-builder/releases) and [workflow runs](https://github.com/Marcelle2003/website-builder/actions).

## v0.2.0 — Project continuity

**Problem:** Ordinary requests in later chats need the website's architecture, decisions, skill routing, and verification commands without requiring the owner to repeat the original setup instructions.

**Approved change:** Generate concise project-specific `AGENTS.md` instructions with a `CLAUDE.md` compatibility import, preserve existing rules, and have the AI maintain `WEBSITE_BRIEF.md` from conversations. Distinguish accepted decisions from assumptions and proposals.

**Verification:** Installer tests and resource checks passed. Temporary new/existing project scenarios preserved owner content and existing instructions. A separate read-only Codex session found the workflow through project instructions without an explicit skill invocation. Claude/Cursor application loading was not exercised. See [validation scope](../VALIDATION.md) and the [v0.2.0 release](https://github.com/Marcelle2003/website-builder/releases/tag/v0.2.0).
