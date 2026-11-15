# UI review: targeted checks

Use this reference for a screen or prototype. Scale the review to the task, and report actual observations, not assumed results.

## Before building

- Identify the intended user, primary task, content, constraints and existing visual system. For ambiguous details that do not block the work, state assumptions in the handoff.
- Choose a direction suited to the task: a dense operational screen needs clear scanning and aligned data; a marketing page may need stronger imagery or storytelling. Respect supplied brand rules.
- Use realistic task content. Avoid author-facing notes, generic marketing fillers and decorative labels in the UI. Keep simulated behavior and fictional data explicit in the handoff; show accurate in-context information when needed to avoid a consequential misunderstanding.

## Review the artifact

- **Task, context fit and hierarchy:** Can the target user (novice vs. expert) see the primary goal, current state and next action immediately? Does information density match task frequency and domain needs (e.g., dense aligned tables with `tabular-nums` for comparative expert tasks vs. guided progressive disclosure for infrequent novice setup)?
- **Anti-slop & necessity check:** Does every card, chart, container border, icon and step earn its place? Group fragmented settings cards into clean sections; replace multi-step modals on reversible actions with direct actions + Undo; remove charts that add no analytical value over direct tabular numbers; and reuse existing UI kit primitives instead of inventing one-off components.
- **Data consistency:** Compare summary totals, displayed rows, filters and periods. When only part of a list is shown, communicate the count shown and total (for example, “Showing 2 of 8 accounts”) and provide a way to see the rest if the task requires it. Do not make incomplete data appear complete.
- **Content & essential disclosures:** Remove “sample data”, “prototype only”, implementation notes, redundant helper text and generic marketing filler from the visible UI unless requested or essential for a consequential decision. **Preserve** all copy required for informed consent, legal/compliance accuracy, safety, accessibility, and error recovery. Retain accessible table names even if the visible title is sufficient.
- **Interaction and state:** Check the requested primary path plus relevant empty, loading, validation, failure, success, back and recovery states. Do not simulate a completed payment, saved data or external action as if it actually happened. Review all copy for unsupported promises about future actions, such as an email confirmation when no email can be sent; remove or accurately qualify those claims.
- **Visual discipline:** Review spacing, alignment, typography, contrast and consistency. Eliminate nested bordered containers, competing shadows/gradients, and multiple competing primary CTAs. Do not treat arbitrary minimalism, particular fonts, colors or asymmetry as inherently good or bad.
- **Accessibility and responsiveness:** Use meaningful structure and controls, labels and visible focus. Inspect keyboard access and reflow at relevant sizes where tools allow; do not claim WCAG conformance from these checks alone.
- **Validation:** Run `python3 scripts/audit_artifact.py` and exercise the actual interaction in a browser when available, recording results honestly. For Figma, inspect the resulting frame or screenshot and verify editable structure; a static design or screenshot does not prove interaction, responsive behavior or accessibility.

Report the artifact, design decisions, simulated elements, tests and remaining gaps separately from the product UI. If a tool is unavailable, name the gap rather than implying it was tested.
