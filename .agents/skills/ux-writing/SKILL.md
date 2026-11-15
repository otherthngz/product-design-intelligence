---
name: ux-writing
description: Write and audit product interface copy, microcopy, empty states, onboarding prompts, action labels and error recovery messages. Use when crafting or reviewing UI text and terminology; do not use for long-form marketing articles or to promise unimplemented backend actions.
---

# Ux Writing

## Purpose and use
Write and audit product interface copy, microcopy, empty states, onboarding prompts, action labels and error recovery messages. Use when crafting or reviewing UI text and terminology; do not use for long-form marketing articles or to promise unimplemented backend actions.

## Inputs
Required: the screen, flow, or component context and the user's primary task. Optional: target audience, brand voice constraints, localization requirements, existing terminology glossary, and error conditions. State missing material and assumptions; ask when a consequential decision cannot be made safely.

## Relevant knowledge
Load only what the task needs: [interface copy](../../../knowledge/ux-design/interface-copy.md), [task hierarchy](../../../knowledge/ux-design/task-hierarchy.md), [responsive accessible ui](../../../knowledge/frontend-engineering/responsive-accessible-ui.md). Choose depth based on context; see the [topic index](../../../knowledge/index.md).

## Workflow
1. Identify the user's task, expertise level, current state, domain objects, and consequential or irreversible actions on the screen.
2. Establish a consistent noun-verb glossary so actions and objects keep the same name across navigation, headings, buttons, and confirmation messages.
3. Draft concise, sentence-case copy for all relevant states: default, empty, loading, validation error, system failure, destructive confirmation, and completion.
4. **Eliminate text overload while protecting essential disclosures:** Remove redundant introductory prose, helper text that repeats the label, vague actions, and generic filler. Omit author notes unless needed to prevent consequential misunderstanding; retain explanations required for informed consent, legal/regulatory compliance, financial/clinical accuracy, safety, accessibility, or error recovery. Ensure no copy falsely confirms an unimplemented payment, save, or external notification.
5. Check accessibility and localization readiness (descriptive link/button text, `aria-live` status clarity, and room for text expansion), then hand off to `ui-prototyping` or `design-handoff`.

## Artifacts
Produce a structured UI copy table, state-by-state microcopy specification, or edited interface artifact. Apply [the output contract](../../../workflows/output-contract.md) at the task's complexity level. Link actual files and distinguish findings from hypotheses.

## Quality
Check coverage against the request, verb specificity, terminology consistency, actionable error recovery, and honest representation of system capabilities. Use [design guidance](../../../knowledge/design-practice.md) and the [review rubric](../../../tests/evaluation-cases.md) as needed.

## Failure modes
Avoid apologetic or vague error messages ("Oops, something went wrong"), inconsistent object naming across steps, author meta-commentary inside product UI, and false promises of emails, saves, or transactions when no backend exists.

## Tools and fallback
Use available local files and inspection tools to review existing strings or templates. If live product screens or localization tools are unavailable, work from supplied text or HTML and note what was not inspected. Obtain approval before destructive, irreversible, publishing or production-impacting actions.

## Example
A copy matrix for a team-invite modal specifying the heading, field label, helper text, specific button label ("Send invite"), duplicate-email validation message, and offline retry message without promising an email when the mail service is unconfigured.
