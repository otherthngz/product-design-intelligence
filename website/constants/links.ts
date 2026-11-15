export const GITHUB = {
  branch: "main",
  org: "otherthngz",
  repo: "pdi",
  user: "otherthngz",
} as const;

const githubUrl = `https://github.com/${GITHUB.org}/${GITHUB.repo}`;

export const LINK = {
  DISCORD: githubUrl,
  GITHUB: githubUrl,
  LICENSE: `${githubUrl}/blob/${GITHUB.branch}/LICENSE`,
  PORTFOLIO: "https://github.com/otherthngz",
  SHADCN_MCP_DOCS: "https://agentskills.io/specification",
  SPONSOR: `https://github.com/sponsors/${GITHUB.user}`,
  X: "https://github.com/otherthngz",
  X_SHADCN_LABS: "https://github.com/otherthngz",
} as const;
