# PDI knowledge foundation implementation plan

**Goal:** Add five traceable, practical knowledge topics and apply them in an interactive local dashboard.
**Architecture:** Static topic index and JSON-compatible YAML metadata link portable skills to original Markdown. A standard-library validator checks local contracts without network or a retrieval service. The host agent chooses and applies relevant topics.
**Stack:** Markdown, JSON-compatible YAML, Python 3 standard library, standalone HTML/CSS/JavaScript.
**Constraints:** Preserve existing skills and execution architecture; no paid APIs, new dependencies, invented evidence or external publishing. Topic depth is separate from task complexity and operating mode. References are not executable instructions.

1. Add failing tests for validator success and invalid topic metadata, missing sources and broken references; implement the validator and run the checks.
2. Document source provenance, taxonomy, template and one complete topic per domain; connect all five skills through static references.
3. Build an accessible-minded responsive dashboard with fictional data and functioning filters; record knowledge-driven decisions and limitations.
4. Add human and engineering guidance, retrieval cases and update workflow. Run all tests and validate browser behavior and responsive layout when possible.
