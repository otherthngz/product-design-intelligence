"use client";

import { CopyButton } from "@/components/copy-button";
import { Button } from "@/components/ui/button";

export const DocsCopyPage = ({ markdownUrl }: { markdownUrl: string }) => (
  <div className="flex items-center gap-1">
    <CopyButton
      value={async () => {
        const response = await fetch(markdownUrl);
        if (!response.ok) throw new Error("Could not load this page as Markdown.");
        return response.text();
      }}
      showTooltip={false}
      variant="secondary"
    >
      Copy page
    </CopyButton>
    <Button asChild variant="ghost" size="sm">
      <a href={markdownUrl}>View Markdown</a>
    </Button>
  </div>
);
