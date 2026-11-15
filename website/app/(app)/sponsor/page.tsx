import Link from "next/link";

import { Button } from "@/components/ui/button";
import { ROUTES } from "@/constants/routes";

export default function SponsorPage() {
  return (
    <section className="container-wrapper flex-1">
      <div className="container mx-auto max-w-4xl px-6 py-16 md:py-24">
        <h1 className="text-4xl font-semibold tracking-tight">Support PDI</h1>
        <p className="mt-4 max-w-xl leading-relaxed text-muted-foreground">Sponsorship details are not available yet.</p>
        <Button asChild variant="link" className="mt-5 px-0"><Link href={ROUTES.HOME}>Back to home</Link></Button>
      </div>
    </section>
  );
}
