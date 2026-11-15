import type { Metadata } from "next";
import Link from "next/link";

import { Button } from "@/components/ui/button";
import { ROUTES } from "@/constants/routes";
import { createPageMetadata } from "@/seo/metadata";

export const metadata: Metadata = createPageMetadata({
  title: "Changelog",
  description: "Updates to Product Design Intelligence.",
  path: ROUTES.CHANGELOG,
});

export default function ChangelogPage() {
  return (
    <section className="container-wrapper flex-1">
      <div className="container mx-auto max-w-4xl px-6 py-16 md:py-24">
        <h1 className="text-4xl font-semibold tracking-tight">Changelog</h1>
        <p className="mt-4 max-w-xl leading-relaxed text-muted-foreground">Updates to Product Design Intelligence.</p>

        <div className="mt-10 space-y-8 border-t border-border pt-8">
          <article>
            <div className="flex items-baseline justify-between gap-4">
              <h2 className="text-xl font-semibold">One-command install &amp; documentation overhaul</h2>
              <time className="text-sm text-muted-foreground">November 2026</time>
            </div>
            <ul className="mt-3 list-disc space-y-2 pl-5 text-muted-foreground">
              <li>Added one-command copy-paste installer on the homepage and installation guide supporting <code className="text-foreground">brew</code>, <code className="text-foreground">bun</code>, <code className="text-foreground">npm</code>, <code className="text-foreground">pnpm</code>, and <code className="text-foreground">yarn</code>.</li>
              <li>Consolidated Agent setup and Installer options into the Install PDI page.</li>
              <li>Expanded How it works, Your first task, Skills, and Working modes with role-based examples and clear activation guidance.</li>
              <li>Improved browser tab icon (favicon) contrast for both light and dark themes.</li>
              <li>Removed redundant Copy page and View markdown buttons from documentation pages.</li>
            </ul>
          </article>
        </div>

        <Button asChild variant="link" className="mt-8 px-0"><Link href={ROUTES.DOCS}>Explore the documentation</Link></Button>
      </div>
    </section>
  );
}
