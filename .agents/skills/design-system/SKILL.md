---
name: design-system
description: Define and audit design tokens, existing UI kit adaptation (shadcn/ui, Nuxt UI, Apple HIG, Material 3, or Custom), component APIs, state matrices and system governance. Use when selecting, reusing, or standardizing UI tokens and component contracts; do not invent bespoke components when a standard UI kit primitive exists.
---

# Design System

## Purpose and use
Define and audit design tokens, existing UI kit adaptation (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`), component APIs, state matrices and system governance. Use when selecting, reusing, or standardizing UI tokens and component contracts; do not invent bespoke components when a standard UI kit primitive exists.

## Inputs
Required: the target components, token scope, or existing UI/codebase to standardize. Optional: active UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`), brand palette, typography scale, dark/high-contrast mode needs, and operating mode (`solo`, `team`, `enterprise`). State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [ui kit adaptation](../../../knowledge/design-systems/ui-kit-adaptation.md), [token governance](../../../knowledge/design-systems/token-governance.md), [component contracts](../../../knowledge/design-systems/component-contracts.md), [responsive accessible ui](../../../knowledge/frontend-engineering/responsive-accessible-ui.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. **Detect or confirm the active UI Kit first:** Inspect the repo (`package.json`, `components.json`, `nuxt.config.ts`, iOS/Android manifests) or ask the user whether the project uses `shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Google Material 3`, or a `Custom` system.
2. **Enforce the Strict Default-First Reuse & Anti-Proliferation Rule:** Map required elements to unmodified native components and variants where possible. Reject new shared components for minor visual variations when existing primitives suffice. If composition cannot meet an essential task or accessibility requirement, document the gap and use the smallest local extension or custom solution; consider a shared component when the need recurs.
3. **Define or align semantic tokens:**
   - For `shadcn/ui`: bind to CSS variables (`--background`, `--foreground`, `--primary`, `--muted`, `--destructive`, `--ring`).
   - For `Nuxt UI`: configure semantic colors (`primary`, `neutral`, `error`, `warning`, `success`) via `app.config.ts`.
   - For `Apple HIG` & `Material 3`: bind to native system dynamic colors (`systemBackground`/`label` or `MaterialTheme.colorScheme`) and native typography scales.
   - For `Custom`: define a clean primitive-to-semantic token table and canonical reusable classes before building screens.
4. **Specify component state contracts without overengineering:** Document props, variants, keyboard navigation, focus rings, and interactive states (default, hover, focus-visible, active, disabled, loading, invalid). Avoid speculative boolean props, feature flags, or wrapper abstractions for one-off elements.
5. **Adapt governance to the operating mode:** Record component mappings and any approved overrides in Section 5 of [the handoff template](../../../templates/handoff-and-changelog.md) and route to `ui-prototyping` or `design-handoff`.

## Artifacts
Produce a UI Kit Component Mapping Table, semantic token specification, or system audit report. Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check 100% reuse of native UI kit primitives where available, explicit justification for any modified/custom component, semantic token naming, and contrast/focus visibility across themes. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid inventing custom HTML/CSS widgets when the project's UI kit already provides them, overriding kit spacing/radii without user feedback, naming semantic tokens after raw colors (`--blue-500`), or using web component conventions on native iOS/Android screens.

## Tools and fallback
Use available local file and code inspection tools to inspect CSS, JSON, or component files. If Figma or a live Storybook instance is unavailable, work from local code or supplied specs and record what could not be verified. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
A UI kit mapping contract for a settings page that maps every control to stock `shadcn/ui` components (`<Card>`, `<Input>`, `<Select>`, `<Button variant="default">`, `<AlertDialog>`) with zero custom CSS overrides, plus a logged rationale in the decision changelog.
