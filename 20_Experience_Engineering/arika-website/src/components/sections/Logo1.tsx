type ImageProps = {
  src: string;
  alt?: string;
};

type Props = {
  heading: string;
  logos: ImageProps[];
};

export type Logo1Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Logo1 = (props: Logo1Props) => {
  const { heading, logos } = {
    ...Logo1Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-12 md:py-16 lg:py-20">
      <div className="container">
        <h2 className="mx-auto mb-6 w-full max-w-lg text-center text-h6 font-bold md:mb-8">
          {heading}
        </h2>
        <div className="flex flex-wrap items-center justify-center gap-x-8 gap-y-4 pt-4 pb-2 md:pt-2">
          {logos.map((logo, index) => (
            <p key={index} className="text-small font-semibold text-cream/70">
              {logo.alt}
            </p>
          ))}
        </div>
      </div>
    </section>
  );
};

export const Logo1Defaults: Props = {
  heading: "Used by the world's leading companies",
  logos: [{ src: "", alt: "Logo" }],
};
