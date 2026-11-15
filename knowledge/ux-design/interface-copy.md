<!-- pdi-topic: {"id":"interface-copy","domain":"ux-design","depths":["foundation","practitioner","advanced"],"sources":["w3c-structure","wcag22","pdi-guidance"]} -->
# Interface copy, microcopy and error recovery messages

## What and why
Interface copy guides people through tasks, explains system state, and helps them recover from errors. Clear, consistent terminology reduces extraneous cognitive load and prevents costly user mistakes without relying on decorative marketing filler, redundant helper text, or author-facing explanations.

## When to apply
When writing or auditing labels, buttons, onboarding steps, empty states, confirmation dialogs, high-consequence disclosures, validation messages, and system notifications.

## Fundamental principles
**Foundation:**
- **Principle & mechanism:** Write from the user's task perspective using plain verbs, sentence case, and a consistent noun-verb glossary. Every interactive control label should state what happens next (`Save preferences`, `Send invite`).
- **Text overload vs. essential disclosure (Boundary condition):** Eliminate redundant introductory prose, helper text that merely repeats the field label, verbose button copy, and unnecessary tooltips. *Critical exception:* Never strip information required for **informed consent, legal/regulatory compliance, financial/clinical accuracy, accessibility, safety, or error recovery** merely to make the UI look minimal.
- **Zero author meta-copy & honest system state:** Never place author notes (`sample data`, `this is a prototype`, `illustrative only`) inside the product UI unless required to prevent a consequential misunderstanding, and never confirm an unimplemented consequential action (payment, save, external email).

## Practical implementation
**Practitioner:**
- **Terminology consistency:** Build a task glossary so the same domain object and action keep the exact same name across navigation, headings, buttons, and status toasts (e.g., if the button says `Invite member`, the toast says `Member invited`, not `User provisioned`).
- **Actionable error recovery:** Structure error messages in two parts: (1) what went wrong in plain, non-blaming terms and (2) the exact action to fix or recover from it. Preserve user-entered data on validation or network failure.
- **Empty states & confirmations:** Treat empty states as a concise starting point with one clear primary action rather than a marketing pitch. For destructive or high-consequence confirmations, name the specific target resource, state the irreversible impact, and label the button with the exact verb (`Delete workspace`).

**Advanced:** Coordinate terminology across product, legal, localization, and support surfaces. Account for text expansion in translations (30–40% longer in many languages), screen-reader announcement priority (`role="status"` / `aria-live="polite"` for routine updates vs. `role="alert"` / `aria-live="assertive"` for blocking errors), and cognitive accessibility (plain language, clear units, and explicit examples for complex inputs).

## Good and bad examples
Good: Button `Delete workspace "Acme"` paired with warning `Permanently deletes 14 projects and revokes team access. This cannot be undone.` In a high-consequence wire-transfer form, keeping concise inline fee/settlement disclosures next to the amount input. Bad: Button `Submit` paired with error `Invalid input (Error 422)`; adding a 3-sentence introductory paragraph explaining how a basic profile form works; or removing mandatory clinical dosage warnings to "reduce text clutter."

## Common mistakes
Using vague action labels (`OK`, `Submit`, `Continue`, `Manage`, `Click here`); blaming or apologizing to the user (`Oops! Something went wrong`); repeating the field label inside placeholder and helper text; mixing synonyms (`Workspace`, `Organization`, `Tenant`) on the same screen; inserting marketing slogans into operational tools; deleting essential safety or compliance instructions in pursuit of visual minimalism.

## Evaluate the result
- **Evaluation signals:** Are all interactive labels specific and predictable? Is redundant filler text removed while essential safety, compliance, and recovery information is preserved? Do error messages state both the cause and recovery step? Is the UI free of author meta-notes and false completion claims?

## AI application
Generate concise, task-specific copy matrices covering default, empty, loading, validation error, failure, and confirmation states. Audit supplied screens for both **text overload** (redundant helper text, marketing fluff, verbose buttons) and **under-specification** (vague CTAs, missing consequence disclosures), and flag any copy that promises unimplemented backend actions.

## Related concepts
[Task hierarchy](task-hierarchy.md), [Responsive and accessible interfaces](../frontend-engineering/responsive-accessible-ui.md), [Tokens and component contracts](../design-systems/component-contracts.md).

## References and further learning
[W3C WAI Page Structure Tutorial](https://www.w3.org/WAI/tutorials/page-structure/), [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) and [PDI design practice](../design-practice.md). [Source registry](../sources.yaml) records provenance and review scope.
