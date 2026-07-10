"use client";

import { Button, type ButtonProps } from "@/components/ui/button";
import { motion, useInView } from "motion/react";
import { useRef } from "react";

type ImageProps = {
  src: string;
  alt?: string;
};

type ImageConfig = {
  image: ImageProps;
  animationAxis: "x" | "y";
  animationDistance: string;
  positionClasses: string;
  hasDelay: boolean;
};

type Props = {
  heading: string;
  description: string;
  leftImages: ImageProps[];
  rightImages: ImageProps[];
  buttons: ButtonProps[];
};

export type Header153Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

const AnimatedImage = ({
  image,
  animationAxis,
  animationDistance,
  positionClasses,
  side,
  hasDelay,
  isInView,
}: {
  image: ImageProps;
  animationAxis: "x" | "y";
  animationDistance: string;
  positionClasses: string;
  side: "left" | "right";
  hasDelay: boolean;
  isInView: boolean;
}) => (
  <div
    className={`absolute inset-0 ${side === "left" ? "right-auto" : "left-auto"} z-20 flex h-full w-[45%] items-center overflow-hidden`}
  >
    <motion.div
      initial={{ [animationAxis]: 0 }}
      animate={{
        [animationAxis]: isInView ? 0 : animationDistance,
      }}
      transition={{
        duration: isInView ? 0.6 : 0.8,
        ease: isInView ? [0.33, 1.25, 0.45, 1] : "easeInOut",
        delay: hasDelay ? 0.1 : 0,
      }}
      className={`absolute w-full max-w-[90%] overflow-hidden rounded-image sm:max-w-[60%] md:max-w-[50%] lg:max-w-[40%] ${positionClasses}`}
    >
      <img src={image.src} alt={image.alt} className="aspect-4/3 size-full object-cover" />
    </motion.div>
  </div>
);

export const Header153 = (props: Header153Props) => {
  const { heading, description, leftImages, rightImages, buttons } = {
    ...Header153Defaults,
    ...props,
  };

  const triggerRef = useRef<HTMLDivElement>(null);
  const isInView = useInView(triggerRef, { once: false, amount: 0 });

  const leftImageConfigs: ImageConfig[] = [
    {
      image: leftImages[0],
      animationAxis: "x",
      animationDistance: "-120%",
      positionClasses: "-left-[70%] sm:-left-[30%] md:-left-[20%] bottom-[68%] lg:-left-[10%]",
      hasDelay: false,
    },
    {
      image: leftImages[1],
      animationAxis: "x",
      animationDistance: "-80%",
      positionClasses: "-left-[80%] sm:-left-[40%] md:-left-[35%] lg:-left-[20%]",
      hasDelay: true,
    },
    {
      image: leftImages[2],
      animationAxis: "x",
      animationDistance: "-140%",
      positionClasses: "-left-[70%] sm:-left-[30%] md:-left-[20%] top-[68%] lg:-left-[10%]",
      hasDelay: false,
    },
    {
      image: leftImages[3],
      animationAxis: "y",
      animationDistance: "130%",
      positionClasses: "right-0 -bottom-[10%] sm:-bottom-[5%] lg:-bottom-[10%]",
      hasDelay: false,
    },
  ];

  const rightImageConfigs: ImageConfig[] = [
    {
      image: rightImages[0],
      animationAxis: "x",
      animationDistance: "90%",
      positionClasses: "-right-[70%] sm:-right-[30%] md:-right-[20%] lg:-right-[10%] bottom-[68%]",
      hasDelay: false,
    },
    {
      image: rightImages[1],
      animationAxis: "x",
      animationDistance: "135%",
      positionClasses: "-right-[80%] sm:-right-[40%] md:-right-[35%] lg:-right-[20%]",
      hasDelay: true,
    },
    {
      image: rightImages[2],
      animationAxis: "x",
      animationDistance: "110%",
      positionClasses: "-right-[70%] sm:-right-[30%] md:-right-[20%] top-[68%] lg:-right-[10%]",
      hasDelay: false,
    },
    {
      image: rightImages[3],
      animationAxis: "y",
      animationDistance: "120%",
      positionClasses:
        "-right-[70%] sm:-right-[30%] -bottom-[10%] sm:-bottom-[5%] md:-right-[20%] md:-bottom-[10%] lg:-bottom-[15%] left-0 lg:-right-[10%]",
      hasDelay: true,
    },
  ];

  return (
    <section className="relative flex h-svh flex-col flex-nowrap items-center justify-center lg:h-screen">
      <div ref={triggerRef} className="absolute inset-0 bottom-auto -z-10 mt-[15vh]" />

      {leftImageConfigs.map((config, index) => (
        <AnimatedImage
          key={`left-${index}`}
          image={config.image}
          animationAxis={config.animationAxis}
          animationDistance={config.animationDistance}
          positionClasses={config.positionClasses}
          side="left"
          hasDelay={config.hasDelay}
          isInView={isInView}
        />
      ))}

      {rightImageConfigs.map((config, index) => (
        <AnimatedImage
          key={`right-${index}`}
          image={config.image}
          animationAxis={config.animationAxis}
          animationDistance={config.animationDistance}
          positionClasses={config.positionClasses}
          side="right"
          hasDelay={config.hasDelay}
          isInView={isInView}
        />
      ))}

      <div className="relative z-10 px-[10%] sm:px-[5%] lg:px-0">
        <div className="px-[5%] py-16 md:py-24 lg:py-28">
          <div className="container">
            <div className="flex flex-col items-center text-center">
              <div className="mx-auto w-full max-w-lg">
                <h1 className="mb-5 text-h1 font-bold md:mb-6">{heading}</h1>
                <p className="text-medium">{description}</p>
                <div className="mt-6 flex items-center justify-center gap-x-4 md:mt-8">
                  {buttons.map((button, index) => (
                    <Button key={index} {...button}>
                      {button.title}
                    </Button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

const defaultImage: ImageProps = {
  src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image.svg",
  alt: "Relume placeholder image",
};

export const Header153Defaults: Props = {
  heading: "Medium length hero heading goes here",
  description:
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat.",
  leftImages: [defaultImage, defaultImage, defaultImage, defaultImage],
  rightImages: [defaultImage, defaultImage, defaultImage, defaultImage],
  buttons: [{ title: "Button" }, { title: "Button", variant: "secondary" }],
};
