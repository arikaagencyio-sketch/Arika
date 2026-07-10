"use client";

import { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { Button, type ButtonProps } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { InstagramLogo, LinkedinLogo, XLogo, YoutubeLogo } from "relume-icons";

type Links = {
  title: string;
  url: string;
  icon?: React.ReactNode;
};

type ColumnLinks = {
  title: string;
  links: Links[];
};

type FooterLink = {
  title: string;
  url: string;
};

type Props = {
  newsletterDescription: string;
  inputPlaceholder?: string;
  button: ButtonProps;
  termsAndConditions: string;
  columnLinks: ColumnLinks[];
  footerText: string;
  footerLinks: FooterLink[];
};

export type Footer16Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Footer16 = (props: Footer16Props) => {
  const {
    newsletterDescription,
    inputPlaceholder,
    button,
    termsAndConditions,
    columnLinks,
    footerText,
    footerLinks,
  } = {
    ...Footer16Defaults,
    ...props,
  };

  const [emailInput, setEmailInput] = useState<string>("");
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log({
      emailInput,
    });
  };

  return (
    <footer className="border-t border-scheme-border px-[5%] py-12 md:py-18 lg:py-20">
      <div className="container">
        <div className="grid grid-cols-1 gap-x-[8vw] gap-y-12 pb-8 md:gap-y-16 md:pb-10 lg:grid-cols-[0.75fr_1fr] lg:gap-y-4 lg:pb-12">
          <div className="flex flex-col">
            <Link href="/" className="mb-5 md:mb-6">
              <Image src="/images/arika-logo-full.png" alt="Arika Agency — Growth Partners" width={742} height={875} className="h-32 w-auto" />
            </Link>
            <p className="mb-5 md:mb-6">{newsletterDescription}</p>
            <div className="w-full max-w-md">
              <form
                className="mb-3 grid grid-cols-1 gap-x-4 gap-y-3 sm:grid-cols-[1fr_max-content] md:gap-y-4"
                onSubmit={handleSubmit}
              >
                <Input
                  id="email"
                  type="email"
                  placeholder={inputPlaceholder}
                  value={emailInput}
                  onChange={(e) => setEmailInput(e.target.value)}
                />
                <Button {...button}>{button.title}</Button>
              </form>
              <div dangerouslySetInnerHTML={{ __html: termsAndConditions }} />
            </div>
          </div>
          <div className="grid grid-cols-1 items-start gap-y-10 sm:grid-cols-3 sm:gap-x-6 md:gap-x-8 md:gap-y-4">
            {columnLinks.map((column, index) => (
              <div key={index} className="flex flex-col items-start justify-start">
                <h3 className="mb-3 font-semibold md:mb-4">{column.title}</h3>
                <ul>
                  {column.links.map((link, linkIndex) => (
                    <li key={linkIndex} className="py-2 text-small">
                      <a href={link.url} className="flex items-center gap-3">
                        {link.icon && <span>{link.icon}</span>}
                        <span>{link.title}</span>
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
        <div className="h-px w-full bg-scheme-border" />
        <div className="flex flex-col-reverse items-start justify-between pt-6 pb-4 text-small md:flex-row md:items-center md:pt-8 md:pb-0">
          <p className="mt-6 md:mt-0">{footerText}</p>
          <ul className="grid grid-flow-row grid-cols-[max-content] justify-center gap-y-4 text-small md:grid-flow-col md:gap-x-6 md:gap-y-0">
            {footerLinks.map((link, index) => (
              <li key={index} className="underline">
                <a href={link.url}>{link.title}</a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </footer>
  );
};

export const Footer16Defaults: Props = {
  newsletterDescription: "Join our newsletter to stay up to date on features and releases.",
  inputPlaceholder: "Enter your email",
  button: {
    title: "Subscribe",
    variant: "secondary",
    size: "sm",
  },
  termsAndConditions: `
  <p class='text-tiny'>
    By subscribing you agree with our
    <a href='#' class='underline'>Privacy Policy</a>
    and provide consent to receive updates from our company.
  </p>
  `,
  columnLinks: [
    {
      title: "Company",
      links: [
        { title: "About", url: "/about" },
        { title: "Services", url: "/services" },
        { title: "Industry Solutions", url: "/industry-solutions" },
        { title: "Case Studies", url: "/case-studies" },
        { title: "Testimonials", url: "/testimonials" },
        { title: "Pricing", url: "/pricing" },
        { title: "Contact", url: "/contact" },
      ],
    },
    {
      title: "Resources",
      links: [
        { title: "Insights", url: "/insights" },
        { title: "Frameworks", url: "/frameworks" },
        { title: "Free Assessments", url: "/assessments" },
        { title: "Book a Strategy Session", url: "/book-a-strategy-session" },
        { title: "Proposal Center", url: "/proposal-center" },
      ],
    },
    {
      title: "Follow us",
      links: [
        {
          title: "Instagram",
          url: "#",
          icon: <InstagramLogo className="size-6 text-scheme-text" />,
        },
        { title: "X", url: "#", icon: <XLogo className="size-6 p-0.5 text-scheme-text" /> },
        { title: "LinkedIn", url: "#", icon: <LinkedinLogo className="size-6 text-scheme-text" /> },
        { title: "Youtube", url: "#", icon: <YoutubeLogo className="size-6 text-scheme-text" /> },
      ],
    },
  ],
  footerText: "© 2026 Arika Agency. All rights reserved.",
  footerLinks: [
    { title: "Privacy Policy", url: "#" },
    { title: "Terms of Service", url: "#" },
  ],
};
