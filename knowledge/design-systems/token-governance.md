<!-- pdi-topic: {"id":"token-governance","domain":"design-systems","depths":["foundation","practitioner","advanced"],"sources":["uswds-tokens","wcag22","pdi-guidance"]} -->
# Design tokens, component APIs and system governance

## What and why
Design tokens and component APIs translate visual and interaction decisions into reusable, maintainable contracts between design and engineering. Governance defines how tokens and components evolve without breaking product consistency or accessibility.

## When to apply
When establishing a new design system, auditing hard-coded styles, defining component props/variants, or managing multi-brand, dark-mode and enterprise adoption rules.

## Fundamental principles
**Foundation:** Separate primitive values (raw hex colors, pixel scales) from semantic tokens (purpose-driven names such as `--color-surface-default`, `--color-text-danger`, `--space-card-padding`). Components consume semantic tokens and expose constrained variants rather than arbitrary style overrides.

## Practical implementation
**Practitioner:** Define a three-tier token hierarchy where needed (primitive → semantic → component-scoped) or a lean two-tier hierarchy (primitive → semantic) for smaller teams. Document each component's anatomy, allowed variants, state matrix (default, hover, focus-visible, active, disabled, loading, invalid), keyboard contract, and content slot constraints (truncation, wrapping, min/max lengths).

**Advanced:** Establish lifecycle states (`experimental`, `stable`, `deprecated`), breaking-change policies, automated token contrast verification across themes, and contribution/exception workflows so product teams know when to compose existing primitives versus proposing a new shared component.

## Good and bad examples
Good: Semantic token `--color-status-warning-bg` mapped to primitive palette values with verified text contrast in both light and dark modes; `<Button variant="danger" isLoading>` disables duplicate submission while keeping focus and announcing busy state. Bad: Passing raw hex codes (`color="#FF3300"`) into component instances or creating a new bespoke card component for every feature page.

## Common mistakes
Naming semantic tokens after visual appearance (`--blue-500` used as a semantic name); exploding component prop APIs with boolean flags that conflict (`isPrimary` + `isDanger` + `isGhost`); claiming a component library is WCAG-compliant without testing focus order, contrast and keyboard behavior in real layouts.

## Evaluate the result
Do semantic token names reflect UI purpose rather than raw color/size values? Are component states, keyboard interactions and ARIA responsibilities explicitly specified? Is there a clear rule for how teams adopt, extend or deprecate tokens and components?

## AI application
Extract semantic token tables and CSS custom properties from existing UIs or design briefs; specify clean component prop/variant contracts and state matrices; audit codebases for hard-coded magic values and inconsistent component overrides without inventing organizational approval policies.

## Related concepts
[Tokens and component contracts](component-contracts.md), [Responsive and accessible interfaces](../frontend-engineering/responsive-accessible-ui.md).

## References and further learning
[USWDS Design tokens](https://designsystem.digital.gov/design-tokens/), [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) and [PDI design practice](../design-practice.md). [Source registry](../sources.yaml) records provenance and review scope.
