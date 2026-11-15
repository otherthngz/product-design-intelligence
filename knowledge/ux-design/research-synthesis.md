<!-- pdi-topic: {"id":"research-synthesis","domain":"ux-design","depths":["foundation","practitioner","advanced"],"sources":["govuk-needs","pdi-guidance"]} -->
# User research planning and evidence synthesis

## What and why
User research planning and evidence synthesis structure how teams learn from real people without inventing observations or overgeneralizing from small samples. It separates direct quotes and observed behaviors from team assumptions and product hypotheses.

## When to apply
Before framing or designing a feature with high uncertainty, when preparing usability tests or discovery interviews, or when synthesizing raw interview notes, support tickets and session observations into actionable product findings.

## Fundamental principles
**Foundation:** Never fabricate participant quotes, sample sizes, quantitative significance or behavioral consensus. Tag every insight by its source: **user-provided**, **verified** (directly observed in supplied transcripts or metrics), **assumption**, or **hypothesis**. Small qualitative samples reveal usability obstacles and mental models, not population percentages.

## Practical implementation
**Practitioner:** Define the decision the research must inform, target participant criteria, recruitment screener constraints, and non-leading task scenarios or interview questions. During synthesis, group raw observations by task and behavior rather than by what users said they might buy. Pair each finding with concrete evidence (e.g., participant ID or ticket reference), severity, confidence level and a testable design recommendation.

**Advanced:** Establish research repositories, privacy/PII redaction rules, consent tracking and triangulation across qualitative usability findings and quantitative product telemetry. Prevent stakeholder confirmation bias by documenting disconfirming evidence and sample limitations explicitly.

## Good and bad examples
Good: "Observed in 3 of 5 supplied onboarding transcripts (P1, P3, P4): participants hesitated at the 'Workspace slug' field and asked whether it could be changed later. Hypothesis: renaming the label and stating editability will reduce setup drop-off." Bad: "80% of users hate technical jargon and want an AI onboarding assistant" (fabricates population claims and jumps to an unvalidated solution).

## Common mistakes
Writing leading interview questions ("How much would this feature save you time?"); treating feature requests from a single vocal customer as a validated pattern; summarizing transcripts by inventing composite quotes; claiming statistical significance from five usability sessions.

## Evaluate the result
Can a reviewer trace every synthesis finding back to a supplied transcript, ticket or dataset? Are sample limits, unrepresented user groups and recruitment biases explicitly stated? Are interview tasks non-leading and tied to a concrete product decision?

## AI application
When asked to plan research, produce neutral task prompts, screening criteria and observation checklists. When asked to synthesize supplied notes, cite exact source identifiers and separate observed actions from inferred motives; if no raw research data is supplied, refuse to invent participant findings and provide a synthesis template or research plan instead.

## Related concepts
[From user needs to product outcomes](../product-design/outcomes.md), [Task hierarchy](task-hierarchy.md).

## References and further learning
[GOV.UK: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) and [PDI design practice](../design-practice.md). [Source registry](../sources.yaml) records provenance and review scope.
