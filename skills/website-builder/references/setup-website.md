# Prepare a website project

Use this for `setup-website`, or as missing preparation during `create`. Its outcome is a connected, locally usable project, not just an empty directory tree. If the user only asked for preparation, stop after the working foundation; do not invent their business or design the entire site.

## Establish the project

Infer a sensible project name and location from the request. Clarify only if ambiguity could put work in the wrong project. Keep websites separate from the toolkit checkout. Inspect the destination before creating files. If it already has a site, preserve it and fill only demonstrated gaps; never run a scaffold command over an existing project.

Read the setup record and run only missing prerequisites from [setup](setup.md). Load installed Astro, Tailwind, and Wagtail guidance, then verify the supported runtime and package combinations in official docs. Use released versions, record the chosen versions, and commit the package-manager lockfiles. Do not invent an old Astro `hybrid` mode or add a deprecated integration to a new Tailwind v4 project.

A useful default structure is `frontend/` for Astro, `backend/` for Django/Wagtail, and `docs/` for project notes. Existing conventions take precedence. Use one JavaScript package manager and an isolated Python project environment. Do not install website dependencies into the toolkit or system Python.

## Connect a minimal editable page

1. Create Astro and integrate Tailwind using the current [Astro integration instructions](https://tailwindcss.com/docs/installation/framework-guides/astro). Verify styles with a visible component.
2. Create a Wagtail project with supported Django/Python versions. Use SQLite for a simple local first run unless the project needs another database; do not require Docker or a hosted database just to get a preview. Separate development settings from deployment configuration.
3. Add an appropriate page model with editable title, introduction, and image, and expose those public fields through the documented Wagtail content API. Model richer reusable content blocks when the brief calls for them, not as an unrestricted CSS editor.
4. Fetch that published content in Astro through a small typed data boundary, with explicit API and media base URLs. Keep CMS credentials and preview tokens server-side. Prefer server/build-time fetching for public content; configure browser cross-origin access only if it is actually required.
5. Choose static generation or on-demand rendering according to the expected publishing experience. For a simple static project, provide and test the local rebuild/refresh path after a publish. For immediate content updates, use an appropriate server adapter and caching policy. Explain the resulting behaviour in user terms.
6. Handle unavailable content visibly during setup. Do not report a CMS connection as working while silently showing hardcoded fallback content. Drafts and unpublished pages must not become public through the content endpoint.

Relevant sources: [Wagtail getting started](https://docs.wagtail.org/en/stable/getting_started/index.html), [API configuration](https://docs.wagtail.org/en/stable/advanced_topics/api/v2/configuration.html), [Astro data fetching](https://docs.astro.build/en/guides/data-fetching/), [Astro rendering](https://docs.astro.build/en/guides/on-demand-rendering/).

## Make it usable by its owner

- Supply simple, OS-appropriate start/stop instructions and working preview/CMS URLs. Prefer an existing supported task runner; do not make a Mac-only shell script the only way to run the project.
- Provide `.env.example` with descriptive placeholders, ignore real secrets, and keep local databases/uploads out of source control unless deliberately using safe test fixtures. Set up an editor account through the supported local flow without committing its password.
- Create project-root `AGENTS.md` and a sibling `CLAUDE.md` importing it, following [project instructions](project-instructions.md). Fill them with the actual architecture, skill routing, and verified commands. Preserve and merge any existing instructions rather than replacing them with a template.
- Create and maintain `WEBSITE_BRIEF.md` from the conversation, plus a short run guide and a record of selected package versions. The AI writes these; the user supplies creative direction and corrections. State how images, content publishing, and future hosting fit together.
- Prepare local feedback handling through [feedback tracking](feedback.md): preserve existing records, set appropriate ignore rules, and create `SKILL_FEEDBACK.md` only when meaningful evidence exists. A shared inbox is optional and needs a user-selected location.
- If the user requested a frontend-only site, document the decision and skip Wagtail; do not present an absent CMS as ready.

## Completion evidence

Run the frontend build, Django checks, and migrations. Start both services. Confirm the homepage displays content fetched from Wagtail. Change a distinctive value in a disposable local page, publish it, perform the documented refresh/rebuild if required, and verify the exact value appears on the frontend. Restore demonstration content if appropriate. Verify a local image URL and a missing-page response too.

If browser access is unavailable, verify API responses and build output and state that editor/browser interactions remain untested. Do not claim a full end-to-end pass. Missing credentials or prerequisites should leave a resumable record and a concrete next step.

Check the persistent instructions against actual files and commands, then perform the [fresh-chat verification](project-instructions.md#verify-a-fresh-chat) when the host supports it. Record instruction loading separately from website runtime checks; a file existing is not proof that the agent loaded it.
