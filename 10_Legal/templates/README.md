# Legal Templates — READ BEFORE USING ANY FILE IN THIS FOLDER

**Created:** 2026-07-15 by Claude Code (Opus 4.8), at the owner's explicit direction.

---

## 🔴 These are unreviewed drafts. None has been seen by a lawyer.

Every document in this folder was written by a **language model**, not an advocate. They are
**starting points for counsel review** — the same category as a commercial template service's
output, and to be treated with the same caution.

**They are drafted to be genuinely usable, which is exactly what makes them dangerous.** A
document that reads like a contract invites signature. **Do not sign, send, or rely on any of
these until a Kenyan-qualified advocate has reviewed them.**

The failure mode is not a bad template. It is a good-looking template that stops anyone asking
whether a lawyer ever saw it. That is why every file carries a banner, and **the banners are
not to be removed until the review actually happens** — at which point the reviewer's name and
date replace them.

## What "reviewed" must mean before use

For each document, record in `10_Legal/LEGAL_OS.md` §8:
- **Who** reviewed it (named advocate/firm, not "a lawyer friend")
- **When**
- **What changed**
- **What jurisdictions it was cleared for**

Until all four exist for a document, it stays a draft.

## Why they exist anyway

`LEGAL_OS.md` §2 recorded this department as an **empty skeleton** with *"no MSA, SOW,
DPA/privacy policy, IP terms, or claims-substantiation policy… anywhere in the repo"*, and §10
called that *"the highest-priority gap to close before onboarding any real client."*

**A blank page costs more counsel hours than a draft to correct.** These exist to make the
review cheaper and faster, and to force the agency's real questions into the open — not to
avoid the review.

> ⚠️ **A deliberate note on provenance:** `CLAUDE.md` instructs *"Do not invent agency-specific
> facts (numbers, client names, pricing, **legal terms**) when source material is missing — flag
> the gap instead."* Drafting these **overrides that standing rule**, on the owner's explicit
> instruction of 2026-07-15. That override is recorded here, in `LEGAL_OS.md` §8, and in
> `GLOBAL_OS.md` §10 rather than left silent — because the rule exists for good reasons and a
> reader six months from now must know the rule was consciously set aside, not forgotten.

## The documents

| File | Covers | Highest risk if wrong |
|---|---|---|
| [`MSA.md`](MSA.md) | Master Services Agreement — the frame every engagement hangs on | Liability, IP ownership, payment |
| [`SOW_TEMPLATE.md`](SOW_TEMPLATE.md) | Per-engagement scope, deliverables, price, timeline | Scope creep, disputes over "done" |
| [`DPA.md`](DPA.md) | Data Processing Agreement + **sub-processor register** | **Regulatory** — Kenya DPA s.48, GDPR Art. 28 |
| [`NDA.md`](NDA.md) | Mutual and one-way NDAs — ideas, campaigns, content | Loss of confidentiality with no remedy |
| [`IP_COPYRIGHT_TRADEMARK_TERMS.md`](IP_COPYRIGHT_TRADEMARK_TERMS.md) | Who owns what; AI-generated work; trademark use | Ownership of deliverables; brand misuse |
| [`CLAIMS_SUBSTANTIATION_POLICY.md`](CLAIMS_SUBSTANTIATION_POLICY.md) | What Arika may claim publicly, and on what evidence | Advertising-law exposure |
| [`API_AND_AI_TOOLING_TERMS.md`](API_AND_AI_TOOLING_TERMS.md) | AI/API use in delivery; client disclosure | Vendor ToS breach; undisclosed AI use |

**Read [`../LEGAL_RESEARCH.md`](../LEGAL_RESEARCH.md) first.** It carries the Kenya + global
research these are drafted against, the counsel brief, and the finding that **Arika already
transfers personal data out of Kenya daily with no documented s.48 basis.**

## Placeholders

`[SQUARE BRACKETS]` mark every value a human must supply. **A document with brackets left in it
is not ready to send.** Common ones: `[CLIENT LEGAL NAME]`, `[ARIKA LEGAL ENTITY]`,
`[GOVERNING LAW]`, `[FEE]`, `[DATE]`.

⚠️ **`[ARIKA LEGAL ENTITY]` is itself an open question** — whether Arika trades as a sole
proprietorship or needs a limited company before signing MSAs with liability caps is **counsel
question 7** in `LEGAL_RESEARCH.md` §6, and was deliberately not researched.
