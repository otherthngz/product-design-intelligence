# Using PDI

PDI is a set of instructions and examples for an AI assistant with access to your work. It helps the assistant think through product decisions and make tangible outputs. You remain responsible for judging the result and deciding what to ship.

## Set up

Download or copy this repository to your computer and open its folder in an agent that can read files. Python 3 is only needed for the example-copy script and checks; a modern browser is needed to use the demo. PDI needs no API credentials of its own, though your chosen assistant may have its own requirements. If your assistant does not discover project skills, ask it to read `AGENTS.md`, `workflows/route-task.md`, and the appropriate `.agents/skills/<name>/SKILL.md` directly. Restart or reload your host if its documentation requires that for skill discovery.

## Make a request

Say what you want, who it serves, the current situation, constraints, and what you want returned. Link the relevant files or give the agent permission to inspect them. For example:

> Review `checkout.png` for a first-time customer on mobile. Identify the three biggest usability risks, explain the evidence, and suggest changes. We cannot change the payment provider.

> Create a local HTML onboarding prototype for a task-planning app. Users should name a workspace and choose a goal. Keep it usable on a phone and include the flow and handoff.

Expect a concise answer for a quick critique, and linked files, decisions, states and validation for bigger work. Ask for revisions. Check whether the agent distinguishes things you supplied, things it observed, and things it assumed. Ask which devices, interactions and accessibility checks were actually tested.

## Modes and complexity

Solo is lightweight; team adds shared context, owners and review; enterprise adds organizational rules and approval checkpoints. These are working conventions rather than access controls. Quick, standard and complex describe the size and risk of the task separately: a solo project can be complex and an enterprise critique can be quick. See [routing](../../workflows/route-task.md).

## Troubleshooting

- **The agent does not find a skill:** give the `SKILL.md` path and check your host's project-skill discovery settings.
- **Python command fails:** run it from the repository root with `python3`; ensure the destination's parent folder exists and the destination is new.
- **The page does not advance:** enable JavaScript in a modern browser; check that a workspace name and a goal are selected.
- **A requested tool is missing:** ask for a file-based alternative, and check the reported limitations. PDI cannot install or operate an integration on its own.

See the [glossary](../concepts/glossary.md) and [limitations](../reference/limitations.md).
