import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Pricing38 } from "@/components/sections/Pricing38";
import { Faq2 } from "@/components/sections/Faq2";

export const metadata: Metadata = {
  title: "Pricing | Arika Agency",
  description: "How Arika Agency prices engagements, by company stage.",
};

export default function PricingPage() {
  return (
    <>
      <PageHeader
        tagline="Pricing"
        heading="Priced by company stage, not a flat rate card"
        description="Engagements are scoped to your ARR band and the outcome you're solving for. We don't publish placeholder dollar figures here — every quote is real and specific to your Revenue Infrastructure Audit findings."
      />

      <Pricing38
        tagline="Engagement tiers"
        heading="Four tiers, one starting point"
        description="Every engagement — regardless of tier — starts with the Revenue Infrastructure Audit."
        pricingPlans={[
          {
            planName: "Discovery",
            price: "Custom",
            priceFrequency: "",
            features: [
              { text: "Revenue Infrastructure Audit" },
              { text: "Ascension-path recommendation" },
            ],
            button: { title: "Book a Strategy Session", variant: "secondary" },
          },
          {
            planName: "Growth",
            price: "Custom",
            priceFrequency: "",
            features: [
              { text: "For post-seed to Series A, $1M-$10M ARR" },
              { text: "Focused infrastructure build on 1-2 outcomes" },
            ],
            button: { title: "Book a Strategy Session" },
          },
          {
            planName: "Scale",
            price: "Custom",
            priceFrequency: "",
            features: [
              { text: "For Series A-C, $5M-$50M ARR" },
              { text: "Full Revenue Operating System build-out" },
            ],
            button: { title: "Book a Strategy Session", variant: "secondary" },
          },
          {
            planName: "Enterprise",
            price: "Custom",
            priceFrequency: "",
            features: [
              { text: "Multi-location or complex organizational structure" },
              { text: "Fractional leadership and retainer options" },
            ],
            button: { title: "Book a Strategy Session", variant: "secondary" },
          },
        ]}
      />

      <Faq2
        heading="Pricing questions"
        description=""
        questions={[
          {
            title: "Why isn't there a price list?",
            answer:
              "Every engagement is scoped to your specific systems and outcomes after the Revenue Infrastructure Audit. Publishing generic numbers here would be less accurate than a real quote.",
          },
          {
            title: "What currency do you invoice in?",
            answer: "Offers are priced in USD.",
          },
        ]}
        footerHeading="Not sure which tier fits?"
        footerDescription="Start with the Revenue Infrastructure Audit and we'll recommend the right scope."
        button={{ title: "Get My Free Assessment" }}
      />
    </>
  );
}
