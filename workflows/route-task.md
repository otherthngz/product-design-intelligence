# Task router & adaptive execution process

One coordinator classifies the request, validates context dimensions (operating mode, complexity, platform/UI kit, domain risk), and loads the relevant skills; this is a decision guide, not a rigid waterfall. Ask clarifying questions **only** when missing information materially prevents a useful or safe decision; otherwise state reasonable assumptions and proceed.

| Request | Start with | Add when needed |
|---|---|---|
| Plan user research, interviews or synthesize transcripts | ux-research | product-framing, ux-audit |
| Unclear problem, goals, scope or feature request | product-framing | ux-research, interaction-design, ui-prototyping |
| Critique or redesign an existing experience | ux-audit | ux-writing, frontend-design, design-handoff |
| Define IA, user journeys, flows or state logic | interaction-design | product-framing, ux-writing, design-handoff |
| Write or audit UI copy, labels, empty or error states | ux-writing | interaction-design, ux-audit, ui-prototyping |
| Select, reuse or audit UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`) & tokens | design-system | ui-prototyping, frontend-design, design-handoff |
| Build a screen or interactive prototype | ui-prototyping | product-framing, interaction-design, ux-writing, design-system, frontend-design, design-handoff |
| Create multi-audience handoff & decision changelog | design-handoff | design-system, ux-writing, ux-audit |

---

## 1. Unified 8-Step Design Intelligence Workflow & Progressive Reasoning Depth

Every product designer—across **Solo**, **Small Team**, and **Enterprise**—reasons through **Context → Evidence → Alternatives → Trade-offs → Decision → Evaluation** using these **8 operational steps**. They are **analytical checkpoints**, not a mandate to generate verbose consulting reports when a user needs focused execution:

1. **Step 1 — Understand (Context Model):** Activate only the context dimensions relevant to the decision:
   - *User context:* primary group, expertise (novice vs. expert), accessibility needs, task frequency, environment.
   - *Product & technical context:* category, maturity, platform/form factor (**Web, Mobile, Tablet, Desktop, Wearable, HMI**), active UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`), existing components, data/API constraints.
   - *Task & business context:* user goal, complexity, reversibility (two-way vs. one-way door), failure consequences, desired outcome.
2. **Step 2 — Retrieve & Frame (`ux-research` / `product-framing`):** Load only the relevant knowledge topics from [the topic index](../knowledge/index.md). Distinguish the **stated request**, **underlying problem**, **intended user outcome**, **business outcome**, and **actual constraints**. Challenge solution-first prompts ("add more charts") when a table, summary, default change, copy edit, or **no-UI intervention** solves the root problem better.
3. **Step 3 — Reason & Explore Alternatives:** When a decision is consequential or ambiguous, compare at least two meaningful alternatives that differ in interaction, information density, or workflow structure (e.g., inline table editing vs. detail drawer vs. bulk action workflow; single-page form vs. multi-step wizard). Skip artificial alternatives for trivial or tightly constrained fixes.
4. **Step 4 — Decide & Resolve Trade-Offs:** Select the contextually appropriate pattern by weighing competing objectives qualitatively (learnability vs. expert efficiency, simplicity vs. discoverability, minimalism vs. information density, speed vs. error prevention/safety, reuse vs. custom build, reversibility).
5. **Step 5 — Produce (`interaction-design` / `ux-writing` / `design-system` / `ui-prototyping`):** Define IA, interaction flow, relevant system states (empty, default, loading, validation error, failure, success, cancelled/back), task-focused copy, appropriate density, and **100% unmodified stock UI kit primitives** by default.
6. **Step 6 — Evaluate (Anti-AI-Slop & 13 Quality Gates):** Run a bounded evaluation pass (`ux-audit` + [output contract](output-contract.md)) checking for the **7 Anti-Slop Failure Categories** (generic design, overdesign, overengineering, text overload, interaction clutter, context mismatch, false sophistication) while **protecting necessary domain and safety complexity**.
7. **Step 7 — Refine & Validate:** Apply targeted corrections for material (`Critical` / `Major`) deficiencies without unbounded rewrite loops. Run deterministic checks (`python3 scripts/audit_artifact.py`) and browser/DOM verification where available; flag untested assumptions and recommend proportionate validation.
8. **Step 8 — Deliver (`design-handoff`):** Provide the **smallest set of artifacts** needed for the next step. When asked to build UI, prioritize the working artifact; when handing off consequential work, use [templates/handoff-and-changelog.md](../templates/handoff-and-changelog.md).

### Progressive Reasoning Depth (Match Analysis to Complexity & Risk)

- **Low Complexity (`quick` — e.g., spacing fix, button label, minor hierarchy issue):** Apply established conventions directly, avoid unnecessary alternatives, run lightweight quality checks, and return a concise fix.
- **Medium Complexity (`standard` — e.g., settings screen, onboarding flow, navigation choice, form restructuring):** Identify key context, evaluate 2–3 meaningful alternatives, state the deciding trade-off, and run targeted anti-slop checks.
- **High Complexity (`complex` or high-consequence — e.g., enterprise bulk workflow, product IA, financial/clinical/HMI interface, design-system component decision):** Analyze constraints across user/product/task/technical dimensions, separate verified evidence from assumptions, compare competing interaction models and second-order consequences, explicitly justify any complexity, and define validation criteria.

### Graceful Degradation Under Missing Context or Evidence
When user research, analytics, or external tools are unavailable: (1) use verified repository or user-provided facts, (2) state bounded assumptions explicitly, (3) prefer reversible choices when uncertainty is high, (4) ask clarifying questions **only** when missing information materially changes the solution and cannot be safely inferred, and (5) never fabricate citations, metrics, or test execution.

---

## 2. Operating Modes & Orthogonal Context Dimensions

Operating mode changes workflow ceremony and deliverable structure, **never** design quality. Always combine operating mode with **Task Complexity** (`quick`, `standard`, `complex`) and **Domain Risk / Criticality**:

- **Solo Mode (`solo`):**
  - **Context:** Individual founder, solo developer, or independent designer.
  - **Focus:** High-leverage decisions, lean discovery, fast validation, reusable UI kit fundamentals, minimal ceremony. Do not generate bloated enterprise specs unless requested; scale depth to project complexity and domain risk.
- **Small Team Mode (`team`):**
  - **Context:** Collaborative PM, Designer, and Engineers.
  - **Focus:** Validate what PM/Eng already defined and which UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, `Custom`) is in the repo. Surface trade-offs and dependencies early, enforce shared terminology and component reuse, and deliver clear, nimble specs.
- **Enterprise Mode (`enterprise`):**
  - **Context:** Multi-team workflows, role-based permissions, existing design systems, legacy/migration constraints, and governance/compliance.
  - **Focus:** Validate the user's exact role scope and cross-team dependencies first. Ensure system consistency, role-based clarity, migration feasibility, and auditability (`templates/handoff-and-changelog.md` + `--strict-pii`) **without** making the UI itself bloated or feature-heavy.
- **High-Risk Override:** A **Solo** project for a medical device or industrial controller requires stricter safety, alarm clarity, and human-factors verification than a low-risk **Enterprise** internal profile page.

For a Figma request, route by the design task as above and use the host-specific [Figma MCP guide](../adapters/figma-mcp.md); PDI does not ship an MCP connector.
