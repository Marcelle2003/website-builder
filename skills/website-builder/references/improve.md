# Improve an existing website

## Inspect before choosing the change

Read project guidance, the website brief, dependency manifests, and relevant components. For WordPress, establish the active parent/child theme, classic/hybrid/block architecture, editor or builder in use, and relevant plugins before choosing where to change it. Inspect the supplied page in the browser when available, including a narrow viewport and the interaction mentioned. A screenshot alone cannot verify opening/closing, keyboard behaviour, or responsive layout.

Preserve existing instruction files and their scope. When adopting Website Builder into the project, merge missing relevant guidance using [project instructions](project-instructions.md); do not overwrite existing rules with the template. If the brief is missing during authorized implementation, create it from available facts and conversation rather than making the owner fill it out.

Determine whether the problem comes from content clarity, missing imagery, hierarchy, visual consistency, or interaction. If the user asks whether to redesign, explain the smallest coherent intervention that addresses the evidence. If they request a specific change, complete that scope rather than imposing a redesign.

Preserve the brand elements and behaviour the user likes. Do not migrate the framework, replace a page builder, convert a block theme to hybrid, change user roles, or alter publishing permissions for a visual request. Load only the relevant specialist guidance; apply it against actual installed versions. In a parent theme managed by an upstream vendor, use the project's supported extension or child-theme approach rather than edits that an update will erase.

Check where the rendered output actually originates. WordPress content, saved Site Editor templates/styles, a builder, plugins, and caches can override or outlast theme-file changes. Do not delete editor customizations to force a result; preserve the existing design and reconcile the specific source of the requested change. Verify both the visitor view and affected editor controls.

## Make the requested improvement consistent

- **Content:** clarify what the business does, who can do what, and the next action. Check navigation, homepage, detail pages, forms, emails only if in scope, and empty/error states for conflicting wording. Copy must reflect implemented behaviour or clearly describe a future step.
- **Colour/type:** change semantic tokens first, then find stale literal values, gradients, opacity blends, SVG fills, borders, hover/focus/disabled states, and image overlays. Check representative pages and forms. Preserve semantic success/error distinctions. An exact colour request should not be silently replaced; show an accessible use of it or clearly explain any remaining contrast limitation.
- **Imagery:** use credible subject-matched assets and preserve user uploads/CMS overrides. Prefer a curated stable selection over a live random-image endpoint. See the source/credit requirements in [design guidance](design-and-motion.md). Write alt text on informative images you add or replace, and give decorative images an empty alt. Generate WebP sub-sizes for new JPEG and PNG uploads when the server can encode them. Do not convert the existing library unless the owner asks.
- **Forms/tracking:** follow [Cognito Forms guidance](cognito-forms.md) when creating or changing forms or adopting the site-wide baseline. Preserve existing provider decisions, mappings and submission workflows; a visual-only request does not authorize replacing them.
- **Site identity:** when setup/branding is in scope, follow the [favicon prompt and verification](site-icon.md); preserve an existing icon or recorded skip.
- **Interaction:** improve the entire state change, including closing, interruption, keyboard use, reduced motion, and repeated navigation. A colour transition alone does not make an expandable panel animate. For broader creative work, inspect reference interactions and propose purposeful sequences alongside the layout; do not restrict every design to generic fade-ins.
- **Search:** when a new page is added or the offer changes, follow [search-led page building](seo-and-ai-search.md), including a Keyword Planner query for that market. Preserve an existing primary keyword unless the owner changes the offer. Use the country or place already recorded in the brief. Ask when the market was never established, and do not invent one. On any public page this improvement changes, keep one H1, an H2/H3 outline that follows the sections, the document title, and one meta description. Do not rerun Keyword Planner or rewrite settled keywords for an unrelated visual fix.
- **Assets:** when theme CSS or JavaScript changes, version that file with its modification time or a content hash. Leave image and font URLs cacheable, and do not restyle the site to change caching. Follow [environment-specific indexing checks](seo-and-ai-search.md#indexing-urls-and-launch) before changing “discourage search engines”; preserve production behaviour if a database is shared. Do not turn it on for a live site that should stay indexed.

Use project tokens and components so the correction applies consistently. When the same type, colour, button, container width, or business detail (name, phone, address) disagrees across pages, name the pages and the measured values, then fix the shared source. Report that spread before a broad restyle. Read [design and motion guidance](design-and-motion.md) when relevant. Avoid adding unrelated flourishes simply because a framework supports them.

## Deliver a reviewable result

Preserve unrelated local work. Use an existing repository's normal branch/checkpoint conventions, or a scoped recoverable backup where needed; do not commit unrelated files. Capture before/after views when they help assess a visual change.

Run the checks in [verification](verification.md) appropriate to the affected flows, fix demonstrated regressions, and update `WEBSITE_BRIEF.md` yourself. Update affected project instructions when architecture or commands change, preserving unrelated rules. Report what changed, where to view it, and what remains unverified. Continue implementing authorized changes until complete; a list of suggestions does not satisfy an implementation request.

If the work exposes a confirmed reusable workflow problem, follow [feedback tracking](feedback.md) to record it locally and merge duplicate evidence. A site preference or ordinary project bug does not automatically imply a missing skill rule. Recording feedback does not authorize changes to the source skill or public uploads.
