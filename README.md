# Product Design Intelligence (PDI)

**Supervised Public Beta (`v1.0.0`)**

PDI adds nine product design skills and curated UX/UI references to your AI coding assistant. Instead of jumping straight into generic UI code, your assistant is guided to understand the user's task, separate facts from assumptions, avoid bloated "AI slop" patterns, and make scoped, maintainable interface decisions.

> PDI is guidance for your AI assistant, not a replacement for human design review or accessibility testing.

---

## Install the skills

### From GitHub (available now, requires Python 3)

```bash
git clone https://github.com/otherthngz/product-design-intelligence.git
python3 product-design-intelligence/scripts/install_pdi.py /path/to/your-project --hosts agents --mode solo --standalone-skills
```

### Via npm

```bash
npx pdi-skills@beta /path/to/your-project --hosts agents --mode solo --standalone-skills
```

### Choose your AI assistant (`--hosts`)

| Assistant | `--hosts` value | Files added to your project |
| --- | --- | --- |
| Codex / `AGENTS.md`-compatible agents | `agents` | `AGENTS.md` and `.agents/skills/` |
| Claude Code | `claude` | `CLAUDE.md` and `.claude/skills/` |
| Cursor | `cursor` | `.cursor/rules/pdi-*.mdc` |
| Windsurf | `windsurf` | `.windsurfrules` |
| GitHub Copilot | `copilot` | `.github/copilot-instructions.md` |
| All of the above | `all` | All host files above |

- **Modes (`--mode`):** `solo` (default), `team`, or `enterprise`.
- **Safe by default:** Existing files are skipped unless you pass `--append` (add to existing instructions) or `--force` (overwrite).

---

## Use PDI in your project

Once installed, ask your assistant to work on a real screen, flow, or spec in your project:

> Review `src/components/SettingsForm.tsx` for usability and accessibility issues. Cite what you observe in the code, separate assumptions from facts, and suggest the smallest fix.

> Design and build a 2-step onboarding flow using our existing UI components. Include empty, validation-error, loading, and success states.

If your assistant does not automatically pick up the skills, tell it to read `AGENTS.md` (or your host's instruction file) and the relevant `.agents/skills/<skill-name>/SKILL.md`.

---

## Included skills

- **`product-framing`** — Frame user problems, goals, constraints, and success criteria before designing.
- **`ux-research`** — Plan discovery and synthesize supplied research notes without inventing evidence.
- **`interaction-design`** — Define user flows, navigation, state logic, and error recovery.
- **`ux-writing`** — Write clear interface copy, labels, empty states, and recovery messages.
- **`design-system`** — Reuse and standardize tokens, UI kits (`shadcn/ui`, `Nuxt UI`, Material 3, Apple HIG), and component APIs.
- **`ui-prototyping`** — Build or refine scoped, multi-state UI implementations using your existing UI kit.
- **`frontend-design`** — Establish intentional visual direction, typography, and hierarchy for custom UI.
- **`ux-audit`** — Critique existing interfaces with evidence-linked severity (`Critical`, `Major`, `Minor`, `Opportunity`).
- **`design-handoff`** — Produce clear engineering handoffs and decision changelogs.

---

## Beta limitations to keep in mind

- **Human review required:** PDI provides decision support, not guaranteed Staff/Principal-level design correctness.
- **Severity calibration (`P0.2`):** Controlled severity-calibration scenarios A–C remain unexecuted; severity labels are heuristic and should be reviewed by a human.
- **Accessibility:** PDI checks do not guarantee WCAG 2.2 conformance or screen-reader compatibility—verify with real assistive technology.
- **Host compatibility & user testing:** Installation is verified across all 5 hosts above, while live behavioral testing has only been run on Codex CLI (`0.167.0`), and no real-user usability study has been conducted.

---

## More information

- [Using PDI](docs/getting-started/using-pdi.md) · [Limitations](docs/reference/limitations.md) · [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [MIT License](LICENSE)
