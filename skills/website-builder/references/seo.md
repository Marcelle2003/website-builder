# Update search for an existing website

Use this for `seo`: a pass that only changes how an existing site is found. Inspect the current site first. Do not restyle it, replace its theme, or scaffold a new one. A new website still uses [creation](create.md). A visual or interaction change still uses [improvement](improve.md), which keeps search markup current on the pages it edits.

## Inspect the pages before changing them

Read the project instructions, the brief, and the active theme, editor, and plugins. Find what already prints the title, meta description, canonical URL, sitemap, and structured data. WordPress core, an existing SEO plugin, or a companion plugin may already own a field. Use that owner. Do not add a second description, a second sitemap, or an SEO plugin whose only job is to print a title and description.

Inspect the public pages in a browser when available, including the rendered head and the heading outline. A template file alone does not prove what visitors receive. Check where the words come from: theme templates, editor content, or saved plugin fields. Preserve editor customizations. Do not delete them to force a result.

If the brief is missing during authorized work, create it from the site and the conversation. Do not ask the owner to fill it out as a form.

## Know the business and the market

Before any keyword call, follow [search-led page building](seo-and-ai-search.md). Know what the business does, which services it offers, who the site is for, and where those people search. Ask for the missing pieces in one short batch. Do not invent a service, and do not assume a country, city, or region.

Run Keyword Planner when the pass is choosing or revising pages or the offer. Use the country or place the owner named, or the one already recorded in the brief. Preserve an existing primary keyword unless the owner changes the offer or the page’s subject. A request to fix headings, titles, descriptions, alt text, or indexing on settled pages does not need a new keyword query.

## Change only the search layer

On the pages in scope, apply [search-led page building](seo-and-ai-search.md):

- one H1 for the page subject, then H2s for real sections and H3s only inside the H2 they belong to
- a unique document title and one meta description, editable in WordPress
- alt text on informative images, and an empty alt on decorative images
- a sensible canonical URL, one sitemap, and structured data that matches visible content
- WebP sub-sizes for JPEG and PNG images this pass adds or replaces, when the server can encode WebP

Do not convert the existing media library unless the owner asks. Do not restyle headings to change their level, and do not change colours, type, layout, or motion to complete this pass. Version theme CSS or JavaScript only when this pass actually changes those files.

Keep “discourage search engines” on for an isolated local or staging site. Follow the indexing and launch checks in [search-led page building](seo-and-ai-search.md#indexing-urls-and-launch) before changing that setting. Do not turn it on for a live site that should stay indexed, and do not remove a live noindex as a side effect of a metadata edit.

## Deliver the search result

Update `WEBSITE_BRIEF.md` with the place, language, result date, and the per-page keyword, title, and description you changed. Run the SEO checks in [verification](verification.md). Confirm the rendered head, heading outline, and alt text for the pages you changed, and that an editor can change a title or description without a code edit. Label indexing, Search Console, and AI citations as verified, inspected, or not tested. Do not promise rankings.

If the work exposes a confirmed reusable workflow problem, follow [feedback tracking](feedback.md). A site’s keyword choice is a brief decision, not a skill defect. Recording feedback does not authorize changes to the source skill.
