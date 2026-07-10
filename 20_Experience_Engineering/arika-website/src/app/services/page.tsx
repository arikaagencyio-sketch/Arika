import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { CardGrid } from "@/components/sections/CardGrid";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Services | Arika Agency",
  description: "Arika Agency's real service lines, one per department capability.",
};

export default function ServicesPage() {
  return (
    <>
      <PageHeader
        tagline="Services"
        heading="Capabilities, not a menu of hours"
        description="Each service line below maps to a real, operating department inside Arika's own Revenue Operating System — the same system we build for clients."
        buttons={[{ title: "Book a Strategy Session" }]}
      />

      <CardGrid
        heading="Our service lines"
        description="Engagements are scoped by outcome (see Solutions) and delivered through these capabilities."
        columns={3}
        items={[
          { heading: "Strategy", description: "Revenue architecture and go-to-market design." },
          { heading: "Branding", description: "Identity, positioning, and narrative systems." },
          { heading: "Marketing", description: "Demand generation, SEO/AEO/GEO, and campaigns." },
          { heading: "Sales", description: "Pipeline, qualification, and outbound systems." },
          { heading: "Web & Experience", description: "Websites and interactive experiences built as real revenue infrastructure." },
          { heading: "Automation", description: "Workflow and engagement automation across the client lifecycle." },
          { heading: "Operations", description: "Delivery systems that hold up under scale." },
          { heading: "Analytics", description: "Measurement built on real KPIs, not vanity metrics." },
          { heading: "AI Systems", description: "AI-assisted agents and workflows wired into real operations." },
          { heading: "Consulting & Advisory", description: "Senior-level guidance for complex revenue decisions." },
        ]}
      />

      <Cta58
        headers={["Start with the", "Revenue Infrastructure Audit"]}
        description="See which service lines matter most for your business before committing to any of them."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
