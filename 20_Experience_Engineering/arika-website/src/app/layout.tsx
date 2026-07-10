import type { Metadata } from "next";
import { Space_Grotesk, Inter } from "next/font/google";
import { Navbar24 } from "@/components/sections/Navbar24";
import { Footer16 } from "@/components/sections/Footer16";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  variable: "--font-space-grotesk",
  subsets: ["latin"],
  weight: ["500", "600", "700"],
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: "Arika Agency — Revenue Infrastructure Partner",
  description:
    "Arika Agency: the 360° Growth Revenue Operating System for B2B SaaS companies.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${spaceGrotesk.variable} ${inter.variable}`}>
      <body className="bg-navy font-body text-cream">
        <Navbar24 />
        {children}
        <Footer16 />
      </body>
    </html>
  );
}
