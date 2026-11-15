# Founder request: critique the existing onboarding interface

**Scenario:** “Review the first-time onboarding experience and identify what to improve.” Source: [onboarding prototype](../onboarding/index.html) and [its handoff](../onboarding/README.md). Routed to `ux-audit`; `task-hierarchy` and `responsive-accessible-ui` inform the review. No actual founder, research or product context was supplied.

## Findings

1. **High · untested completion promise.** The side panel and “About 1 minute” create expectations, but the duration is illustrative rather than measured (source: page copy and example README). **Impact hypothesis:** an inaccurate expectation could reduce trust. **Recommendation:** measure completion time with representative users or remove the estimate. Confidence: high for the copy, low for impact.
2. **Medium · unclear value of goal selection.** Step 2 says the choice shapes first steps, yet this prototype only displays a summary (source: prototype flow). **Impact hypothesis:** users may not understand why it is required. **Recommendation:** explain the real effect or make it optional once product behavior is defined. Confidence: high for prototype behavior, low for real-world impact.
3. **Medium · mobile form starts below contextual content.** The narrow layout puts the introductory panel above the form (source: responsive CSS and previously recorded 390px browser review). **Impact hypothesis:** extra scrolling may delay starting. **Recommendation:** test a compact intro with first-time users. Confidence: high for layout, unverified for impact.

**What was checked:** actual supplied source and prior browser validation documented in the example; this audit did not run a user study, screen reader or new interaction test. Prioritize user interviews and completion timing before claiming that these are demonstrated user problems.
