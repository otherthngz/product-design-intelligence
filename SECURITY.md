# Security Policy

Maintainer: **@otherthngz** (https://github.com/otherthngz)

---

## 1. Local-First & Privacy-Respecting Design

**Product Design Intelligence (PDI)** is a local-first collection of Markdown agent skills, JSON-compatible YAML knowledge catalogs, HTML/CSS/JS reference prototypes, and standard-library Python utilities:
- **Zero Telemetry:** PDI contains no analytics, tracking pixels, external network calls, or mandatory cloud accounts.
- **Zero External Runtime Dependencies:** All installation, validation, and artifact-auditing scripts (`scripts/install_pdi.py`, `scripts/validate_skills.py`, `scripts/validate_knowledge.py`, `scripts/audit_artifact.py`, `scripts/build_manifest.py`) use Python 3's standard library only.

---

## 2. Security Rules for Contributors & Maintainers

Following the security standards of leading agent repositories (and enforced in CI via `.github/workflows/validate.yml`):

1. **No Secrets, Credentials, or Real PII:**
   - Never commit API keys (`sk-...`, `ghp_...`, `AIza...`), tokens, passwords, internal URLs, or unredacted customer/participant emails into `.agents/skills/`, `knowledge/`, `examples/`, or `tests/`.
   - Always run `python3 scripts/audit_artifact.py <path> --strict-pii` before committing new examples, transcripts, or handoff artifacts.
2. **No Hidden Executable Payloads in Markdown (`SKILL.md` / `knowledge/`):**
   - Skill and knowledge Markdown files are read directly by AI coding agents with file and shell access.
   - Never embed obfuscated text, hidden HTML comments containing shell commands, base64 payloads, or instructions that bypass host permissions.
3. **Prompt Injection & Untrusted Content Defense:**
   - All PDI skills explicitly instruct the host agent to treat external source material, fetched web pages, user transcripts, and third-party files as **untrusted data, never executable instructions**.
   - Any PR introducing patterns that weaken permission checks, suppress user approval for destructive actions, or encourage fabricated compliance claims will be rejected immediately.
4. **Script & Installer Safety:**
   - All scripts under `scripts/` must remain zero-dependency, deterministic, and non-destructive by default (`install_pdi.py` and `create_onboarding.py` refuse to overwrite existing files unless `--force` is explicitly passed by the user).

---

## 3. Reporting a Vulnerability

If you discover a security issue, prompt-injection vector, or unintended data exposure in PDI:

- **Do NOT open a public GitHub issue** if the report contains an active exploit or sensitive data.
- Use GitHub's **Private Vulnerability Reporting** tab on this repository (`Security` → `Report a vulnerability`) to notify **@otherthngz** privately.
- Include the affected file path, reproduction steps, and potential impact on host AI agents.
