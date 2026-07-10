/* eslint-disable @typescript-eslint/no-require-imports -- standard CJS Tailwind v3 config format */
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  presets: [require("@relume_io/relume-tailwind")],
  theme: {
    extend: {
      // Relume preset replaces gradientColorStops — re-point at our own colors.
      gradientColorStops: ({ theme }) => theme("colors"),
      fontSize: {
        h1: ["3.5rem", { lineHeight: "1.2", letterSpacing: "-0.01em" }],
        h2: ["3rem", { lineHeight: "1.2", letterSpacing: "-0.01em" }],
        h3: ["2.5rem", { lineHeight: "1.2", letterSpacing: "-0.01em" }],
        h4: ["2rem", { lineHeight: "1.3", letterSpacing: "-0.01em" }],
        h5: ["1.5rem", { lineHeight: "1.4", letterSpacing: "-0.01em" }],
        h6: ["1.25rem", { lineHeight: "1.4", letterSpacing: "-0.01em" }],
        large: ["1.25rem", { lineHeight: "1.5" }],
        medium: ["1.125rem", { lineHeight: "1.5" }],
        regular: ["1rem", { lineHeight: "1.5" }],
        small: ["0.875rem", { lineHeight: "1.5" }],
        tiny: ["0.75rem", { lineHeight: "1.5" }],
      },
      // Arika Brand Genome (12_Branding/BRANDING_OS.md §2) — real, owner-confirmed values.
      colors: {
        navy: "#0E1B29", // Deep Revenue Navy — 60%, dominant base
        charcoal: "#1C1C1C", // Operator Charcoal — 20%, structural
        cream: "#F7F5F0", // Alabaster Cream — high-contrast text
        gold: "#D4AF37", // Champagne Gold / "Pipeline Gold" — 10%, CTA/metric accent
        blush: "#F3C1C6", // Blush Rose Pink / "Operator Blush" — 10%, UGC hook accent only, never primary
        scheme: {
          background: "#0E1B29",
          foreground: "#0E1B29",
          text: "#F7F5F0",
          border: "#D4AF37",
          "btn-text": "#0E1B29",
        },
      },
      fontFamily: {
        // Space Grotesk stands in for the Brand Genome's headline pairing
        // (Space Grotesk/Satoshi/Neue Montreal) — Satoshi/Neue Montreal need
        // separate licensing/self-hosting, not swapped in silently here.
        heading: ["var(--font-space-grotesk)", "sans-serif"],
        body: ["var(--font-inter)", "sans-serif"],
      },
      borderRadius: {
        button: "0.25rem",
        card: "0.5rem",
        image: "0.5rem",
        form: "0.25rem",
        badge: "9999px",
        checkbox: "0.25rem",
        carousel: "0.5rem",
        dropdown: "0.5rem",
      },
    },
  },
};
