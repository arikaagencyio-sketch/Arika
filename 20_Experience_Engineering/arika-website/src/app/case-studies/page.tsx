import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Portfolio23 } from "@/components/sections/Portfolio23";

export const metadata: Metadata = {
  title: "Case Studies | Arika Agency",
  description: "How every Arika Agency engagement is structured, start to finish.",
};

export default function CaseStudiesPage() {
  return (
    <>
      <PageHeader
        tagline="Case Studies"
        heading="Real engagements will be published here as they complete"
        description="We don't publish invented case studies. Below is the actual structure every engagement follows — real client results will populate this page as engagements complete."
      />

      <Portfolio23
        tagline="How We Work"
        title="Problem → Strategy → Implementation → Results → ROI"
        description="Every engagement is scoped against a real diagnosed problem, mapped to a strategy, implemented against a defined workflow, and measured against agreed outcomes."
        projects={[
          {
            heading: "Diagnose",
            tags: ["Revenue Infrastructure Audit"],
            description:
              "Every engagement starts with the 7-sub-audit Revenue Infrastructure Audit — a real, evidence-based diagnosis, not a generic playbook.",
            buttons: [{ title: "See the Audit", variant: "secondary" }],
            image: {
              src: "/images/strategy-war-room.png",
              alt: "Strategy war room where audit findings are diagnosed",
            },
          },
          {
            heading: "Build",
            tags: ["Ascension Model"],
            description:
              "Clients ascend from the audit to a scoped infrastructure build only where the findings warrant it — never a default upsell.",
            buttons: [{ title: "See Solutions", variant: "secondary" }],
            image: {
              src: "/images/revenue-operations-center.png",
              alt: "Revenue operations center where the infrastructure build runs",
            },
          },
          {
            heading: "Measure",
            tags: ["Real KPIs, not vanity metrics"],
            description:
              "Results are measured against the outcomes agreed at the start of the engagement — published here once real engagements complete.",
            buttons: [{ title: "Book a Strategy Session", variant: "secondary" }],
            image: {
              src: "/images/hero-executive-lobby.png",
              alt: "Executive lobby representing the polished, measured outcome of an engagement",
            },
          },
        ]}
      />
    </>
  );
}
