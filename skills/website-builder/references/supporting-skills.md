# Supporting skills

Reviewed on 2026-10-14. The machine-readable installation source is [supporting-skills.json](../supporting-skills.json). It pins three named skills to complete Git commits. These provide framework knowledge; Website Builder supplies the design, implementation, and verification workflow.

This was a scoped review of the entrypoints, dependency trees, licenses, installation requirements, and selected technical examples. It is not an exhaustive audit or an endorsement of every upstream claim. Consult documentation matching the project's installed versions. The corrections below take precedence over conflicting examples in the selected skills.

## How to load and install

Use the installed skill with its original name: `astro-best-practices` for Astro architecture, `tailwind` for Tailwind v4, and `wagtail` for CMS work. Discover and read the files in the selected agent's skill directory; do not invent a cross-agent invocation API. Read this page's relevant caveats before relying on a supporting skill.

The installer must copy the entire selected directory, the repository's root `LICENSE`, and source provenance. Preserve relative paths. Do not copy only `SKILL.md` from a skill with resources. Never run downloaded scripts during skill installation, follow symlinks out of the source tree, or overwrite an unrelated installed skill. A pinned source does not authorize installing every skill in its repository. See [setup](setup.md) for the kit's installation workflow.

## Astro: `astro-best-practices`

- Repository: [incluud/astro-agent-skills](https://github.com/incluud/astro-agent-skills).
- Revision: `4b4355ecea8ef4f68c9025f3de5a73c27df59310`.
- Directory: [`skills/astro-best-practices`](https://github.com/incluud/astro-agent-skills/tree/4b4355ecea8ef4f68c9025f3de5a73c27df59310/skills/astro-best-practices).
- License: [MIT, root `LICENSE`](https://github.com/incluud/astro-agent-skills/blob/4b4355ecea8ef4f68c9025f3de5a73c27df59310/LICENSE).
- Required resources: one `SKILL.md`; no local sibling resources, scripts, editor dependencies, or runtime installer.

This community baseline favors `.astro` components, small deliberate islands, semantic markup, predictable project structure, and version-aware documentation. Its scoped-CSS preference explicitly yields to an existing styling system, so use this kit's Tailwind design tokens and conventions. It does not replace current documentation for adapters, rendering, content loaders, or framework upgrades. Check [Astro's setup prerequisites](https://docs.astro.build/en/install-and-setup/) before selecting a Node version.

## Tailwind v4: `tailwind`

- Repository: [pproenca/dot-skills](https://github.com/pproenca/dot-skills).
- Revision: `cf93c57cac89d6fc3e4194686000411567f5caf3`.
- Directory: [`skills/.curated/tailwind`](https://github.com/pproenca/dot-skills/tree/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.curated/tailwind).
- License: [MIT, root `LICENSE`](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/LICENSE).
- Required resources: all 50 files: `SKILL.md`, `AGENTS.md`, `README.md`, `metadata.json`, `assets/templates/_template.md`, and all 45 files under `references/`. No executable scripts are present in this selected directory.

Use this community skill as a topic index and secondary reference. Apply these specific corrections:

1. **Dark mode:** `references/theme-dark-mode-class.md` incorrectly defines a variant with `@variant`. Use `@custom-variant dark (&:where(.dark, .dark *));` for a class-driven theme, as shown in the [official dark-mode documentation](https://tailwindcss.com/docs/dark-mode). Adding a theme switcher remains a product decision.
2. **Native CSS:** `references/bundle-avoid-preprocessors.md` shows Sass-style `&__item` concatenation as native nesting and uses an undefined `--spacing-4` variable. Use valid selectors and a defined token; Tailwind's spacing calculation can use `calc(var(--spacing) * 4)`. Validate examples against [Tailwind compatibility guidance](https://tailwindcss.com/docs/compatibility).
3. **Toolchain:** its Node 20 guidance is not a complete minimum for an Astro project or an external skills installer. Use the strictest requirement among the chosen supported runtimes and tools; see [compatibility](compatibility.md). For Astro with Tailwind v4, use `@tailwindcss/vite` and the CSS import described by the [official Astro integration guide](https://tailwindcss.com/docs/installation/framework-guides/astro). Do not substitute the older Astro Tailwind v3 integration.
4. **Motion and examples:** add visible keyboard focus, reduced-motion handling, and real browser verification to motion examples. `transition-discrete` alone does not define an opacity/transform transition. Follow [official transition behavior guidance](https://tailwindcss.com/docs/transition-behavior) and this kit's design and motion workflow.
5. **Optimization claims:** do not repeat the skill's numerical performance claims as measured results. Avoid adding critical-CSS plugins, changing minifiers, removing dependencies, or rewriting working styles without a relevant measurement and compatibility check. Several examples are written for other frameworks; adapt them to Astro deliberately. The skill's older README also differs from its entrypoint on rule count; the pinned directory inventory is the installation authority.

This is not a Tailwind v3 migration request. Existing projects keep their version and architecture until a migration is explicitly in scope.

## Wagtail: `wagtail`

- Repository: [official wagtail/wagtail-cli](https://github.com/wagtail/wagtail-cli).
- Revision: `f079f20210e7f0f30e2f30f530ac9f363df70683`.
- Directory: [`skills/wagtail`](https://github.com/wagtail/wagtail-cli/tree/f079f20210e7f0f30e2f30f530ac9f363df70683/skills/wagtail).
- Required source resources: one `SKILL.md`; its further workflow resources are bundled in the separately installed CLI package.
- License provenance: the [skill's frontmatter](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/skills/wagtail/SKILL.md) declares MIT, while the [root `LICENSE`](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/LICENSE) and runtime package declare BSD-3-Clause. Keep both upstream declarations and the full root license; do not relabel the entire package MIT.

The published runtime is **`wagtail-cli==0.4.0`**, requiring **Python 3.12 or later**. Its release exists and was not yanked when checked in [PyPI release metadata](https://pypi.org/pypi/wagtail-cli/0.4.0/json). Install it when preparing Wagtail support:

```sh
uv tool install wagtail-cli==0.4.0
wt --help
wt skills list
wt skills get core
```

Use an existing compatible Python or provision one through the setup workflow. If `wt` is not on PATH, inspect `uv tool dir --bin` and use uv's documented shell setup; see [uv tools](https://docs.astral.sh/uv/guides/tools/). This isolated tool install does not create the website's Python environment or install its Django/Wagtail dependencies. The runtime version is pinned; its transitive dependencies are not fully locked by this manifest.

Load specialist instructions on demand with `wt skills get`, using names returned by `wt skills list`. Use `--full` when the requested skill needs its bundled references and templates. Version 0.4.0 includes the core, CLI API, CLI docs, API, backend, content-modeling, frontend, and upgrade specialists; CLI API also bundles `references/commands.md` and `references/writing-content.md`. Install the package intact instead of copying those runtime resources individually. Docs and skill lookup do not require website API credentials. CMS operations require appropriate project configuration and authorization.

The CLI is marked alpha in its [pinned package metadata](https://github.com/wagtail/wagtail-cli/blob/f079f20210e7f0f30e2f30f530ac9f363df70683/pyproject.toml). Its API client and API specialist target **Wagtail API v3 preview**, introduced in Wagtail 8.0. Existing API v2 projects must use matching v2 documentation and their existing integrations; never silently upgrade them or apply v3 payloads to v2. Check installed versions before loading a specialist. Keep CMS credentials server-side and preserve the distinction between saving drafts and publishing.

## Reviewed alternatives and exclusions

- The official [`wagtail/agent-skills` revision `40f44f29fb48a3e94f83d67cb8598fec7ba54adc`](https://github.com/wagtail/agent-skills/tree/40f44f29fb48a3e94f83d67cb8598fec7ba54adc) has a bare `BSD-3-Clause` line inside its YAML frontmatter, with a root MIT license. It was excluded from direct installation because that metadata is malformed. Its earlier published content revisions have the same issue. The selected CLI entrypoint has valid metadata and is the installation approach recommended by that repository.
- `delineas/astro-framework-agents` was not selected because inspected guidance uses Astro's removed `hybrid` output mode. Check the [official Astro 5 migration documentation](https://docs.astro.build/en/guides/upgrade-to/v5/#removed-hybrid-rendering-mode) when encountering such advice.
- [Lombiq/Tailwind-Agent-Skills](https://github.com/Lombiq/Tailwind-Agent-Skills) provides a documentation snapshot workflow, but requires additional Python/Git tooling, local writes, refresh management, and acceptance of the upstream documentation license. It is not part of this compact default installation. Do not package its downloaded documentation into this public repository.

## Installation verification record

All three pinned archives were read without executing their contents. Their selected skill frontmatter parsed successfully; selected folders contained only regular files, and their root license files existed. Operative local resource links resolved. Tailwind's README includes a literal `(URL)` example placeholder rather than a missing required dependency. The Wagtail CLI 0.4.0 wheel's SHA-256 matched PyPI metadata; its discovery stub exactly matched the pinned source, and its specialist files were present. The CLI was inspected, not installed or executed during this review.

Measured archive sizes at these pins: Astro 10,272 bytes compressed / 25,731 bytes of regular file content; dot-skills 9,639,594 / 35,538,084 bytes; Wagtail CLI 2,813,854 / 4,025,393 bytes. The complete dot-skills archive has 8,411 files even though only 50 are selected, so installation limits should account for that. A repository update requires a new review, full revision pin, license/resource check, and relevant compatibility verification.
