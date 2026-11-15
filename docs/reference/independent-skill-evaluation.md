# Independent skill evaluation

On 2026-11-14, a separately delegated agent received realistic requests and used the PDI skills. This was a limited evaluation within the same conversation, not a blinded study or a comparison across models. The original generated artifacts are retained here as evidence, including their known problems; they are not recommended UI examples.

## Customer-success dashboard

**Request:** Build a responsive B2B analytics dashboard with metrics, accounts to follow up and a period selector. The agent selected `ui-prototyping` and `frontend-design`, and produced [HTML](../../examples/evaluations/independent-dashboard/index.html) and a [handoff](../../examples/evaluations/independent-dashboard/handoff.md).

**Observed:** No author-facing sample-data badge or prototype footer appeared in the HTML; fictional data and missing services were documented in the handoff. A Node test with a simulated DOM exercised the period handler and observed changed metrics, accounts and status. No browser was available to the evaluator, so actual responsive layout, keyboard behavior and screen-reader behavior were not verified.

**Finding:** The metric said 8 accounts needed follow-up while the table showed 2 without communicating that the list was partial. The handoff acknowledged the mismatch, but an end user could not see it. The [review guide](../../.agents/skills/ui-prototyping/references/review.md) now requires checking totals, visible rows and filtering; if a list is partial, show the count and total and provide access to the rest when the task requires it. The existing analytics demo now reports “Showing 2 of 12 accounts” and updates that count with the period; the rest of the list is still not implemented.

## Checkout without a payment service

**Request:** Build a checkout prototype with a Pay button and no payment service. The agent selected `interaction-design`, `ui-prototyping` and `frontend-design`, and produced [HTML](../../examples/evaluations/independent-checkout/index.html) and a [handoff](../../examples/evaluations/independent-checkout/handoff.md).

**Observed:** A Node test with a simulated DOM called the submit handler, which prevented navigation and reported that no payment had occurred. This is not a browser click and does not verify native form validation, focus or responsive layout.

**Finding:** The interface promised an order-confirmation email although no email or order service existed. The review guide and skill now explicitly check the whole interface for unsupported future promises, as well as false success states. The original evaluation artifact retains the issue so the finding remains inspectable.

## Limits and next steps

These two examples show both useful behavior and failure cases, not a measured reliability rate. After updating the rules, the same delegated agent performed a separate re-test; results are below. Figma MCP was not exercised. More representative tasks, actual browser and assistive-technology checks, and human design review are needed before claiming the skills reliably produce high-quality designs.

## Re-test after the skill update

The same delegated agent read the updated skill and created a new [dashboard](../../examples/evaluations/independent-retest/dashboard.html), [checkout](../../examples/evaluations/independent-retest/checkout.html) and [handoff](../../examples/evaluations/independent-retest/handoff.md). This is not a blinded or cross-model test. The dashboard displayed “2 of 8” and offered a control to reveal all eight; the checkout stated that payment was unavailable and did not promise an email. The agent tested the handlers with a simulated DOM, including the list toggle and checkout status; it could not test browser rendering, native keyboard behavior, contrast or assistive technology.

Separately, the main agent checked the existing PDI dashboard in an in-app browser: changing the period updated the count from “2 of 12” to “2 of 9” and changed the displayed rows. The existing dashboard still has no way to reveal the remaining accounts.
