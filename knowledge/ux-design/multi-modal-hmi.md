<!-- pdi-topic: {"id":"multi-modal-hmi","domain":"ux-design","depths":["foundation","practitioner","advanced"],"sources":["w3c-structure","wcag22","pdi-guidance"]} -->
# Designing beyond web: mobile, desktop, tablet, wearable and HMI

## What and why
Product design spans diverse physical form factors and industry domains—from consumer mobile apps and dense enterprise/developer desktop workstations to multi-pane tablets, glanceable smartwatches, and safety-critical Human–Machine Interfaces (HMI) in healthcare, finance, automotive, and industrial operations. Each platform and domain imposes distinct attentional, ergonomic, risk, and density requirements.

## When to apply
Whenever framing, selecting interaction patterns, choosing UI kits, or prototyping across form factors (Web, Mobile, Tablet, Desktop, Wearable, HMI) or across domains with different complexity and risk profiles (Enterprise SaaS, Consumer, Developer Tools, Financial, Healthcare, E-commerce, Analytics, Internal Operations).

## Fundamental principles
**Foundation:** Never apply one universal visual or interaction style across all platforms and domains. Match the interface to:
1. **Attention budget & viewing distance:** Brief glances may be needed on wearables or in vehicles, while desktop workstations can support sustained scanning. Establish limits from the task, environment, applicable requirements, and testing.
2. **Input physics:** Consider thumb reach and coarse touch on mobile; pointer and keyboard on desktop; stylus and split-view on tablets; and device-specific physical, touch, voice, or haptic controls on wearables and HMI.
3. **Domain criticality & necessary complexity:** Distinguish **domain/necessary complexity** (e.g., multi-parameter clinical monitoring, financial order books, developer log filtering) from **accidental or decorative complexity** (nested card wrappers, gratuitous animations). Never strip controls required for professional precision merely to make an expert tool look like a consumer marketing page.

## Practical implementation
**Practitioner (Rules by Form Factor & Domain Context):**

- **1. Mobile (`iOS Apple HIG` / `Android Material 3`) & Consumer Flows:**
  - **Ergonomics:** Place primary navigation and frequent actions in the bottom thumb zone (`TabView` / `NavigationBar`); avoid top-corner reach traps.
  - **Touch & Density:** Minimum `44x44pt` (iOS) or `48x48dp` (Android) hit targets; single-column vertical flow; progressive disclosure via native sheets (`Sheet` detents / `ModalBottomSheet`). Respect Safe Areas and virtual keyboard overlap.

- **2. Tablet (`iPadOS` / `Large-screen Android` / Touch Kiosks):**
  - **Ergonomics:** Use adaptive multi-pane architectures (Master-Detail / Split View, collapsible sidebar + canvas) rather than stretching a phone layout across 11–13 inches. Support seamless switching between touch, pointer, and hardware keyboard.

- **3. Desktop (`macOS`, `Windows`, `Linux`, Enterprise SaaS, Developer & Financial Tools):**
  - **Ergonomics:** Optimize for high information density, aligned tabular comparison (`tabular-nums`), resizable split panels, command palettes (`Cmd/Ctrl+K`), keyboard-only navigation, inline table editing, bulk actions, and persistent filter bars. Do not force desktop power users through mobile-style single-question wizard steps or oversized card grids when a structured table or split pane is faster.

- **4. Wearable (`watchOS`, `Wear OS`, Fitness/Health Trackers):**
  - **Ergonomics:** Prioritize glanceable content and sufficiently operable controls for the task; use voice, quick replies, or a companion device when text entry is impractical. Account for available input hardware, contrast, battery, and the actual operating environment; do not impose a universal time, target count, or color.

- **5. Safety-Critical HMI & High-Consequence Domains (Automotive IVI, Industrial Controls, Medical/Healthcare Devices):**
  - **Safety & Eyes-Off-Task Budget:** Determine applicable distraction and safety requirements for the actual equipment and context. Do not bury critical operational controls in nested navigation. An emergency stop must not be delayed by a confirmation dialog; distinguish stopping from controlled reset or restart.
  - **Input, Environment & Safeguards:** Determine target size, spacing, physical controls, feedback, and lighting from equipment, operating conditions, applicable standards, and human-factors testing; no generic pixel size establishes safety. Verify high-risk inputs when appropriate, without delaying emergency action or claiming unverified certification. Involve qualified safety and domain experts.

**Advanced:** Design cross-device continuity and domain-specific role adaptation—defining which tasks happen on a wearable or mobile companion (alert acknowledgment, quick triage) versus which tasks require a desktop workstation (bulk editing, reconciliation, root-cause analysis).

## Good and bad examples
Good: An industrial HMI distinguishes alarm acknowledgment from an immediately accessible emergency-stop control; its reset and restart behavior is validated for the equipment. A developer log viewer uses a dense, monospace filterable table with keyboard navigation. Bad: Applying a generic consumer SaaS card grid with large hero banners and hover-only tooltips to a factory touchscreen, a clinical dosage form, or a high-frequency financial blotter.

## Common mistakes
Designing wearables like miniature smartphones; placing safety-critical HMI controls inside swipe carousels or deep settings menus; penalizing legitimate information density in expert desktop or developer tools; applying aggressive promotional upsells in trust-sensitive healthcare or financial workflows; inventing legal or medical compliance claims.

## Evaluate the result
- **Evaluation signals:** Does the design explicitly match the target form factor, viewing distance, attention budget, input modality, and domain risk profile? Are expert desktop workflows protected from mobile-first oversimplification, and are consumer/mobile flows protected from enterprise configuration bloat?

## AI application
Before proposing flows or UI, confirm the physical form factor, user expertise, and domain context. Detect and correct **context mismatch** (e.g., consumer card layouts on dense expert workflows, or complex enterprise controls on simple first-time consumer flows).

## Related concepts
[Task hierarchy](task-hierarchy.md), [Cognitive human factors](cognitive-human-factors.md), [Adapting to existing UI kits](../design-systems/ui-kit-adaptation.md), [Responsive and accessible interfaces](../frontend-engineering/responsive-accessible-ui.md).

## References and further learning
[W3C WAI Page Structure Tutorial](https://www.w3.org/WAI/tutorials/page-structure/), [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) and [PDI design practice](../design-practice.md). [OSHA's machine-guarding trainer guide](https://www.osha.gov/sites/default/files/2020-04/Trainer%26%23039%3Bs%20Guide_0.pdf) describes rapid emergency deactivation; determine requirements for the actual equipment. [Source registry](../sources.yaml) records provenance and review scope.
