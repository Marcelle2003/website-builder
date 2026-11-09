# Build pages from search demand

Use this while creating a site, during an [SEO-only pass](seo.md), and when an improvement adds a page or changes what the business offers. Query Google Ads Keyword Planner before that page list is settled, then build the WordPress pages from the result. When the work only edits an existing public page, keep its heading outline, document title, meta description, and alt text current without a new keyword query. A closing check confirms the affected pages still match the chosen keywords. This is research for the site being built. It does not add a keyword tool to the theme, and it does not promise rankings.

## Know the business first

Before any keyword call, be able to say what the business does, which services it actually offers, who the site is for, and where those people search. Take that from the conversation or from material the owner supplied. If any of it is missing, ask in one short batch. Do not invent services to produce a seed list.

The search location comes from the owner. Do not assume a country, city, or region because the Ads account is in one market, because an example on this page names one, or because the agent is running in one. Use the language the owner wants on the site, and ask for the language only when that is unclear.

A business that serves a country uses that country. A business that serves a city or region uses that place, and the owner has to name it. Do not widen a local business to the whole country, or narrow a national one to a city, unless they said so.

## Get the numbers from Keyword Planner

Call `KeywordPlanIdeaService` on the Google Ads API. The Google Cloud CLI does not provide these methods. Current references: [keyword planning](https://developers.google.com/google-ads/api/docs/keyword-planning/overview), [historical metrics](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics), and [access levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels).

- Use `GenerateKeywordIdeas` when the seeds are the business, its services, a competitor URL, or the site URL. Each idea already includes historical metrics.
- Use `GenerateKeywordHistoricalMetrics` when a keyword list already exists. Send at most 10,000 keywords in one request. The API merges close variants, so the result can be shorter than the request.
- Pass the country the owner named, and the city or region when they named one. Record average monthly searches, monthly history, ads competition, and the low and high top-of-page bids. Label these as low/high top-of-page bid estimates in the account currency, not actual or average CPC. Request average CPC only with `HistoricalMetricsOptions.include_average_cpc`; Google returns that field for legacy support.
- Ads competition measures paid competition. The API does not return organic keyword difficulty. Record the two separately.
- Cache a result for the same keywords, location, and language. Google says the response stays stable for hours or days, and monthly volumes refresh monthly. Keyword planning is rate-limited more tightly than other Ads API calls.

Resolve `scripts/keyword_ideas.py` relative to the installed Website Builder `SKILL.md`, and invoke its absolute path from the website project. Do not assume the website has a `scripts/` copy. Run it only after the owner has named the market. It reads `~/.config/website-builder/google-ads.json`, or the file named by `WEBSITE_BUILDER_GOOGLE_ADS_CONFIG`. That file has `customer_id` and `service_account_key_file` for the one Ads account that calls Keyword Planner. Keep the key beside it, outside the website and outside git. The customer ID is the calling account, not the client’s market. The figures follow the country, place, and language you pass, so a new client does not need an Ads account. The script has no default country.

```bash
python3 "/absolute/path/to/website-builder/scripts/keyword_ideas.py" --country XX --language xx --seed "named service"
```

`XX` and `xx` stand for the codes the owner gave. They are not a market to reuse. Add `--place` with the city or region when the owner named one. Repeat `--seed` for each service they offer. Use exactly one `--url` for the client’s site or a competitor; run separate requests for additional URLs. For ambiguous place names, ask which returned location is intended and repeat the same `--place` with its confirmed `--place-id`. Never choose the city just because a city and region share a name. Use `--keyword` on its own when the phrase list already exists; that calls historical metrics, and the API may merge close variants. The script caches a matching request for 24 hours, separately for each Ads customer and API version. Pass `--refresh` to call again. Record the printed country, place, language, date, and per-keyword figures in the brief. Bids are in the calling account’s currency, named by `currency_code`. If a named place cannot be resolved, ask for a clearer one. Do not quietly replace it with the whole country.

The Ads user is a service account with Read-only access on that one customer. It cannot accept mail, so the address ending in `.iam.gserviceaccount.com` is added directly and does not need a Cloud project role. Email-only cannot call the API. Access sits on the Cloud project. Developer tokens are retired, and Explorer cannot call Keyword Planner. The project needs Basic access, after brand verification, or Standard access. At Standard, follow Google’s permissible-use rule for keyword research. The official Google Ads connector does not expose Keyword Planner. If the script fails, say the volumes are unavailable, keep building from the brief, and do not invent search volume or bids.

## Turn keywords into pages

Use search demand to inform page choices, not to veto real services, niche offerings, visitor needs, or explicit owner requests. Missing or low reported volume is not proof that a page has no value. Group related searches by intent rather than creating near-duplicate pages for every phrase or location. Choose a primary topic/search intent per page and use relevant terms naturally in its slug, title, H1, description, and introduction. Preserve established URLs unless a URL change is authorized; then map permanent redirects and update internal links and canonical URLs. Use supporting terms from the same idea in subheadings and in links between those pages. State the main offer on the homepage in the words people search with.

Write the country or place the owner named, the language, the result date, and the per-page figures into `WEBSITE_BRIEF.md`. An editor must be able to change the words later in WordPress without losing the markup.

The site provides these through WordPress core, the existing SEO plugin, or a small companion plugin where needed. Inspect the current owner of each output before adding code; do not duplicate core/plugin tags or sitemap generators:

- a document title and meta description that match the page and stay unique across the site
- one H1 for the page’s subject, then H2s for its real sections and H3s only inside the H2 they belong to
- an appropriate absolute canonical URL on indexable pages, with existing duplicate/pagination policies preserved
- one coherent XML sitemap system (reuse WordPress core or the established SEO plugin)
- relevant structured data for supported page types, matching visible and verified content
- alt text on informative images
- the page language on the document element

Enable `title-tag` support so WordPress prints the document title. Where no existing SEO provider owns the output, print one `<meta name="description">` for that page, taken from the page’s own description field, because WordPress does not emit a meta description by itself. Write that description when the page is created, from the primary keyword and the offer, in ordinary language. An editor must be able to change the title and the description later without a code edit. Do not add a keywords meta tag, and do not install an SEO plugin only to print these two fields. If the site already has one, use its fields instead of printing a second description.

Keep persistent SEO fields and nonvisual SEO behaviour in the existing SEO plugin or companion plugin so a theme change does not discard them. Escape metadata for HTML attributes and encode structured data with WordPress JSON helpers.

When an informative image is added, write its alt text on the media attachment, describing what the picture shows. `wp_get_attachment_image()` then prints that stored value. A decorative image gets an empty alt. Do not leave the field blank and do not paste the page’s keyword into every image.

Build that heading outline from the content, not from the type scale. A heading level is the section’s place in the page. Its size comes from CSS, so a design does not skip from H2 to H4 to get smaller type, and it does not turn a label into an H1 because the style is large. Do not turn logos, navigation or buttons into headings for styling; footer groups may use appropriate headings when they represent real sections. On an inner page the H1 is that page’s subject, not the site name. The H1 should describe the primary topic naturally; exact-match wording is not mandatory. One main H1 is our clarity convention, not a claimed Google ranking requirement. A supporting term becomes an H2 only when that section is really about it.

Write the words as HTML text. Do not place the heading or the offer inside an image. Links between pages use the name of the destination, not “read more” or “click here” as the whole label. Header, navigation, main content, and footer stay distinct regions so the outline is the page and not the chrome.

## Indexing, URLs and launch

On confirmed local/staging installations, keep “discourage search engines” on and verify the emitted directives. That database setting can affect production when environments share a database: inspect isolation before changing it; use the existing environment-specific controls when necessary. Use authentication/access restrictions for private staging; noindex is not access control.

For an authorized launch, verify the intended live hostname, remove only staging-specific noindex restrictions, and preserve intentional page-level exclusions. Inspect actual HTML, HTTP X-Robots-Tag headers, robots.txt, canonical tags, redirects and sitemap output after relevant caches are refreshed. A robots.txt disallow can prevent a crawler from seeing noindex; robots.txt alone is not a deindexing mechanism. Do not change production indexability as a side effect of a visual edit.

Use stable URLs. For authorized URL moves, use a permanent redirect to the relevant replacement and update links and sitemaps. Keep real missing pages as 404/410 rather than redirecting every missing path to the homepage. Canonical targets should be appropriate indexable URLs; do not point every page at the homepage or collapse distinct paginated pages without inspecting their content. Avoid tracking parameters in canonical URLs. Canonicals are signals, not a guarantee of Google's selection. Sitemaps should contain intended canonical, indexable URLs, not drafts, staging addresses, redirects or error pages; retain truthful last-modified dates.

## AI search and trustworthy content

Google's AI search features use the same foundational SEO requirements; no special AI schema or llms.txt file is required. Do not promise rankings, citations, indexing, or rich results. Other providers have distinct crawler controls: check their current official documentation when relevant and preserve the owner's separate choices about search access and model training.

Prioritize useful original content, clear answers, accurate business details, and evidence for claims. Do not fabricate reviews, credentials, service areas or schema facts. Validate applicable structured data against the relevant type requirements and visible content; syntactic validity alone does not establish rich-result eligibility. Avoid location/keyword doorway pages and fixed word-count or keyword-density targets. Titles and descriptions should be concise and descriptive; Google may generate different title links or snippets, so character counts are editorial guides rather than strict ranking rules.

Primary references: [Google AI features](https://developers.google.com/search/docs/appearance/ai-features), [noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing), [canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [snippets](https://developers.google.com/search/docs/appearance/snippet), [structured data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), and [WordPress sitemaps](https://developer.wordpress.org/reference/classes/wp_sitemaps/).


## Check the built pages

Check representative page types and all affected pages, including homepage, service pages, archives/pagination and missing routes where applicable. Confirm no unintended URL or topic changes, that the rendered head contains that one description, and that its H2s and H3s follow the page’s sections without skipped levels. Confirm informative images carry the attachment alt text and decorative images have an empty alt. Check the indexing and launch conditions above, unique metadata ownership, and applicable structured data. Edit a test SEO field through the local WordPress editor and confirm the escaped rendered output updates. Label anything that needs a live site as verified, inspected, or not tested. Search Console, a Google Business Profile, reviews, and whether an AI assistant mentions the business are outside this build. Do not claim those from theme files or from Keyword Planner.
