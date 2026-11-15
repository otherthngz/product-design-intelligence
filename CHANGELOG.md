# Changelog

## 1.0.0 — Supervised Public Beta (2026-11-15)

### Added
- Single-coordinator architecture (`AGENTS.md`), task router (`workflows/route-task.md`), and evidence-linked output contract (`workflows/output-contract.md`).
- Nine modular design skills under `.agents/skills/`: `product-framing`, `ux-research`, `interaction-design`, `ux-writing`, `design-system`, `ui-prototyping`, `frontend-design`, `ux-audit`, and `design-handoff`.
- Eleven curated knowledge topics under `knowledge/` with schema and link validation (`scripts/validate_knowledge.py`).
- Multi-host installer (`scripts/install_pdi.py`) and zero-dependency Node CLI wrapper (`bin/pdi.js`) supporting `agents`, `claude`, `cursor`, `windsurf`, and `copilot`.
- Static HTML/Markdown artifact auditor (`scripts/audit_artifact.py`) with PII/secret scanning (`--strict-pii`), heading/label/focus checks, and anti-slop review signals (updated to recognize fluid CSS `clamp()`/`minmax()` layouts without false-positive `@media` warnings).
- Automated validation and regression suite (`npm run pdi:validate`, `npm run pdi:test`) covering skill contracts, knowledge integrity, prototype state logic, and multi-host npm tarball installation.

### Known Limitations
- Controlled P0.2 severity-calibration scenarios A–C (`tests/evaluation-cases.md`) remain blocked by external Codex CLI quota exhaustion.
- Live behavioral verification has only been conducted on Codex CLI (`0.167.0`); cross-model behavioral reliability across Claude Code, Cursor, Windsurf, and Copilot is unverified.
- Static checks do not establish rendered visual quality, screen-reader behavior, WCAG conformance, or real-user task effectiveness; human review is required before shipping.
