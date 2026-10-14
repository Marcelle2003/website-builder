# Improve an existing website

## Inspect before choosing the change

Read project guidance, the website brief, dependency manifests, and relevant components. Inspect the supplied page in the browser when available, including a narrow viewport and the interaction mentioned. A screenshot alone cannot verify opening/closing, keyboard behaviour, or responsive layout.

Determine whether the problem comes from content clarity, missing imagery, hierarchy, visual consistency, or interaction. If the user asks whether to redesign, explain the smallest coherent intervention that addresses the evidence. If they request a specific change, complete that scope rather than imposing a redesign.

Preserve the brand elements and behaviour the user likes. Do not migrate the framework, install a CMS, change user roles, or alter publishing permissions for a visual request. Load only the relevant specialist guidance; apply it against actual installed versions.

## Make the requested improvement consistent

- **Content:** clarify what the business does, who can do what, and the next action. Check navigation, homepage, detail pages, forms, emails only if in scope, and empty/error states for conflicting wording. Copy must reflect implemented behaviour or clearly describe a future step.
- **Colour/type:** change semantic tokens first, then find stale literal values, gradients, opacity blends, SVG fills, borders, hover/focus/disabled states, and image overlays. Check representative pages and forms. Preserve semantic success/error distinctions. An exact colour request should not be silently replaced; show an accessible use of it or clearly explain any remaining contrast limitation.
- **Imagery:** use credible subject-matched assets and preserve user uploads/CMS overrides. Prefer a curated stable selection over a live random-image endpoint. See the source/credit requirements in [design guidance](design-and-motion.md).
- **Interaction:** improve the entire state change, including closing, interruption, keyboard use, reduced motion, and repeated navigation. A colour transition alone does not make an expandable panel animate.

Use project tokens and components so the correction applies consistently. Read [design and motion guidance](design-and-motion.md) when relevant. Avoid adding unrelated flourishes simply because a framework supports them.

## Deliver a reviewable result

Preserve unrelated local work. Use an existing repository's normal branch/checkpoint conventions, or a scoped recoverable backup where needed; do not commit unrelated files. Capture before/after views when they help assess a visual change.

Run the checks in [verification](verification.md) appropriate to the affected flows, fix demonstrated regressions, and update `WEBSITE_BRIEF.md`. Report what changed, where to view it, and what remains unverified. Continue implementing authorized changes until complete; a list of suggestions does not satisfy an implementation request.
