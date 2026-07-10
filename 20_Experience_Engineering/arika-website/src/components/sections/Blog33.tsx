import { Button, type ButtonProps } from "@/components/ui/button";

type ImageProps = {
  src: string;
  alt?: string;
};

type BlogPost = {
  url: string;
  image: ImageProps;
  category: string;
  readTime: string;
  title: string;
  description: string;
  avatar: ImageProps;
  fullName: string;
  date: string;
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  button: ButtonProps;
  blogPosts: BlogPost[];
};

export type Blog33Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Blog33 = (props: Blog33Props) => {
  const { tagline, heading, description, button, blogPosts } = {
    ...Blog33Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mb-12 md:mb-18 lg:mb-20">
          <div className="mx-auto w-full max-w-lg text-center">
            <p className="mb-3 font-semibold md:mb-4">{tagline}</p>
            <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
            <p className="text-medium">{description}</p>
          </div>
        </div>
        <div className="grid grid-cols-1 gap-x-8 gap-y-16 md:grid-cols-2 md:gap-y-12 lg:grid-cols-3">
          {blogPosts.map((post, index) => (
            <div key={index}>
              <a href={post.url} className="mb-6 inline-block w-full max-w-full">
                <div className="w-full overflow-hidden">
                  <img
                    src={post.image.src}
                    alt={post.image.alt}
                    className="aspect-[3/2] size-full rounded-image object-cover"
                  />
                </div>
              </a>
              <a
                href={post.url}
                className="mr-4 mb-2 inline-block max-w-full text-small font-semibold"
              >
                {post.category}
              </a>

              <a href={post.url} className="mb-2 block max-w-full">
                <h3 className="text-h5 font-bold">{post.title}</h3>
              </a>
              <p>{post.description}</p>
              <div className="mt-5 flex items-center md:mt-6">
                <div>
                  <div className="flex items-center">
                    <p className="text-small">{post.date}</p>
                    <span className="mx-2">•</span>
                    <p className="text-small">{post.readTime}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        <div className="flex items-center justify-center">
          <Button {...button} className="mt-12 md:mt-18 lg:mt-20">
            {button.title}
          </Button>
        </div>
      </div>
    </section>
  );
};

export const Blog33Defaults: Props = {
  tagline: "Insights",
  heading: "Short heading goes here",
  description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  button: { title: "View all insights", variant: "secondary" },
  blogPosts: [
    {
      url: "#",
      image: {
        src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image-landscape.svg",
        alt: "Relume placeholder image 1",
      },
      category: "Category",
      title: "Blog title heading will go here",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros.",
      avatar: {
        src: "https://d22po4pjz3o32e.cloudfront.net/placeholder-image.svg",
        alt: "Relume placeholder avatar 3",
      },
      fullName: "Full name",
      date: "11 Jan 2022",
      readTime: "5 min read",
    },
  ],
};
