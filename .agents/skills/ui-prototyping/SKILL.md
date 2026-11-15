---
name: ui-prototyping
description: Build or modify an executable interface prototype or UI implementation using the project's active UI kit and validated design foundations. Use when a user needs a working screen or interactive artifact; do not use for critique alone, invent custom components over an existing UI kit, or imply a prototype is production-ready.
---

# Ui Prototyping

## Purpose and use
Build or modify an executable interface prototype or UI implementation using the project's active UI kit and validated design foundations. Use when a user needs a working screen or interactive artifact; do not use for critique alone, invent custom components over an existing UI kit, or imply a prototype is production-ready.

## Inputs
Required: the request and any available source material. Optional: active UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`), audience, goals, constraints, project context, and evidence. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [ui kit adaptation](../../../knowledge/design-systems/ui-kit-adaptation.md), [multi modal hmi](../../../knowledge/ux-design/multi-modal-hmi.md), [component contracts](../../../knowledge/design-systems/component-contracts.md), [responsive accessible ui](../../../knowledge/frontend-engineering/responsive-accessible-ui.md), [human reviewed ai](../../../knowledge/ai-product-building/human-reviewed-ai.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

For visual direction when creating a custom brand or marketing experience, also load [frontend-design](../frontend-design/SKILL.md); apply it in service of the product and never override an established UI kit's component structure unless requested. For a targeted review, use [UI review checks](references/review.md). For work in Figma, follow the host tools and [Figma MCP guide](../../../adapters/figma-mcp.md).

## Workflow
1. **Verify design foundations, complexity & form factor first:** Scale setup to task complexity—for a trivial spacing or label fix, apply the change directly; for a feature or screen, confirm user needs (`ux-research`), problem framing & the "no-redesign" check (`product-framing`), context-appropriate pattern selection & 7-state logic (`interaction-design`), and interface copy (`ux-writing`). Confirm the target medium (**Web, Mobile, Desktop, Tablet, Wearable, or HMI**), user expertise (novice vs. expert), and operating mode (`solo`, `team`, `enterprise`).
2. **Lock the UI Kit & enforce Anti-AI-Slop discipline:** Identify whether the target uses `shadcn/ui`, `Nuxt UI`, `Apple HIG (iOS/watchOS)`, `Material Design 3 (Android/Wear OS)`, or a `Custom` token/HMI system (`design-system`). Compose from unmodified stock components and semantic tokens by default; document and address an essential task or accessibility gap when composition cannot meet it. Reject all 7 categories of AI slop: (A) generic SaaS card grids or charts for every metric, (B) overdesigned nested borders/gradients, (C) overengineered one-off wrapper components, (D) text overload and author meta-notes, (E) interaction clutter and competing primary CTAs, (F) context mismatch (e.g., consumer cards on dense expert tables), and (G) false sophistication. Preserve necessary domain complexity and compliance disclosures.
3. **Implement all relevant states & task-focused copy:** Build the artifact with semantic controls, associated labels, visible `:focus-visible` styles, `tabular-nums` for comparable data, responsive layout, and every relevant state (empty, default, loading, validation error, failure, success, back/cancel). Never place author notes (`sample data`, `this is a prototype`, `illustrative only`) inside the product UI unless required to prevent a consequential misunderstanding.
4. **Run bounded anti-slop evaluation & deterministic checks:** Run `python3 scripts/audit_artifact.py` on generated HTML/Markdown, correct any material (`Critical` / `Major`) issues in a single bounded pass, and review the rendered interface at suitable desktop and mobile widths when browser tools are available.
5. **Deliver handoff & decision changelog proportionally:** Deliver artifact paths, UI kit component mappings, implementation limits, sample-data provenance, and key trade-offs/decisions (using [the handoff template](../../../templates/handoff-and-changelog.md) for standard/complex work). Never claim simulated operations (payments, saves, emails) actually occurred.

## Artifacts
Produce the executable prototype or UI code plus a companion handoff/changelog summary. Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check UI kit fidelity and documented exceptions, relevant states, necessary in-context disclosures, and honest validation. The artifact auditor checks limited markup signals; it does not verify accessibility conformance. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid jumping into UI code without IA/flow/state foundations, inventing custom components when the UI kit already has them, modifying standard UI kit styles without user feedback, placing "sample data" badges in the UI, or showing false confirmations for unimplemented backend actions.

## Tools and fallback
Use available local files and appropriate inspection or execution tools. If a browser, design tool, source material, or integration is unavailable, identify the gap, work from supplied evidence, and state the limitation; never fabricate execution. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
Create an account settings screen composed strictly of unmodified `shadcn/ui` (or canonical custom token) primitives covering default, dirty, validation-error, and saved states, accompanied by a handoff component table and decision changelog.
