import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { CardGrid } from "@/components/sections/CardGrid";
import { Contact3 } from "@/components/sections/Contact3";

export const metadata: Metadata = {
  title: "Proposal Center | Arika Agency",
  description: "Request a proposal from Arika Agency.",
};

export default function ProposalCenterPage() {
  return (
    <>
      <PageHeader
        tagline="Proposal Center"
        heading="Request a real, scoped proposal"
        description="Tell us about your project and we'll come back with a proposal scoped to your actual budget, timeline, and business questionnaire — not a generic rate card."
      />

      <CardGrid
        heading="What we ask for"
        columns={3}
        items={[
          {
            heading: "Business questionnaire",
            description: "A short set of questions about your current revenue systems and goals.",
          },
          {
            heading: "Project scope",
            description: "What you're trying to solve, and any constraints we should know about.",
          },
          {
            heading: "Budget & timeline",
            description: "Your real range and timeline so the proposal is realistic, not aspirational.",
          },
        ]}
      />

      <Contact3
        tagline="Request a Proposal"
        heading="Submit your project details"
        description="Prefer to upload a brief or supporting documents? Mention it in your message and we'll send a secure upload link."
        button={{ title: "Request Proposal" }}
      />
    </>
  );
}
