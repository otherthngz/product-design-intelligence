# Development and skill authoring

1. Inspect relevant skills, router, knowledge and examples. Add only a distinct responsibility.
2. Create `.agents/skills/<lowercase-hyphen-name>/SKILL.md` with YAML frontmatter containing `name` matching the directory and a concise `description` stating when to use and not use it. Follow the [Agent Skills specification](https://agentskills.io/specification).
3. Give required and optional inputs, steps, expected artifacts, quality checks, failure modes, a concrete example, tool needs and a missing-tool fallback. Keep shared rules linked rather than copied into lengthy prompts. Add references inside the skill folder when supporting detail is necessary.
4. Update routing and evaluation cases. Keep project-specific policies out of portable defaults. Test realistic examples with an agent and review using the rubric; document host and evidence.
5. Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests -v`. Validate actual behavior in a browser or target host when relevant. Structural checks do not prove behavioral quality or complete YAML/spec compliance.

For the prototype, edit `examples/onboarding/index.html`, open it locally, test the main and error paths and record the result in its README. No build step or dependencies are required. Preserve the no-overwrite behavior of the copy script. See the [implementation plan](../superpowers/plans/2026-11-14-pdi-foundation.md) and [evaluation rubric](../../tests/evaluation-cases.md).

The bundled frontend-design skill is maintained upstream by Anthropic and includes its own license. See [the visual review](../reference/visual-design-review.md) for its pinned revision and integration. The local validator accepts the simple optional `license` field used by this skill; it is not a general YAML validator.

For visual work, the `ui-prototyping` skill asks agents to choose a direction appropriate to the product and review the rendered result where tools are available. Keep notes about example data and implementation in the handoff; provide user-facing explanations when needed for consequential decisions, and never show a simulated action as a real completion. Manual [copy and visual cases](../../tests/evaluation-cases.md) cover the intended behavior.
