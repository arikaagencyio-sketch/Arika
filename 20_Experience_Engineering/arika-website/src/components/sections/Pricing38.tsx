import { Button, type ButtonProps } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Check } from "relume-icons";

type Feature = {
  text: string;
};

type PricingPlan = {
  planName: string;
  price: string;
  priceFrequency: string;
  discount?: string;
  features: Feature[];
  button: ButtonProps;
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  pricingPlans: PricingPlan[];
};

export type Pricing38Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Pricing38 = (props: Pricing38Props) => {
  const { tagline, heading, description, pricingPlans } = {
    ...Pricing38Defaults,
    ...props,
  };

  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mb-12 max-w-lg md:mb-18 lg:mb-20">
          <p className="mb-3 font-semibold md:mb-4">{tagline}</p>
          <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
          <p className="text-medium">{description}</p>
        </div>
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3">
          {pricingPlans.map((plan, index) => (
            <PricingPlanCard key={index} plan={plan} />
          ))}
        </div>
      </div>
    </section>
  );
};

const PricingPlanCard = ({ plan }: { plan: PricingPlan }) => (
  <Card className="flex h-full flex-col justify-between px-6 py-8 md:p-8">
    <div>
      <div className="mb-6 text-center md:mb-8">
        <h3 className="mb-2 text-h6 font-bold">{plan.planName}</h3>
        <p className="mb-2 text-h1 font-bold">
          {plan.price}
          <span className="text-h4 font-bold">{plan.priceFrequency}</span>
        </p>
        {plan.discount && <p>{plan.discount}</p>}
      </div>
      <div className="grid grid-cols-1 gap-4 py-2">
        {plan.features.map((feature, index) => (
          <div key={index} className="flex self-start">
            <div className="mr-4 flex-none self-start">
              <Check className="size-6 text-gold" />
            </div>
            <p>{feature.text}</p>
          </div>
        ))}
      </div>
    </div>
    <div className="mt-6 md:mt-8">
      <Button {...plan.button} className="w-full">
        {plan.button.title}
      </Button>
    </div>
  </Card>
);

export const Pricing38Defaults: Props = {
  tagline: "Pricing",
  heading: "Pricing plan",
  description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  pricingPlans: [
    {
      planName: "Discovery",
      price: "Fixed fee",
      priceFrequency: "",
      features: [{ text: "Feature text goes here" }],
      button: { title: "Get started" },
    },
  ],
};
