<!-- pdi-topic: {"id":"cognitive-human-factors","domain":"ux-design","depths":["foundation","practitioner","advanced"],"sources":["w3c-structure","wcag22","pdi-guidance"]} -->
# Human cognition, perception and behavioral principles in product design

## What and why
Every interface interacts with human perception, selective attention, working memory, motor control, and decision-making under uncertainty. Grounding design decisions in cognitive science and human factors prevents interfaces that overwhelm memory, bury critical signals, induce catastrophic errors, or misapply simplified UX folklore as universal dogma.

## When to apply
When structuring information density, choosing between progressive disclosure and dense expert views, sizing interactive targets, designing confirmation or undo flows, building alarm/notification hierarchies, or calibrating user trust in automated and AI-assisted workflows.

## Fundamental principles
**Foundation (Mechanism, Applicability & Boundary Conditions):**
- **Cognitive load & working memory:** Working memory holds only a few active chunks at once. Distinguish **intrinsic load** (inherent domain complexity, which must be preserved), **extraneous load** (confusing layout, inconsistent terminology, decorative clutter, or forcing users to remember values from one screen to type into another—which must be eliminated), and **germane load** (schema building). Prefer **recognition over recall** by keeping decision context visible.
- **Selective attention & visual search:** Users scan interfaces goal-directedly using peripheral vision and pre-attentive attributes (contrast, position, size, isolation). When everything is bold, boxed, badge-tagged, or animated, nothing stands out (banner blindness and visual competition).
- **Choice architecture & Hick–Hyman law (with exceptions):** Reaction and decision time increase with the number and ambiguity of choices. *Exception:* Do **not** mechanically reduce every menu to 3–5 items—collapsing 12 familiar, well-categorized navigation links into vague submenus weakens information scent and increases interaction cost. Categorization, familiarity, and searchability matter more than raw item count.
- **Perceptual grouping (Gestalt) vs. container bloat:** Proximity, alignment, similarity, and shared background establish clear grouping with minimal visual noise. Reserve explicit borders and card enclosures (`common region`) for genuinely independent modules; wrapping every label-value pair in its own bordered card fragments scanning.
- **Habituation & spatial consistency:** Frequent users develop motor memory for control locations. Moving primary actions across steps or showing routine confirmation modals for low-risk actions breeds habituation—users click through automatically without reading.

## Practical implementation
**Practitioner:**
- **Expertise & frequency trade-offs (Novice vs. Expert):**
  - *Novices / infrequent tasks (e.g., annual tax setup, first-run onboarding):* Prioritize explicit labels, guided steps, sensible defaults, and inline definitions.
  - *Experts / high-frequency daily workflows (e.g., enterprise triage, developer tools, financial analysis):* Prioritize high information density, compact tabular views, persistent filters, inline editing, bulk selection, and keyboard shortcuts (`Cmd+K`, row navigation). Progressive disclosure that requires 3 clicks per row harms expert efficiency.
- **Motor physics (Fitts's law & target constraints):** Place frequent actions near the current locus of attention with adequate hit targets (`>=44x44pt` mobile, `>=24x24px` CSS minimum / larger on touch or HMI), and physically separate destructive controls from routine actions to prevent motor slips.
- **Slips vs. mistakes, confirmation vs. Undo:**
  - *Slips* are unintended physical actions (tapping Delete instead of Archive); prevent them via target spacing and instant **Undo**.
  - *Mistakes* are flawed intentions due to incomplete information; prevent them via clear consequence previews and inline constraints.
  - *Confirmation rule:* Use lightweight Undo for reversible actions when recovery is reliable. Consider blocking confirmation for irreversible, high-consequence actions (permanent deletion, financial transfer, production deploy, clinical dosage), naming the exact resource and consequence. Do not delay an emergency stop with confirmation; its reset and restart are separate safety decisions.
- **Signal detection & trust calibration:** In operational, clinical, or AI-assisted interfaces, reserve high-salience alerts for actionable anomalies to prevent alarm fatigue, and expose confidence, provenance, and immediate human override.

**Advanced:** Resolve competing human-factors trade-offs (**simplicity vs. discoverability**, **minimalism vs. information density**, **speed vs. safety**, **consistency vs. contextual optimization**) by explicitly evaluating task frequency, error severity, user expertise, and physical environment. Distinguish established perceptual/motor research from context-dependent UI conventions.

## Good and bad examples
Good: An enterprise operations console keeps 50 rows of comparable records visible in a compact, keyboard-navigable table with instant Undo for status changes and an explicit consequence modal only for permanent account deletion. Bad: Hiding 15 frequently used expert tools inside a minimalist 3-dot overflow menu "to reduce cognitive load," or adding a "Confirm save?" modal to a routine preference toggle.

## Common mistakes
Treating named laws (Hick's, Miller's, Fitts's) as unconditional rules to strip out needed controls; equating whitespace and large cards with low cognitive load when it actually forces scrolling and memory recall across viewports; using confirmation modals instead of Undo; stripping essential risk/compliance explanations in high-consequence forms to make the page look "clean."

## Evaluate the result
- **Evaluation signals:** Does the interface eliminate extraneous memory recall across screens while preserving necessary domain controls? Is density calibrated to user expertise and task frequency? Are reversible actions undoable without modal friction, and are irreversible high-consequence actions guarded with specific consequence disclosures?

## AI application
Evaluate cognitive mechanisms and boundary conditions before recommending a layout or flow. State how user expertise, task frequency, and error severity shaped the trade-off between progressive disclosure and direct density.

## Related concepts
[Task hierarchy](task-hierarchy.md), [Designing beyond web: mobile, desktop, tablet, wearable and HMI](multi-modal-hmi.md), [Human-reviewed AI workflows](../ai-product-building/human-reviewed-ai.md).

## References and further learning
[W3C WAI Page Structure Tutorial](https://www.w3.org/WAI/tutorials/page-structure/), [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) and [PDI design practice](../design-practice.md). [Source registry](../sources.yaml) records provenance and review scope.
