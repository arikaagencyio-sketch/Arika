import { Button, type ButtonProps } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ChevronRight, RelumeIcon } from "relume-icons";

type ImageProps = {
  src: string;
  alt?: string;
};

type SubHeadingProps = {
  title: string;
  description: string;
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  buttons: ButtonProps[];
  image: ImageProps;
  subHeadings: SubHeadingProps[];
};

export type Layout639Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Layout639 = (props: Layout639Props) => {
  const { tagline, heading, description, buttons, image, subHeadings } = {
    ...Layout639Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <Card className="grid auto-cols-fr grid-cols-1 md:grid-cols-2">
          <div className="flex flex-col justify-center p-6 md:p-8 lg:p-12">
            <p className="mb-2 inline-block text-small font-semibold">{tagline}</p>
            <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
            <p className="mb-6 text-medium md:mb-8">{description}</p>
            <div className="grid grid-cols-1 gap-6 py-2 lg:grid-cols-2">
              {subHeadings.map((subHeading, index) => (
                <div key={index} className="flex">
                  <div className="mr-4 flex-none self-start">
                    <RelumeIcon className="size-8 text-scheme-text" />
                  </div>
                  <div>
                    <h6 className="mb-3 text-h6 font-bold md:mb-4">{subHeading.title}</h6>
                    <p>{subHeading.description}</p>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-6 flex flex-wrap items-center gap-4 md:mt-8">
              {buttons.map((button, index) => (
                <Button key={index} {...button}>
                  {button.title}
                </Button>
              ))}
            </div>
          </div>
          <div className="flex items-center justify-center">
            <img src={image.src} className="size-full object-cover" alt={image.alt} />
          </div>
        </Card>
      </div>
    </section>
  );
};

export const Layout639Defaults: Props = {
  tagline: "Tagline",
  heading: "Medium length section heading goes here",
  description:
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat.",
  buttons: [
    { title: "Button", variant: "secondary" },
    {
      title: "Button",
      variant: "link",
      size: "link",
      iconRight: <ChevronRight className="text-scheme-text" />,
    },
  ],
  image: {
    src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image.svg",
    alt: "Relume placeholder image",
  },
  subHeadings: [
    {
      title: "Subheading one",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros.",
    },
    {
      title: "Subheading two",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros.",
    },
  ],
};
