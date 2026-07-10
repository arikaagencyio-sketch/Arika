import { Header153 } from "@/components/sections/Header153";
import { Layout639 } from "@/components/sections/Layout639";
import { Layout640 } from "@/components/sections/Layout640";
import { Stats1 } from "@/components/sections/Stats1";
import { Logo1 } from "@/components/sections/Logo1";
import { Portfolio23 } from "@/components/sections/Portfolio23";
import { Blog33 } from "@/components/sections/Blog33";
import { Cta58 } from "@/components/sections/Cta58";

export default function Home() {
  return (
    <>
      <Header153
        heading="A Revenue Infrastructure Partner for B2B SaaS"
        description="Arika Agency designs and operates the systems that turn strategy, marketing, sales, and automation into one connected revenue engine — built for B2B SaaS companies from post-seed through Series C."
        buttons={[
          { title: "Get My Free Assessment" },
          { title: "Book a Strategy Session", variant: "secondary" },
        ]}
      />

      <Layout639
        tagline="The Problem"
        heading="Most B2B SaaS companies run growth as disconnected parts, not one system"
        description="Marketing, sales, branding, and automation usually operate as separate functions with separate owners and no shared source of truth. The result is fragmented data, duplicated effort, and revenue left on the table between the handoffs."
        buttons={[{ title: "See How We Fix This", variant: "secondary" }]}
        image={{ src: "/images/strategy-war-room.png", alt: "Strategy war room whiteboard mapping fragmented revenue systems" }}
        subHeadings={[
          {
            title: "Fragmented systems",
            description: "Marketing, sales, and delivery tools that don't talk to each other.",
          },
          {
            title: "No single source of truth",
            description: "Pipeline, content, and automation data scattered across platforms.",
          },
        ]}
      />

      <Layout640
        tagline="Our Methodology"
        heading="A Revenue Operating System, not another marketing retainer"
        description="The 360° Growth Revenue Framework is how we architect Strategy, Marketing, Sales, Branding, and Automation as one connected system rather than isolated services. Every engagement starts with the Revenue Infrastructure Audit, our fixed-fee diagnostic across 7 sub-audits (funnel, sales, CRM, automation, acquisition, team, offer), and ascends from there."
        buttons={[{ title: "Explore the Framework", variant: "secondary" }]}
        image={{ src: "/images/revenue-operations-center.png", alt: "Revenue operations center with live dashboard panels" }}
        subHeadings={[
          {
            title: "Diagnose first",
            description: "A 7-14 day, fixed-fee audit before any larger engagement is proposed.",
          },
          {
            title: "Ascend deliberately",
            description: "Clients move from audit to infrastructure build only where it's warranted.",
          },
        ]}
      />

      <Stats1
        tagline="How the engagement is structured"
        heading="Built on a real, fixed-fee diagnostic — not a guess"
        description="The Revenue Infrastructure Audit is Arika's Gateway Offer: a fast, modular diagnostic that gives every engagement a real evidence base before any larger recommendation is made."
        buttons={[{ title: "See the Audit", variant: "secondary" }]}
        stats={[
          { percentage: "7", heading: "Sub-audits: funnel, sales, CRM, automation, acquisition, team, offer" },
          { percentage: "7-14", heading: "Days from signed engagement to delivered findings report" },
          { percentage: "3", heading: "SaaS company tiers we work with, from post-seed to Series C" },
        ]}
      />

      <Logo1
        heading="Built for B2B SaaS at every stage"
        logos={[
          { src: "", alt: "Tier 1 — Series A-C, $5M-$50M ARR" },
          { src: "", alt: "Tier 2 — Post-Seed-Series A, $1M-$10M ARR" },
          { src: "", alt: "Tier 3 — Multi-location niche SaaS verticals" },
        ]}
      />

      <Portfolio23
        tagline="How We Work"
        title="Every engagement follows the same real structure"
        description="We don't publish invented case studies. Here is the actual structure every engagement follows, from first audit to measured result — real client work will populate this section as engagements complete."
        projects={[
          {
            heading: "Problem → Strategy → Implementation → Results → ROI",
            tags: ["Revenue Infrastructure Audit", "Ascension Model"],
            description:
              "Every engagement is scoped against a real diagnosed problem, mapped to a strategy, implemented against a defined workflow, and measured against agreed outcomes — the same structure our future case studies will report against.",
            buttons: [{ title: "Read the Methodology", variant: "secondary" }],
            image: {
              src: "/images/hero-executive-lobby.png",
              alt: "Executive lobby representing the premium infrastructure standard behind every engagement",
            },
          },
        ]}
      />

      <Blog33
        tagline="Insights"
        heading="Revenue intelligence, published as we build it"
        description="Organized by our 7 content pillars — Revenue Intelligence, Architecture, Operations, Transformation, Leadership, Signals, and Reality. Articles are in production; this section will fill in as they publish."
        button={{ title: "View All Insights", variant: "secondary" }}
        blogPosts={[
          {
            url: "#",
            image: {
              src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
              alt: "Revenue Intelligence — coming soon",
            },
            category: "Revenue Intelligence",
            title: "Coming soon",
            description: "Why revenue behaves the way it does — published as pieces go live.",
            avatar: { src: "", alt: "" },
            fullName: "",
            date: "",
            readTime: "",
          },
          {
            url: "#",
            image: {
              src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
              alt: "Revenue Architecture — coming soon",
            },
            category: "Revenue Architecture",
            title: "Coming soon",
            description: "Designing the systems that produce revenue — published as pieces go live.",
            avatar: { src: "", alt: "" },
            fullName: "",
            date: "",
            readTime: "",
          },
          {
            url: "#",
            image: {
              src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
              alt: "Revenue Signals — coming soon",
            },
            category: "Revenue Signals",
            title: "Coming soon",
            description: "Reading real buying signals before your competitors do.",
            avatar: { src: "", alt: "" },
            fullName: "",
            date: "",
            readTime: "",
          },
        ]}
      />

      <Cta58
        headers={["Start with the", "Revenue Infrastructure Audit"]}
        description="A fixed-fee, 7-14 day diagnostic across funnel, sales, CRM, automation, acquisition, team, and offer — with a clear recommendation on what to fix first."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
