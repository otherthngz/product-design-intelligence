# Practical audit of PDI

**Assessment date:** 2026-11-14. **Verdict:** PDI is a structured design-agent kit and can be operated by a capable host agent to create local artifacts; the repository itself does not run a model, automatically route requests or execute tools. It is therefore more than a loose prompt collection in its contracts, examples and checks, but it is not an independently running autonomous agent system. The scenarios below were carried out by the same assistant that extended the repository, using the skills as instructions; this is a self-review, not an independent blinded evaluation or proof of repeatable behavior across hosts.

## Method and scoring

For each scenario we selected the documented skills, read relevant knowledge, created or inspected the linked artifact and assessed it. Scores are subjective reviewer judgments **0–5** per criterion: **0** absent or misleading; **1** severely incomplete; **2** major gaps; **3** useful with material gaps; **4** strong with limited gaps; **5** complete and supported by appropriate evidence for the specific scenario. The four criteria are: **Routing** (correct skill/topic selection), **Reasoning** (task coverage and trade-offs), **Evidence** (separates facts, assumptions and validation), and **Delivery** (clear, usable artifact for intended audiences). Scores reflect the artifacts produced in this session, not measured future agent performance. Automated checks appear separately below.

| Scenario | Skills and artifact | Routing | Reasoning | Evidence | Delivery | Findings and missing capability |
|---|---|---:|---:|---:|---:|---|
| Founder critiques an existing interface | `ux-audit`: [critique](../../examples/audit-scenarios/ux-critique.md) | 5 | 4 | 4 | 4 | Identifies observable issues and labels impact hypotheses; no actual users, behavioral research or screen-reader review. |
| Designer defines checkout | `product-framing`, `interaction-design`: [flow](../../examples/audit-scenarios/checkout-flow.md) | 5 | 4 | 4 | 4 | Covers declines, uncertain payment and recovery; real payment-provider, regional, tax and privacy constraints remain unknown. No checkout integration was executed. |
| Developer requests responsive settings | `interaction-design`, `ui-prototyping`: [settings prototype](../../examples/audit-scenarios/settings.html) and [notes](../../examples/audit-scenarios/settings.md) | 5 | 3 | 5 | 4 | Browser interaction and narrow layout exercised; controls only produce local feedback, not persisted settings or an actual email/display change. |
| PM has unclear onboarding requirements | `product-framing`, `interaction-design`: [feature specification](../../examples/audit-scenarios/onboarding-spec.md) | 5 | 4 | 5 | 4 | Defines a testable direction without inventing a product or metrics; final requirements and actual user research are missing. |
| Team requests design-system handoff | `design-handoff`: [handoff](../../examples/audit-scenarios/design-system-handoff.md) | 5 | 3 | 5 | 4 | Component behavior and mapping questions are explicit; an actual design system, approved tokens, owners and API contracts were not supplied. |

**Why delivery is not 5:** artifact clarity was reviewed by the author; neither engineers nor non-engineers participated in comprehension testing. Expert reasoning has not been independently reviewed. Browser interaction does not prove user outcomes or accessibility conformance.

## Executed validation

- In the in-app browser, dashboard period selection changed the status, summary counts, weekly values and account examples; the narrow viewport was set to 390 × 844 and the visible layout reflowed without page-level horizontal overflow. The table is horizontally scrollable by design. The chart visual was inspected, but individual bar heights were not independently measured against data.
- In the same browser, the settings prototype accepted “Off” and “Compact” and displayed the matching local saved-for-this-page status. At 390 × 844 it reflowed with no page-level horizontal overflow. The prototype does not persist settings or change email delivery or display density.
- Automated results are supplied by `python3 scripts/validate_skills.py`, `python3 scripts/validate_knowledge.py`, and `python3 -m unittest discover -s tests -v`. They validate deterministic structure, links and safe local generation; they do not exercise agent skill selection, browser interactions or design quality. `node tests/test_prototypes.js` separately checks dashboard state updates and settings feedback using a small simulated DOM; it requires Node.js and is not a substitute for browser testing.
- No screen-reader, complete keyboard, zoom, color-contrast, cross-browser, usability or accessibility-conformance testing was performed. The onboarding critique relies on the documented prior browser observations and inspected source, not a new user study.

## High-impact changes made

Added five scenario artifacts and two locally executable prototypes, cleared stale settings feedback when a selection changes, explicit skill-to-knowledge retrieval links, traceable source and topic metadata, a human-review update workflow, and offline checks for broken topic/skill links, missing source IDs, invalid source URLs, duplicate topic IDs and missing index entries. These close gaps in evidence, inspectability and knowledge retrieval; they do not turn the repository into an agent runtime. No additional skills were introduced.

## Capability matrix

| Capability | Status | Boundary |
|---|---|---|
| Route requests and apply design skills | **Advises** | A host agent reads the instructions and decides; no autonomous classifier or model is bundled. |
| Produce critique, flows, specs and handoffs | **Executes with host** | Host must have a model and appropriate file access; quality requires human review. Examples demonstrate one session. |
| Build and inspect local HTML prototypes | **Executes with host** | HTML runs locally; browser and file tools are host-provided. Python can copy the original onboarding sample. |
| Validate topic metadata and local references | **Executes locally** | Standard-library Python; deterministic structural checks only. |
| Conduct user research or claim accessibility compliance | **Advises** | Requires real participants, tools, qualified review and evidence. |
| Edit Figma, query live data, publish, persist settings or deploy | **Requires integration** | No adapter runtime, credentials, API or service is provided; external effects require appropriate authorization. |
| Continuously learn and update its knowledge | **Advises** | Source review and proposed changes are manual; human review is a documented convention, not automated enforcement. |

Next: run the five cases independently across representative host agents, compare actual artifacts against the rubric, test with designers and engineers, and establish an accessible testing matrix before making broader capability claims.
