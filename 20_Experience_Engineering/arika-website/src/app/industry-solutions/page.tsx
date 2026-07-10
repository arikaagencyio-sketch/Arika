import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { CardGrid } from "@/components/sections/CardGrid";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Industry Solutions | Arika Agency",
  description: "Arika Agency works with B2B SaaS companies across three real ICP tiers.",
};

// NOTE: This page uses the recommended reframe flagged in
// `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md` §8 — organizing by
// real SaaS company stage/tier (confirmed ICP, `01_Sector/SECTOR_OS.md`)
// rather than the generic industry verticals (Healthcare/Finance/etc.) from
// the original pasted vision, which don't match Arika's actual B2B-SaaS-only
// ICP. This is the recommended approach, not yet a final owner sign-off —
// revisit if the owner prefers the generic-vertical framing instead.
export default function IndustrySolutionsPage() {
  return (
    <>
      <PageHeader
        tagline="Industry Solutions"
        heading="Built for B2B SaaS, organized by company stage"
        description="Arika's confirmed ICP is B2B SaaS only — so instead of generic industry verticals, we organize by the stage where your revenue systems actually need to change."
        buttons={[{ title: "Get My Free Assessment" }]}
      />

      <CardGrid
        heading="Three real tiers"
        description="Every engagement is scoped to the tier that matches your ARR and organizational complexity."
        columns={3}
        items={[
          {
            heading: "Tier 1 — Scale",
            description:
              "Series A-C, $5M-$50M ARR. Full Revenue Operating System build-outs across strategy, marketing, sales, branding, and automation.",
          },
          {
            heading: "Tier 2 — Growth",
            description:
              "Post-Seed to Series A, $1M-$10M ARR. Focused infrastructure builds on 1-2 outcomes at a time.",
          },
          {
            heading: "Tier 3 — Niche",
            description:
              "Multi-location or niche vertical SaaS. Scoped engagements around the specific system that's breaking down first.",
          },
        ]}
      />

      <Cta58
        headers={["Not sure which tier", "you fall into?"]}
        description="The Revenue Infrastructure Audit will tell you — and recommend the right scope."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
