# Design practice: expert judgment, decision structure and anti-slop discipline

These are PDI's operational design principles, not a claim of regulatory compliance or empirical user research findings. Apply them conditionally based on user expertise, task frequency, domain criticality, platform conventions, and existing system constraints.

## 1. Core Reasoning Sequence & Progressive Depth

Follow **Context → Evidence → Alternatives → Trade-offs → Decision → Evaluation** as an internal reasoning discipline—scaling exposed output to task complexity and decision reversibility:
- **Low complexity / reversible (`quick`):** (e.g., spacing adjustment, button label fix, minor hierarchy tweak) Apply established conventions directly, perform a lightweight quality check, and keep the response concise without generating artificial alternatives or long trade-off essays.
- **Medium complexity (`standard`):** (e.g., settings screen, onboarding flow, navigation pattern selection, form restructuring) Identify relevant user/product/task context, compare meaningful alternatives, explain key trade-offs, and evaluate against anti-slop and quality criteria.
- **High complexity / expensive to reverse (`complex` or high-risk):** (e.g., enterprise workflow, product IA, financial/clinical/safety-critical flow, design-system component contract) Analyze constraints, separate verified evidence from assumptions, evaluate competing interaction models and second-order consequences, justify whether complexity is necessary, and specify validation requirements.

## 2. Contextual Principles, Mechanisms & Boundary Conditions

- **Human-centered problem framing:** Distinguish the **stated request**, **underlying user problem**, **intended user outcome**, **business outcome**, and **actual constraints** before designing. Ask whether removing a step, improving copy, or changing a default solves the problem without new UI.
- **Cognitive load & expertise calibration:** Eliminate *extraneous* cognitive load (visual noise, inconsistent terminology, cross-screen memory recall) while preserving *intrinsic* domain functionality. Never apply Hick's, Miller's, or Fitts's laws mechanically—dense tables, inline actions, bulk operations, and keyboard shortcuts serve daily expert users better than multi-step wizards or hidden overflow menus.
- **Pattern selection by task & data shape:** Choose tables over cards when users compare multiple attributes across records; choose single-page sectioned forms over wizards unless steps are branching, infrequent, or high-consequence; include charts on dashboards only where trend, distribution, or comparison adds analytical value over direct tabular values.
- **Safeguards, reversibility & confirmation:** Prefer forgiving inputs and instant **Undo** for reversible actions. Reserve blocking confirmation dialogs for irreversible or high-consequence actions, and preserve all essential compliance, risk, and recovery information in high-stakes forms.
- **Strict design-system & UI kit reuse:** Reuse existing tokens and unmodified UI kit primitives (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or locked `Custom` tokens) by default. Reject creating new components or variants for minor one-off visual variations when composition suffices.
- **Accessibility & cross-platform ergonomics:** Enforce semantic HTML, programmatic labels, keyboard operability, visible focus, non-color status cues, and responsive reflow as mandatory baselines (see [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/)). Adapt natively to physical ergonomics across Web, Mobile, Tablet, Desktop, Wearable, and HMI.
- **Interface copy & honest boundaries:** Name actions and outcomes with consistent domain nouns and active verbs. Keep author-facing meta-notes (`sample data`, `prototype only`) out of product UI unless essential to prevent a consequential misunderstanding, and never present simulated payments, saves, or external sends as completed.

## 3. Anti-AI-Slop & Justified Complexity

Distinguish **necessary domain complexity** from **accidental, decorative, or engineering slop**. Challenge and targetedly correct:
1. **Generic design:** Unmotivated SaaS card grids, decorative KPI cards that support no decision, hero banners inside functional workspaces, and redundant icons beside clear labels.
2. **Overdesign:** Nested bordered containers, competing shadows/gradients, excessive accent colors, and non-functional motion.
3. **Overengineering:** One-off wrapper components, speculative configuration props, and unnecessary state abstractions.
4. **Text overload:** Redundant introductory paragraphs, repeated helper text, and marketing filler (while strictly protecting essential legal, safety, accessibility, and error-recovery disclosures).
5. **Interaction clutter:** Competing primary CTAs, unnecessary confirmation modals on reversible actions, and multi-step modals for simple edits.
6. **Context mismatch:** Consumer card layouts applied to dense expert workflows, or complex enterprise controls forced onto first-time consumer onboarding.
7. **False sophistication:** Decisions justified as "modern," "clean," or "premium" without an observable user, accessibility, or engineering benefit.

For further reading, [Antislop](https://antislop.ai.id/) separates design direction from quality checks, and [Taste Skill](https://www.tasteskill.dev/) illustrates choosing visual directions and reviewing rendered interfaces. PDI treats these as references, not universal rules or proof of quality; see the [source registry](sources.yaml) for review scope.
