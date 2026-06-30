# Owner Decision Worksheet

**Purpose:** This is the working companion to [`OWNER_INPUT_NEEDED.md`](OWNER_INPUT_NEEDED.md) — that file is the technical tracker (what's open, why, where it lives); this file is the action surface. Every still-open tracker item is below, sorted into two kinds:

- **[DECISION]** — there's nothing more to wait for. You have a real choice to make, and I've given you my actual recommendation, reasoned from what's already confirmed in this repo (`AGENCY_VISION.md`, `AGENCY_REVENUE_TARGETS.md`, the confirmed positioning/sector/offer catalog) — not a generic best-practice guess.
- **[WAITING ON DATA]** — there's genuinely nothing to decide yet. These resolve themselves once the agency has operated for a real period and produces real numbers. No recommendation is possible without inventing figures, which violates this repo's no-silent-invention rule. Listed here so you can see the gap, not so you can act on it today.

**How to use this:** for each [DECISION] item, write your call in the **Your decision** line — either agree with my recommendation, modify it, or override it entirely. You can write directly in this file, or just tell me in conversation and I'll fill it in. Once you've gone through it, tell me which ones to action and I'll update the real source files and close out `OWNER_INPUT_NEEDED.md` to match.

**Tally (updated 2026-06-30):** Started at 18 open items. The Offer department's 6 bigger decisions (items 7, 37, 38, 39, 40, 41) are now resolved — see the Offer section below for what was decided. Remaining: 7 [DECISION] items, 5 [WAITING ON DATA] items.

---

## Quick wins (5 minutes, low-stakes)

### Item 31 — Sector's partial chat export
**The question:** Should we still try to get the full "Sider Fusion" chat export that produced the Tier 2/3 ICP material, or leave it as-is?
**My recommendation:** Leave it. You already made this call once (2026-06-30) — proceed with what's captured. Tier 1 (your primary, most-detailed ICP) is fully real and unaffected; only the Tier 2/3 deep-dives are partial. Not worth revisiting unless the export becomes trivially available.
**Your decision:** _______________________________________________

### Item 14 — Marketing's MCP/connector blueprint
**The question:** Is any of the 7 documented connector-class layers (the marketing automation/integration blueprint) actually wired up and in use, or is all of it still aspirational?
**My recommendation:** Given Finance's integrations turned out to be zero real connectors and you confirmed no payment platform is in use yet, I'd bet this is the same — entirely aspirational. But this is a 10-second factual answer only you can give (yes/no, or "X of the 7").
**Your decision:** _______________________________________________

### Item 10 — Sales' missing companion `.docx` files
**The question:** 11 files referenced in Sales' source registry (e.g. `HE SALES OS_2024.docx`) aren't anywhere in this repo. Do you have them somewhere else, or should we mark them confirmed-lost and move on?
**My recommendation:** Mark confirmed-absent and move on. Sales' citation system is otherwise solid (verified against what *is* present); these 11 are a minor completeness gap, not a trust problem. Only worth digging up if you happen to know exactly where they are.
**Your decision:** _______________________________________________

---

## Threshold/defaults decisions (pattern already set by Finance)

These four follow the exact precedent you already set for Finance (item 26/27): generic doctrine defaults stay in place until real operating data exists to calibrate against, rather than guessing real numbers prematurely. Flagging them so you can either rubber-stamp the same logic or override it department-by-department.

### Item 4 — Agency-wide KPI thresholds
**The question:** Every metric in `AGENCY_KPI_DICTIONARY.md` has an owner and cadence now, but no threshold (e.g., "alert if CAC > $X"). Set real thresholds now, or wait?
**My recommendation:** Same logic as Finance — keep `(unset)` for now. Setting real alert thresholds before the agency has run a single real month against the $1M target would be guessing, and a wrong threshold (false alarms or missed real problems) is worse than an honest "not yet measured." Revisit after the first full operating month.
**Your decision:** _______________________________________________

### Item 28 — Branding's 20 AI agents: wire to a real LLM?
**The question:** Same question as Finance's 7 agents, but for Branding's 20-agent roster — keep as structured prompts/routing metadata, or wire to a live LLM now?
**My recommendation:** Keep spec-only, matching the Finance decision exactly — and for the same reason: BOIS has never run against the agency's own real brand (see item 30 below), so there's no real data yet for live agents to reason over. Resolve item 30 first; revisit this once there's something real to point the agents at.
**Your decision:** _______________________________________________

### Item 29 — Branding's `BrandScoringEngine` thresholds
**The question:** Generic 70-78 default scoring thresholds — keep or calibrate?
**My recommendation:** Keep, same logic as item 4/26. No real BOIS run against a real client (including the agency itself) has happened yet — nothing to calibrate against.
**Your decision:** _______________________________________________

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

### Item 24 — Client Success offboarding/churn process
**The question:** This is confirmed to barely exist (an empty filename placeholder). Should I draft a real offboarding SOP now?
**My recommendation:** Yes — this is the same category of work as the offer completions: a real process design exercise, not a fact that needs to come from your operating history. I can draft a Claude-synthesized offboarding/churn SOP (exit triggers, asset handover, knowledge transfer, win-back logic) calibrated against Client Success's already-real 9-stage client journey model and the Constitution's risk-class framework, clearly labeled as synthesized for your review — same discipline as everything in the Offer catalog.
**Your decision:** _______________________________________________

### Item 30 — Define Arika Agency's own real brand for BOIS
**The question:** BOIS (the branding system) has only ever run against a hypothetical example client. Should I build it a real brand object for Arika Agency itself?
**My recommendation:** Yes, and unlike most remaining gaps, **this one is mostly buildable right now from facts already confirmed elsewhere in this repo** — not from scratch. We already have: the real name (Arika Agency), the confirmed positioning ("Revenue Infrastructure Partner"), the full vision/mission (`AGENCY_VISION.md`), the confirmed target client (B2B SaaS, Tier 1/2/3), and the operating philosophy (ROCBO, the "do-or-die" revenue framing). What's still missing and would need to come from you: visual identity preferences (if any exist yet) and voice/tone specifics beyond what's implicit in the existing positioning. I can assemble a first real brand object from what's confirmed and flag the visual/voice gaps explicitly, rather than waiting until every field is real before starting.
**Your decision:** _______________________________________________

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
