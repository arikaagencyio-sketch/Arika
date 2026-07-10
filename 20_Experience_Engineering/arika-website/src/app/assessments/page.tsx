import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Stats1 } from "@/components/sections/Stats1";
import { Faq2 } from "@/components/sections/Faq2";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Free Assessment — Revenue Infrastructure Audit | Arika Agency",
  description:
    "The Revenue Infrastructure Audit: a fixed-fee, 7-14 day diagnostic across funnel, sales, CRM, automation, acquisition, team, and offer.",
};

export default function AssessmentsPage() {
  return (
    <>
      <PageHeader
        tagline="Free Assessment"
        heading="The Revenue Infrastructure Audit"
        description="Our Gateway Offer: a fast, fixed-fee diagnostic that gives you a real evidence base before any larger recommendation is made. No guesswork, no generic playbook — a structured look at your actual systems."
        buttons={[{ title: "Request Your Audit" }]}
      />

      <Stats1
        tagline="What's inside"
        heading="7 sub-audits, one findings report"
        description="Each sub-audit is itself a discrete, modular diagnostic — together they give a complete picture of where revenue is leaking."
        buttons={[]}
        stats={[
          { percentage: "7", heading: "Funnel, Sales, CRM, Automation, Acquisition, Team, Offer" },
          { percentage: "7-14", heading: "Days from signed engagement to delivered report" },
          { percentage: "1", heading: "Fixed fee — no scope creep, no hourly surprises" },
        ]}
      />

      <Faq2
        heading="Common questions about the audit"
        description="If your question isn't answered here, ask it directly on the strategy call."
        questions={[
          {
            title: "What exactly do I get at the end?",
            answer:
              "A findings report with a clear ascension-path recommendation — what to fix first, and whether that's a standalone fix or part of a larger infrastructure build.",
          },
          {
            title: "How long does it take?",
            answer:
              "7-14 days from signed engagement: data/access collection (days 1-3), parallel sub-audit analysis (days 3-10), synthesis and quantification (days 10-12), report production (days 12-13), delivery and review call (day 14).",
          },
          {
            title: "Is this the same as a sales pitch for a bigger engagement?",
            answer:
              "No — it's priced and delivered as a standalone diagnostic. Some clients stop here; others ascend to a larger infrastructure build only where the audit shows it's warranted.",
          },
          {
            title: "Who is this built for?",
            answer:
              "B2B SaaS companies from post-seed through Series C — see our Solutions page for how we tier engagements by company stage.",
          },
        ]}
        footerHeading="Ready to see where your revenue is leaking?"
        footerDescription="Get your free assessment and a real, evidence-based recommendation."
        button={{ title: "Book a Strategy Session", variant: "secondary" }}
      />

      <Cta58
        headers={["Request Your", "Revenue Infrastructure Audit"]}
        description="Fixed fee. 7-14 days. A real findings report, not a sales pitch."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
