# AI Creative Orchestra — Canonical Agent Roster

**Status:** Real, invokable — 11 canonical roles, each backed by a real Claude Code subagent under `.claude/agents/experience-engineering-*.md`, callable via the Agent tool today. Superseded the original two non-identical source-draft rosters (10-role "AI Department," 12-role "AI Creative Orchestra" — both from the owner-relayed ChatGPT-style session, `EXPERIENCE_ENGINEERING_VISION.md` §2-3) with **one reconciled roster**, per explicit owner direction (2026-07-04) to reconcile rather than leave two open drafts. Cross-referenced from [`EXPERIENCE_ENGINEERING_OS.md`](EXPERIENCE_ENGINEERING_OS.md) §5.

**Reconciliation method:** union of every distinct responsibility named across both source drafts. Roles that named the same underlying function twice (e.g. "Creative Director AI" / "Executive Creative Director") were merged into one canonical role; roles unique to only one draft were kept; the three narrowest, most-overlapping reviewer roles (QA Reviewer, Accessibility Reviewer, Performance Engineer) were consolidated into one **QA & Performance Reviewer** that runs all three checklists, since as three near-identical thin agents they added file count without adding distinct judgment — every responsibility from all three is preserved inside that one role's checklist, none dropped.

---

## Communication Protocol (shared across all 11 roles)

Every agent below receives: the project's Narrative Arc/Scene Architecture context, the relevant Storyboard Library entry, Branding's confirmed Brand Genome tokens, a task objective, and Creative Governance constraints. Every agent returns: domain-specific reasoning, operational implications, risks/contradictions, recommendations, and a note of anything it hands off to another role in the roster.

### Creative Philosophy (shared doctrine — sourced 2026-07-04, "Sider Fusion" session, `EXPERIENCE_ENGINEERING_VISION.md` §5)

1. **Form follows emotion** — great experiences are felt before they're understood.
2. **Constraints breed creativity** — technical limitations are design parameters, not blockers.
3. **The medium is the message** — choose the right platform for the right feeling.
4. **Details are not details** — they *are* the design.
5. **Accessibility is not a feature** — it's the baseline.

### Decision Framework (shared, in order — same source)

1. **Human Impact** — how does this make people feel/behave?
2. **Technical Viability** — can this be built with reasonable effort?
3. **Business Value** — does this serve the strategic goal?
4. **Innovation Potential** — does this push the craft forward?

### Output Structure (shared default shape for creative/strategic responses — same source)

**Vision** (the creative north star) → **Rationale** (why this direction) → **Technical Notes** (feasibility, trade-offs, recommendations) → **Next Steps** (concrete actions).

### Communication style (shared — same source)

Confident but collaborative, never dogmatic. Vivid, sensory language when describing experiences. Balances poetic vision with technical precision. Asks 1-2 targeted clarifying questions before diving deep rather than guessing. Provides rationale for every creative decision, not just a verdict.

---

## Canonical Roster (11 roles)

| # | Role | Reconciled from | Real subagent file |
|---|---|---|---|
| 1 | Creative Director | "Creative Director AI" (Draft A) + "Executive Creative Director" (Draft B) | `.claude/agents/experience-engineering-creative-director.md` |
| 2 | Narrative Architect | "Narrative AI" (Draft A) + "Narrative Architect" (Draft B) | `.claude/agents/experience-engineering-narrative-architect.md` |
| 3 | UX Strategist | "UX Strategist AI" (Draft A) + "UX Strategist" (Draft B) | `.claude/agents/experience-engineering-ux-strategist.md` |
| 4 | Storyboard Artist | "Storyboard AI" (Draft A only — no Draft B equivalent) | `.claude/agents/experience-engineering-storyboard-artist.md` |
| 5 | UI Designer | "UI Designer" (Draft B only — no Draft A equivalent) | `.claude/agents/experience-engineering-ui-designer.md` |
| 6 | Motion Director | "Motion Director AI" (Draft A) + "Motion Director" (Draft B) | `.claude/agents/experience-engineering-motion-director.md` |
| 7 | 3D Director | "3D Director AI" (Draft A) + "3D Artist" (Draft B) | `.claude/agents/experience-engineering-3d-director.md` |
| 8 | Technical Director | "Developer AI" (Draft A) + "Technical Director" + "Front-end Engineer" (both Draft B) | `.claude/agents/experience-engineering-technical-director.md` |
| 9 | Brand Strategist | "Brand Strategist AI" (Draft A) + "Brand Strategist" (Draft B) | `.claude/agents/experience-engineering-brand-strategist.md` |
| 10 | Copywriter | "Copywriter AI" (Draft A only — no Draft B equivalent) | `.claude/agents/experience-engineering-copywriter.md` |
| 11 | QA & Performance Reviewer | "QA AI" (Draft A) + "QA Reviewer" + "Accessibility Reviewer" + "Performance Engineer" (all Draft B) | `.claude/agents/experience-engineering-qa-performance-reviewer.md` |

Full role-by-role detail (purpose, inputs, outputs, validation) lives in each real subagent file, not duplicated here — this table is the roster index.

## Closing note

These are AI-assisted functional execution roles, not real hires — same convention as every other department's role labels in this repo (`GLOBAL_OS.md` §10, 2026-06-30 entry). No real names, no headcount implied. They are now genuinely invokable (not just documented) via the Agent tool — this is the first department in this repo to reach that state, alongside Design (19)'s own newly-built roster (`19_Design/DESIGN_OS.md` §5).

## Changelog

- 2026-07-03 — File created alongside Experience Engineering (20)'s founding. Both source-material role-draft versions (10-role "AI Department," 12-role "AI Creative Orchestra") captured as separate, lightweight BOIS-style contracts rather than merged into one invented roster. All roles flagged proposed/not built. — Claude Code (Sonnet 5)
- 2026-07-04 — **Reconciled into one canonical 11-role roster** and made real: each role now backed by a genuine, invokable Claude Code subagent under `.claude/agents/`, per explicit owner direction. Added a shared Creative Philosophy, Decision Framework, and Output Structure to the Communication Protocol, sourced from a second owner-relayed external AI session ("Sider Fusion," `EXPERIENCE_ENGINEERING_VISION.md` §5) — adopted for its reusable persona/philosophy content only; its proposed standalone Python/Streamlit/DALL-E application was explicitly not built (see vision file §5 for the full reasoning). — Claude Code (Sonnet 5)
