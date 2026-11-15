<!-- pdi-topic: {"id":"product-outcomes","domain":"product-design","depths":["foundation","practitioner","advanced"],"sources":["govuk-needs"]} -->
# From user needs to product outcomes

## What and why
Product framing connects a person's underlying need and task context to a business objective and a decision the product can support. It prevents teams from shipping requested screens that fail to solve the root problem or optimizing vanity engagement metrics that degrade user experience.

## When to apply
At discovery, when requirements are ambiguous, when a stakeholder requests a solution-first feature ("add a dashboard with more charts"), or when selecting product metrics and experiment plans.

## Fundamental principles
**Foundation:**
- **Principle & mechanism:** Distinguish the **stated request** from the **underlying problem**, the **intended user outcome**, the **desired product/business outcome**, and the **actual constraints**. Users hire a product to complete a job or make a decision; features are merely mechanisms.
- **Evidence hierarchy:** Rank inputs by reliability without treating any tier as infallible: (1) verified user research and observed product behavior, (2) reliable product analytics and validated experiments, (3) applicable accessibility and regulatory standards, (4) established human-factors research, (5) existing product conventions and design system constraints, (6) well-supported design heuristics, and (7) explicit professional judgment and assumptions. Mandatory accessibility or safety standards cannot be overridden by conversion metrics.

## Practical implementation
**Practitioner:**
- **Applicability & context dependencies:** Frame problems using: *"When [situation/context], [user group] needs to [job/decision] so [observable user outcome], enabling [business outcome] under [constraints]."* Adapt framing depth to product maturity (early discovery vs. mature enterprise workflow), task criticality, and decision reversibility.
- **The "No-UI / Smaller Intervention" check:** Before proposing a new screen, dashboard, or workflow, evaluate whether the problem is better solved by removing a step, changing a default setting, fixing unclear terminology, or exposing existing data inline.
- **Alternatives & trade-offs:** Compare at least two meaningful alternatives when a decision is consequential or ambiguous. Recognize when business goals and user outcomes conflict—increasing interaction frequency, time-on-page, or conversion through friction or dark patterns harms long-term retention and trust. Pair every primary success metric with a **counter-metric** (e.g., task completion time, error/reversal rate, support ticket volume).
- **Exceptions:** Do not block straightforward, reversible implementation tasks (copy tweaks, spacing fixes) with heavyweight problem-framing workshops.

**Advanced:** Examine conflicts among customer segments (novice buyers vs. daily operators), role permissions, privacy boundaries, and operational maintenance cost. Distinguish reversible two-way-door decisions (copy, layout density tweaks) from expensive one-way-door decisions (navigation taxonomy, data-model workflows, component API contracts) and scale validation rigor accordingly.

## Good and bad examples
Good: When asked to "add a dashboard with more charts," framing identifies which operational decision the account manager must make before weekly reviews, compares a multi-chart dashboard against a prioritized exception table, and proposes measuring follow-up completion without increasing review time. Bad: "Increase dashboard engagement by 30%" with no user decision, fabricated baseline percentages, and six decorative KPI charts.

## Common mistakes
Treating a stakeholder's requested UI pattern as a validated user need; inventing research findings or quantitative baselines when evidence is missing; equating higher click volume or time-in-app with user success; using fictional personas as empirical evidence; applying identical framing overhead to trivial UI fixes and core workflow architecture.

## Evaluate the result
- **Evaluation signals:** Can a reviewer clearly distinguish the stated request, underlying user problem, user outcome, business outcome, and hard constraints? Are evidence sources (`user-provided`, `verified`, `assumption`, `hypothesis`) explicitly separated? Were simpler or non-UI alternatives considered? Is validation proportional to decision reversibility?

## AI application
When context or analytics are missing, do not fabricate citations or metrics—use verified repository facts, declare bounded assumptions explicitly, prefer reversible design choices, and ask clarifying questions only when missing information materially changes the solution.

## Related concepts
[Task hierarchy](../ux-design/task-hierarchy.md), [cognitive human factors](../ux-design/cognitive-human-factors.md), [human-reviewed AI](../ai-product-building/human-reviewed-ai.md).

## References and further learning
[GOV.UK: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) supports learning and validating needs. [Source registry](../sources.yaml) records provenance and review scope.
