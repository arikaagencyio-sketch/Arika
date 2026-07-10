import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { CardGrid } from "@/components/sections/CardGrid";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "About | Arika Agency",
  description: "Arika Agency — a Revenue Infrastructure Partner for B2B SaaS.",
};

export default function AboutPage() {
  return (
    <>
      <PageHeader
        tagline="About"
        heading="A Revenue Infrastructure Partner, not another marketing retainer"
        description="Arika Agency exists to architect the systems that turn strategy, marketing, sales, branding, and automation into one connected revenue engine — built for B2B SaaS companies, operating in Kenya and serving clients globally."
      />

      <CardGrid
        heading="What we believe"
        columns={3}
        items={[
          {
            heading: "Diagnose before you prescribe",
            description: "Every engagement starts with a real audit, not an assumption.",
          },
          {
            heading: "Systems over silos",
            description: "Marketing, sales, branding, and automation should share one source of truth.",
          },
          {
            heading: "Evidence over opinion",
            description: "Recommendations are backed by the audit findings, not a generic playbook.",
          },
        ]}
      />

      <Cta58
        headers={["Want to work", "with us?"]}
        description="Start with the Revenue Infrastructure Audit — a real, fixed-fee diagnostic."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
