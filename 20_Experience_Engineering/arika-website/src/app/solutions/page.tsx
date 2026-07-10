import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { CardGrid } from "@/components/sections/CardGrid";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Solutions | Arika Agency",
  description: "Outcome-led solutions for B2B SaaS revenue infrastructure.",
};

export default function SolutionsPage() {
  return (
    <>
      <PageHeader
        tagline="Solutions"
        heading="Businesses buy outcomes, not services"
        description="Every engagement is scoped against a real business outcome, then mapped back to the specific systems — strategy, marketing, sales, branding, or automation — that produce it."
        buttons={[{ title: "Get My Free Assessment" }]}
        image={{ src: "/images/solutions-outcome-room.png", alt: "Outcome-mapping strategy room with an abstract branching flow diagram" }}
      />

      <CardGrid
        heading="Choose the outcome you're solving for"
        description="Each of these maps to real department capabilities inside Arika's Revenue Operating System — not a generic service menu."
        columns={3}
        items={[
          {
            heading: "Increase Revenue",
            description: "Architect the revenue systems that compound, not just campaigns that spike.",
          },
          {
            heading: "Generate More Leads",
            description: "Demand generation built on real signal intelligence, not spray-and-pray.",
          },
          {
            heading: "Improve Conversion",
            description: "Funnel and CRM engineering that closes the gaps between stages.",
          },
          {
            heading: "Scale Operations",
            description: "Operational systems that hold up as headcount and deal volume grow.",
          },
          {
            heading: "Automate Processes",
            description: "Automation architecture that removes manual work without losing control.",
          },
          {
            heading: "Strengthen Brand",
            description: "Positioning and identity systems built to support premium pricing.",
          },
          {
            heading: "Increase Retention",
            description: "Client success systems that catch churn risk before it's a lost renewal.",
          },
          {
            heading: "Digital Transformation",
            description: "A connected revenue infrastructure spanning every department, not silos.",
          },
        ]}
      />

      <Cta58
        headers={["Not sure which outcome", "you need first?"]}
        description="Start with the Revenue Infrastructure Audit — it tells you exactly where to focus."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
