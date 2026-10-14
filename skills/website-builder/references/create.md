# Create a website

## Understand the website before designing it

Read the current brief and supplied material. Establish the purpose, intended visitors, primary action, essential pages/content, and visual references. Ask the few missing questions that would materially change the result; use small batches and familiar terms. Make ordinary implementation decisions yourself.

Explain what the site does on the homepage. An About page can develop the story; it cannot repair an unclear first impression. Use honest draft copy and explicitly labelled demonstration content. Do not invent client testimonials, credentials, partner logos, or business capabilities.

If the user is still exploring direction, describe one recommended direction and a small number of meaningful alternatives. For an implementation request with enough context, proceed to a reviewable first version using stated assumptions. Do not force a separate approval for every component.

## Develop a coherent first version

Prepare missing infrastructure via [project setup](setup-website.md). Record the brief with the [template](../assets/WEBSITE_BRIEF.md). Load the relevant specialist skills and [design and motion guidance](design-and-motion.md).

Build a representative page with the real navigation, typography, colour roles, content hierarchy, images, and mobile behaviour. Establish reusable components and tokens from that page, then carry the direction through the requested pages. Use real content lengths early so a design does not depend on unrealistically short copy.

Make routine business content editable in Wagtail. Keep stable layout/interaction code in Astro; model appropriate sections as content blocks when editors need to add or reorder them. Explain the available editing controls in plain language. Do not promise a visual drag-and-drop layout editor unless one has actually been built.

Choose useful Astro and Tailwind capabilities: reusable layouts, optimized responsive images, static or server-rendered content appropriate to publishing, scoped interactive islands where needed, responsive utility composition, explicit state variants, and shared tokens. Do not add a client framework or heavy animation library just to make the technology visible.

## Refine with the user

Open the working preview and describe two or three concrete design decisions they can evaluate. Incorporate requested changes consistently across representative page types and states. Update the brief with accepted direction and deferred work.

Use [verification](verification.md) before delivery. Explain how to open the preview and edit content, and distinguish a locally working site from a deployed one. When asked how the stack helped, connect each implemented feature to its visible or operational benefit; do not advertise unused features.
