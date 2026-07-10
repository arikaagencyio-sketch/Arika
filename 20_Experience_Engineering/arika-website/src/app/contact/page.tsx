import type { Metadata } from "next";
import { Contact3 } from "@/components/sections/Contact3";

export const metadata: Metadata = {
  title: "Contact | Arika Agency",
  description: "Contact Arika Agency.",
};

export default function ContactPage() {
  return (
    <>
      <Contact3
        tagline="Contact"
        heading="Let's talk"
        description="Tell us where things are breaking down and we'll follow up to schedule your Revenue Infrastructure Audit or a strategy session."
        button={{ title: "Submit" }}
      />
    </>
  );
}
