export const FALLBACK_SITE_ORIGIN = "http://localhost:3000" as const;

const getBaseUrl = () => {
  if (process.env.NODE_ENV !== "production") {
    return "http://localhost:3000";
  }

  if (process.env.SITE_URL) return process.env.SITE_URL;

  if (process.env.VERCEL_PROJECT_PRODUCTION_URL) {
    return `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`;
  }

  if (process.env.VERCEL_URL) return `https://${process.env.VERCEL_URL}`;

  return FALLBACK_SITE_ORIGIN;
};

const baseUrl = getBaseUrl();

export const SITE = {
  AUTHOR: {
    NAME: "otherthngz",
    TWITTER: "@otherthngz",
  },
  DESCRIPTION: {
    LONG: "PDI provides practical guidance for research, design decisions, prototypes, and reviews.",
    SHORT: "Product design guidance for AI assistants",
  },
  KEYWORDS: [
    "agent-skills",
    "product-design",
    "ux-design",
    "design-systems",
    "shadcn",
    "nuxt-ui",
    "claude-code",
    "cursor",
    "windsurf",
    "copilot",
    "antigravity",
  ] as const,
  NAME: "pdi",
  OG_IMAGE: `${baseUrl}/og`,
  REGISTRY: baseUrl,
  URL: baseUrl,
};

export const META_THEME_COLORS = {
  dark: "#09090b",
  light: "#ffffff",
};

export const UTM_PARAMS = {
  utm_source: new URL(baseUrl).hostname,
};
