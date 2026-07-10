"use client";

import * as CheckboxPrimitive from "@radix-ui/react-checkbox";
import { Check } from "relume-icons";

import { cn } from "@/lib/utils";

function Checkbox({ className, ...props }: React.ComponentProps<typeof CheckboxPrimitive.Root>) {
  return (
    <CheckboxPrimitive.Root
      data-slot="checkbox"
      className={cn(
        "size-[1.125rem] rounded-checkbox transition-all duration-200 focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50",
        "border border-scheme-border data-[state=checked]:bg-neutral-darkest data-[state=checked]:text-white",
        className,
      )}
      {...props}
    >
      <CheckboxPrimitive.Indicator
        data-slot="checkbox-indicator"
        className="flex items-center justify-center text-current transition-none"
      >
        <Check className="size-4" />
      </CheckboxPrimitive.Indicator>
    </CheckboxPrimitive.Root>
  );
}

export { Checkbox };
