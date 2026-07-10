"use client";

import { useRef } from "react";
import { motion, useTransform, useScroll, type MotionValue } from "motion/react";
import { Badge } from "@/components/ui/badge";
import { Button, type ButtonProps } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ChevronRight } from "relume-icons";

type ImageProps = {
  src: string;
  alt?: string;
};

type Project = {
  heading: string;
  tags: string[];
  description: string;
  buttons: ButtonProps[];
  image: ImageProps;
};

type Props = {
  tagline: string;
  title: string;
  description: string;
  projects: Project[];
};

export type Portfolio23Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

const MotionCard = motion.create(Card);

const ProjectCard = ({ project }: { project: Project }) => {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });

  const scale: MotionValue<number> = useTransform(
    scrollYProgress,
    [0, 0.2, 0.7, 0.9, 1],
    [0.9, 1, 1, 0.95, 0.9],
  );
  const opacity: MotionValue<number> = useTransform(
    scrollYProgress,
    [0, 0.2, 0.7, 0.9, 0.95],
    [0, 1, 1, 0.5, 0],
  );

  return (
    <MotionCard
      ref={ref}
      style={{ scale, opacity }}
      className="grid grid-cols-1 gap-x-20 gap-y-6 p-6 md:grid-cols-[3fr_4fr] md:gap-y-20 md:p-8 lg:p-12"
    >
      <div className="flex flex-col justify-between">
        <div>
          <h3 className="text-h3 font-bold">{project.heading}</h3>
          <div className="mt-3 flex flex-wrap gap-2 md:mt-4">
            {project.tags.map((tag, index) => (
              <Badge key={index}>{tag}</Badge>
            ))}
          </div>
        </div>
        <div className="mt-6 text-medium md:mt-8">{project.description}</div>
        <div className="mt-6 flex flex-wrap items-center gap-4 md:mt-8">
          {project.buttons.map((button, index) => (
            <Button key={index} {...button}>
              {button.title}
            </Button>
          ))}
        </div>
      </div>
      <div>
        <img
          src={project.image.src}
          alt={project.image.alt}
          className="aspect-[3/2] w-full rounded-image object-cover"
        />
      </div>
    </MotionCard>
  );
};

export const Portfolio23 = (props: Portfolio23Props) => {
  const { tagline, title, description, projects } = {
    ...Portfolio23Defaults,
    ...props,
  };

  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <header className="mx-auto mb-12 max-w-lg text-center md:mb-18 lg:mb-20">
          <p className="mb-3 font-semibold md:mb-4">{tagline}</p>
          <h2 className="mb-5 text-h2 font-bold md:mb-6">{title}</h2>
          <p className="text-medium">{description}</p>
        </header>
        <div className="grid grid-cols-1 gap-6 md:gap-12 lg:gap-20">
          {projects.map((project, index) => (
            <ProjectCard key={index} project={project} />
          ))}
        </div>
      </div>
    </section>
  );
};

export const Portfolio23Defaults: Props = {
  tagline: "Case Studies",
  title: "Short heading goes here",
  description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  projects: [
    {
      heading: "Project name",
      tags: ["Tag one", "Tag two", "Tag three"],
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat.",
      buttons: [
        {
          title: "Button",
          variant: "secondary",
        },
        {
          title: "Button",
          variant: "link",
          size: "link",
          iconRight: <ChevronRight className="text-scheme-text" />,
        },
      ],
      image: {
        src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
        alt: "Relume placeholder image center",
      },
    },
  ],
};
