---
name: interaction-design
description: Define information architecture (IA), user journeys, flows, state logic matrices, transitions and error recovery for a feature. Use for onboarding, forms, navigation structure, or task flows; do not use for visual-only styling with no behavior to define.
---

# Interaction Design

## Purpose and use
Define information architecture (IA), user journeys, flows, state logic matrices, transitions and error recovery for a feature. Use for onboarding, forms, navigation structure, or task flows; do not use for visual-only styling with no behavior to define.

## Inputs
Required: the request and any available source material. Optional: audience, goals, constraints, target platform/UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`), project context, and evidence. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [task hierarchy](../../../knowledge/ux-design/task-hierarchy.md), [cognitive human factors](../../../knowledge/ux-design/cognitive-human-factors.md), [multi modal hmi](../../../knowledge/ux-design/multi-modal-hmi.md), [outcomes](../../../knowledge/product-design/outcomes.md), [ui kit adaptation](../../../knowledge/design-systems/ui-kit-adaptation.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. **Identify context, expertise & physical medium (Design Beyond Screens):** Establish the entry point, user expertise (novice vs. daily expert), task frequency, reversibility, failure consequences, and exact form factor: **Web, Mobile (iOS/Android), Desktop, Tablet, Wearable (watchOS/Wear OS), or HMI (automotive, medical, industrial, kiosk)**. Account for viewing distance, attention budget (<2s glance for wearable/HMI), and input modality (touch, thumb zone, pointer/keyboard shortcuts, rotary dial, physical buttons, gloved hands, voice/haptic).
2. **Compare meaningful pattern alternatives & trade-offs:** Before locking an interaction model, evaluate context-appropriate alternatives:
   - *Data display:* Dense aligned **Table** (for comparing 4+ attributes or many rows) vs. **Cards** (for small visual catalogs).
   - *Input & editing:* **Inline table / bulk editing** (for frequent expert updates) vs. **Single-page sectioned form** (<8–10 related fields) vs. **Multi-step wizard** (for infrequent, high-consequence, or branching setup).
   - *Safeguards:* Direct action + **Undo** (for reversible actions) vs. **Explicit consequence confirmation** (for irreversible/high-risk actions).
   - *Complexity calibration:* Preserve necessary domain controls and density for expert users; use progressive disclosure only when it aids comprehension without slowing frequent workflows.
3. **Define Information Architecture (IA) & user flow:** Remove unnecessary steps or modals before adding new ones. Map the navigation hierarchy (App Shell → Route/Section → Screen/Panel), reading priority (H1 → H2 → H3, primary decision → core controls → secondary actions), and end-to-end Mermaid flow. Never force web navigation onto native mobile, wearable, or safety-critical HMI screens.
4. **Build the State Logic Matrix:** Explicitly specify triggers, visible UI behavior, data retention, and keyboard/focus recovery across relevant states: **Empty (first-run)**, **Default (loaded)**, **Loading/Pending**, **Validation Error**, **System/Network Failure**, **Success/Completed**, and **Cancelled/Back** (scale ceremony for trivial fixes).
5. **Walk and route:** Verify every path against the user objective, record decisions and rejected alternatives in the changelog, and hand off to `ux-writing`, `ui-prototyping`, or `design-handoff`.

## Artifacts
Produce an IA hierarchy, user flow diagram, and State Logic Matrix (following Sections 2 and 3 of [the handoff template](../../../templates/handoff-and-changelog.md)). Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check IA clarity, coverage of all 7 state transitions, data retention on Back/Error, keyboard focus movement, and honest validation. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid skipping IA hierarchy, leaving error/empty/loading states undefined, losing user input when navigating back, or forcing web navigation patterns onto native mobile flows.

## Tools and fallback
Use available local files and appropriate inspection or execution tools. If a browser, design tool, source material, or integration is unavailable, identify the gap, work from supplied evidence, and state the limitation; never fabricate execution. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
An onboarding IA and flow specification with a tree hierarchy, Mermaid flow diagram, and a 7-state logic matrix showing how workspace name and goal selection persist when returning to an earlier step or recovering from a network timeout.
