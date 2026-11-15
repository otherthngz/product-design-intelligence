# Analytics dashboard demonstration

[Open the revised local prototype](index.html) or [compare the original](before.html). No server, credentials, AI model or backend is required. Use **Reporting period** to switch the illustrative data. The dashboard is not connected to a product and does not save or transmit data.

## Framing and assumptions

**Request supplied:** an accessible, responsive analytics dashboard for a B2B SaaS product. **Assumptions:** a customer-success team needs to prepare a review and identify accounts for follow-up; the sample counts, names, periods and flags are invented for demonstration. No real user needs, definitions, baselines or business goals were supplied. **Hypothesis:** a short summary followed by a detailed table helps a team decide where to investigate; this requires user research. Active accounts are unique over the selected period; weekly activity is a separate count and should not be summed into the period total. A flag is a sample label, not a predictive model.

## Knowledge-driven decision log

| Decision | Topic and reasoning | Alternative / trade-off |
|---|---|---|
| Organize around a review decision, explicitly label sample data and flag uncertain metric definitions. | [Product outcomes](../../knowledge/product-design/outcomes.md): connect a user job to an observable decision. | A general analytics dashboard could cover more roles, but would need evidence about their priorities. |
| Put summary first, followed by the accounts needing review, then the trend and exact weekly table. | [Task hierarchy](../../knowledge/ux-design/task-hierarchy.md): support scanning and access to exact values. | A dense table-first layout may work better for expert analysts; test it. |
| Use a shared metric strip, panel, token and status vocabulary. | [Component contracts](../../knowledge/design-systems/component-contracts.md): consistent anatomy and states. | A real team system should replace these illustrative tokens after review. |
| Use labeled native select, semantic table, text status, visible focus and narrow-screen reflow. | [Responsive accessible UI](../../knowledge/frontend-engineering/responsive-accessible-ui.md): preserve keyboard and text access. | A chart offers visual scanning but needs its tabular alternative. |
| Keep the “review” wording human-directed and avoid an AI-generated prediction. | [Human-reviewed AI](../../knowledge/ai-product-building/human-reviewed-ai.md): expose uncertainty and keep consequential judgments with people. | Real AI assistance would require data permissions, evaluation and review controls. |

These links show how guidance informed design choices; they do not prove retrieval improved an agent's performance compared with a controlled baseline. No AI feature or trained model is implemented.

## Implementation and handoff

The period selector updates all summary values, weekly table values, bars, account examples and a status message from local sample data. Cards are static summaries, not navigation. The chart is decorative to assistive technology; the adjacent table supplies exact weekly values. Tables scroll horizontally at narrow widths when necessary. For a real product, define metric semantics and time zones, obtain actual data and permissions, handle loading, no data and network failure, validate server responses, use the team's component system and review with users and assistive technology. The flagging method and review owner remain unspecified.

## Validation

Validation results are recorded after execution in [the audit report](../../docs/reference/practical-audit.md). Reasoning and trade-offs above are expert hypotheses, not evidence that users find the design effective or that it meets an accessibility standard.

## Visual re-review

The original used the same green, serif headline and rounded card treatment as the unrelated onboarding demo. The revision adopts a compact, neutral data workspace with a clear “Account overview” heading and puts the review list before the chart. This is a design judgment informed by the [frontend-design skill](../../.agents/skills/frontend-design/SKILL.md), not evidence of improved user outcomes. The [re-review](../../docs/reference/visual-design-review.md) records observations and unresolved issues.

The account list shows the number of visible rows and the total flagged accounts. The remaining records and a way to view them are not implemented.
