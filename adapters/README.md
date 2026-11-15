# Execution capability contract

This is a tool-independent contract for a coordinating agent, not an implemented adapter API. A host maps each operation to its own tools, checks permissions, reports errors and never claims success without checking the result.

| Capability | Input → expected result | v0 status and fallback |
|---|---|---|
| Read/inspect | path or repository → content and source location | Host-provided. Ask for supplied material if unavailable. |
| Create/edit | authorized path and content → actual file and outcome | Host-provided. Without write access return copyable content and say no file was created. |
| Run validation | command and working directory → exit status and output | Host-provided. Python checks are supplied; otherwise list checks not run. |
| Browser | local URL and viewport → observed state/interaction | Host-dependent; if unavailable use static checks and mark behavior unverified. |
| Design tool / MCP | configured tool and authorized target → observed changes or evidence | Conceptual only. Use a local artifact or specification; do not claim external edits. |

The included `scripts/create_onboarding.py OUTPUT` is the one implemented local execution utility: it reads the checked-in HTML and creates a byte-identical new file using exclusive creation. It requires Python 3 and an existing destination directory; it refuses overwrite and does not call an AI service. HTML/CSS/JavaScript prototype editing is possible with host file tools; TypeScript support requires host tooling and is not provided here. Obtain explicit approval for destructive, irreversible, external publishing, or production-impacting actions; respect the host's stricter rules.

For hosts that provide Figma MCP, see the [Figma MCP guide](figma-mcp.md) for inputs, execution, review and fallback. The guide is not an implemented connector.
