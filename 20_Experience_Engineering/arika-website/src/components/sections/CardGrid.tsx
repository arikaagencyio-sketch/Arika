import { Card } from "@/components/ui/card";
import { RelumeIcon } from "relume-icons";

type GridItem = {
  heading: string;
  description: string;
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  items: GridItem[];
  columns?: 2 | 3;
};

export type CardGridProps = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const CardGrid = ({ tagline, heading, description, items = [], columns = 3 }: CardGridProps) => {
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mx-auto mb-12 max-w-lg text-center md:mb-18 lg:mb-20">
          {tagline && <p className="mb-3 font-semibold md:mb-4">{tagline}</p>}
          {heading && <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>}
          {description && <p className="text-medium">{description}</p>}
        </div>
        <div
          className={`grid grid-cols-1 gap-6 sm:grid-cols-2 ${columns === 3 ? "lg:grid-cols-3" : "lg:grid-cols-2"}`}
        >
          {items.map((item, index) => (
            <Card key={index} className="flex flex-col gap-4 p-6 md:p-8">
              <RelumeIcon className="size-8 text-gold" />
              <h3 className="text-h5 font-bold">{item.heading}</h3>
              <p>{item.description}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};
