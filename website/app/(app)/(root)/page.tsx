import Link from "next/link";

import { CodeBlockCommand } from "@/components/code-block-command";
import { Button } from "@/components/ui/button";
import { ROUTES } from "@/constants/routes";
import { BreadcrumbJsonLd } from "@/seo/json-ld";

export const dynamic = "force-static";
export const revalidate = false;

export default function IndexPage() {
  return (
    <>
      <BreadcrumbJsonLd items={[{ name: "Home", path: ROUTES.HOME }]} />
      <section className="container-wrapper">
        <div className="container mx-auto max-w-4xl px-6 py-20 md:py-28">
          <p className="mb-6 text-sm font-medium text-muted-foreground">Product Design Intelligence</p>
          <h1 className="max-w-3xl text-4xl font-semibold tracking-tight sm:text-5xl md:text-6xl">
            Give your AI assistant a better way to approach product design.
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-relaxed text-muted-foreground sm:text-xl">
            PDI provides practical guidance for research, design decisions, prototypes, and reviews.
          </p>
          <div className="mt-8 max-w-xl space-y-4">
            <CodeBlockCommand
              __brew__="brew install otherthngz/tap/pdi"
              __bun__="bunx pdi-skills"
              __npm__="npx pdi-skills"
              __pnpm__="pnpm dlx pdi-skills"
              __yarn__="yarn dlx pdi-skills"
              className="border border-border"
            />
            <div className="flex flex-wrap items-center gap-3">
              <Button asChild variant="outline" size="lg"><Link href={ROUTES.HOW_IT_WORKS}>How it works</Link></Button>
              <Button asChild variant="ghost" size="lg"><Link href={ROUTES.DOCS_INSTALLATION}>Installation guide</Link></Button>
            </div>
          </div>
        </div>
      </section>
      <section id="how-it-works" className="container-wrapper scroll-mt-20 border-t border-border">
        <div className="container mx-auto grid max-w-4xl gap-8 px-6 py-16 md:grid-cols-[1fr_1.5fr] md:gap-16 md:py-20">
          <div>
            <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl">How it works</h2>
            <p className="mt-4 leading-relaxed text-muted-foreground">Give your assistant context, then review its work with a clearer process.</p>
          </div>
          <ol className="space-y-8">
            <li>
              <h3 className="font-medium">1. Add PDI to your project</h3>
              <p className="mt-2 leading-relaxed text-muted-foreground">
                Run one command above to add <code className="text-foreground">.agents/skills/</code> and host instructions (<code className="text-foreground">AGENTS.md</code>, <code className="text-foreground">CLAUDE.md</code>, or <code className="text-foreground">.cursor/rules/</code>) to your repo. No runtime dependencies are added.
              </p>
            </li>
            <li>
              <h3 className="font-medium">2. Describe your task</h3>
              <p className="mt-2 leading-relaxed text-muted-foreground">
                Share who it is for, the problem, and any constraints, whether you are a product manager framing a feature, an engineer building UI, or a non-technical founder reviewing a flow.
              </p>
            </li>
            <li>
              <h3 className="font-medium">3. Review and ship</h3>
              <p className="mt-2 leading-relaxed text-muted-foreground">
                Your AI assistant reads the relevant PDI skill, surfaces assumptions and trade-offs, and proposes the smallest effective change. You decide what to keep and what to ship.
              </p>
            </li>
          </ol>
        </div>
      </section>
      <section className="container-wrapper border-t border-border">
        <div className="container mx-auto max-w-4xl px-6 py-16 md:py-20">
          <h2 className="text-2xl font-semibold tracking-tight">Start with a real task</h2>
          <blockquote className="mt-6 max-w-2xl border-l-2 border-border pl-5 text-lg leading-relaxed text-muted-foreground">
            Review our onboarding flow for first-time users. Identify the main usability issues and suggest the smallest changes that would help.
          </blockquote>
          <Button asChild variant="link" className="mt-5 px-0"><Link href="/docs/first-task">See how to use PDI</Link></Button>
        </div>
      </section>
    </>
  );
}
