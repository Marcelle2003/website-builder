# Visual direction, imagery, and refined movement

These are design starting points, not a mandatory aesthetic. Follow the user's brand and audience. Do not reuse an unrelated project's palette, typeface, photographs, or business model.

## Establish the visual system

Start with purpose and hierarchy: a clear first screen, a primary action, supporting evidence, and readable content. Define semantic colour roles, typography, spacing, widths, borders, and image treatment centrally. Give the site intentional variation without making every section a different design system.

Translate reference images into an explicit palette and design choices; don't merely approximate the dominant colour. Check rendered text, surfaces, hover/focus states, gradients, opacity, and form defaults together. Use accessible text/background pairings. Self-host fonts when their licence and project requirements permit, with only needed weights and robust fallbacks.

## Choose credible images

Ask for supplied assets only when necessary to the task; use available assets or suitable placeholders while independent work continues. Match the kind of photography to the site. Ordinary marketplace inventory may need honest, uneven product photos; a studio portfolio may need art-directed work. More polished is not automatically more appropriate.

For internet images, find subject-relevant sources with clear usage terms. Record the creator, source page, licence, any required attribution, and modifications in the project. Use stable assets; download and optimize only when source terms and the agent's tools permit it. Otherwise retain supported embeds or ask for usable files. Avoid unlicensed search-result copying, unstable random endpoints, and unsupported claims that demo photos depict real inventory.

Preserve actual uploads and CMS-selected images. Provide source/credit UI when required. Use meaningful alt text for informative images and empty alt text for decoration. Set dimensions, choose contain versus crop deliberately, generate responsive sizes, and lazy-load below-the-fold media. Do not hide a whole product merely to make thumbnails uniform.

## Introduce motion in useful passes

For a broad request to bring a site to life, these passes provide an order of work. Skip passes outside the user's scope or without a clear benefit.

1. **Expandable controls:** menus, FAQs, filters, disclosure panels. Animate both opening and closing; keep icons and panel state synchronized. Support varying content height and rapid toggling. Do not hide or remove the content before the closing animation finishes, or leave hidden controls in the tab order. Preserve semantic disclosure behaviour, keyboard activation, accurate expanded state, and a usable fallback if scripting fails. Modal menus also need appropriate focus containment, Escape, focus return, and scroll restoration.
2. **Controls and cards:** subtle hover, focus, press, selected, and disabled states. Use a small colour, border, shadow, or transform change that confirms interactivity. Essential information must be available without hovering. Disabled controls should not look active, and keyboard focus should remain obvious.
3. **Navigation and galleries:** maintain continuity between views when it helps orientation. Use stable unique transition identities; verify back/forward behaviour and direct links. Check script setup/cleanup under Astro navigation so listeners do not duplicate and controls work after each visit. Keep native navigation if router complexity has no benefit.
4. **Content arrival and status feedback:** restrained reveals, filter changes, loading, empty, error, and success states. Never conceal essential content indefinitely waiting for an observer. No decorative delay before users can act. Announce meaningful asynchronous results without noisy repeated announcements.
5. **Final tuning:** align timing/easing across components, remove gratuitous movement, and test reduced motion, touch, keyboard, low-width layouts, and repeated interactions. Do not add this as a separate permission gate for already authorized work.

For a calm starting point, try roughly 120–180 ms for control feedback and 180–280 ms for disclosures; tune to distance, content, and the user's desired character. These are adjustable design defaults. Prefer specific transition properties over `transition-all`; use transform/opacity where appropriate and deliberate height animation for content expansion. Avoid continuous motion without a functional reason.

Use Tailwind state and responsive variants where they clarify implementation, and small CSS/JavaScript primitives where necessary. Tailwind does not itself manage focus or disclosure state. Reduced-motion preferences should remove unnecessary movement while preserving the final visible state and feedback.

Consult current primary references for implementation: [Tailwind transitions](https://tailwindcss.com/docs/transition-property), [state variants and reduced motion](https://tailwindcss.com/docs/hover-focus-and-other-states), [Astro view transitions](https://docs.astro.build/en/guides/view-transitions/), and [ARIA disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/).
