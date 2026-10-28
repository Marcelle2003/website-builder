# Supporting skills

Reviewed on 2026-10-15. [supporting-skills.json](../supporting-skills.json) pins complete source commits and distinguishes the default pack from optional specialists. Website Builder owns the creative workflow, hybrid-theme architecture, content-editing contract, and verification. Supporting skills supply focused technical or design guidance; load only those relevant to the current task.

## Selection and installation

`--with-supporting` installs six default skills:

- `wordpress-router` and `wp-project-triage`: understand the actual WordPress project before choosing a workflow.
- `wp-plugin-development`: content types and site functionality that should survive a theme change, with WordPress security conventions.
- `wp-wpcli-and-ops`: repeatable local setup and carefully targeted WordPress operations.
- `tailwind`: Tailwind v4 styling guidance, subject to the corrections below.
- `frontend-design`: visual direction, typography, composition, and critique grounded in the user's brief.

Optional skills can be selected with `--supporting NAME [NAME ...]`, alone or with the default pack. The installer includes declared dependencies once and rejects unknown names before writing anything. For example, after selecting the actual agent and scope as described in [setup](setup.md):

```sh
python3 skills/website-builder/scripts/install.py --agent codex --scope user --with-supporting --supporting wp-block-development gsap-scrolltrigger gsap-performance --dry-run
```

Repeat without `--dry-run` for an authorized install. This example installs GSAP core and timeline guidance as dependencies of ScrollTrigger. It does not install the GSAP JavaScript package, build a website, or force an animation into the design. `--update` is only for an intentional replacement after inspecting existing files; it keeps recoverable backups. Updating this toolkit does not remove older Astro/Wagtail skills or migrate existing websites.

Optional choices in this reviewed catalogue:

- **Editable custom sections:** `wp-block-development`. A hybrid theme can use blocks without becoming a full block theme.
- **Full Site Editor projects:** `wp-block-themes`, or selected references for `theme.json` and patterns in a hybrid theme. Preserve the chosen architecture.
- **Backend profiling:** `wp-performance`; this does not cover browser animation performance.
- **PHP analysis:** `wp-phpstan`; configure the runtime tooling only when appropriate to the project.
- **Local Docker environment:** `wp-env`, only if that environment is selected. Reuse a working environment first.
- **Coordinated animation:** `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, and `gsap-performance`. Start with CSS for simple transitions; add the relevant GSAP guidance and runtime when the approved design benefits from them.

Read skills from the current agent's discovered installation paths, preserving their original names. There is no universal cross-agent skill-calling API. A reference to another skill is not evidence that it is installed. For a specialist outside this catalogue, inspect its current source and resources before a separately authorized installation, or use official documentation. Avoid installing a whole repository to satisfy one feature.

The installer copies complete selected folders, their applicable upstream license, and source provenance; it never runs downloaded code. It downloads each pinned repository once per run. Skill installation is separate from PHP, WP-CLI, Composer, Node, Docker, GSAP, and browser-tool setup. Read supporting scripts before executing them against the intended project.

## WordPress: official collection

Source: [WordPress/agent-skills](https://github.com/WordPress/agent-skills/tree/55cd0f78b996f453c194a1a6ecc5c9a2e0f6cf15), revision `55cd0f78b996f453c194a1a6ecc5c9a2e0f6cf15`. Each selected directory is `skills/<name>`. Preserve the root `LICENSE` notice, copyright, GPL-2.0-or-later licensing, and provenance; these are not relabeled under Website Builder's MIT license.

The nine selected folders contain their local references and scripts; inspected JavaScript imports use Node built-ins. Other workflows may need separately installed tools. Apply these integration rules:

1. **Hybrid themes need our own architecture guidance.** The collection has no dedicated classic/hybrid theme skill. Follow [project setup](setup-website.md) and [creation](create.md). Do not switch to a block theme merely because `wp-block-themes` exists.
2. **Verify theme detection.** The pinned triage and theme detectors use folder heuristics that can classify a hybrid theme with `theme.json` and a `patterns/` directory as a block theme. Inspect the actual PHP templates and block-template entry points, including `templates/index.html`, and the intended editing experience before acting on the report.
3. **Resolve installed paths.** Examples such as `node skills/wp-project-triage/scripts/detect_wp_project.mjs` assume a repository layout. Resolve the actual installed script path and run it with the target website as the working directory. If Node is unavailable, inspect the relevant files, manifests, and versions directly; copying or reading skills does not require running their detectors. Prepare Node only when the selected website tooling needs it. WP-CLI operations must also target the correct installation, URL/site, and environment.
4. **Separate source and runtime scan scopes.** Identify the authored theme/plugin, the workspace containing build manifests, and any nested local WordPress installation before interpreting detector results. For component work, classify the authored component and inspect workspace manifests separately. A broad workspace scan can inventory the environment, but matches inside bundled core, runtime copies or unrelated plugins do not establish features of the component being changed. Inspect match paths and each relevant scan's truncation flag before choosing specialist workflows; a truncated scan leaves uncertainty, not proof of absence. Preserve sibling authored components in scope for multi-component work. Do not delete or blanket-ignore runtime directories: an intentional WordPress core task may target them.
5. **Match versions.** The pinned upstream compatibility policy targets WordPress 7.0+. Its PHP minimum is not a recommended new production version. Detect the site's versions and use matching official documentation; never upgrade WordPress or PHP just to match a skill. Check the current runtime package's requirements rather than relying on an old Node minimum in a skill.
6. **Preserve data during environment checks.** `wp-env` recommends resets in its verification/troubleshooting examples. Do not run `reset` or `destroy` as routine checks or generic repairs on a populated environment. Inspect logs first; reserve destructive operations for an explicitly disposable target or authorized recovery work with a suitable backup and restoration plan.
7. **Use focused routes.** `wp-testing`, `wp-security`, and `wp-build-tooling` are mentioned as planned in the router; do not claim they are available. REST, Interactivity API, Abilities, Playground, and Blueprint skills are separate optional subjects outside this reviewed installation set. Their absence does not block ordinary PHP theme work. `wpds` concerns WordPress editor/admin UI and requires additional tooling; it is not a public-site creative design system.

## Tailwind v4: community guidance

Source: [pproenca/dot-skills](https://github.com/pproenca/dot-skills/tree/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.curated/tailwind), revision `cf93c57cac89d6fc3e4194686000411567f5caf3`, directory `skills/.curated/tailwind`, root MIT `LICENSE`. Preserve the complete 50-file folder, including its references and assets. This is a community topic index and secondary reference, not official Tailwind guidance.

Corrections retained from the previous source review:

- `references/theme-dark-mode-class.md` uses `@variant` to define a variant; class-based dark mode uses `@custom-variant dark (&:where(.dark, .dark *));`. A theme switcher remains a product decision. [Official dark mode](https://tailwindcss.com/docs/dark-mode)
- `references/bundle-avoid-preprocessors.md` uses Sass-style `&__item` concatenation and an undefined `--spacing-4` as native CSS. Use valid selectors and defined tokens, such as `calc(var(--spacing) * 4)` where appropriate. [Compatibility](https://tailwindcss.com/docs/compatibility)
- Do not assume its Node or framework-specific setup examples fit this website. Use the existing build tool or the supported Tailwind CLI; compile deployable assets and enqueue them through WordPress. Detect complete class names in PHP, block, pattern, and JavaScript sources. Database-only classes and string fragments such as `bg-${color}-500` need an explicit strategy, such as bounded complete-class mappings or validated CSS variables. [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files)
- Account for WordPress core block styles and Preflight; do not reset the entire admin interface. Keep editor content styles aligned with the theme. [Preflight](https://tailwindcss.com/docs/preflight)
- `transition-discrete` alone does not define opacity/transform animation. Add focus, reduced-motion handling, and browser verification. Do not repeat numerical performance claims as measured outcomes or add optimization plugins without a demonstrated need.

Existing Tailwind v3 projects keep their version until migration is in scope.

## Visual design: Anthropic

Source: [anthropics/skills](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design), revision `dbd4588f9e1033efb41dad4bef2f7947c8993d44`, directory `skills/frontend-design`. Preserve its own `LICENSE.txt` (Apache-2.0), not a presumed repository-wide license.

Use `frontend-design` during new visual direction or a meaningful redesign. The entrypoint's imagined client history is creative framing, not a fact about the actual user. Its aesthetic preferences do not override an approved brand, reference, font, or narrow task. Do not demand a new creative approval round when the user has already settled the direction. Website Builder's brief and scope control the work.

## Motion: official GSAP collection

Source: [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/aed9cfd3277740755f6bfc1155c7aa645403b760), revision `aed9cfd3277740755f6bfc1155c7aa645403b760`, directories `skills/gsap-core`, `skills/gsap-timeline`, `skills/gsap-scrolltrigger`, and `skills/gsap-performance`. Preserve each complete folder and the root MIT `LICENSE`. That license covers these instructions; check the separate runtime's terms when adding GSAP to a website.

Use vanilla JavaScript examples for conventional WordPress unless the specific component uses another framework. Installing these skills does not imply React, a client router, scroll smoothing, or live 3D rendering. See [design and motion](design-and-motion.md) for content, accessibility, lifecycle, and responsive requirements.

The official collection also contains errors; the scoped source review found these corrections:

- The ScrollTrigger skill reverses `refreshPriority` ordering: **higher values refresh earlier**. Prefer creating triggers in page order. [Official sort documentation](https://gsap.com/docs/v3/Plugins/ScrollTrigger/static.sort()/)
- Its horizontal-scroll snippet uses `Max.max`, mixes a pixel distance into `xPercent`, and omits the scroll scrubbing it describes. Rebuild the effect from the actual container dimensions with `Math.max`, appropriate `x` pixel or `xPercent` units, `ease: 'none'`, and the intended `scrub` behaviour; test resizing and overflow. Do not paste that snippet unchanged. [Official ScrollTrigger documentation](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
- Use the documented timeline position argument; do not infer a tween `position` property from the timeline skill's wording. [Position parameter](https://gsap.com/resources/position-parameter/)
- Scoped cleanup should revert a component's own timelines, triggers, and listeners. Do not copy global `ScrollTrigger.getAll().forEach(...kill)` cleanup into an isolated component and break other sections. Reduced-motion layouts must show all essential content, not just set a duration to zero while leaving long pinned scenes.
- Treat performance advice as hypotheses to measure. `scrub` smoothing, pinning, and `will-change` do not guarantee compositor promotion or better frame rates. Avoid permanent layer hints on every animated element.

## Forms: Cognito Forms MCP

Cognito Forms is a standard setup integration, supplied through its official remote MCP connector rather than the pinned filesystem skill manifest. Follow [connection, form-building and prefill guidance](cognito-forms.md). Confirm tools and organization access in the selected agent; file installation alone does not connect it. The reusable head/footer assets ship inside Website Builder, with no additional JavaScript package required.

## Browser, accessibility, and quality checks

Use the current agent's available browser tooling and project test tools. A portable skill cannot supply a browser connection merely by mentioning Playwright. Follow [verification](verification.md) for keyboard, mobile, reduced motion, editing, security-sensitive flows, and browser performance checks. Add a host-specific testing skill/tool only when it is available, useful, and within setup scope; do not install several overlapping browser stacks by default.

Astro and Wagtail are no longer in this branch's default supporting pack. Preserve them when working on an existing site that actually uses them; do not remove the user's installed skills or packages as part of this update.

## Review scope

The pinned archives were inspected without executing their contents: entrypoints, selected resource trees, licenses, script dependencies, and specific examples. This is not an exhaustive audit. Live temporary installation and workflow checks are recorded in the repository's `VALIDATION.md`; do not interpret copied instructions as proof of a working WordPress environment or a tested animation. Source updates require renewed version, license, resource, and compatibility review.
