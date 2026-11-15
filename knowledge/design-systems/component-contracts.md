<!-- pdi-topic: {"id":"component-contracts","domain":"design-systems","depths":["foundation","practitioner","advanced"],"sources":["uswds-tokens"]} -->
# Tokens and component contracts

## What and why
A design system connects shared visual tokens, reusable UI primitives, and documented behavioral contracts. Tokens give recurring design decisions semantic names; a component contract specifies anatomy, states, accessibility guarantees, and composition boundaries so teams do not reinvent or fracture the interface.

## When to apply
When building repeated UI, evaluating whether to create a new component vs. reusing or composing existing primitives, defining component state matrices, or handing a design to engineers.

## Fundamental principles
**Foundation (Reuse vs. Proliferation Decision Rule):**
- **Default to reuse and composition:** Before proposing a new component or variant, inspect existing system primitives. Minor visual variations, one-off layout arrangements, or hypothetical future use cases do **not** justify a new reusable component.
- **When a new component is justified:** A shared component may be warranted when existing primitives cannot meet a validated, recurring interaction need and reuse outweighs maintenance and migration costs. For a one-off essential accessibility or task requirement that existing composition cannot satisfy, make the smallest documented local extension or custom solution; do not require recurrence or promotion into the shared system.
- **Overengineering prevention:** Do not wrap trivial single-use HTML elements in multi-prop abstraction layers, add feature flags/variants for unrequested edge cases, or introduce global state management for local UI state.

## Practical implementation
**Practitioner:**
- **Semantic tokens & anatomy:** Define tokens by semantic role (`--color-surface-default`, `--color-text-muted`), not raw appearance. Document component anatomy, required vs. optional slots, and content overflow behavior (truncation, wrapping, tabular alignment).
- **Complete state & accessibility contract:** Specify behavior across `default`, `hover`, `focus-visible`, `active`, `disabled`, `loading`, and `invalid/error` states. Define keyboard interaction (`Tab`, arrow keys, `Escape`, `Enter`/`Space`), ARIA roles/attributes (`aria-expanded`, `aria-invalid`, `aria-busy`), and focus restoration.

**Advanced:** Assign ownership, versioning, deprecation migration paths, and contribution criteria. Evaluate changes across products and platform constraints; allow documented exceptions only when a shared pattern fails a proven user or domain requirement. Treat governance as a socio-technical process, not just a token file.

## Good and bad examples
Good: Rejecting a developer proposal to create a `<HighlightedMetricCard>` component for a minor border tweak, and instead composing the existing `<Card>` and `<Badge variant="secondary">` primitives with standard semantic tokens. Bad: Creating 4 competing button components with 18 boolean props, or building a bespoke custom dropdown that breaks keyboard navigation.

## Common mistakes
Creating a new component for a one-off visual variation (pattern proliferation); inventing new variants without checking existing primitives; relying on color alone to distinguish states; overcomplicating component APIs for hypothetical future requirements.

## Evaluate the result
- **Evaluation signals:** Did the recommendation inspect existing primitives first and favor reuse or composition over component invention? Can an engineer identify component props, all interactive states, keyboard/ARIA contracts, and the single source of truth? Are any intentional deviations explicitly justified?

## AI application
Inspect existing components and tokens before proposing changes. Challenge requests to create redundant components or variants when composition of stock primitives suffices, state assumptions clearly, and never claim an organization has approved a new standard without verification.

## Related concepts
[Task hierarchy](../ux-design/task-hierarchy.md), [token governance](token-governance.md), [ui kit adaptation](ui-kit-adaptation.md), [responsive and accessible UI](../frontend-engineering/responsive-accessible-ui.md).

## References and further learning
[USWDS design tokens](https://designsystem.digital.gov/design-tokens/) illustrates named design decisions. See [source registry](../sources.yaml).
