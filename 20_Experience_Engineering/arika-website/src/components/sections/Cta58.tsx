"use client";

import { useState } from "react";
import { motion } from "motion/react";
import clsx from "clsx";
import { Button, type ButtonProps } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

type Props = {
  headers: string[];
  description: string;
  inputPlaceholder: string;
  button: ButtonProps;
  termsAndConditions: string;
};

export type Cta58Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Cta58 = (props: Cta58Props) => {
  const { headers, description, inputPlaceholder, button, termsAndConditions } = {
    ...Cta58Defaults,
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
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mx-auto max-w-lg text-center">
          <h2>
            {headers.map((heading, index) => (
              <motion.span
                key={index}
                initial={{ x: index % 2 === 0 ? "-50%" : "50%", opacity: 0 }}
                whileInView={{ x: "0%", opacity: 1 }}
                viewport={{ once: true }}
                transition={{
                  type: "spring",
                  bounce: 0,
                  duration: 0.5,
                  delay: index * 0.2,
                }}
                className={clsx("block text-h1 font-bold", {
                  "mb-5 md:mb-6": index !== 0,
                })}
              >
                {heading}
              </motion.span>
            ))}
          </h2>
          <p className="text-medium">{description}</p>
          <div className="mx-auto mt-6 w-full max-w-sm md:mt-8">
            <form
              className="mb-4 grid max-w-sm grid-cols-1 gap-y-3 sm:grid-cols-[1fr_max-content] sm:gap-4"
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
      </div>
    </section>
  );
};

export const Cta58Defaults: Props = {
  headers: ["Medium length CTA", "heading goes here"],
  description:
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique.",
  inputPlaceholder: "Enter your work email",
  button: { title: "Get My Free Assessment" },
  termsAndConditions: `
  <p class='text-tiny'>
    By clicking Get My Free Assessment you're confirming that you agree with our
    <a href='#' class='underline'>Terms and Conditions</a>.
  </p>
  `,
};
