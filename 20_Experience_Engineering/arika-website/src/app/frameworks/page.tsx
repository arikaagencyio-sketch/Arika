import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Layout640 } from "@/components/sections/Layout640";
import { CardGrid } from "@/components/sections/CardGrid";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Frameworks & Methodology | Arika Agency",
  description: "How Arika Agency thinks: the 360° Growth Revenue Framework and the Ideal Ascension Model.",
};

export default function FrameworksPage() {
  return (
    <>
      <PageHeader
        tagline="Frameworks & Methodology"
        heading="How we think, not just what we sell"
        description="The 360° Growth Revenue Framework is how we architect Strategy, Marketing, Sales, Branding, and Automation as one connected system rather than isolated services."
      />

      <Layout640
        tagline="Entry Point"
        heading="Everything starts with the Revenue Infrastructure Audit"
        description="A fixed-fee, 7-14 day diagnostic across 7 sub-audits: funnel, sales, CRM, automation, acquisition, team, and offer. It's Arika's Gateway Offer — the real evidence base every recommendation is built on."
        buttons={[{ title: "See the Audit", variant: "secondary" }]}
        image={{ src: "/images/strategy-war-room.png", alt: "Strategy war room where the audit findings are mapped" }}
        subHeadings={[
          {
            title: "Modular by design",
            description: "Each sub-audit is itself a discrete, potentially standalone diagnostic.",
          },
          {
            title: "Ascension, not upsell",
            description: "Clients move to a larger build only where the audit shows it's warranted.",
          },
        ]}
      />

      <CardGrid
        heading="The Ideal Ascension Model"
        description="How engagements grow, stage by stage, once the audit identifies where to focus."
        columns={3}
        items={[
          {
            heading: "Stage 1 — Diagnose",
            description: "Revenue Infrastructure Audit: a fixed-fee, evidence-based starting point.",
          },
          {
            heading: "Stage 2 — Build",
            description: "A scoped infrastructure build against the specific outcome the audit surfaced.",
          },
          {
            heading: "Stage 3 — Operate",
            description: "Ongoing retainer or fractional leadership once the infrastructure is live.",
          },
        ]}
      />

      <Cta58
        headers={["Start with the", "Revenue Infrastructure Audit"]}
        description="See the framework in action against your own revenue systems."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
