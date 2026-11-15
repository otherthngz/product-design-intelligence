# Design team request: dashboard handoff

**Source:** [analytics dashboard prototype](../analytics-dashboard/index.html) and [decision log](../analytics-dashboard/README.md). Routed to `design-handoff` with `component-contracts` and `responsive-accessible-ui`. No actual team design system or tokens were supplied: the following are prototype choices, not approved organizational requirements.

| Element | Proposed contract | Required review |
|---|---|---|
| Reporting period | Native labeled select; changing it updates the same period across summaries, chart, table and status text. | Map to the existing select component and agree date/time zone semantics. |
| Metric card | Label, numerical value and explanation; no card click action. | Define each metric, missing data behavior and precision; map type, spacing and colors to existing tokens. |
| Weekly activity | Visual bars hidden from assistive technology with exact values in a semantic table and caption. | Review chart/table equivalence, contrast, accessibility and sample-to-real data mapping. |
| Flagged list | Account name, last check-in and textual status; horizontal scrolling if needed on narrow screens. | Define flags and actions, permissions, empty/loading/error states, and account links in the real system. |

**Layout:** the revised overview places the account review table after summary metrics and before the trend; the example uses a shared blue-neutral palette and a single system font. These are prototype decisions, not approved tokens. Tables live in focusable named scroll regions for keyboard access.

**Acceptance criteria:** keyboard can reach the selector and table regions with visible focus; changing period updates all associated values; text remains available without depending on bar color; layout reflows at narrow widths. **Validation:** see [practical audit](../../docs/reference/practical-audit.md). **Dependencies and open decisions:** actual component library, tokens, data contracts, ownership, accessibility target, failure behavior and sign-off are not available. The prototype is not a complete production specification.
