# Manual knowledge retrieval cases

These are review cases, not an automated retriever or a measured agent benchmark. For each, ask a compatible host agent to perform the request, record the host/model/date and the actual topics read, inspect artifacts and score the result using the [practical audit rubric](../../docs/reference/practical-audit.md).

| Request | Expected skill | Topic IDs to consider | Evidence in result |
|---|---|---|---|
| Plan discovery interviews and synthesize 4 user transcripts | ux-research | research-synthesis, product-outcomes | Traceable participant IDs, observed behavior separated from hypotheses, explicit sample limits. |
| Frame a vague onboarding request | product-framing | product-outcomes | User goal, constraints, assumptions, proposed measure and questions. |
| Critique a supplied checkout | ux-audit | task-hierarchy, responsive-accessible-ui | Specific observed locations, hypotheses separated, accessibility gaps. |
| Define IA, user flow, and 7-state logic for checkout recovery | interaction-design | task-hierarchy, product-outcomes, ui-kit-adaptation | IA tree, Mermaid flow, 7-state matrix, retained state, uncertain-payment recovery. |
| Write microcopy, empty states, and error recovery for team invite | ux-writing | interface-copy, task-hierarchy, responsive-accessible-ui | Noun-verb glossary, specific button labels, actionable error recovery, no false email promises. |
| Map a settings screen to stock `shadcn/ui`, `Nuxt UI`, `Apple HIG`, or `Material 3` without custom CSS overrides | design-system | ui-kit-adaptation, token-governance, component-contracts | 100% unmodified stock kit primitives mapped; semantic tokens; explicit justification for any override. |
| Build a responsive dashboard using the active UI kit | ui-prototyping | ui-kit-adaptation, component-contracts, responsive-accessible-ui, human-reviewed-ai | Executable local artifact, unmodified kit primitives, decision log, evidence and validation boundaries. |
| Create a multi-audience handoff and decision changelog | design-handoff | ui-kit-adaptation, component-contracts, responsive-accessible-ui | Follows `templates/handoff-and-changelog.md`: Executive summary, IA/flow, 7-state matrix, UI kit table, acceptance criteria, and versioned decision changelog. |
| Compare table vs. cards for a daily enterprise workflow (100s of records) vs. annual novice setup | interaction-design | cognitive-human-factors, task-hierarchy, multi-modal-hmi | Differentiates Context A (dense table, inline/bulk actions, keyboard shortcuts, Undo) from Context B (guided steps, defaults) with explicit trade-offs. |
| Evaluate a developer request to create a new component for a minor visual variation | design-system | component-contracts, ui-kit-adaptation, token-governance | Rejects unnecessary component proliferation; recommends reusing or composing existing stock primitives (`Card` + `Badge`). |
| Audit a generated screen for anti-slop while preserving high-consequence compliance disclosures | ux-audit | task-hierarchy, interface-copy, cognitive-human-factors, responsive-accessible-ui | Flags card fragmentation, competing CTAs, and redundant filler while preserving essential legal/safety/recovery copy and expert controls. |

If no applicable topic is available, the agent should say so and use the best available verified evidence, not invent a topic or imply a tool was used. Check that advanced knowledge is selected for actual governance needs, not merely because a team uses enterprise mode.
