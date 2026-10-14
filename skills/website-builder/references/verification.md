# Verify the result

Match checks to the change. Run the project's required build, lint, type, and relevant behavioural checks. Add tests for meaningful logic and regression risks, not for every reversible copy or colour edit.

## Browser evidence

When browser tools are available, inspect the rendered result at a representative wide and narrow viewport. Check more than the homepage when shared components changed. Confirm loaded images/fonts, readable text, no accidental horizontal overflow, visible focus, and usable touch targets. Check browser errors and failed requests related to the change.

Exercise affected interactions: open and close menus/FAQs, rapid toggle, gallery navigation, back/forward navigation, keyboard activation/Escape/focus return, and reduced-motion preferences where supported. Test actual forms with safe local data; do not submit messages or payments to real services as a visual check.

For a palette change, inspect computed styles and interactive states as well as searching source literals. For image replacements, inspect the rendered image, not only a successful HTTP response. For CMS integration, publish a distinctive local test value and verify that value reaches the page using the documented update path.

For new or materially changed project instructions, follow [fresh-chat verification](project-instructions.md#verify-a-fresh-chat). Check instruction loading independently from installation and build results. Keep the AI-maintained brief current with confirmed decisions and actual implementation status before handing work back.

## Scope and truthful reporting

Check that the diff matches the request and unrelated user work remains intact. Run checks once successfully, expanding or repeating them when a subsequent change or unresolved issue warrants it. If a prerequisite is missing, perform useful remaining checks and record the specific blocked verification.

Keep a short evidence record: commands and outcomes, pages/viewport sizes, interactions exercised, screenshots when useful, and untested items. Never label a build-only check as visual QA, claim WCAG compliance from a quick review, or report macOS testing based on Linux alone.

Record meaningful confirmed skill problems through [local feedback](feedback.md), preserving the difference between an observed failure and an inferred cause. Exclude raw feedback, private inbox data, and `.website-builder-local.json` from routine commits. A successful website check does not validate a proposed skill change or authorize publishing it.

End with the usable result: preview location, key changes, how to edit relevant content, passed checks, and concrete remaining limitations. Only describe framework capabilities that are actually used in the implementation.
