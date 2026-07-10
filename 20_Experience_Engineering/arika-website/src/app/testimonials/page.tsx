import type { Metadata } from "next";
import { PageHeader } from "@/components/sections/PageHeader";
import { Cta58 } from "@/components/sections/Cta58";

export const metadata: Metadata = {
  title: "Testimonials | Arika Agency",
  description: "Client testimonials — published as real engagements complete.",
};

// Deliberately no testimonial cards on this page yet: no real client
// testimonials exist anywhere in this repo, and inventing placeholder
// quotes/names would violate the no-silent-invention rule this whole
// project follows. See `ARIKA_WEBSITE_PROJECT.md` §3 and §8.
export default function TestimonialsPage() {
  return (
    <>
      <PageHeader
        tagline="Testimonials"
        heading="Real testimonials, published as engagements complete"
        description="We don't publish placeholder quotes. As real client engagements finish, their testimonials — with permission — will appear here, organized by industry tier."
      />

      <Cta58
        headers={["Want to be one of", "our first published stories?"]}
        description="Start with the Revenue Infrastructure Audit and we'll build the case study together."
        inputPlaceholder="Enter your work email"
        button={{ title: "Get My Free Assessment" }}
        termsAndConditions="<p class='text-tiny'>By submitting, you agree to be contacted about your assessment. No spam.</p>"
      />
    </>
  );
}
