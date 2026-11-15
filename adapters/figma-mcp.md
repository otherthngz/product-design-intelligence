# Figma MCP: host integration guide

PDI's skills are portable instructions. A compatible host may provide Figma MCP tools; this repository does not implement its own Figma connector, authenticate users, or guarantee tool availability. The host's current Figma tool instructions and permissions control the actual workflow. A Figma file is an external artifact, not a local HTML prototype.

## Inputs and routing

For design creation or editing, use `product-framing` and `interaction-design` as needed, then `ui-prototyping` plus `frontend-design`. For design-to-code, add the host's Figma design-to-code guidance. Ask for an existing Figma file or node link when the user wants a specific destination; determine the requested page, screen and desired output (editable Design, Figma Code, or a local implementation). For an existing project, inspect its components, styles and variables before designing. Do not copy or replace a shared library without authorization.

## Host workflow

1. Discover the available Figma MCP tools and follow their prerequisite skills and current documentation. Connection, plan, file access and tool support vary by host. A user may need to connect Figma and grant access.
2. Open the supplied file and relevant node, inspect the existing design and design system, and establish the scope. Use applicable components and tokens. When the task requires a new file, follow the host's file-creation instructions and the user's requested destination.
3. Produce or update the requested artifact using the available tool. Native Design nodes, an imported live webpage, and a Code layer have different editability and behavior; verify the capabilities of the chosen path rather than promising equivalence. Keep author-facing notes and fake-data explanations out of the product UI unless essential for a consequential decision.
4. Inspect the returned file or node and render it with the available screenshot/inspection tool. Check the requested screens, content, visual hierarchy, components and relevant states. Report the actual file and node links, what was created, what is editable, and any missing components or unresolved decisions.
5. Put assumptions, simulated data, unfinished interactions and integration gaps in the handoff. A Figma screenshot or static frame does not prove keyboard, responsive, screen-reader, runtime or accessibility behavior. Validate executable behavior in a browser when a real implementation exists.

## Fallback

If the connector, file or write access is unavailable, explain the limitation and deliver an inspectable local prototype or design specification using available tools. Do not claim that a Figma file was created or that a design system was inspected. Follow the user's authorization and the host's rules for external, destructive or publishing actions.

## Current host observation

On 2026-11-14 this environment advertised Figma tools for reading design context, inspecting screenshots and libraries, writing Design nodes, importing a webpage into an existing file, and importing code into Figma Code. Availability does not establish access to a particular file or successful execution. No Figma file was opened or changed for this guide. These tool names are host-specific examples, not part of the portable PDI core.
