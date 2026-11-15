import { ROUTES } from "@/constants/routes";

export const AGENT_DOCS_DIRECTIVE_TEXT =
  `For the documentation index, see llms.txt. Documentation pages are available as Markdown by appending .md or sending an Accept: text/markdown header. An agent skill is available at ${ROUTES.AGENT_SKILLS_SITE_SKILL}.` as const;

export const AGENT_DOCS_DIRECTIVE_MARKDOWN =
  `> For the documentation index, see [llms.txt](${ROUTES.LLMS}). Documentation pages are available as Markdown by appending \`.md\` or sending an \`Accept: text/markdown\` header. An agent skill is available at [${ROUTES.AGENT_SKILLS_SITE_SKILL}](${ROUTES.AGENT_SKILLS_SITE_SKILL}).` as const;
