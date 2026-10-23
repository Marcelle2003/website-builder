# Visual direction, imagery, and refined movement

These are design starting points, not a mandatory aesthetic. Follow the user's brand and audience. Do not reuse an unrelated project's palette, typeface, photographs, or business model.

## Establish the visual system

Start with purpose and hierarchy: a clear first screen, a primary action, supporting evidence, and readable content. Define semantic colour roles, typography, spacing, widths, borders, and image treatment centrally. Give the site intentional variation without making every section a different design system.

Translate reference images into an explicit palette and design choices; don't merely approximate the dominant colour. Check rendered text, surfaces, hover/focus states, gradients, opacity, and form defaults together. Use accessible text/background pairings. Self-host fonts when their licence and project requirements permit, with only needed weights and robust fallbacks.

## Choose credible images

Ask for supplied assets only when necessary to the task; use available assets or suitable placeholders while independent work continues. Match the kind of photography to the site. Ordinary marketplace inventory may need honest, uneven product photos; a studio portfolio may need art-directed work. More polished is not automatically more appropriate.

For internet images, find subject-relevant sources with clear usage terms. Record the creator, source page, licence, any required attribution, and modifications in the project. Use stable assets; download and optimize only when source terms and the agent's tools permit it. Otherwise retain supported embeds or ask for usable files. Avoid unlicensed search-result copying, unstable random endpoints, and unsupported claims that demo photos depict real inventory.

Preserve actual uploads and CMS-selected images. Provide source/credit UI when required. Use meaningful alt text for informative images and empty alt text for decoration. Set dimensions, choose contain versus crop deliberately, generate responsive sizes, and lazy-load below-the-fold media. Do not hide a whole product merely to make thumbnails uniform.

## Design movement alongside the layout

Motion can express a site's character as well as confirm an action. When the brief includes animated references, open them in an actual browser where tools permit and exercise scrolling, menus, filters, and page navigation. Record what moved, what triggered it, how it ended, and what remained usable throughout. Distinguish observed behaviour from guesses; do not infer a library or framework from appearance. If browser inspection is unavailable, say which interactions remain unverified instead of describing imagined animation as evidence.

Recommend a coherent motion direction with the page composition. A quiet business site may need only smooth disclosures and responsive controls. A creative portfolio may benefit from changing typography, a choreographed menu, or a scroll sequence connecting project imagery and narrative. References such as [Jozue](https://jozue.fr/) and [Webdrift](https://www.webdrift.be/en) illustrate possibilities, not a required visual style or a template to copy.

For a signature sequence, define its purpose, trigger, participating elements, editable content, ending state, and small-screen/reduced-motion treatment before building it. Keep text and images editable without requiring an editor to calculate animation timings. Prototype the sequence with realistic content and verify it in motion before repeating the pattern elsewhere. Do not make content lengths or viewport heights depend on a single desktop screenshot.

## Interpret requests for movement

For a broad request such as “add movement” or “bring the website to life,” include both scroll-triggered animation and hover/focus feedback as the starting direction. Choose a small, coherent set that fits the brand and content; do not animate every element. Preserve explicit requests for a static experience or a narrower change: fixing an FAQ does not authorize adding effects across the site.

- **Scroll reveals:** introduce selected sections, images, or groups as they enter view with restrained opacity/position changes. Prefer revealing once over replaying on every scroll. Keep content accessible on direct links, restored scroll positions, and when scripts fail; avoid long stagger chains that make visitors wait.
- **Hover and focus:** give links, buttons, cards, and image-led actions clear feedback through colour, underline, border, shadow, or a small transform. Provide equivalent keyboard focus feedback where appropriate. Apply hover-specific movement only to devices that support hover; touch users must be able to act immediately without a first tap merely revealing an action.
- **Expand and collapse:** smoothly open and close menus, FAQs, filters, and accordions, following the disclosure behaviour below.
- **Entrance sequences:** optionally coordinate a brief hero heading, image, and call-to-action introduction. Keep navigation and actions available immediately; skip decorative introductions when revisiting if they would interrupt the task.
- **Interaction feedback:** use press states and meaningful form, cart, or other action feedback to show what happened. Animation must reflect the real pending, success, or error state, never imply an unconfirmed success.
- **Content transitions:** gently connect changes between form steps, tabs, gallery slides, testimonials, or filtered results while keeping selection, focus, and content state clear. Avoid adding autoplay merely to create movement.
- **Navigation feedback:** consider a compact header on scroll or an active-section indicator when useful for orientation. Avoid layout jumps, obscured anchor targets, and headers that interfere with keyboard focus.

A useful baseline is scroll reveals, hover/focus feedback, and smooth expandable elements where those components exist. Entrance sequences, content transitions, and navigation effects are options, not a mandatory checklist. Reserve parallax, pinned sections, large transforms, and elaborate scroll choreography for a deliberate creative direction; preserve normal scrolling and a simpler mobile experience. Honour reduced-motion preferences from the outset, with visible content and usable controls when decorative motion is removed. Record the chosen direction and any user exceptions in the website brief.

## Make a motion preview easy to evaluate

When the user asks to see an animation example, choose one clearly visible sequence in an identifiable section, preferably encountered early in ordinary browsing. Make the change legible at the actual viewport and normal scrolling speed; a tiny movement hidden far down the page can fail as a demo even when its code works. Explain where to scroll or hover and what should change. Keep a later section if it better serves the design, but provide a direct route and trigger instructions.

Show the sequence in motion, including its ending state, before repeating it elsewhere. Adjust distance, contrast, pacing or composition when the user cannot see the effect, while keeping text readable, actions available, and touch/reduced-motion alternatives usable. A request for a noticeable demo is not a universal requirement for intense animation or pinned/parallax sections on future websites.

## Choose the smallest suitable implementation

Use CSS and Tailwind state variants for simple feedback, reveals, and transitions. Consider GSAP timelines and ScrollTrigger when multiple elements need coordinated sequencing, scrubbing, or pinning. Load the relevant optional skills and their review notes through [supporting skills](supporting-skills.md), then check the actual library version and official documentation. An installed animation skill does not mean every site needs its runtime.

In WordPress, enqueue assets through the theme/plugin APIs and load heavier interaction code only where it is used. Keep animation behaviour with the component it controls. Avoid fragile selectors that depend on incidental editor markup. Use appropriate setup and cleanup for the actual navigation and rendering lifecycle; account for viewport changes and media loading when calculating positions. Prefer native document navigation unless the requested experience justifies a more complex page-transition system. Do not introduce a client-side router solely to make a transition possible.

Both hybrid and block themes can provide these effects. Hybrid templates keep intricate sequences in code; custom blocks can expose carefully chosen content and layout controls when the editing model calls for them. Keep design decisions separate from theme-type assumptions.

## Implement and refine the affected interactions

For a broad request to bring an existing site to life, these passes provide an order of work. For a new expressive site, develop its signature sequence alongside the representative page. Skip anything outside the user's scope or without a clear benefit.

1. **Expandable controls:** menus, FAQs, filters, disclosure panels. Animate both opening and closing; keep icons and panel state synchronized. Support varying content height and rapid toggling. Do not hide or remove the content before the closing animation finishes, or leave hidden controls in the tab order. Preserve semantic disclosure behaviour, keyboard activation, accurate expanded state, and a usable fallback if scripting fails. Modal menus also need appropriate focus containment, Escape, focus return, and scroll restoration.
2. **Controls and cards:** subtle hover, focus, press, selected, and disabled states. Use a small colour, border, shadow, or transform change that confirms interactivity. Essential information must be available without hovering. Disabled controls should not look active, and keyboard focus should remain obvious.
3. **Navigation and galleries:** maintain continuity between views when it helps orientation. Use stable unique transition identities if the chosen technique needs them; verify back/forward behaviour and direct links. Check setup/cleanup so listeners do not duplicate and controls work after each visit. Keep native navigation if router complexity has no benefit.
4. **Content arrival and status feedback:** restrained reveals, filter changes, loading, empty, error, and success states. Never conceal essential content indefinitely waiting for an observer. No decorative delay before users can act. Announce meaningful asynchronous results without noisy repeated announcements.
5. **Final tuning:** align timing/easing across components, remove gratuitous movement, and test reduced motion, touch, keyboard, low-width layouts, and repeated interactions. Do not add this as a separate permission gate for already authorized work.

For a calm starting point, try roughly 120–180 ms for control feedback and 180–280 ms for disclosures; tune to distance, content, and the user's desired character. These are adjustable defaults, not timing limits for deliberate narrative sequences. Prefer specific transition properties over `transition-all`; use transform/opacity where appropriate and deliberate height animation for content expansion. Continuous decorative motion needs a clear design purpose and appropriate pause/reduced-motion treatment.

Use Tailwind state and responsive variants where they clarify implementation, and small CSS/JavaScript primitives where necessary. Tailwind does not itself manage focus or disclosure state. Reduced-motion preferences should remove unnecessary movement while preserving visible content and feedback. Simplify or remove pinning, parallax, and large transforms where mobile layouts or motion preferences make them unsuitable. Preserve normal scrolling, readable text, and usable links throughout; do not make essential information depend on completing a decorative animation.

Consult current primary references for implementation: [Tailwind transitions](https://tailwindcss.com/docs/transition-property), [state variants and reduced motion](https://tailwindcss.com/docs/hover-focus-and-other-states), [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/), [WordPress asset loading](https://developer.wordpress.org/themes/core-concepts/including-assets/), and [ARIA disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/).
