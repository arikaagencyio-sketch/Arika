"use client";

import { useState } from "react";
import Image from "next/image";
import { motion } from "motion/react";
import { useMediaQuery } from "@/hooks/use-media-query";
import { Button, type ButtonProps } from "@/components/ui/button";
import { KeyboardArrowDown } from "relume-icons";
import { Badge } from "@/components/ui/badge";

type ImageProps = {
  url?: string;
  src: string;
  alt?: string;
  button?: ButtonProps;
};

type SubMenuLink = {
  title: string;
  url: string;
};

type MegaMenuItem = {
  url: string;
  image: ImageProps;
  name: string;
  variant: string;
  price: string;
  badge?: string;
};

type MegaMenuProps = {
  title: string;
  description: string;
  button: ButtonProps;
  items: MegaMenuItem[];
  subLinks?: SubMenuLink[];
};

type LinkProps = {
  title: string;
  url: string;
  megaMenu?: MegaMenuProps;
};

type Props = {
  logo: ImageProps;
  links: LinkProps[];
  buttons: ButtonProps[];
};

export type Navbar24Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Navbar24 = (props: Navbar24Props) => {
  const { logo, links, buttons } = {
    ...Navbar24Defaults,
    ...props,
  };

  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const isMobile = useMediaQuery("(max-width: 991px)");

  return (
    <section className="relative z-[999] flex w-full items-center justify-between border-b border-scheme-border bg-scheme-background lg:min-h-18 lg:px-[5%]">
      <div className="size-full lg:flex lg:items-center lg:justify-between">
        <div className="lg:flex">
          <div className="flex min-h-16 items-center justify-between px-[5%] md:min-h-18 lg:min-h-full lg:px-0">
            <a href={logo.url} className="flex items-center gap-2 text-h6 font-bold text-cream">
              <Image src="/images/arika-logo-icon.png" alt="" width={32} height={32} className="size-8 rounded-sm" />
              {logo.alt}
            </a>
            <button
              className="-mr-2 flex size-12 flex-col items-center justify-center lg:hidden"
              onClick={() => setIsMobileMenuOpen((prev) => !prev)}
            >
              <motion.span
                className="my-[3px] h-0.5 w-6 bg-cream"
                animate={isMobileMenuOpen ? ["open", "rotatePhase"] : "closed"}
                variants={topLineVariants}
              />
              <motion.span
                className="my-[3px] h-0.5 w-6 bg-cream"
                animate={isMobileMenuOpen ? "open" : "closed"}
                variants={middleLineVariants}
              />
              <motion.span
                className="my-[3px] h-0.5 w-6 bg-cream"
                animate={isMobileMenuOpen ? ["open", "rotatePhase"] : "closed"}
                variants={bottomLineVariants}
              />
            </button>
          </div>
          <motion.div
            variants={{
              open: {
                height: "var(--height-open, 100dvh)",
              },
              close: {
                height: "var(--height-closed, 0)",
              },
            }}
            initial="close"
            exit="close"
            animate={isMobileMenuOpen ? "open" : "close"}
            transition={{ duration: 0.4 }}
            className="overflow-auto px-[5%] lg:ml-6 lg:flex lg:items-center lg:px-0 lg:[--height-closed:auto] lg:[--height-open:auto]"
          >
            {links.map((link, index) =>
              link.megaMenu ? (
                <SubMenu
                  key={index}
                  megaMenu={link.megaMenu}
                  title={link.title}
                  isMobile={isMobile}
                />
              ) : (
                <a
                  key={index}
                  href={link.url}
                  className="text-md block py-3 first:pt-7 lg:px-4 lg:py-6 lg:text-base first:lg:pt-6"
                >
                  {link.title}
                </a>
              ),
            )}
            <div className="mt-6 flex w-full flex-col gap-y-4 pb-24 lg:hidden lg:pb-0">
              {buttons.map((button, index) => (
                <Button key={index} className="w-full" {...button}>
                  {button.title}
                </Button>
              ))}
            </div>
          </motion.div>
        </div>
        <div className="hidden lg:flex lg:gap-4">
          {buttons.map((button, index) => (
            <Button key={index} {...button}>
              {button.title}
            </Button>
          ))}
        </div>
      </div>
    </section>
  );
};
const SubMenu = ({
  title,
  isMobile,
  megaMenu,
}: {
  title: string;
  isMobile: boolean;
  megaMenu: MegaMenuProps;
}) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  return (
    <div
      onMouseEnter={() => !isMobile && setIsDropdownOpen(true)}
      onMouseLeave={() => !isMobile && setIsDropdownOpen(false)}
    >
      <button
        className="text-md flex w-full items-center justify-between gap-x-2 py-3 text-center lg:w-auto lg:flex-none lg:justify-start lg:px-4 lg:py-6 lg:text-base"
        onClick={() => setIsDropdownOpen((prev) => !prev)}
      >
        <span>{title}</span>
        <motion.span
          variants={{
            rotated: { rotate: 180 },
            initial: { rotate: 0 },
          }}
          animate={isDropdownOpen ? "rotated" : "initial"}
          transition={{ duration: 0.3 }}
        >
          <KeyboardArrowDown className="text-scheme-text" />
        </motion.span>
      </button>
      <motion.div
        variants={{
          open: {
            visibility: "visible",
            opacity: 1,
            height: "var(--height-open, auto)",
          },
          close: {
            visibility: "hidden",
            opacity: "0",
            height: "var(--height-close, 0)",
          },
        }}
        initial="close"
        exit="close"
        animate={isDropdownOpen ? "open" : "close"}
        transition={{ duration: 0.3 }}
        className="top-full bottom-auto left-0 w-full max-w-full min-w-full overflow-hidden bg-scheme-background lg:absolute lg:w-[100vw] lg:border-b lg:border-scheme-border lg:px-[5%] lg:[--height-close:auto]"
      >
        <div className="grid w-full auto-cols-fr grid-cols-1 lg:grid-cols-[1fr_0.5fr] lg:gap-12">
          <div className="flex w-full flex-col items-start justify-start gap-6 py-6 sm:gap-12 md:flex-row md:items-center md:justify-between md:py-8">
            <div className="max-w-sm">
              <h4 className="mb-3 text-2xl font-bold md:mb-4 md:text-3xl md:leading-[1.3] lg:text-4xl">
                {megaMenu.title}
              </h4>
              <p>{megaMenu.description}</p>
              <div className="mt-6 flex flex-wrap items-center gap-4 md:mt-8">
                <Button {...megaMenu.button}>{megaMenu.button.title}</Button>
              </div>
            </div>
            <div className="grid w-full max-w-md auto-cols-fr grid-cols-1 grid-rows-[auto_auto] gap-x-8 gap-y-4 sm:grid-cols-2 md:gap-x-10">
              {megaMenu.subLinks?.map((link, index) => (
                <a
                  key={index}
                  href={link.url}
                  className="py-2 text-2xl leading-[1.2] font-bold underline"
                >
                  {link.title}
                </a>
              ))}
            </div>
          </div>
          <div className="relative w-full px-8 py-6 sm:py-8 lg:pl-16">
            <div className="absolute top-0 bottom-0 left-0 z-0 w-full bg-neutral-lightest lg:w-screen" />
            <div className="grid w-full auto-cols-max auto-rows-max grid-cols-1 grid-rows-[max] gap-6 lg:gap-8">
              {megaMenu.items.map((item, index) => (
                <div key={index} className="flex flex-col items-stretch">
                  <a href={item.url} className="relative">
                    <div className="mb-3">
                      <div className="h-full w-full overflow-hidden md:mb-4 md:h-auto">
                        <img
                          src={item.image.src}
                          alt={item.image.alt}
                          className="aspect-[10/12] size-full rounded-image object-cover"
                        />
                      </div>
                    </div>
                    <div className="mb-2">
                      <p className="md:text-md font-semibold">{item.name}</p>
                      <p className="text-sm">{item.variant}</p>
                    </div>
                    <p className="text-md font-semibold md:text-lg">{item.price}</p>
                    {item.badge && <Badge className="absolute top-4 left-4">{item.badge}</Badge>}
                  </a>
                </div>
              ))}
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export const Navbar24Defaults: Props = {
  logo: {
    url: "/",
    src: "",
    alt: "Arika Agency",
  },
  links: [
    { title: "Solutions", url: "/solutions" },
    { title: "Insights", url: "/insights" },
    { title: "Case Studies", url: "/case-studies" },
    { title: "Pricing", url: "/pricing" },
  ],
  buttons: [
    {
      title: "Free Assessment",
      variant: "secondary",
      size: "sm",
    },
    {
      title: "Book a Strategy Session",
      size: "sm",
    },
  ],
};

const topLineVariants = {
  open: {
    translateY: 8,
    transition: { delay: 0.1 },
  },
  rotatePhase: {
    rotate: -45,
    transition: { delay: 0.2 },
  },
  closed: {
    translateY: 0,
    rotate: 0,
    transition: { duration: 0.2 },
  },
};

const middleLineVariants = {
  open: {
    width: 0,
    transition: { duration: 0.1 },
  },
  closed: {
    width: "1.5rem",
    transition: { delay: 0.3, duration: 0.2 },
  },
};

const bottomLineVariants = {
  open: {
    translateY: -8,
    transition: { delay: 0.1 },
  },
  rotatePhase: {
    rotate: 45,
    transition: { delay: 0.2 },
  },
  closed: {
    translateY: 0,
    rotate: 0,
    transition: { duration: 0.2 },
  },
};
