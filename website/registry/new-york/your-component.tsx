import type { HTMLAttributes } from "react";
import { forwardRef } from "react";

import { cn } from "@/lib/utils";

export type YourComponentProps = HTMLAttributes<HTMLDivElement>;

const YourComponent = forwardRef<HTMLDivElement, YourComponentProps>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        "p-5 rounded-md text-left bg-muted/20 space-y-2.5 border border-muted flex flex-col justify-center",
        className
      )}
      {...props}
    >
      <p className="text-sm font-medium text-foreground">
        9 Specialist Agent Skills · 11 Curated Knowledge Topics · 13 Design Quality Gates
      </p>
      <p className="text-muted-foreground text-xs leading-relaxed">
        Works across{" "}
        <code className="bg-muted rounded px-1.5 py-0.5 text-xs">
          Antigravity
        </code>{" "}
        <code className="bg-muted rounded px-1.5 py-0.5 text-xs">
          Claude Code
        </code>{" "}
        <code className="bg-muted rounded px-1.5 py-0.5 text-xs">
          Cursor
        </code>{" "}
        <code className="bg-muted rounded px-1.5 py-0.5 text-xs">
          Windsurf
        </code>{" "}
        <code className="bg-muted rounded px-1.5 py-0.5 text-xs">
          Copilot
        </code>
      </p>
    </div>
  )
);

YourComponent.displayName = "YourComponent";

export { YourComponent };
