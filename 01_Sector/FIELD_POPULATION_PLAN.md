# Field-Population Plan — Sector (01) + Content (04) databases

**Version:** v0.1 · **Created:** 2026-08-19 · **Owner:** Mary Thuo (Sector 01)
**Purpose:** The owner asked, before scraping/decision-maker/outreach work begins: *go through the whole repository and, for every field in the Sector and Content databases, say where its data comes from and whether it can be filled now — never guess a relevant-but-empty field.* This is that map. It is a **decide-then-apply** plan: it classifies every field, it does **not** fill anything on its own.
**Companion specs (the source of truth for the schemas):** [`SECTOR_NOTION_SCHEMA.md`](SECTOR_NOTION_SCHEMA.md) · [`../04_Content/CONTENT_INTELLIGENCE_SCHEMA.md`](../04_Content/CONTENT_INTELLIGENCE_SCHEMA.md).

---

## 0. The three fill-sources (and the one hard rule)

Every empty field resolves to exactly one of four dispositions. **A field is only filled from its true source — an empty field is a legitimate state; a plausible-looking guess is a constitutional breach** (`AGENCY_OPERATING_CONSTITUTION.md` §3; `CONTENT_INTELLIGENCE_SCHEMA.md` law 6).

| Disposition | Who fills it | Honesty gate |
|---|---|---|
| **🟢 Fillable now** | Claude Code + web research, or transcription from an existing repo/owner source | Cite the source; set `Confidence` to match (research = Medium; owner-adopted = High). Web-verified, dated. |
| **🟡 Needs owner** | A decision only the owner can make (focus, ruling, campaign context, real client IDs) | Not a research task — do not infer it. |
| **🔴 Needs scraping** | IntOS Collection layer (gated: API key + cost governance + Approval-Matrix row; cloud routines have **no web**) | Writes to CRM/CPAROS as real `Person`/`Company`; never invented. Deferred (Part E). |
| **⚫ Never fill / template** | Nobody until a real external system connects | Live-booking/property numbers, performance metrics, unpublished results. Stays a template. |

**The freshness/decision-purpose gate still applies:** populate a field only when it has a named downstream decision or execution purpose (`SECTOR_ACTIVATION_CONTRACT.md` §13). Everything below already has one — that is why it is listed.

---

## 1. The critical path — the unlock sequence (read this first)

The databases are a chain. **One decision unblocks most of the empty fields**, and everything else follows a fixed order. Do not fill breadth-first; fill this depth-first for **one target sub-sector at a time**.

> **⚑ Reframe (2026-08-19, ADDENDUM 4):** step ① is **superseded** — the focus is now **data-derived, not owner-blocked**. The **Sector Priority Score** already named the September focus (P1: **B2B SaaS · Hospitality→Accommodation · Professional Services→Legal & Accounting**); those are promoted to `Status = Target` **by the score** (advisory; owner may veto/add). The pilot depth-target is **Hospitality → Accommodation** (owner-chosen). The chain below runs now — no fresh naming ruling is waited on.

```
① FOCUS (data-derived): promote the P1-scored sub-sectors  Status = Target   (Sub-Sectors DB)
        └─ score is the decision (advisory); unblocks EVERYTHING downstream
                 │
② RESEARCH (🟢, per target sub-sector, web-cited):
        Sector Intelligence findings ─┬─► Sector Linguistics (words to use/avoid)
                                       ├─► Audience Roles (4 roles: Operators/Buyers/Amplifiers/Enablers)
                                       ├─► Decision-Maker Registry (titles + triggers — NOT contacts)
                                       └─► Sector Signals (real events/regulation for that sector)
                 │
③ DISTIL (🟢): Sector State ("what's happening now") + Sector Forecast (forward view)
                 │
④ CONTENT unblocks automatically:  DB3 Sector×Platform ─► DB5 Opportunity ─► DB6 Translation ─► DB7 Brief
                 │
⑤ OWNER: campaign context (a real campaign idea) ─► DB4 Campaign Intelligence  (fast path — see §4)
                 │
⑥ SCRAPING (🔴, gated): Decision-Maker CONTACTS + Company Intelligence ─► CRM/CPAROS ─► ICP + Signal Scores ─► outreach
```

**Two things are loadable today with zero owner input** and remove standing gaps: **the 12 Offer Registry rows** (Content DB 8) and **the 10 narrative beliefs** (Content DB 2). See §3.

---

## 2. Sector (01) databases — field disposition

Legend: 🟢 fillable now · 🟡 needs owner · 🔴 needs scraping · ⚫ never/template · ✅ already populated.

### DB 1 — Sectors Master (25 verticals) — **mostly populated**
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| Sector Name · Category · Atlas Layer · Portfolio Mode · Priority Tier · Industry Type · Lifecycle State · **Sector Priority Score · Priority Band · Rationale** | ✅ all 25 | atlas + scoring pass (2026-08-19) | done |
| `Strategic Priority` (Primary/Secondary/Tertiary) | partial | owner GTM call | 🟡 owner |
| `Related Clients (CRM)` | empty | real ClickUp `Client` IDs | 🔴 (none exist yet) |
| `Last Intelligence Update` · `Next Review` | empty | review cadence | 🟡 owner sets cadence |
| `Definition` | ✅ most | Draft 3 one-liner | 🟢 fill the 3 new grouping verticals |

### DB 2 — Sub-Sectors (321) — **the hub; breadth vs depth split**
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| Name · Parent Sector · Industry · Sub-Sector ID · Status · Confidence | ✅ all 321 | atlas | done |
| `Industry Type` | ✅ established · empty growth/frontier | atlas | 🟢 (established done; growth/frontier optional) |
| Tool-Stack block (`Chaos Risk`·`Typical Stack`·`Fragmentation Type`) | ✅ established + frontier(Strategic/Future) · empty growth | web research per sector | 🟢 per target |
| `Business Model` · `Company Archetype` · `Core Value Prop` · `Revenue Model` · `GTM Motion` · `Ecosystem Dependencies` | ✅ 52 SaaS · empty 269 | web research (per **target** sub-sector only) | 🟢 per target |
| `Readiness` (Ready/In-Progress/Asleep) | ✅ 52 SaaS · empty rest | owner + market research | 🟡/🟢 per target |
| `Opportunity Score` | empty | `sector-readiness-analyst` | 🟢 agent-advisory |
| Relations: `Intelligence`·`Linguistics`·`Audience Roles`·`Decision-Makers`·`ICP`·`Signal Scores`·`Offers`·`Campaigns`·`Content Opportunities`·`Calendar Events` | mostly empty | fill as each related DB is loaded (step ②–⑥) | follows the chain |

### DB 3 — Sector Intelligence — **the biggest content-blocking gap**
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| 52 Sheet-03 findings (SaaS `Buying Psychology`) | ✅ | xlsx Sheet 03 | done (Confidence Medium) |
| Sheets 04–07 (struggles · revenue-intel · strategic-nodes · relationship-map) — SaaS | empty | xlsx Sheets 04–07 | 🟢 same loader pattern |
| **Findings for the 88 established + growth industries** | **none** | web research, cited (per target sector) | 🟢 per target — *this is the fuel Content DB 5 needs* |
| `Category = Tool-Stack Chaos` findings | empty | the per-sector chaos reads → promote to findings | 🟢 per target |

### DB 7 — Sector Signals (SCIC) (24 rows)
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| 24 signals (Signal Type, source, Last Verified) | ✅ | web-verified | done |
| Full depth (geo · 6 lead-time dates · 8 impact fields · linked finding) | ✅ 3 rows only | derived offsets + web facts | 🟢 per target signal |
| **Signals for the new verticals** (Hospitality/RealEstate/Health/etc. events + regulation) | thin | web-verify (organizer/gov pages) | 🟢 per target |
| Live-booking/property layer (pickup·ADR·RevPAR·comp-set) | template | a client's connected RMS/PMS | ⚫ never fabricate |

### DB 8 — Agency Opportunity Map → Industry Offer Matrix (87 rows)
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| Ladder (Entry/Expansion/Transformation capability) · Offer/Gap · Outreach Angle · Scraping Fields · KPIs · Tier/Type/Mode | ✅ 87 established | atlas (2026-08-19) | done |
| Relations `Pain Points`·`Buying Triggers`·`Target Decision-Maker` | empty | fill from DB 3 / DB 10 as those load | 🟢 follows the chain |
| `CRM Opportunities` | empty | real ClickUp deal IDs | 🔴 (none exist) |
| Growth/Frontier matrix rows | none (by design) | promote on real pull | 🟡 owner promotes |

### DB 9 — Audience Roles — **EMPTY · critical blocker**
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| The 4 roles per sub-sector (Operators/Buyers/Amplifiers/Enablers) + `Wants`/`Rejects` + persona | **empty** | web research (roles/titles) per target; individuals via scraping | 🟢 roles/titles · 🔴 individuals |
> Blocks Content DB 5 `Audience` and DB 7 `Persona`. Load roles/titles by research now; real people come with scraping (→ CRM `Person`).

### DB 10 — Decision-Maker Registry (52 SaaS rows)
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| Titles + buying triggers + outreach intelligence — SaaS | ✅ 52 | xlsx Sheet 09 | done |
| **Titles + triggers for the 88 established + growth industries** | none | web research (per target sector) | 🟢 per target |
| Actual **named decision-makers** (people, companies) | none | scraping → CRM `Person`/`Company` | 🔴 gated |

### DB 11 — Sector Linguistics — **EMPTY · critical blocker**
| Field(s) | State | Source of truth | Disposition |
|---|---|---|---|
| 5-layer linguistic map (words-to-use / avoid / metaphors / proof-language) per sub-sector | **empty** | web research per target sector | 🟢 per target |
> Blocks Content DB 3 `Words to Avoid` and DB 6 vocabulary. Highest-leverage 🟢 research task after the findings.

### DB — ICP Classification · Prospect Signal Scores — **empty by design**
Written by `sector-icp-fit` / `sector-signal-scorer` at runtime, **against real companies**. 🔴 gated (needs scraped companies + agent runs). Do not seed.

### DB — Geography (seeded Global→EU/USA) · Sector State (empty) · Sector Forecast (empty)
| DB | State | Source | Disposition |
|---|---|---|---|
| Geography | ✅ seed | expand as signals cite new places | 🟢 incidental |
| Sector State ("what's happening now" per sector×geo) | empty | **distil** from Intelligence+Signals+State once ② is done | 🟢 per target (after ②) |
| Sector Forecast (forward view) | empty | same, forward | 🟢 per target (after ②) |

---

## 3. Content (04) databases — field disposition

The Content layer is **structurally complete and almost entirely empty by design**; most of it is gated on Sector (step ②) or the owner (campaign). Full flow: `CONTENT_INTELLIGENCE_SCHEMA.md` §3.

| DB | Rows | State | What fills it | Disposition |
|---|---|---|---|---|
| **DB 1 Platform Registry** | 10 | ✅ seeded | light-profile fields (Threads/TikTok/YouTube) from PIL; `Account Status` as accounts get created | 🟢 minor · 🟡 account status |
| **DB 2 Narrative Registry** | 10 | ✅ seeded | **the 10 deferred beliefs are loadable now** (real, owner-adopted); DRAGON ruling; Sector Scope/Linguistics relations per sector | 🟢 beliefs · 🟡 DRAGON |
| **DB 8 Offer Registry (thin)** | 0 (12 pending) | empty | **transcribe the 12 offers from `OFFER_OS.md` §3** — no owner input needed (no price fields exist) | 🟢 **load now** |
| **DB 3 Sector × Platform Matrix** | 0 | blocked | a `Target` sub-sector (①) + its Linguistics/DM (②); `Buyer Behavior Delta`/`Trust Proof` = web research | 🟡 then 🟢 |
| **DB 5 Content Opportunity** | 0 | blocked | real Sector Intelligence findings (②) + a manual `content-opportunity-mapper` run | 🟢 after ② |
| **DB 6 Content Translation Matrix** | 0 | blocked | DB 3 + narrative; the multiplication-engine tree | 🟢 after DB 3 |
| **DB 7 Content Briefs v2** | 0 | blocked (structural) | an Opportunity + a Translation must exist first (no manual escape hatch, by design) | follows chain |
| **DB 4 Campaign Intelligence** | 0 | blocked | **a real campaign idea + context from the owner** (see §4) | 🟡 owner — the fast path |

**⚫ Never-fill in Content:** any `Performance`/metric field (nothing published), `Narrative Preserved = Yes` guesses, `Account Status = Live` before an account is live. **`Confidence` mapping at the boundary:** Sector `High/Medium/Low` → Content `Confirmed/Working Hypothesis/Experimental` (never retype).

---

## 4. The campaign fast-path (the owner's "I have an idea" entry point)

The owner noted they may arrive with a campaign idea + context. **Content DB 4 Campaign Intelligence is that entry point.** A campaign is the one place structured owner context legitimately seeds the whole content chain for a target sector without waiting on the full research load:

1. Owner gives the campaign context (objective · thesis · core insight · target sub-sector · offer · platforms · dates).
2. That fills DB 4 (Business/Revenue Objective · Campaign Thesis · Core Insight · Objective · Phase · Offer → DB 8 · Sector Scope · Narrative Positions).
3. The campaign then **pulls** opportunities (DB 5) and translations (DB 6) into itself — turning a loose idea into a real, sourced production plan.
4. Still gated on: the target sub-sector being `Target` (①) and having ≥1 real finding + linguistics (②) so the content isn't generic.

So the minimum to run a real campaign end-to-end = **① pick the sector + ② one research pass + the campaign context.** That is the smallest honest slice to reach actual outreach.

---

## 5. What is fillable **today** (no owner decision, no scraping)

These remove standing gaps immediately and are pure transcription/research — say the word and I execute (decide-then-apply):

1. 🟢 **Content DB 8 — load the 12 Offer Registry rows** (from `OFFER_OS.md` §3; no prices).
2. 🟢 **Content DB 2 — load the 10 narrative beliefs** (real, owner-adopted; second-pass deferred rows).
3. 🟢 **Sector Intelligence — Sheets 04–07** for the 52 SaaS sub-sectors (same loader as Sheet 03).
4. 🟢 **Sector DB 1 — `Definition`** for the 3 new grouping verticals; **Geography** tidy-up.

Everything else is now driven by **① the data-derived focus** (ADDENDUM 4 reframe): per-sector research (findings, linguistics, audience, DM titles, signals) is spent depth-first on the **P1 `Target` sectors** — starting with the **Hospitality → Accommodation** pilot — not sprayed across 321 rows.

---

## 6. What I need from the owner to start the real build

| # | Decision | Unblocks |
|---|---|---|
| 1 | **Which sub-sectors are the September focus?** (recommend the P1s: B2B SaaS, Hospitality→Accommodation, Professional Services→Legal/Accounting; + any owner pick) → set `Status = Target` | the entire chain (②–⑥) |
| 2 | Any **campaign idea + context** ready now? | the DB 4 fast-path (§4) |
| 3 | The **DRAGON** terminology ruling | Content DB 2 row 10 |
| 4 | Green-light the **🟢 today list** (§5) | 4 standing gaps closed now |
| 5 | When to open **scraping** (Part E: API key + cost governance + Approval-Matrix row) | decision-maker contacts + ICP/Signal scoring |

---

## 6.5 Decisions & Gaps ledger (standing view — the owner's "we need to view them")

*Maintained rollup of what is decided, what is still the owner's call, and where the relevant-but-empty fields are. Updated as state changes.*

**✅ Decisions LOCKED**
- Multi-vertical universe · Sector = the first live IntOS slice · kernel + Industry Revenue Engine loaded (25 verticals · 321 sub-sectors · 87-row Industry Offer Matrix · 211 Intelligence findings).
- **September focus is data-derived** (P1: B2B SaaS · Hospitality→Accommodation · Professional Services→Legal & Accounting) — not owner-blocked.
- **Pilot = Hospitality → Accommodation** (owner-chosen). Build the cross-loop here first, then generalize.
- **Data posture = recommend + register now; paid people-data MCPs deferred** to post-pilot, owner-authorized, gated.
- CRM = **ClickUp (live)** — Sector bridges onto it, no new store. "real-time" = **freshness cadence**, not a live stream. No unattended web.

- **LSEI (2026-08-19)** — calendar layer becomes source-backed + directional. **2 net-new DBs** (14 Signal Sources · 15 Market Routes); **Google Calendar → Notion Calendar** as the sync/view path; **market scope = Kenya-inbound**; **decide-then-apply**. Spec: [`CALENDAR_INTELLIGENCE.md`](CALENDAR_INTELLIGENCE.md); doctrine: `SECTOR_ACTIVATION_CONTRACT.md` §15.

- **Sector OS Architecture (2026-08-20)** — **Universal Core vs Sector Plugin** separation; a sector is activated by authoring a **14-slot plugin pack**, never by adding a store. **Hospitality = Sector Plugin #001.** Four owner decisions locked: **(1)** Destination Intelligence = **net-new DB 16 Destination Profile** (keeps shared Geography lean), **(2)** the **Client Calendar is a resolution, not a store**, **(3)** **Gate 1 is documentation-only** — no Notion/ClickUp writes, **(4)** the extra opportunity factors (Timeliness · Destination Fit · Client Fit) land as **upstream engine gates**, leaving Content DB 5's score and `content-opportunity-mapper`'s `output_schema` untouched. Architecture: [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md); doctrine: `SECTOR_ACTIVATION_CONTRACT.md` §16; plugin: [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md).

**⚑ Decisions OPEN (owner)**
| # | Decision | Blocks / affects |
|---|---|---|
| 1 | **DRAGON** terminology ruling | Content DB 2 belief row 10 |
| 2 | Review **cadence** for Sectors Master (`Last / Next Review`) | freshness governance |
| 3 | `Strategic Priority` (Primary/Secondary/Tertiary) per vertical | GTM sequencing beyond the P1 pilot |
| 4 | **When to authorize the paid people-data MCP** (Apollo/Clay) | real decision-maker contacts → CRM (§6 item 5) |
| 5 | The **go-live scraping gate** (API key + cost governance + Approval-Matrix row + Legal posture) | all 🔴 contact/company/ICP/Signal fields |
| 6 | **Zoho Books lapsed-trial** decision (downgrade / pay / re-open) — *money-facing standing flag* | Invoice object (`CRM_SCHEMA.md`) |
| 7 | Any **campaign idea + context** to seed the DB 4 fast-path (§4) | Content chain shortcut for a `Target` sector |
| 8 | **Google Calendar account** to hold the external `.ics` subscriptions (which address, agency-owned) | the whole live-calendar follow layer (`TECHSTACK_OS.md` §3) |
| 9 | **Paid event-API cost gate** (event-data / ticketing discovery APIs, `AEIT_08` §3.2 T3) | breadth of event discovery — T1 sources work without it |
| 10 | Owner of the undocumented **`Platform Overlays`** relation on DB 7 (`collection://bb21b3fc-…`) | must be identified before DB 7 is extended (`SECTOR_NOTION_SCHEMA.md` DB 7 flag) |

**🟢 GAPS — empty-but-relevant, fillable now (per `Target` sector, web-cited):** Sector **Linguistics** (EMPTY — blocks Content) · **Audience Roles** (EMPTY — blocks Content) · Sector **Intelligence** for the 88 established industries (none) · Decision-Maker **titles/triggers** for established · **Sector State + Forecast** (empty) · per-sector **Sector Signals** depth (only 3 rows full) · Sheet 07 relationship map (SaaS, pending).

**🟢 GAPS — LSEI (specified 2026-08-19)** — *⚠️ superseded 2026-08-20 by the Gate 2 block below; kept for the audit trail:* **DB 14 Signal Sources** (~~not built~~ **✅ built, 0 rows** — the candidate pack is `AEIT_08` §3.2, every row still unverified) · **DB 15 Market Routes** (~~not built~~ **✅ built, 0 rows** — seed set `Germany/UK/US/Regional-Africa → Kenya`) · DB 7 **extensions** (`Signal Source`/`Market Routes`/`Signal Role`/`Previous Signal Date`/`Change Reason` + 5 `Signal Type` values) · **Geography** Kenya-inbound tree (holds only Global/EU/USA today — no Africa, no city level) · **`Source Tier` null on 20 of 28** signal rows (back-fill) · the **4 Hospitality rows sourced to vendor blogs** (re-source to T1, supersede on contradiction — 🔴 never delete) · DB 7 **retirement list** (legacy `Calendar Type`; title `Event` → `Signal`; `Content Relevance`; `Community / Entry Strategy`).

**✅ CLOSED at Gate 2 (2026-08-20) — structure built, 0 rows:** **DB 14 Signal Sources** · **DB 15 Market Routes** · **DB 16 Destination Profile** all live · DB 7 wired to DB 14/15 (`Signal Source`, `Market Routes`) · DB 3 `Geography` relation + `Demand Pattern` category · DB 11 `Destination` level. Also closed: the **`Tool-Stack Chaos` drift** (documented 2026-08-19, never actually applied to DB 3 — created this pass).

**🟢/🔲 GAPS — still open after Gate 2:** every one of the 3 new DBs is **empty** — no source is `active`, no route exists, no destination is profiled · **Maasai Mara + Diani still mis-levelled `City`** (re-levelling = plugin slot P4, first Gate 3 action) · the **Hospitality source pack is entirely `candidate`, with no URLs recorded** — nothing may be promoted without a live verification call · plugin **P3 demand-pattern rows** and **P12 pillar/angle set** (unauthored — research tasks) · the **`sector-calendar-resolver`** — **superseded 2026-08-24: it is now skill S09, not a Gate-5 agent** ([`SECTOR_SKILL_MATRIX.md`](SECTOR_SKILL_MATRIX.md) §2), because the Resolution Engine is eight deterministic steps rather than reasoning; still blocked on DB 14/15/16 having rows · Content DB 5's **`Destination` relation** (**now unblocked** — add it when Content next opens) · the 4 vendor-blog-sourced Hospitality signal rows (re-source to T1, supersede on contradiction, never delete) · a **second-sector proof** (the Protocol is unvalidated until one non-hospitality sector runs through it without a core edit).

**🔴 / ⚫ GAPS — gated or template (never guessed):** real decision-maker **contacts** + Company data (scraping) · **ICP + Prospect Signal scores** (need real companies) · live-booking/property numbers (⚫ template) · CRM `Related Clients` / `CRM Opportunities` (no real deals yet).

---

## 7. Honesty ledger (what this plan will never do)

- Never fill Decision-Maker **contacts**, ICP, or Signal Scores by research — those are scraped real data (🔴) or agent runs against real companies.
- Never fill live-booking/property numbers or any performance metric — template/⚫ until a real system connects.
- Never spray per-sector intelligence across all 321 sub-sectors — depth-first on `Target` sectors only.
- Never retype upstream truth downstream — Content inherits Sector via rollups; Sector references CRM by ID.
- Every 🟢 fill is web-cited and dated, `Confidence` set to match; a blank stays blank rather than becoming a guess.

---

## 8. Changelog
- **v0.1 (2026-08-19):** Created. Full field-by-field disposition of the 13 Sector + 8 Content databases, the critical-path unlock sequence, the campaign fast-path, and the fillable-today list. Companion to `SECTOR_NOTION_SCHEMA.md` + `CONTENT_INTELLIGENCE_SCHEMA.md`. — Claude Code (Opus 4.8)
- **v0.2 (2026-08-19, ADDENDUM 4):** Reframed §1 step ① — focus is **data-derived** (Sector Priority Score names the P1 `Target` set), not owner-blocked; pilot = Hospitality→Accommodation. Added **§6.5 Decisions & Gaps ledger** (standing view — locked / open / 🟢 / 🔴-⚫). Updated §5 close to the depth-first-on-P1 discipline. — Claude Code (Opus 4.8)
- **v0.4 (2026-08-20, Sector OS Architecture Gate 1):** Recorded the four locked owner decisions (DB 16 Destination Profile · Client Calendar as a resolution not a store · documentation-only Gate 1 · opportunity factors as engine gates) and added the **Sector OS Architecture gap block** — DB 16 unbuilt, the DB 3/DB 11 extensions specified-not-applied, two plugin slots unauthored, the resolver agent deliberately deferred, and the Protocol unvalidated until a second sector runs it. — Claude Code (Opus 5)
- **v0.3 (2026-08-19, LSEI Pass 1):** Recorded the LSEI decisions in §6.5 (2 net-new DBs · Google/Notion Calendar sync · Kenya-inbound scope · decide-then-apply), added **3 open owner decisions** (Google Calendar account · paid event-API cost gate · the unowned `Platform Overlays` relation), and added the **LSEI 🟢 gap block** — DB 14/15 unbuilt, Geography missing Africa/Kenya, `Source Tier` null on 20 of 28 signal rows, and the 4 vendor-blog-sourced Hospitality rows awaiting re-sourcing to T1. — Claude Code (Opus 5)
