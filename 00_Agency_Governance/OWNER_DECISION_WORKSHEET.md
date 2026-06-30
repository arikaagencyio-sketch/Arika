# Owner Decision Worksheet

**Purpose:** This is the working companion to [`OWNER_INPUT_NEEDED.md`](OWNER_INPUT_NEEDED.md) — that file is the technical tracker (what's open, why, where it lives); this file is the action surface. Every still-open tracker item is below, sorted into two kinds:

- **[DECISION]** — there's nothing more to wait for. You have a real choice to make, and I've given you my actual recommendation, reasoned from what's already confirmed in this repo (`AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md`, the confirmed positioning/sector/offer catalog) — not a generic best-practice guess.
- **[WAITING ON DATA]** — there's genuinely nothing to decide yet. These resolve themselves once the agency has operated for a real period and produces real numbers. No recommendation is possible without inventing figures, which violates this repo's no-silent-invention rule. Listed here so you can see the gap, not so you can act on it today.

**How to use this:** for each [DECISION] item, write your call in the **Your decision** line — either agree with my recommendation, modify it, or override it entirely. You can write directly in this file, or just tell me in conversation and I'll fill it in. Once you've gone through it, tell me which ones to action and I'll update the real source files and close out `OWNER_INPUT_NEEDED.md` to match.

**Tally (updated 2026-06-30):** Started at 18 open items. The Offer department's 6 bigger decisions (items 7, 37, 38, 39, 40, 41), the 3 threshold/defaults items (4, 28, 29), the 3 quick wins (31, 14, 10), and item 30 (Branding's real brand for BOIS) are now resolved. Remaining: 5 [WAITING ON DATA] items (8, 9, 13, 20), 0 open [DECISION] items.

---

## Quick wins (5 minutes, low-stakes)

**All 3 resolved 2026-06-30, all matched the recommendation:**
- **Item 31** — Sector's partial chat export: left as-is.
- **Item 14** — Marketing's MCP/connector blueprint: confirmed none of the 7 layers are in real use yet.
- **Item 10** — Sales' 11 missing companion `.docx` files: confirmed-lost, not pending location.

---

## Threshold/defaults decisions (pattern already set by Finance) — ALL 3 RESOLVED 2026-06-30

Verified Branding's `bois/` codebase directly (zero LLM SDK dependency, same check as Finance) before asking — confirmed the premise of item 28 exactly. All 3 matched the recommendation:

- **Item 4** (agency-wide KPI thresholds): stay unset, revisit after the first full real operating month.
- **Item 28** (Branding's 20 AI agents): stay spec/routing-only until item 30 (the agency's own real brand) gives them something real to reason over.
- **Item 29** (`BrandScoringEngine` thresholds): keep the generic 70-78 defaults until a real BOIS run exists to calibrate against.

### Item 8 / Item 13 — Offer's and Marketing's historical conversion/margin/LTV/CAC figures
**The question:** Both KPI tables only have industry-benchmark template numbers, no agency actuals.
**My recommendation:** Same logic — these are **[WAITING ON DATA]**, not a decision, listed here only because they're the same pattern. Nothing to do until real deals close.
**Your decision:** *(no action needed yet)*

---

## Offer department — the bigger decisions

**All 6 resolved 2026-06-30 — see `OWNER_INPUT_NEEDED.md` Resolved table for the canonical record. Summary of what was decided:**

- **Item 39 (team-role roster):** Reframed, not standardized as asked — these are AI-assisted functional labels, not real headcount, since you solo-orchestrate with AI. Real hiring deferred to `11_HR_People_Ops/HR_OS.md`.
- **Item 38 (segmentation variable):** ARR-band primary, rep-count secondary (sales-team offers only). Your call, matched the recommendation.
- **Item 7 (pricing floor):** Computed a first provisional floor, ARR-banded, explicitly flagged part-real/part-synthesized — see `02_Offer/OFFER_OS.md` §10.
- **Item 37 (offer #2 synthesis):** Approved as-is.
- **Item 40A (offers #5-11 batch):** Approved as-is.
- **Item 40B (division mapping):** You went further than my recommendation — promoted Automation, Consulting & Advisory, Audits & Diagnostics, and AI Enablement to real departments (14-17), rather than keeping them as offer-internal categories. New `{DEPT}_OS.md` files created for each, seeded from their founding offer drafts.
- **Item 41 (offer #8 vs. ClientPartner Acquisition):** Confirmed no conflict after reading both files directly — different audiences, same mechanics.

---

## Build-now items (not blocked on data — these are real work I can do once you say go)

### Item 24 — Client Success offboarding/churn process — DONE, expanded scope
**Resolved 2026-06-30.** Built broader than originally scoped — per your direction to make sure all Client Success workflows exist, not just offboarding, I added the full Process Library: Retention, Expansion, Advocacy, Offboarding & Churn, and Re-entry/Win-back. Every owned stage of the 9-stage lifecycle now has a real workflow (`07_Client_Success/CLIENTSUCCESS_OS.md` §4, §10). Still Claude-synthesized, not owner-original — worth a read when convenient, same review discipline as the Offer catalog.

### Item 30 — Define Arika Agency's own real brand for BOIS — DONE
**Resolved 2026-06-30 ("act on item 30 now").** Built and ran `bois/executions/run_arika_agency_brand.py`: assembled a real `ClientObject` for Arika Agency itself from facts already confirmed elsewhere in this repo (name, "Revenue Infrastructure Partner" positioning, `AGENCY_VISION.md`, the 3-tier B2B SaaS ICP, the 11-offer services catalog, ROCBO/"do-or-die" operating philosophy, Kenya + global geography) — no invention. Ran it through the full pipeline: real client workspace created (`bois/clients/arika-agency/`), retrieval gate completed with zero missing sources, 11 of 20 agents activated for the task "define Arika Agency's own core brand identity, positioning, and voice." As anticipated, `competitors`, `visual_preferences`, `typography_preferences`, `color_preferences` had no real source anywhere in this repo — left empty and flagged rather than invented. Worth a follow-up owner pass whenever visual identity/competitive-positioning work happens for real.

---

## Genuinely waiting on data (nothing to decide — listed for visibility only)

| Item | What it's waiting on |
|---|---|
| 8 | Real historical conversion/margin/LTV figures (Offer) — needs closed deals |
| 9 | Real historical Sales KPI actuals — needs operating history against the now-real daily targets |
| 13 | Real Marketing KPI values — needs campaign history |
| 20 | Real ClientPartner Acquisition partner names/deals/revenue-share — needs actual partners (none yet, consistent with solo operation) |
| 31 | *(see Quick Wins above — already addressed)* |

These will close on their own as the agency operates. No action needed now; they're listed so the full picture is visible in one place.

---

## Changelog

- 2026-06-30 — Created at owner's request, as a working action-companion to `OWNER_INPUT_NEEDED.md`. Sorted all 18 open tracker items into [DECISION] (13 items, with reasoned recommendations) vs. [WAITING ON DATA] (5 items, no action possible). — Claude Code (Sonnet 4.6)
- 2026-06-30 — Owner made 2 new real decisions outside this worksheet's original 18 items, as part of go-live preparation: **Zoho CRM** (replacing the already-resolved item 5/HubSpot) paired with **Zoho Books** (closing item 25), and **Claude (Anthropic API)** as the agency-standard LLM (closing items 27 and 28). See `OWNER_INPUT_NEEDED.md`'s Changelog "Zoho/Claude entry" and the new `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 4.6)
