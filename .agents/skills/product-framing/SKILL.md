---
name: product-framing
description: Frame ambiguous product requests into problems, goals, constraints, assumptions and success criteria. Use before solution design when the problem or scope is unclear; do not use for a narrowly specified copy edit.
---

# Product Framing

## Purpose and use
Frame ambiguous product requests into problems, goals, constraints, assumptions and success criteria. Use before solution design when the problem or scope is unclear; do not use for a narrowly specified copy edit.

## Inputs
Required: the request and any available source material. Optional: audience, goals, constraints, project context, existing system, and evidence. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [outcomes](../../../knowledge/product-design/outcomes.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. **Understand the human, business, and physical context:** Identify the primary user group, expertise level, task frequency, business goal, trigger, and physical medium (Web, Mobile, Desktop, Tablet, Wearable, or HMI); separate verified facts from unknowns.
2. **Distinguish request from problem & apply the "No-Redesign" Check:** Separate the **stated request**, **underlying problem**, **intended user outcome**, **desired product outcome**, and **actual constraints**. Challenge solution-first prompts (e.g., "add a dashboard with more charts")—if a simpler copy change, default setting, prioritized table, or removal of steps solves the underlying problem better, recommend that proportionate solution instead.
3. **Compare alternatives & trade-offs proportionally:** For consequential or ambiguous scope decisions, compare at least two meaningful directions (e.g., new dedicated workflow vs. inline enhancement) and state the key trade-offs and counter-metrics so local optimizations do not harm user experience. Skip heavyweight framing for trivial fixes.
4. **Label evidence, assumptions & reversibility:** Tag inputs using PDI's evidence hierarchy (`user-provided`, `verified`, `assumption`, `hypothesis`), distinguish reversible decisions from expensive one-way-door commitments, and suggest a practical way to validate the highest-risk assumption.
5. If a missing answer blocks a consequential decision, ask; otherwise state bounded assumptions and proceed. Route to `interaction-design` or another relevant skill when the request calls for a deliverable.

## Artifacts
Produce the requested artifact or a concise Markdown result. Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check coverage against the request, a clear next action, evidence labels, relevant accessibility considerations, and honest validation. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid invented research or metrics, unsupported compliance claims, unexplained design decisions, and treating assumptions as facts. Do not silently skip requested states or constraints.

## Tools and fallback
Use available local files and appropriate inspection or execution tools. If a browser, design tool, source material, or integration is unavailable, identify the gap, work from supplied evidence, and state the limitation; never fabricate execution. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
A first-run onboarding brief with a measurable proposed outcome, explicit assumptions, and an open question about the user's first meaningful action.
