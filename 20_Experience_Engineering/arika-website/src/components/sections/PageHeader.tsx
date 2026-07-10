import Image from "next/image";
import { Button, type ButtonProps } from "@/components/ui/button";

type Props = {
  tagline?: string;
  heading: string;
  description: string;
  buttons?: ButtonProps[];
  image?: { src: string; alt: string };
};

export type PageHeaderProps = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const PageHeader = ({ tagline, heading, description, buttons, image }: PageHeaderProps) => {
  return (
    <section className="border-b border-scheme-border px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className={image ? "grid items-center gap-x-12 gap-y-8 md:grid-cols-2 md:gap-x-16" : "max-w-lg"}>
          <div className={image ? "" : undefined}>
            {tagline && <p className="mb-3 font-semibold md:mb-4">{tagline}</p>}
            <h1 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h1>
            <p className="text-medium">{description}</p>
            {buttons && buttons.length > 0 && (
              <div className="mt-6 flex flex-wrap items-center gap-4 md:mt-8">
                {buttons.map((button, index) => (
                  <Button key={index} {...button}>
                    {button.title}
                  </Button>
                ))}
              </div>
            )}
          </div>
          {image && (
            <div className="relative aspect-[4/3] w-full overflow-hidden rounded-image md:aspect-[16/10]">
              <Image src={image.src} alt={image.alt} fill className="object-cover" />
            </div>
          )}
        </div>
      </div>
    </section>
  );
};
