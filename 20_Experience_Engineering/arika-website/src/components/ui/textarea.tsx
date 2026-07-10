import { cn } from "@/lib/utils";

function Textarea({ className, ...props }: React.ComponentProps<"textarea">) {
  return (
    <textarea
      data-slot="textarea"
      className={cn(
        "flex w-full rounded-form focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50",
        "border border-scheme-border bg-scheme-background",
        "min-h-11 p-3",
        className,
      )}
      {...props}
    />
  );
}

export { Textarea };
