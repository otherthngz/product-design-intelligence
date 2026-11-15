<!-- pdi-topic: {"id":"responsive-accessible-ui","domain":"frontend-engineering","depths":["foundation","practitioner","advanced"],"sources":["wcag22","w3c-structure"]} -->
# Responsive, accessible interface implementation

## What and why
Frontend implementation turns information architecture, visual hierarchy, and interaction contracts into an operable interface across devices and assistive technologies. Semantic HTML, disciplined visual composition, responsive CSS, and reliable state handling ensure people can perceive, understand, navigate, and operate the product without unnecessary technical complexity.

## When to apply
When prototyping or implementing a page, form, component, or dashboard, or when auditing rendered interfaces for accessibility, visual discipline, and overengineering.

## Fundamental principles
**Foundation:**
- **Enforceable accessibility requirements vs. context-dependent heuristics:**
  - *WCAG 2.2 A/AA criteria:* Apply the success criteria relevant to the content, including keyboard access, visible focus, accessible names, contrast, error identification, and target size with its exceptions. The applicable legal or policy standard depends on context. Semantic elements, logical heading levels, `aria-invalid`, `:focus-visible`, and reduced-motion preferences are useful techniques or practices, not universally mandated implementations. Disabling interaction-triggered motion is a separate WCAG 2.2 AAA criterion; consult the actual criteria and exceptions rather than equating this checklist with conformance.
  - *Context-dependent recommendations:* Visual density, multi-column vs. single-column desktop layouts, and table horizontal scroll vs. stacked rows depend on task comparison needs and user expertise.
- **Visual discipline vs. arbitrary minimalism:** Use typography scale, alignment, proximity, and semantic color tokens to create clear hierarchy. Do not treat whitespace or visual minimalism as an unconditional goal—dense tabular alignment (`font-variant-numeric: tabular-nums`) is superior for data comparison, while generous spacing helps first-run reading comprehension. Avoid decorative complexity (multiple competing shadows, gradients, nested bordered boxes, or unmotivated icons beside obvious labels).

## Practical implementation
**Practitioner:**
- **Semantic structure & state handling:** Use native HTML elements (`<button>`, `<select>`, `<input>`, `<dialog>`, `<table>`, `<th scope="col|row">`) before reaching for custom ARIA widgets. Render dynamic data with safe text APIs (`textContent`) and implement explicit empty, loading, validation-error, network-failure, and success states.
- **Keyboard & focus management:** Keep tab order matched to visual reading order. When a step changes, a modal opens/closes, or validation fails, move focus predictably (e.g., to the new step heading, first invalid input, or triggering button) and announce asynchronous updates via `role="status"` or `role="alert"`.
- **Proportional engineering (anti-overengineering):** Match technical complexity to actual requirements. Do not introduce heavy state libraries, premature component abstractions, or complex client-side routing for a simple form or localized prototype.

**Advanced:** Consider state ownership, idempotent API submission (preventing duplicate charges or mutations while pending), privacy/PII protection, progressive enhancement, performance budgets, and assistive technology interoperability. Automated linters and DOM checks catch structural regressions but never prove full WCAG conformance or real-world usability.

## Good and bad examples
Good: A labeled period selector updates a semantic `<table>` with `tabular-nums`, focusable scroll region (`tabindex="0" role="region" aria-label="..."`), visible `:focus-visible` outline, and an `aria-live` status update. Bad: Clickable `<div>` buttons with no keyboard support, skipped heading levels (`<h1>` to `<h3>`), unlabeled inputs relying on placeholder text, or wrapping a 3-field form in a 5-layer custom state machine.

## Common mistakes
Confusing automated check passes with full accessibility conformance; relying on color or placeholder text alone; losing focus after modal dismissal or step transitions; adding unnecessary dependencies or reusable component wrappers for one-off layouts; shipping author meta-notes (`sample data`) in visible product DOM.

## Evaluate the result
- **Evaluation signals:** Do deterministic checks (`python3 scripts/audit_artifact.py`) pass with zero errors? Are all primary and error recovery flows completable by keyboard alone with visible focus? Does layout reflow cleanly at narrow (`320px–390px`) and desktop viewports without unintended page-level horizontal overflow? Is technical implementation free of overengineering?

## AI application
Inspect the existing stack and UI kit before writing code; build real, semantic artifacts when authorized; run deterministic validation (`scripts/audit_artifact.py` and DOM state checks); and explicitly separate verified checks from untested assistive-technology or live-backend requirements.

## Related concepts
[Task hierarchy](../ux-design/task-hierarchy.md), [cognitive human factors](../ux-design/cognitive-human-factors.md), [component contracts](../design-systems/component-contracts.md), [ui kit adaptation](../design-systems/ui-kit-adaptation.md).

## References and further learning
[W3C page structure tutorial](https://www.w3.org/WAI/tutorials/page-structure/), [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/), [W3C heading checks](https://www.w3.org/WAI/test-evaluate/preliminary/), and [animation from interactions, level AAA](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions). See [source registry](../sources.yaml).
