import { createHash } from "node:crypto";

import { LINK } from "@/constants/links";
import { ROUTES } from "@/constants/routes";
import { SITE } from "@/constants/site";

export const SITE_AGENT_SKILL_MD = `---
name: pdi
description: Product Design Intelligence (PDI) — Principal Product Designer skills, knowledge base, and multi-host installer for AI coding agents.
---

# ${SITE.NAME} — Product Design Intelligence

## Summary

PDI provides guidance for product research, design decisions, prototypes, and reviews. Agent capabilities and skill discovery depend on the host.

## Discovery & Resources

- Website documentation bundle: \`${ROUTES.LLMS_FULL}\`
- LLM Index: \`${ROUTES.LLMS}\`
- Documentation: ${ROUTES.DOCS}
- Agent Skills Spec: ${LINK.SHADCN_MCP_DOCS}

## Quick Install

Public installation is not available yet. If you already have a copy of PDI, follow the installation guide: ${ROUTES.DOCS_INSTALLATION}
`;

export const siteAgentSkillDigest = (): string => {
  const hex = createHash("sha256")
    .update(SITE_AGENT_SKILL_MD, "utf-8")
    .digest("hex");

  return `sha256:${hex}`;
};
