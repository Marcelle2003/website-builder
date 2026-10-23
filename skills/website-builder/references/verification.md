# Verify the result

Match checks to the change. Run the project's required asset build, PHP syntax/coding checks, and relevant behavioural checks. Use the installed WordPress/PHP versions and existing test tools rather than imposing a new suite for every task. Add tests for meaningful logic and regression risks, not for every reversible copy or colour edit.

## WordPress integration

For a new theme, verify activation on a disposable local or staging installation, correct templates, asset loading, and the absence of related PHP errors. Check the actual content workflow: edit a distinctive local test value or image in WordPress, save/publish it, and confirm it reaches the visitor page through the documented cache/update path. Do not publish test content to a live client site without authorization. Check appropriate previews and empty content states.

Verify editor controls remain usable and represent the promised editing model. Tailwind output must include variants used by editable components; global resets must not damage WordPress or third-party controls. For block-theme or Site Editor changes, account for saved database customizations before concluding that a template file is unused or broken.

When changing PHP that handles data, check context-appropriate escaping, input validation, authorization, and nonce protection where applicable. Keep durable functionality out of theme-only storage. Exercise relevant plugin integrations when the change touches them; a normal theme change does not call for a blanket security audit.

## Browser evidence

When browser tools are available, inspect the rendered result at a representative wide and narrow viewport. Check more than the homepage when shared components changed. Confirm loaded images/fonts, readable text, no accidental horizontal overflow, visible focus, and usable touch targets. Check browser errors and failed requests related to the change.

Exercise affected interactions: open and close menus/FAQs, rapid toggle, gallery navigation, back/forward navigation, keyboard activation/Escape/focus return, and reduced-motion preferences where supported. For scroll sequences, inspect actual movement through the entire section, both scroll directions, responsive layout changes, and final content visibility. Check animation setup/cleanup on any navigation mechanism actually used. Test actual forms with safe local data; do not submit messages or payments to real services as a visual check.

For broad movement work, exercise scroll reveals and hover/focus feedback on the affected components. Check touch activation without hover, direct links and restored scroll positions, reduced-motion content visibility, and any entrance sequence with immediate navigation/actions. Confirm feedback matches actual action outcomes.

For a palette change, inspect computed styles and interactive states as well as searching source literals. For image replacements, inspect the rendered image, not only a successful HTTP response. Verify coordinated motion in the browser; a final screenshot cannot establish its timing or behaviour.

For new or materially changed project instructions, follow [fresh-chat verification](project-instructions.md#verify-a-fresh-chat). Check instruction loading independently from installation and build results. Keep the AI-maintained brief current with confirmed decisions and actual implementation status before handing work back.

## Scope and truthful reporting

Check that the diff matches the request and unrelated user work remains intact. Run checks once successfully, expanding or repeating them when a subsequent change or unresolved issue warrants it. If a prerequisite is missing, perform useful remaining checks and record the specific blocked verification.

Keep a short evidence record: commands and outcomes, pages/viewport sizes, interactions exercised, screenshots when useful, and untested items. Never label a build-only check as visual QA, claim WCAG compliance from a quick review, or report macOS testing based on Linux alone.

Record meaningful confirmed skill problems through [local feedback](feedback.md), preserving the difference between an observed failure and an inferred cause. Exclude raw feedback, private inbox data, and `.website-builder-local.json` from routine commits. A successful website check does not validate a proposed skill change or authorize publishing it.

End with the usable result: preview location, key changes, how to edit relevant content, passed checks, and concrete remaining limitations. Only describe framework capabilities that are actually used in the implementation.
