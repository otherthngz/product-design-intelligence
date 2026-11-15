<!-- pdi-topic: {"id":"task-hierarchy","domain":"ux-design","depths":["foundation","practitioner","advanced"],"sources":["w3c-structure","wcag22"]} -->
# Task hierarchy and usable flows

## What and why
Task hierarchy and information architecture (IA) organize content, navigation, and interaction patterns around what people need to find, compare, decide, and execute. Proper pattern selection minimizes visual search, cognitive friction, and motor effort while protecting against consequential errors.

## When to apply
When defining navigation taxonomy, choosing between competing interaction patterns (tables vs. cards, single-page forms vs. multi-step wizards, inline vs. modal editing, browse vs. search), mapping multi-step flows, or designing analytics dashboards.

## Fundamental principles
**Foundation:**
- **Information scent & taxonomy:** Structure navigation around user mental models and domain objects (task-oriented or object-oriented IA), not internal org charts. Strong information scent allows users to predict what lies behind a link or category before activating it.
- **Visual hierarchy & Gestalt grouping:** Use heading levels (`H1`→`H3`), spatial proximity, alignment, contrast, and typography to establish a clear scanning order (primary decision → core controls → secondary metadata) without wrapping every element in nested bordered boxes.
- **Evidence quality:** Semantic structure (`<nav>`, `<main>`, `<table>`, heading hierarchy) and keyboard operability are enforceable standards (WCAG 2.2); layout patterns (cards vs. tables, tabs vs. sidebar) are context-dependent engineering and human-factors trade-offs.

## Practical implementation
**Practitioner (Context-Sensitive Pattern Selection Matrix):**
- **1. Tables vs. Cards for Data Display:**
  - *Mechanism:* Aligned columns and `tabular-nums` support rapid vertical scanning and multi-attribute comparison; cards isolate heterogeneous media or standalone summaries.
  - *When to consider a Table:* Users compare attributes across many records, sort/filter columns, or scan dense operational/financial data.
  - *When to consider Cards:* Browsing visual catalog items or distinct dashboard modules where images or individual summaries support the task. Attribute counts alone do not determine the pattern.
  - *Failure mode:* Defaulting to a 3-column card grid for enterprise record management, destroying scan efficiency and hiding rows below the fold.
- **2. Single-Page Form vs. Multi-Step Wizard vs. Inline Editing:**
  - *When to consider a Single-Page Form:* Related fields where users benefit from seeing the whole scope at once; field count alone does not determine complexity.
  - *When to choose a Multi-Step Wizard:* Infrequent, high-consequence, or branching setup flows (onboarding, tax/compliance filing, checkout) where chunking reduces initial overwhelm and step-by-step validation prevents downstream errors.
  - *When to choose Inline / Bulk Editing:* Expert users updating 1–2 fields repeatedly across dozens of rows; wizards or modals here cause severe interaction clutter.
- **3. Progressive Disclosure vs. Direct Visibility:**
  - *Applicability:* Disclose secondary or rare configuration options on demand (accordions, drawers, advanced toggles) to keep primary flows clear for novices.
  - *Exception:* Never hide high-frequency expert controls, critical status alerts, or destructive-action warnings behind overflow menus or extra clicks.
- **4. Search vs. Browse & Filtering:**
  - *Applicability:* Provide direct browse/hierarchy when users benefit from seeing the collection or do not know exact item names; consider search and faceted filtering when collection size, known-item seeking, or comparison warrants them. Test findability rather than relying on an item-count threshold.
- **5. Analytics Dashboards & Data Visualization:**
  - *Decision rule:* Start from the operational decision. Use summary metrics only when paired with comparison context (baseline, period delta, or threshold); use line/bar charts only when temporal trends, distributions, or multi-series comparisons matter; use prioritized action tables when users must inspect and act on specific records. Never generate a chart for every metric or duplicate the same numbers across KPI cards, charts, and prose.

**Advanced:** Balance cross-role workflows (e.g., novice requester vs. expert approver) by offering clean defaults alongside high-density views, saved filters, and keyboard shortcuts rather than forcing one lowest-common-denominator flow.

## Good and bad examples
Good: An enterprise account-review workspace places the filterable table of flagged accounts (`Showing 12 of 84`) and inline status actions above a single trend chart, with exact tabular values for accessibility. Bad: A settings screen split into 12 separate cards with a 3-step modal to toggle email notifications, or an analytics page with 8 decorative charts that support no concrete action.

## Common mistakes
Defaulting to card grids for comparative data; forcing daily power users through multi-step wizards; hiding primary actions in `...` menus to make the screen look "clean"; adding search bars to 5-item lists; designing dashboards around chart variety rather than decision hierarchy.

## Evaluate the result
- **Evaluation signals:** Does the chosen container (table, list, card, wizard, inline row) match task frequency, attribute count, and user expertise? Can users complete the primary flow via keyboard with preserved state on `Back` or validation error? Does every dashboard chart answer a distinct analytical question?

## AI application
Before generating a layout, explicitly justify the structural pattern against user expertise, task frequency, and data shape. Reject generic SaaS dashboard templates and unmotivated card grids when a structured table, sectioned form, or direct action is more effective.

## Related concepts
[Product outcomes](../product-design/outcomes.md), [cognitive human factors](cognitive-human-factors.md), [responsive and accessible UI](../frontend-engineering/responsive-accessible-ui.md).

## References and further learning
[W3C page structure tutorial](https://www.w3.org/WAI/tutorials/page-structure/) and [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/) provide structure and accessibility guidance. See [source registry](../sources.yaml).
