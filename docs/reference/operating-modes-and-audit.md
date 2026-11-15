# Universal Product Designer Workflow, UI Kit Reuse & Operating Modes

This reference defines:
1. **The Universal 8-Stage Product Designer Workflow** (identical across Solo, Small Team, and Enterprise).
2. **How each Operating Mode adapts focus and scope** after validating the user's situation.
3. **The Strict UI Kit Reuse Mechanism** (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Google Material 3`, and `Custom`).
4. **The Multi-Audience Handoff & Product Decision Changelog** (`templates/handoff-and-changelog.md`).

---

## 1. Universal 8-Stage Product Designer Workflow

Every product designer—whether working **Solo**, in a **Small Team**, or in an **Enterprise**—follows the **exact same 8-stage methodology**. AI agents must never jump straight to Stage 7 (`ui-prototyping`) from scratch without verifying Stages 1–6:

| Stage | Skill | Core Deliverable |
|---|---|---|
| **1. Scope & Kit Validation** | Router (`route-task.md`) | Validate operating mode (`solo`/`team`/`enterprise`), complexity (`quick`/`standard`/`complex`), role scope, and active UI kit (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`). |
| **2. Discovery & Synthesis** | `ux-research` | Research plan, interview guide, or tagged evidence synthesis (`user-provided`, `verified`, `assumption`, `hypothesis`). |
| **3. Problem & Outcome Framing** | `product-framing` | User job, problem statement, measurable business outcome, constraints, and ranked uncertainties. |
| **4. IA, Flows & State Logic** | `interaction-design` | **Information Architecture (IA)** tree, Mermaid user flow, and **7-State Logic Matrix** (Empty, Default, Loading, Validation Error, System Failure, Success, Cancelled/Back). |
| **5. Interface Copy & Glossary** | `ux-writing` | Domain noun-verb glossary, specific CTA labels, empty states, and actionable error recovery copy. |
| **6. UI Kit & Token Mapping** | `design-system` (+ `frontend-design`) | Map every UI element to **100% unmodified stock components** from the active UI kit and semantic tokens. |
| **7. Prototype & Verification** | `ui-prototyping` + `ux-audit` | Working interactive artifact + deterministic check (`python3 scripts/audit_artifact.py`). |
| **8. Multi-Audience Handoff & Changelog** | `design-handoff` | Complete spec and versioned **Product Decision Changelog** via [templates/handoff-and-changelog.md](../../templates/handoff-and-changelog.md). |

---

## 2. How Operating Modes Adapt Focus (Same Workflow, Situational Scope)

The workflow never changes, but **each mode starts by validating the user's context and tailoring focus**:

| Dimension | Solo Mode (`--mode solo`) | Small Team Mode (`--mode team`) | Enterprise Mode (`--mode enterprise`) |
|---|---|---|---|
| **First validation question** | *"What is the project complexity (`quick`, `standard`, `complex`) and which UI kit are we using?"* | *"Which parts are already defined by PM/Engineering, and what UI kit is in the repo?"* | *"What is your exact role scope, which partner teams own upstream/downstream stages, and what org policies/approvals apply?"* |
| **Workflow coverage** | Runs all 8 stages end-to-end scaled to project complexity; one person owns all decisions. | Lightweight & nimble cross-functional execution; focuses on unblocking PM/Design/Eng alignment and reusing the team's UI kit. | Scoped to the practitioner's assigned responsibility (e.g., end-to-end feature flow, or deep interaction + handoff integrating with a dedicated Research/Design System squad). |
| **Documentation weight** | Single cohesive handoff & changelog file; zero bureaucratic sign-off ceremony. | Nimble shared handoff, UI glossary, component mapping table, and peer review checkpoints. | Formal handoff + changelog, `--strict-pii` audit, 3-tier token governance, and named stakeholder approval sign-offs. |

---

## 3. Strict UI Kit Adaptation Mechanism (Stop AI From Inventing Custom Components)

AI agents often make the mistake of inventing custom CSS components or overriding spacing/colors when a standard UI kit is already chosen. PDI enforces a **Strict Default-First Reuse Rule** (see [knowledge/design-systems/ui-kit-adaptation.md](../../knowledge/design-systems/ui-kit-adaptation.md)):

1. **Web — `shadcn/ui` (React / Next.js / Tailwind):**
   - Inspect `components.json` and `components/ui/`. Use stock primitives (`Button`, `Input`, `Select`, `Dialog`, `Sheet`, `Table`, `Card`, `Alert`, `Form`) with native `variant` and `size` props and semantic CSS variables (`bg-background`, `text-foreground`, `bg-primary`, `text-destructive`). Zero custom CSS overrides by default.
2. **Web — `Nuxt UI` (Vue 3 / Nuxt / Tailwind):**
   - Inspect `nuxt.config.ts` and `app.config.ts`. Use stock Nuxt UI components (`UButton`, `UInput`, `UForm`, `UFormField`, `USelect`, `UModal`, `USlideover`, `UTable`, `UCard`, `UAlert`) with semantic `color` and `variant` props.
3. **Mobile — `Apple HIG (iOS)` & `Google Material Design 3 (Android)`:**
   - Never apply web navigation or custom web dropdowns to mobile.
   - **Apple HIG:** Use native `NavigationStack`, `TabView`, `.insetGrouped` lists, `Sheet` detents, `Alert`/`ConfirmationDialog`, Dynamic Type, SF Symbols, `44x44pt` hit targets, and system semantic colors.
   - **Material 3:** Use native `Scaffold`, `TopAppBar`, `NavigationBar`, `FilledButton`, `OutlinedTextField`, `ModalBottomSheet`, `Snackbar`, `MaterialTheme.colorScheme`, and `48x48dp` touch targets.
4. **Custom UI Kit / Bespoke System:**
   - Lock a semantic token table and canonical component classes (`.btn-primary`, `.field`, `.card`, `.alert`) in Stage 6 **before** building screens, then reuse those exact classes everywhere without per-page overrides.

> **When is modification allowed?** Only when the user provides explicit feedback requesting a visual/behavioral modification, or when a task requirement cannot be met by any native component in the kit—and every exception must be justified in Section 5 of the handoff template.

---

## 4. Multi-Audience Handoff & Product Decision Changelog

All handoffs use [templates/handoff-and-changelog.md](../../templates/handoff-and-changelog.md), structured so four audiences can read the same source of truth:

- **Non-Product / Non-Engineers / Stakeholders:** Read **Section 1 (Executive Summary)** and **Section 7 (Product Decision Changelog)** to understand business impact, scope, and why decisions changed over time.
- **Product Designers & Researchers:** Read **Section 2 (IA Tree & Mermaid Flow)**, **Section 3 (7-State Logic Matrix)**, and **Section 4 (UI Copy Glossary)**.
- **Software Engineers:** Read **Section 3 (State Logic)**, **Section 5 (UI Kit Component Mapping Table)**, and **Section 6 (Acceptance Criteria)**.
- **AI Coding Agents:** Parse the machine-readable header (`<!-- pdi-handoff: ... -->`) plus Sections 3, 5, 6, and 7 to implement or update code deterministically without inventing components.
