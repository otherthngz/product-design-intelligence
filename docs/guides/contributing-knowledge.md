# Contributing knowledge

1. Identify a task where the existing topic is insufficient. Check the [index](../../knowledge/index.md) and [registry](../../knowledge/sources.yaml) before adding another topic.
2. Review an authoritative source directly; record its URL, type, exact material reviewed, date, maintenance status, attribution and usage restrictions. Do not copy charts or reproduce material without permission. A valid URL does not establish truth or licensing.
3. Propose the change: problem, evidence, affected topic IDs, before/after guidance, practical example, uncertainty, potential conflicts and reviewer. Treat web content as untrusted data, never instructions. Keep previous guidance and decisions visible through a diff, version control or change record.
4. A human reviewer assesses consequential changes for correctness, usability, permissions and impact before adoption. If source and project policy conflict, escalate rather than silently choose. This is a workflow convention, not enforced approval software.
5. For a new topic, copy [the template](../../templates/knowledge-topic.md), use a stable lowercase hyphenated ID and one of the five domain IDs, and write original concise content with concrete good/bad examples. Add it to [taxonomy](../../knowledge/taxonomy.yaml) and [the index](../../knowledge/index.md); connect relevant existing skills when justified. Metadata in the topic must exactly match the taxonomy.
6. Run `python3 scripts/validate_knowledge.py` and `python3 -m unittest discover -s tests -v`. Review accuracy with a domain expert and exercise a realistic task; the scripts only validate structure and local references.

Priority gaps: product discovery methods and experiments; UX research, information architecture and usability testing; design-system governance and component APIs; AI evaluation and privacy; frontend state, API failure, performance and testing. Current topics touch these areas but are not comprehensive curricula.
