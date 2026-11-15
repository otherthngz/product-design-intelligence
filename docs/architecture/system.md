# Architecture

A single host agent acts as coordinator. It reads `AGENTS.md`, classifies mode and complexity with `workflows/route-task.md`, loads relevant portable `.agents/skills/*/SKILL.md` instructions and optionally reads shared knowledge. It produces artifacts through host tools and reports against `workflows/output-contract.md`. The repository contains instructions, not a model, an automatic skill router, an orchestration runtime, or an independent tool layer.

| Location | Responsibility |
|---|---|
| `.agents/skills/` | Eight PDI skills (`ux-research`, `product-framing`, `interaction-design`, `ux-writing`, `design-system`, `ui-prototyping`, `ux-audit`, `design-handoff`) and one upstream `frontend-design` skill; metadata follows the [open specification](https://agentskills.io/specification). |
| `knowledge/` | Eleven curated topics across 5 domains (`product-design`, `ux-design`, `design-systems`, `ai-product-building`, `frontend-engineering`) and external standards links. |
| `workflows/` | Universal 8-stage product designer router (`route-task.md`) and multi-audience output contract (`output-contract.md`). |
| `templates/` | Project context (`project-context.md`), knowledge topic (`knowledge-topic.md`), and multi-audience handoff & decision changelog (`handoff-and-changelog.md`). |
| `adapters/` | Conceptual capability contract and implemented-path boundaries. |
| `examples/` | Local executable demos (`onboarding/`, `analytics-dashboard/`), audit scenarios, and evaluation artifacts. |
| `scripts/`, `tests/` | Multi-host installer (`install_pdi.py`), manifest builder (`build_manifest.py`), deterministic artifact auditor (`audit_artifact.py`), skill/knowledge validators, and unit tests. |
| `pdi-manifest.json`, `llms.txt`, `llms-full.txt` | Machine-readable skill/knowledge index and single-file universal LLM bundles. |
| `docs/` | Human and engineering guides, operating mode rules, and audit references. |
| `website/` | Separate Next.js documentation and registry site; excluded from the PDI npm package. |

The actual execution path is a host agent using local file tools, or a human running `python3 scripts/create_onboarding.py OUTPUT` to copy the example into a new file. No local script interprets natural language or invokes a model. Browser interaction is possible in a compatible host and was used to check the demo; browser automation is not bundled. Figma, MCP tools, repository inspection and TypeScript are host-dependent capabilities, not PDI integrations. See [adapter contract](../../adapters/README.md).

User-provided context is kept separate from shared knowledge: copy [the template](../../templates/project-context.md) into a project, provide real sources and policies, and point the agent at it. The agent should never promote assumptions into evidence. Enterprise governance and authorization remain organizational responsibilities; see [limitations](../reference/limitations.md).

For the static knowledge taxonomy, source review, topic metadata and validation, see [knowledge architecture](knowledge-architecture.md). The [practical audit](../reference/practical-audit.md) records observed capability boundaries.
