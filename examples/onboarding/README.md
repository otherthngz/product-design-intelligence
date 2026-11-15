# Example: first-time SaaS onboarding

[Open the prototype](index.html). It is fictional and local; no sign-up, storage or backend is implemented.

## Framing and evidence

**Objective (user-provided brief):** demonstrate a responsive SaaS onboarding experience for first-time users. **Assumptions:** the fictional product, Fieldnote, helps organize work; first-time users need a workspace name and a starting goal; these two choices are useful before their first task. No user interviews, research or business metrics were provided. **Hypothesis:** asking for two small choices reduces uncertainty about starting; test this with real users before adopting it. A possible success measure is the proportion of new users reaching a meaningful first action; no target or baseline is known.

**Scope:** local, two-step exploration, not actual account creation. **Constraints:** no external services or credentials, responsive layout, honest local-state messaging. **Open question:** what constitutes the product's actual first meaningful action, and is goal selection necessary?

## Flow and decisions

1. Enter workspace name → trim whitespace; empty/whitespace-only input shows a message and focuses the field.
2. Choose one goal → browser requires a selection. Back returns to the name and preserves it.
3. Finish → summary displays the selected values. Edit choices returns to step 2; Back allows editing the name. Refresh discards everything.

We chose two steps to keep each decision focused. A single form would be faster and may be preferable if testing finds the extra transition unnecessary. No invitation step is included because the brief does not establish a need for one. The “one minute” label is illustrative copy, not measured completion time. Responsive layout stacks the contextual panel above the form on narrow screens; the additional scrolling is a trade-off to review with users.

## Engineering handoff

**Source of truth:** [index.html](index.html). The current implementation has two forms, three radio options, and a local success panel. Use the existing labels, error text and summaries as prototype content, subject to product review.

Acceptance criteria:

- Workspace name is required, trimmed, and limited to 80 characters. Blank input stays on step 1 with an associated error and focus on the field.
- Exactly one goal is required; a valid selection reaches the summary. Back and Edit retain current values while the page remains open.
- After a successful transition, focus moves to the new heading; controls have visible focus styles and labels. Layout stacks at widths of 720px or below.
- Summary displays user text as text, not HTML; no request, account creation or persistence occurs.

**Unresolved for production:** account and workspace ownership, persistence and server-side validation, authorization, duplicate names, network/loading/failure states, editing after onboarding, analytics consent, product copy and design-system mapping. No owner or approval policy has been supplied. Implement these in the real product rather than interpreting the local success panel as an actual save.

## Validation recorded

On 2026-11-14 the in-app browser was used against a local server: blank workspace showed the error and focus, a name with surrounding spaces was trimmed, Back retained it, selecting a goal reached a summary with both values and focus moved to the success heading. A 390 × 844 viewport displayed a stacked layout; a DOM measurement reported no horizontal overflow at that viewport. Automated standard-library tests check metadata shape, case coverage, safe copy creation, and basic prototype markup. These are limited checks; full keyboard navigation, all paths, assistive technologies, contrast, zoom, other browsers and user testing remain unverified. No accessibility conformance claim is made.
