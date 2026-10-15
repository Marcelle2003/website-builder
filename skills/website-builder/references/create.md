# Create a website

## Understand the website before designing it

Read the current brief and supplied material. Establish the purpose, intended visitors, primary action, essential pages/content, and visual references. Ask the few missing questions that would materially change the result; use small batches and familiar terms. Make ordinary implementation decisions yourself.

Explain what the site does on the homepage. An About page can develop the story; it cannot repair an unclear first impression. Use honest draft copy and explicitly labelled demonstration content. Do not invent client testimonials, credentials, partner logos, or business capabilities.

If the user is still exploring direction, describe one recommended direction and a small number of meaningful alternatives. For an implementation request with enough context, proceed to a reviewable first version using stated assumptions. Do not force a separate approval for every component.

## Develop a coherent first version

Prepare missing infrastructure via [project setup](setup-website.md), including the [persistent project instructions](project-instructions.md). Create the brief yourself from the conversation using the [template](../assets/WEBSITE_BRIEF.md); do not ask the owner to complete it as a form. Load the relevant specialist skills and [design and motion guidance](design-and-motion.md).

Inspect supplied reference websites in a browser when available, including scrolling, opening and closing menus, and transitions between pages. Separate observed behaviour from ideas inferred from a screenshot. Translate the references into a direction suited to this business, including where movement adds character or explains relationships.

Build a representative page with the real navigation, typography, colour roles, content hierarchy, images, mobile behaviour, and proposed signature interaction where appropriate. Establish reusable theme components and tokens from that page, then carry the direction through the requested pages. Use real content lengths early so a design does not depend on unrealistically short copy.

## Build the theme and its editing model together

For the default hybrid approach, keep distinctive layouts and animation sequences in PHP templates and reusable theme components. Model routine content in WordPress: for example, a project has a title, description, category, images, and optional case-study content. Use the block editor for suitable page bodies and reusable sections; expose only the layout controls that editors actually need. Keep durable content types, taxonomies, and business behaviour in a companion plugin so they survive a theme change. Do not install a field plugin or paid dependency unless the chosen editing model needs it and its use is authorized.

Explain editing through a concrete example: an editor changes a project's images and copy in WordPress; the theme supplies its layout and movement. AI can change that design when requested. A custom theme does not automatically provide a drag-and-drop editor, and a block theme is also a valid choice when full visual layout editing is wanted.

Use WordPress APIs for content, media, menus, asset loading, and template hooks. Match frontend styles and editor presets deliberately, using `theme.json` where useful. Keep colour and typography roles aligned with Tailwind tokens rather than maintaining competing design systems. Build CSS from classes present in theme/plugin source; map editor choices to complete known classes or CSS variables rather than expecting Tailwind to scan arbitrary database content. Load page-specific scripts only where needed.

Implement simple transitions in CSS; add a coordinated animation library only for sequences that justify it. Read [design and motion guidance](design-and-motion.md) for reference inspection, choreography, and accessible fallbacks. Do not add a frontend framework, headless API, or client-side router merely to make the stack look sophisticated.

## Refine with the user

Open the working preview and describe two or three concrete design decisions they can evaluate. Incorporate requested changes consistently across representative page types and states. Maintain the brief with accepted direction and deferred work; keep suggestions separate from decisions. Update project instructions if architecture or commands changed.

Use [verification](verification.md) before delivery. Explain how to open the preview and edit content, and distinguish a locally working site from a deployed one. When asked how the stack helped, connect each implemented feature to its visible or operational benefit; do not advertise unused features.

Record meaningful verified workflow problems locally through [feedback tracking](feedback.md) as they arise. Merge repeated evidence and keep the owner's creative choices in the brief. Mention only actionable pending improvements at a useful milestone; complete the website request without turning feedback into an unsolicited skill rewrite.
