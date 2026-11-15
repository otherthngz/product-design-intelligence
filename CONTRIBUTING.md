# Contributing to Product Design Intelligence (PDI)

Maintainer & Code Owner: **@otherthngz** (https://github.com/otherthngz)  
License: **[MIT License](LICENSE)**

---

## ⚠️ Mandatory Pre-Approval & Assignment Policy (Wajib Izin Terlebih Dahulu)

PDI is released under the **[MIT License](LICENSE)**—anyone is free to **use, install, fork, and adapt** these skills in their own projects.

However, to protect the quality, security, and architectural coherence of this upstream repository, **all contributions to this repository require prior permission or explicit issue assignment from `@otherthngz` before opening a Pull Request**:

1. **🇮🇩 Bahasa Indonesia:** Jangan langsung mengirim Pull Request (PR) tanpa izin. Buka Issue terlebih dahulu menggunakan template [Skill or Knowledge Proposal](.github/ISSUE_TEMPLATE/skill-or-knowledge-proposal.md), jelaskan alasan dan sumber buktinya, lalu tunggu sampai **@otherthngz** menyetujui dan melakukan **assign** Issue tersebut ke akun Anda (atau jika Anda memang sudah di-assign langsung oleh `@otherthngz`).
2. **🌐 English:** Do not submit unsolicited Pull Requests. Open an issue first using the [Skill or Knowledge Proposal template](.github/ISSUE_TEMPLATE/skill-or-knowledge-proposal.md) and wait until **@otherthngz** approves and explicitly **assigns** the issue to you. Unassigned PRs will be closed.

---

## 🛠️ Contribution Standards & Quality Gates

Once your issue is approved and assigned by `@otherthngz`, follow these engineering and design rules:

### 1. Skill Authoring (`.agents/skills/<name>/SKILL.md`)
- Must follow the [Agent Skills open specification](https://agentskills.io/specification).
- Frontmatter must contain `name` (matching the folder name in `kebab-case`) and a concise single-line `description` stating when to use and when **not** to use the skill.
- Every skill must include: `Purpose and use`, `Inputs`, `Relevant knowledge`, `Workflow`, `Artifacts`, `Quality`, `Failure modes`, `Tools and fallback`, and `Example`.
- Enforce PDI's core rules: **Problem Before Interface**, **Strict UI Kit Reuse** (`shadcn/ui`, `Nuxt UI`, `Apple HIG`, `Material 3`, or `Custom`), **Cross-Platform / HMI Awareness**, **Reject AI Slop**, and **Evidence Over Assumptions**.

### 2. Curated Knowledge (`knowledge/`)
- Copy [templates/knowledge-topic.md](templates/knowledge-topic.md) and include all 10 required headings (`What and why`, `When to apply`, `Fundamental principles`, `Practical implementation`, `Good and bad examples`, `Common mistakes`, `Evaluate the result`, `AI application`, `Related concepts`, `References and further learning`).
- Register the topic in [knowledge/taxonomy.yaml](knowledge/taxonomy.yaml), [knowledge/index.md](knowledge/index.md), and verify source provenance in [knowledge/sources.yaml](knowledge/sources.yaml).

### 3. Security & Honesty Rules
- Review [SECURITY.md](SECURITY.md): no secrets, no real PII, no executable code hidden in Markdown, and no prompt-injection patterns.
- Never fabricate user research, participant quotes, usability metrics, or accessibility compliance claims.

---

## ✅ Mandatory Local Checks Before Submitting a PR

Run all five commands from the repository root and confirm zero errors:

```bash
# 1. Validate all 9+ SKILL.md files and local links
python3 scripts/validate_skills.py

# 2. Validate knowledge taxonomy, sources, and 10-heading topic contracts
python3 scripts/validate_knowledge.py

# 3. Rebuild pdi-manifest.json, llms.txt, and llms-full.txt
python3 scripts/build_manifest.py

# 4. Run deterministic accessibility, UI anti-slop, and strict PII checks
python3 scripts/audit_artifact.py examples/onboarding/index.html --strict-pii
python3 scripts/audit_artifact.py examples/analytics-dashboard/index.html --strict-pii

# 5. Run the full unit & multi-host installer test suite
python3 -m unittest discover -s tests -v
```
