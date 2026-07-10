import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { Button, type ButtonProps } from "@/components/ui/button";

type QuestionsProps = {
  title: string;
  answer: string;
};

type Props = {
  heading: string;
  description: string;
  footerHeading: string;
  footerDescription: string;
  button: ButtonProps;
  questions: QuestionsProps[];
};

export type Faq2Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Faq2 = (props: Faq2Props) => {
  const { heading, description, questions, footerHeading, footerDescription, button } = {
    ...Faq2Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mb-12 w-full max-w-lg md:mb-18 lg:mb-20">
          <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
          <p className="text-medium">{description}</p>
        </div>
        <Accordion type="multiple">
          {questions.map((question, index) => (
            <AccordionItem key={index} value={`item-${index}`}>
              <AccordionTrigger className="text-medium md:py-5">{question.title}</AccordionTrigger>
              <AccordionContent className="md:pb-6">{question.answer}</AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
        <div className="mt-12 md:mt-18 lg:mt-20">
          <h3 className="mb-3 text-h4 font-bold md:mb-4">{footerHeading}</h3>
          <p className="text-medium">{footerDescription}</p>
          <div className="mt-6 md:mt-8">
            <Button {...button}>{button.title}</Button>
          </div>
        </div>
      </div>
    </section>
  );
};

export const Faq2Defaults: Props = {
  heading: "FAQs",
  description:
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique.",
  questions: [
    {
      title: "Question text goes here",
      answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    },
  ],
  footerHeading: "Still have questions?",
  footerDescription: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  button: {
    title: "Contact",
    variant: "secondary",
  },
};
