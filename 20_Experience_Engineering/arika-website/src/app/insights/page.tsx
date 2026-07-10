import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Blog33 } from "@/components/sections/Blog33";

export const metadata: Metadata = {
  title: "Insights | Arika Agency",
  description: "Revenue intelligence, architecture, operations, and leadership — organized by pillar.",
};

const pillars = [
  { name: "Revenue Intelligence", description: "Why revenue behaves the way it does." },
  { name: "Revenue Architecture", description: "Designing the systems that produce revenue." },
  { name: "Revenue Operations", description: "Executing those systems consistently." },
  { name: "Revenue Transformation", description: "Scaling via AI, automation, and operational redesign." },
  { name: "Revenue Leadership", description: "Leadership decisions that determine growth." },
  { name: "Revenue Signals", description: "Reading real buying signals before your competitors do." },
  { name: "Revenue Reality", description: "Unfiltered, operator-level perspective on running a revenue system." },
];

export default function InsightsPage() {
  return (
    <>
      <PageHeader
        tagline="Insights"
        heading="Revenue intelligence, organized by pillar"
        description="Our 7 content pillars — the same structure we use internally to plan and produce every article, framework, and playbook we publish."
        image={{ src: "/images/insights-intelligence-pod.png", alt: "Executive intelligence briefing pod with abstract data walls" }}
      />

      <Blog33
        tagline="Insights"
        heading="Articles are in production"
        description="This hub will fill in as pieces publish. Each pillar below is a real, planned content category — not a placeholder taxonomy."
        button={{ title: "Subscribe for Updates", variant: "secondary" }}
        blogPosts={pillars.map((pillar) => ({
          url: "#",
          image: {
            src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
            alt: `${pillar.name} — coming soon`,
          },
          category: pillar.name,
          title: "Coming soon",
          description: pillar.description,
          avatar: { src: "", alt: "" },
          fullName: "",
          date: "",
          readTime: "",
        }))}
      />
    </>
  );
}
