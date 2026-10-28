# Cognito Forms and attribution

Cognito Forms is the default form-building integration for Website Builder. Use its official MCP connector to build forms where the connected tools support the operation; preserve an existing provider or an explicit alternative. The reusable website baseline includes the tracking head script and footer integration on every public page, including landing pages without a form. A skill update alone does not modify existing websites: apply this baseline during new-site preparation or authorized adoption/form work, not as a surprise side effect of an unrelated copy edit.

## Connect the agent

Include Cognito in full setup's connection checks, separate from filesystem supporting skills. Reuse a connected official Cognito Forms toolset. If missing, use the host's supported connector/MCP setup and the [official connection guide](https://www.cognitoforms.com/support/1038/data-integration/mcp-connector). The service endpoint is `https://mcp.cognitoforms.com/mcp`; follow the current OAuth setup for the selected agent. Account sign-in and organization selection are user steps. Never put access tokens in this skill, website assets or tracked configuration. Do not substitute Amazon Cognito or a third-party connector with different capabilities.

As checked on 2026-10-28, the connector requires a supported paid Cognito organization and administrator access. Consult the guide for current plan/authentication requirements. Copying this skill does not connect the account. Record connection as ready, unavailable or awaiting sign-in; keep independent website work moving. Do not claim MCP readiness until a read-only tool call confirms the intended organization/form access. Discover actual tool schemas rather than inventing tool names or assuming form-edit operations are supported.

## Build the form

Identify the intended organization, form and purpose; reuse an existing form when appropriate. Before authorized changes, inspect its schema, internal field names, embed mode and existing workflows. Draft the requested fields and conditional rules, then use available MCP creation/edit tools within the user's scope. If an operation is unavailable, use the supported form builder or provide the specific remaining manual step. Do not describe an unexecuted schema change as complete. Installing the skill does not itself authorize creating forms, submitting entries, enabling notifications or publishing live forms.

Every new Cognito website form needs these **optional Textbox fields**, with these exact internal names at the form root. Use input fields, not calculated fields. Preserve existing business prefills and required fields. Existing nested layouts need a deliberate payload mapping; labels alone do not determine internal names.

| Query/stored value | Cognito internal field | Default |
| --- | --- | --- |
| gclid | Gclid | null |
| gbraid | Gbraid | null |
| wbraid | Wbraid | null |
| utm_source | LeadSource | Website |
| utm_medium | UtmMedium | Form |
| utm_campaign | CampaignName | null |
| utm_adset | AdsetName | null |
| utm_ad | AdName | null |
| utm_term | UtmTerm | null |
| utm_content | UtmContent | null |
| First landing page URL | LandingPage | captured URL |
| First browser user agent | UserAgent | captured user agent |

Set **Show This Field → When** on all twelve fields: First Name equals `ADMIN` **AND** Last Name equals `ADMIN`. For a root Name field whose internal name is `Name`, the expression is:

```text
=Name.First = "ADMIN" and Name.Last = "ADMIN"
```

Use the actual name-field paths from the schema and validate the expression in Cognito. Require both uppercase values without trimming or case normalization. Hide fields for blank, ordinary, lowercase, mixed-case or only-one-ADMIN names; hide them again when either name changes. Do not prefill the visitor's name with ADMIN. These fields remain populated while hidden. Test that hidden values survive an authorized test submission; CSS hiding alone is not the visibility rule. This is a diagnostic visibility shortcut, not authentication or permission to access private data. Never put credentials or trusted authorization decisions in these fields.

Sources: [prefill syntax and restrictions](https://www.cognitoforms.com/support/65/data-integration/prefilling-a-form), [field visibility](https://www.cognitoforms.com/support/23/building-forms/showing-hiding-fields). Authenticated forms do not support this prefill mechanism; record that limitation instead of claiming it works.

## Install the site scripts

Copy [tracking-head.js](../assets/cognito/tracking-head.js) and [tracking-footer.js](../assets/cognito/tracking-footer.js) into the website's durable integration code, normally its companion plugin. Enqueue them using WordPress APIs, with the head script before embeds and the footer script after the chosen embed/configuration. Keep `wp_head()` and `wp_footer()` in templates. Do not put literal script tags into a JavaScript file or paste scripts into every editor page. Avoid duplicate installations, and follow the site's existing CSP and consent lifecycle where configured rather than bypassing them.

The head script preserves the supplied contract: `tracking_parameters` in same-origin localStorage, first-visit attribution for 90 days, Website/Form defaults, full landing URL and user agent, and `window.__cognitoTrackingPrefill`. A later campaign does not overwrite a valid first touch, including an initial direct visit. Missing, malformed or expired storage is recaptured. Blocked storage falls back to memory for the current page; cross-page persistence is then unavailable. Expiry is checked on use, not by a background deletion service. These values are visitor-controlled attribution data, not trusted identity. Do not add production console logging of identifiers or URLs.

The footer supports delayed embed loading with a bounded wait (about 15 seconds), and avoids duplicate prefills after dispatch. With no configured targets it stays idle, so it can be included on pages without forms. For one form, set this configuration before the footer script, after the form's official embed code:

```js
window.__cognitoTrackingTargets = [{ key: 'contact' }];
```

Use that unscoped form only when the page contains exactly one Cognito embed. For multiple Seamless embeds, supply each real `data-form` ID and its unique wrapper selector, following [Cognito's mounting instructions](https://www.cognitoforms.com/support/380/style-publish/seamless-embedding):

```js
// Example IDs: replace with the actual embed IDs and matching wrapper elements.
window.__cognitoTrackingTargets = [
    { key: 'contact', formId: '9', selector: '#contact-form' },
    { key: 'quote', formId: '10', selector: '#quote-form' }
];
```

For a form revealed/inserted after the initial wait, call `window.prefillCognitoTracking([target])` from its embed initialization path using its configured target. Reusing a dispatched key does not overwrite visitor edits. A deliberately remounted form needs a new instance key. For iframe embeds, follow the [documented iframe integration](https://www.cognitoforms.com/support/168/style-publish/iframe-embedding); do not query or edit a cross-origin frame's DOM. Use only one Cognito prefill method per page; merge any existing business prefill into the integration before dispatch so tracking does not replace it.

`window.__cognitoTrackingStatus` reports pending, dispatched, unavailable or error per target. Dispatched means only that the SDK call returned; verify rendered values and saved entry data separately. If the SDK reports ready before accepting prefills, use its actual supported initialization path for that embed and test it; do not invent a ready event or retry forever.

## Verification

Test fresh and returning visits, all parameter mappings, encoded query values, direct-visit defaults, exact expiry, invalid JSON, invalid expiry and blocked storage. Confirm attribution survives navigation until expiry without sliding renewal. Test delayed SDK loading, pages without forms, multiple forms, repeated initialization and a lazy form after timeout. Check real fields in a connected preview and an authorized test entry with external notifications/workflows contained. Verify all visibility combinations above and preservation of hidden values. Never create a real sales lead merely to test tracking.

Record the actual form/internal names, script locations, connection status, visibility rule and completed checks in the brief/run guide without secrets. Script tests using a stub SDK do not prove the live Cognito form, OAuth connection or saved entries work.
