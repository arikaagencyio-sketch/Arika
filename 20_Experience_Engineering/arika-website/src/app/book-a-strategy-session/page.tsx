import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Contact3 } from "@/components/sections/Contact3";

export const metadata: Metadata = {
  title: "Book a Strategy Session | Arika Agency",
  description: "Book a strategy session with Arika Agency.",
};

export default function BookAStrategySessionPage() {
  return (
    <>
      <PageHeader
        tagline="Book a Strategy Session"
        heading="Let's talk about your revenue infrastructure"
        description="A strategy session is a real qualification and discovery conversation — not a sales pitch. Tell us where things are breaking down and we'll follow up to schedule a time."
      />

      <Contact3
        tagline="Get Started"
        heading="Request your strategy session"
        description="We'll respond with next steps, including whether the Revenue Infrastructure Audit is the right starting point for you."
        button={{ title: "Request a Session" }}
      />
    </>
  );
}
