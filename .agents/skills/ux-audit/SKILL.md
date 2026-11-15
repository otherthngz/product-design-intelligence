---
name: ux-audit
description: Evaluate an existing interface for usability, hierarchy, interaction, consistency and accessibility evidence. Use for a critique or audit of supplied or inspectable experiences; do not use as a substitute for user research or to invent observations.
---

# Ux Audit

## Purpose and use
Evaluate an existing interface for usability, hierarchy, interaction, consistency and accessibility evidence. Use for a critique or audit of supplied or inspectable experiences; do not use as a substitute for user research or to invent observations.

## Inputs
Required: the request and any available source material. Optional: audience, goals, constraints, project context, existing system, and evidence. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [task hierarchy](../../../knowledge/ux-design/task-hierarchy.md), [cognitive human factors](../../../knowledge/ux-design/cognitive-human-factors.md), [interface copy](../../../knowledge/ux-design/interface-copy.md), [multi modal hmi](../../../knowledge/ux-design/multi-modal-hmi.md), [ui kit adaptation](../../../knowledge/design-systems/ui-kit-adaptation.md), [responsive accessible ui](../../../knowledge/frontend-engineering/responsive-accessible-ui.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. Establish the task, user expertise (novice vs. daily expert), task frequency, physical device/environment (Web, Mobile, Desktop, Tablet, Wearable, or HMI), active UI kit, domain criticality, and available evidence. Inspect the actual interface or supplied material and run `python3 scripts/audit_artifact.py` where applicable.
2. Walk the primary task and error recovery paths; assess visibility, navigation, language, feedback, consistency, keyboard/touch/rotary/voice access, attention budget, and responsive behavior across the **10 Evaluation Dimensions** (Necessity, Contextual fit, Functional clarity, Information efficiency, Interaction efficiency, Visual discipline, System coherence, Accessibility, Complexity justification, Evidence alignment).
3. **Execute Operational Anti-AI-Slop Evaluation while Protecting Necessary Complexity:**
   - Detect the **7 Failure Categories**: (A) **Generic design** (unmotivated card grids, decorative KPI cards/charts, hero sections in functional tools, redundant icons), (B) **Overdesign** (nested containers, competing shadows/gradients/accents, gratuitous motion), (C) **Overengineering** (one-off components, speculative variants/state), (D) **Text overload** (redundant intro prose, repeated helper text, verbose buttons, author meta-notes), (E) **Interaction clutter** (competing primary CTAs, frequent actions buried in overflow menus, confirmation modals on reversible actions, multi-step modals for simple edits), (F) **Context mismatch** (consumer cards on dense expert workflows, or enterprise complexity in first-time consumer flows), and (G) **False sophistication** ("modern/clean/premium" rationales with no user benefit).
   - **Protect Justified Complexity:** Never recommend removing dense tables, bulk/inline controls, or mandatory compliance/safety/error-recovery disclosures when required by expert workflows or high-consequence tasks.
4. **Classify severity & specify targeted corrections:** Classify each issue as `Critical`, `Major`, `Minor`, or `Opportunity` (never label subjective stylistic preferences as `Critical`). For each substantive issue, state: (1) the problematic design decision, (2) why it is inappropriate in context, (3) its practical impact (separating observed facts from hypotheses), (4) the **smallest effective correction** (favoring targeted fixes over complete redesigns), and (5) any relevant trade-off.
5. Prioritize blockers, avoid unbounded rewrite loops, and state what could not be inspected. Do not claim WCAG conformance or validated user outcomes from a heuristic review.

## Artifacts
Produce the requested artifact or a concise Markdown result. Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check coverage against the request, a clear next action, evidence labels, relevant accessibility considerations, and honest validation. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid invented research or metrics, unsupported compliance claims, unexplained design decisions, and treating assumptions as facts. Do not silently skip requested states or constraints.

## Tools and fallback
Use available local files and appropriate inspection or execution tools. If a browser, design tool, source material, or integration is unavailable, identify the gap, work from supplied evidence, and state the limitation; never fabricate execution. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
A critique of a checkout screenshot might flag an unclear button label as an observed issue and mark abandonment impact as a hypothesis.
