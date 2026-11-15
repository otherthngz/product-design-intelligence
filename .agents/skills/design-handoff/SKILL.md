---
name: design-handoff
description: Create a multi-audience implementation handoff and product decision changelog from a design or prototype. Structured so AI coding agents, product designers, software engineers, and non-technical stakeholders can each read what they need without invented specifications.
---

# Design Handoff

## Purpose and use
Create a multi-audience implementation handoff and product decision changelog from a design or prototype. Structured so AI coding agents, product designers, software engineers, and non-technical stakeholders can each read what they need without invented specifications.

## Inputs
Required: the request and any available source design, prototype, or flow material. Optional: active UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`), audience, operating mode (`solo`, `team`, `enterprise`), constraints, and prior decision logs. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [ui kit adaptation](../../../knowledge/design-systems/ui-kit-adaptation.md), [component contracts](../../../knowledge/design-systems/component-contracts.md), [responsive accessible ui](../../../knowledge/frontend-engineering/responsive-accessible-ui.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. **Use the structured Multi-Audience Handoff & Changelog Template:** Follow [templates/handoff-and-changelog.md](../../../templates/handoff-and-changelog.md), scaling depth to task complexity while ensuring clarity for all four reader groups:
   - **Non-Product / Non-Engineers / Stakeholders (Section 1 & Section 7):** Plain-language Executive Summary, user problem, business outcome, scope boundaries, and high-level Decision Changelog.
   - **Product Designers & Researchers (Section 2, Section 3 & Section 4):** Information Architecture (IA) tree, Mermaid user flow diagram, 7-state logic matrix, and UI Copy Glossary.
   - **Software Engineers & AI Coding Agents (Section 3, Section 5 & Section 6):** Machine-parseable metadata header (`<!-- pdi-handoff: ... -->`), deterministic State Logic Matrix, UI Kit Component Mapping Table (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`), and observable Acceptance Criteria (`AC-1..N`).
2. **Audit UI Kit reuse vs. customization (Section 5):** List every UI element and its native UI kit component/variant. Explicitly verify whether each component is used **as-is (unmodified)**; if any component was customized or built from scratch, require an explicit user-feedback citation or documented kit gap.
3. **Record the Product Decision Log & Changelog (Section 7):** Document every key product/design decision (`DEC-01`, `CHG-01`, etc.), the stage/skill that produced it, the rationale, the evidence tag (`user-provided`, `verified`, `assumption`, `hypothesis`), rejected alternatives, and the version history when designs evolve after feedback.
4. **Verify honesty & completeness:** Separate confirmed requirements, assumptions, and unresolved decisions; identify unimplemented backends, sample-data provenance, and exact validation checks run vs. not run.

## Artifacts
Produce a complete or complexity-proportioned handoff and decision changelog Markdown document following [templates/handoff-and-changelog.md](../../../templates/handoff-and-changelog.md). Apply [the output contract](../../../workflows/output-contract.md). Link actual files and distinguish findings from hypotheses.

## Quality
Check readability across all four audiences (AI, Designer, Engineer, Non-Technical), completeness of IA, flow, and 7-state logic, strict UI kit mapping, traceable decision changelog entries, and honest validation. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid unstructured prose handoffs that bury engineering specs or confuse non-technical readers, omitting IA or error/loading/empty state logic, allowing undocumented custom component overrides when a standard UI kit is active, or failing to log design changes in the changelog.

## Tools and fallback
Use available local files and appropriate inspection or execution tools. If a browser, design tool, source material, or integration is unavailable, identify the gap, work from supplied evidence, and state the limitation; never fabricate execution. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
A multi-audience handoff for a workspace onboarding flow containing an executive summary for stakeholders, an IA tree and Mermaid flow for designers, a 7-state logic matrix and stock `shadcn/ui` component mapping table for engineers and AI agents, and a versioned Product Decision Changelog (`v1.0` → `v1.1`).
