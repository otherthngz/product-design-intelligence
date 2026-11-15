# Product Design Intelligence (PDI)

**Status: Supervised Public Beta (`v1.0.0`).** PDI is a collection of skills, guidance, and examples that help AI coding agents work through product design problems. It encourages an agent to understand the user and the task, examine evidence and assumptions, and choose an appropriate solution before designing an interface.

PDI is guidance for an AI assistant, not an AI model, automated design-assurance tool, or replacement for human design review. Output quality depends on the context you provide, your host agent's capabilities, and human judgment before shipping.

## What's included

- Nine [design skills](.agents/skills/) covering research, product framing, interaction design, UX writing, design systems, prototyping, visual design, audits, and handoff.
- A [knowledge library](knowledge/index.md) with 11 practical design and frontend references.
- A [task router](workflows/route-task.md) and [output contract](workflows/output-contract.md) that help an agent choose skills and structure evidence-linked critique.
- [Examples](examples/) and scripts for installing (`scripts/install_pdi.py`, `bin/pdi.js`), auditing (`scripts/audit_artifact.py`), and validating the package.

The repository also contains a separate documentation website in `website/`. It is not part of the skill installation or npm package.

## Quickstart

### 1. Install into a project

Using Python 3 from this repository (or `npx pdi-skills@beta`, pending npm publication):

```bash
python3 scripts/install_pdi.py /path/to/your-project --hosts agents --mode solo --standalone-skills
# once published to npm beta:
npx pdi-skills@beta /path/to/your-project --hosts agents --mode solo --standalone-skills
```

- **Hosts (`--hosts`):** `agents` (`AGENTS.md` + `.agents/skills/`, compatible with Codex and AGENTS.md-aware tools), `claude`, `cursor`, `windsurf`, `copilot`, or `all`. Packaging and clean installation are verified for all 5 hosts; live behavioral evaluation has only been run on Codex CLI (`0.167.0`).
- **Modes (`--mode`):** `solo` (default), `team`, or `enterprise`.
- **Overwrite safety:** The installer skips existing files by default. Use `--append` to append to supported existing host files, or `--force` only after reviewing what may be overwritten.

### 2. Verify installation and run static checks

```bash
npm run pdi:validate
npm run pdi:test
python3 scripts/audit_artifact.py /path/to/artifact.html
```

### 3. Run a representative design task

Ask your assistant for a concrete task and link the relevant artifact:

> Review `examples/analytics-dashboard/index.html` using the repository's UX audit workflow. Cite observed evidence, distinguish assumptions from facts, and recommend the smallest effective fix.

If your assistant does not auto-discover project skills, ask it to read `AGENTS.md`, `workflows/route-task.md`, and the relevant `.agents/skills/<name>/SKILL.md`. See [Using PDI](docs/getting-started/using-pdi.md) for more examples and troubleshooting.

## Known limitations (Public Beta)

- **Design judgment:** PDI provides decision support, not guaranteed Staff/Principal-level design correctness; human review is required for consequential design recommendations.
- **Unresolved P0.2 severity gate:** Controlled severity-calibration scenarios A–C in [`tests/evaluation-cases.md`](tests/evaluation-cases.md) remain blocked by external Codex CLI quota exhaustion; severity classifications are heuristic, context-dependent, and require human review.
- **No automated accessibility or browser guarantee:** `scripts/audit_artifact.py` and browser checks do not establish complete WCAG conformance, contrast, or screen-reader compatibility.
- **Agent compatibility:** Packaging and installation were tested across all 5 supported hosts, but live behavioral evaluation has only been run on Codex CLI (`0.167.0`); equivalent reliability across other hosts is unverified.
- **No real-user validation:** Product design recommendations have not been validated through real-user usability studies.

See [Limitations and next steps](docs/reference/limitations.md) for full details.

## Preview the website

From the root of this repository, install the website dependencies and start the development server:

```bash
cd website
pnpm install
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000). The terminal will show the address if another port is used. Press `Ctrl+C` to stop the server. The site uses Next.js and requires Node.js and pnpm; Python 3 is needed for the PDI scripts, not for browsing the site.

For a production deployment outside Vercel, set `SITE_URL` to the public website URL so metadata and sharing links use the correct address.

The website's documentation lives in `website/content/docs/`. This README is the repository's landing page on GitHub and is edited separately in `README.md`.

## Repository structure and publishing

- `.agents/skills/`, `knowledge/`, `workflows/`, `adapters/`, and `templates/` are the PDI material used by agents.
- `scripts/` and `bin/` contain the installer and supporting tools. `docs/` and `examples/` provide reference material.
- `website/` is a private Next.js project for browsing documentation. It can be deployed separately and is excluded from the npm package.
- `tests/`, `.github/`, and `packaging/` support development and distribution. Local dependencies, build output, environment files, and editor settings are not part of the published npm package.

The root `package.json` lists the files included when packaging PDI for npm. Run `npm pack --dry-run --ignore-scripts` to inspect the package before publishing. No package or website is published automatically.

## Checks

To validate the skills and knowledge, then run the PDI tests:

```bash
python3 scripts/validate_skills.py
python3 scripts/validate_knowledge.py
python3 -m unittest discover -s tests -v
```

With the website development server running, `pnpm --dir website test:smoke` checks the main pages, installation guide, and agent discovery endpoints.

The [documentation index](docs/README.md) has more details on the architecture, examples, and limitations.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution policy and [SECURITY.md](SECURITY.md) for security reporting. PDI is available under the [MIT License](LICENSE).
