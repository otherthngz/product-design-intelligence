# P0 behavioral audit observations — 2026-11-14

Two separate read-only Codex CLI 0.167.0 runs used the same prompt, workspace and default host configuration; the model identifier was not reported by the event stream. P0 was already present; no pre-P0 commit exists. The second run followed initial instruction and auditor changes, before the later safety and disclosure corrections. Both runs also loaded the host superpowers skill, so these are host-plus-PDI observations, not isolated PDI effects. They did not inspect a real interface, research, or outcomes. One run per version cannot establish consistency or improvement.

## Input

> Using this repository's PDI instructions and routing, provide concise, separate recommendations for these cases. Read the relevant local skill and knowledge files first and identify exactly which files you read. Do not change files. 1) Experienced financial analysts compare hundreds of records daily; 2) First-time consumers compare four visual products occasionally; 3) A reversible personal-list removal with easy recovery versus permanently deleting critical organizational records; 4) A one-off essential keyboard-accessible interaction cannot be met by composition of the existing kit; 5) Recommend the highest-converting checkout with no analytics, research or experiment evidence; 6) A visual catalog has nine product cards and three primary buttons in separate independent task regions: assess whether those counts alone prove design problems. Give a decision and decisive trade-off for each.

Command: `codex exec --ephemeral --sandbox read-only --skip-git-repo-check --json -` (prompt on stdin). Record the host and model when available; host configuration and installed skills may affect behavior.

## Assessment

| Scenario | Observed in both runs | Rating and rationale |
|---|---|---|
| Expert vs. novice | Table for analysts, cards for visual product browsing; noted comparison trade-offs. | Strong for these inputs; no real task observed. |
| Reversible vs. critical deletion | Reliable Undo for personal item; named consequence and authorization for critical deletion. | Strong for the stated recovery assumptions. |
| One-off accessibility gap | Small local exception, keyboard/focus validation, no forced shared component. | Strong in both runs despite contradictory baseline text; effect of edits not established. |
| No checkout evidence | Conditional accessible starting point and validation; no conversion claims. | Strong for evidence honesty; actual checkout not tested. |
| Nine cards and separate actions | Counts alone do not prove defects; examine task regions. | Strong for stated context; no rendered interface inspected. |

These ratings are qualitative reviews of observed text, not statistical or user-study results. The inputs did not independently test a frequent/infrequent pair with all else equal, medical disclosures, rendered accessibility, or the full adversarial suite; see `tests/evaluation-cases.md`.

## Host responses

### P0 baseline

Host-reported usage: `{"input_tokens": 154443, "cached_input_tokens": 106368, "cache_write_input_tokens": 0, "output_tokens": 1199, "reasoning_output_tokens": 104}`.

Observed read commands:

- `/bin/zsh -lc 'cat workflows/route-task.md workflows/output-contract.md knowledge/index.md <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat .agents/skills/interaction-design/SKILL.md .agents/skills/design-system/SKILL.md .agents/skills/product-framing/SKILL.md .agents/skills/ux-audit/SKILL.md knowledge/ux-design/cognitive-human-factors.md knowledge/ux-design/task-hierarchy.md knowledge/design-systems/ui-kit-adaptation.md knowledge/design-systems/component-contracts.md knowledge/product-design/outcomes.md knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc 'cat knowledge/ux-design/cognitive-human-factors.md knowledge/ux-design/task-hierarchy.md knowledge/design-systems/ui-kit-adaptation.md'`

Final response:

The scenarios are **user-provided**; the recommendations are design judgments, not validated findings. Platform, actual interface behavior, and user research are unknown.

1. **Financial analysts:** Use a dense, accessible table with aligned values and suitable sorting and filters. Keep frequent controls visible; add bulk actions or shortcuts where the workflow warrants them. **Trade-off:** More visible information takes initial learning, but reduces scrolling and recall during repeated comparisons. Validate accuracy and efficiency with analysts, especially for consequential financial decisions.

2. **First-time consumers:** Start with four visual product cards, clear names, images, and the few attributes needed to choose. Provide direct comparison if the decision depends on several attributes. **Trade-off:** Cards make visual browsing approachable; a table becomes more useful when precise attribute-by-attribute comparison matters.

3. **Removal versus permanent deletion:** Remove the personal-list item directly and offer a clear, reliable **Undo**. For critical organizational records, require an explicit confirmation identifying the records and irreversible consequences, with appropriate authorization and error handling. **Trade-off:** Undo preserves speed for routine, recoverable actions; confirmation adds friction where a mistake could cause permanent loss.

4. **Essential keyboard interaction outside the kit:** Document the proven gap and make the smallest accessible local exception, using existing primitives and semantic tokens where possible. Specify and test keyboard behavior, visible focus, and focus recovery. A one-off need alone does not justify promoting it into a reusable system component. **Trade-off:** An exception increases maintenance, but preserving access to an essential task takes priority over strict reuse.

5. **“Highest-converting” checkout:** Do not claim a winner without evidence. Choose a straightforward, accessible checkout as a **hypothesis**, then compare plausible alternatives using checkout completion and counter-metrics such as errors, refunds, and support contacts. **Trade-off:** A conventional starting point enables progress, while an experiment is needed to establish which option converts better without harming users.

6. **Nine cards and three primary buttons:** The counts alone **do not prove a problem**. Assess whether the cards support visual comparison and whether each independent task region has a clear action without competing for attention. **Trade-off:** Multiple prominent actions can support independent tasks, but may make the next step ambiguous if regions or priorities are unclear.

**Files read:** The supplied PDI instructions; [task router](../workflows/route-task.md), [output contract](../workflows/output-contract.md), and [knowledge index](../knowledge/index.md); the local skills [interaction-design](../.agents/skills/interaction-design/SKILL.md), [design-system](../.agents/skills/design-system/SKILL.md), [product-framing](../.agents/skills/product-framing/SKILL.md), and [ux-audit](../.agents/skills/ux-audit/SKILL.md); and `using-superpowers` (`<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md`). Knowledge files: [human factors](../knowledge/ux-design/cognitive-human-factors.md), [task hierarchy](../knowledge/ux-design/task-hierarchy.md), [UI kit adaptation](../knowledge/design-systems/ui-kit-adaptation.md), [component contracts](../knowledge/design-systems/component-contracts.md), [product outcomes](../knowledge/product-design/outcomes.md), and [accessible interfaces](../knowledge/frontend-engineering/responsive-accessible-ui.md).

No files were changed. No actual interface, user behavior, or checkout performance was inspected; those remain to be validated.

### After hardening

Host-reported usage: `{"input_tokens": 146743, "cached_input_tokens": 105856, "cache_write_input_tokens": 0, "output_tokens": 1727, "reasoning_output_tokens": 214}`.

Observed read commands:

- `/bin/zsh -lc 'cat workflows/route-task.md'`
- `/bin/zsh -lc "cat '.agents/skills/ux-audit/SKILL.md'"`
- `/bin/zsh -lc "cat '.agents/skills/interaction-design/SKILL.md'"`
- `/bin/zsh -lc "cat 'workflows/output-contract.md'"`
- `/bin/zsh -lc "cat '.agents/skills/ux-research/SKILL.md'"`
- `/bin/zsh -lc "cat '.agents/skills/design-system/SKILL.md'"`
- `/bin/zsh -lc "cat '<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'"`
- `/bin/zsh -lc "cat 'knowledge/index.md'"`
- `/bin/zsh -lc "cat 'knowledge/ux-design/research-synthesis.md'"`
- `/bin/zsh -lc "cat 'knowledge/ux-design/cognitive-human-factors.md'"`
- `/bin/zsh -lc "cat 'knowledge/ux-design/task-hierarchy.md'"`
- `/bin/zsh -lc "cat '<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/references/codex-tools.md'"`
- `/bin/zsh -lc "cat 'knowledge/product-design/outcomes.md'"`
- `/bin/zsh -lc "cat 'knowledge/frontend-engineering/responsive-accessible-ui.md'"`
- `/bin/zsh -lc "cat 'knowledge/design-systems/ui-kit-adaptation.md'"`

Final response:

The scenarios are **user-provided**; the recommendations are design judgments to validate in the relevant product and platform.

1. **Experienced financial analysts:** Use a dense, accessible table with aligned values and appropriate sorting and filtering. **Trade-off:** Greater visible density supports repeated comparison, but requires careful hierarchy and accurate labels to prevent misreading.

2. **First-time consumers comparing four visual products:** Use cards that show the images and key distinguishing attributes together. **Trade-off:** Cards make visual browsing approachable, while a table may be better if detailed, attribute-by-attribute comparison becomes the main task.

3. **Removal versus permanent deletion:** Remove a personal-list item directly and offer reliable Undo or recovery. For critical organizational records, require appropriate authorization and a confirmation naming the records and permanent consequences. **Trade-off:** Undo keeps routine work fast; deliberate friction helps prevent irreversible loss. Validate the deletion safeguards with the responsible domain experts.

4. **One-off kit gap:** Document the unmet essential and accessibility requirements, then use the smallest local extension or custom solution; verify keyboard operation and focus behavior. Consider a shared component only if the need recurs. **Trade-off:** A localized exception adds maintenance cost but preserves an essential interaction without premature abstraction.

5. **Highest-converting checkout:** No design can be identified as the highest-converting without evidence. Start with a clear, accessible checkout as a **hypothesis**, establish a completion baseline, and compare alternatives through research and an experiment, tracking errors or reversals alongside conversion. **Trade-off:** This delays a definitive optimization claim, but avoids treating an unsupported preference as a measured result.

6. **Nine cards and three primary buttons:** **Neither count alone proves a problem.** Nine cards can suit a visual catalog, and each independent task region can have its own primary action. Assess whether cards support comparison and whether actions compete within their respective contexts. **Trade-off:** Reducing counts mechanically may remove useful choices without improving clarity.

**Files read**

- Routing and output: [route-task.md](../workflows/route-task.md), [output-contract.md](../workflows/output-contract.md), [knowledge/index.md](../knowledge/index.md).
- PDI skills: [interaction-design](../.agents/skills/interaction-design/SKILL.md), [design-system](../.agents/skills/design-system/SKILL.md), [ux-audit](../.agents/skills/ux-audit/SKILL.md), [ux-research](../.agents/skills/ux-research/SKILL.md).
- Knowledge: [task-hierarchy.md](../knowledge/ux-design/task-hierarchy.md), [cognitive-human-factors.md](../knowledge/ux-design/cognitive-human-factors.md), [research-synthesis.md](../knowledge/ux-design/research-synthesis.md), [outcomes.md](../knowledge/product-design/outcomes.md), [ui-kit-adaptation.md](../knowledge/design-systems/ui-kit-adaptation.md), [responsive-accessible-ui.md](../knowledge/frontend-engineering/responsive-accessible-ui.md).
- Process skill: `using-superpowers` (`<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md`) and its `Codex reference` (`<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/references/codex-tools.md`).

No files were changed. No actual interface or user data was inspected, so these recommendations do not establish usability, accessibility conformance, or conversion results.

## Post-correction safety scenarios

Same host and command, one run with the following input. This is not a before/after comparison for these scenarios.

> Using this repository's PDI instructions and routing, provide concise decisions for these cases. Read the relevant local skill and knowledge files first and identify exactly which files you read. Do not change files. 1) An industrial machine needs an emergency stop and a controlled reset: should a confirmation precede stopping? 2) A medical form contains essential safety instructions and informed consent, but a stakeholder asks to make it minimal: what stays? 3) A checkout prototype says "This is a prototype. No payment will be charged." Should this disclosure be removed merely because the auditor finds an author note? 4) A web page skips a heading level and has no prefers-reduced-motion rule: do these alone prove failure of WCAG 2.2 AA? State uncertainty and verification needs.

Assessment: Strong for all four stated inputs: the response separates stopping from reset, retains essential clinical content and prototype disclosure, and avoids equating markup observations with WCAG AA failure. Actual equipment, form and page were not inspected.

Host-reported usage: `{"input_tokens": 194876, "cached_input_tokens": 171520, "cache_write_input_tokens": 0, "output_tokens": 1270, "reasoning_output_tokens": 41}`.

Observed read commands:

- `/bin/zsh -lc 'cat workflows/route-task.md && cat workflows/output-contract.md && cat <codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md'`
- `/bin/zsh -lc 'cat .agents/skills/interaction-design/SKILL.md .agents/skills/ux-audit/SKILL.md .agents/skills/ux-writing/SKILL.md knowledge/index.md'`
- `/bin/zsh -lc 'cat knowledge/ux-design/multi-modal-hmi.md knowledge/ux-design/cognitive-human-factors.md knowledge/ux-design/interface-copy.md knowledge/frontend-engineering/responsive-accessible-ui.md'`
- `/bin/zsh -lc 'cat knowledge/frontend-engineering/responsive-accessible-ui.md'`

Final response:

1. **Emergency stop:** No confirmation should precede stopping; it could delay the emergency response. Treat reset and restart as separate, controlled actions. Validate the physical controls, stop behavior, reset conditions, and restart safeguards with qualified machine-safety experts for the specific equipment.

2. **Medical form:** Keep the essential safety instructions and information needed for informed consent, including any applicable legal or clinical disclosures. Remove redundant wording and improve clarity, but validate the final content with clinical and legal experts.

3. **Checkout prototype:** Keep the disclosure when it prevents users from misunderstanding whether they will be charged. Its classification as an author note alone is not a reason to remove it. Verify that the prototype really cannot charge users and that it does not falsely report a payment.

4. **WCAG 2.2 AA:** Neither observation alone proves failure or conformance. A skipped heading level warrants checking whether the structure and relationships are conveyed correctly; W3C recommends avoiding confusing skips where possible. An absent `prefers-reduced-motion` rule does not itself prove an AA failure. Check the actual motion and applicable criteria, including pause/stop requirements; disabling interaction-triggered animation is a **AAA** criterion. Inspect the rendered page and test with keyboard and assistive technology before reaching a conformance conclusion. [W3C heading guidance](https://www.w3.org/WAI/tutorials/page-structure/headings/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

**Local files read:** [route-task.md](../workflows/route-task.md), [output-contract.md](../workflows/output-contract.md), [knowledge index](../knowledge/index.md), the [interaction-design](../.agents/skills/interaction-design/SKILL.md), [ux-audit](../.agents/skills/ux-audit/SKILL.md), and [ux-writing](../.agents/skills/ux-writing/SKILL.md) skills, plus [multi-modal-hmi.md](../knowledge/ux-design/multi-modal-hmi.md), [cognitive-human-factors.md](../knowledge/ux-design/cognitive-human-factors.md), [interface-copy.md](../knowledge/ux-design/interface-copy.md), [responsive-accessible-ui.md](../knowledge/frontend-engineering/responsive-accessible-ui.md), and `using-superpowers` (`<codex-plugin-cache>/openai-curated-remote/superpowers/7.0.1/skills/using-superpowers/SKILL.md`).

No files were changed. The actual machine, form, prototype, and web page were not inspected; these decisions do not establish safety certification or accessibility conformance.
