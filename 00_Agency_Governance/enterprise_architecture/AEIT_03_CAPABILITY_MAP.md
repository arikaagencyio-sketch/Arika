# AEIT_03 — Agency Capability Map (Analysis)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `GLOBAL_OS.md` §6 cross-department Capability rollup ("none yet — would live in Agency
Governance"). Rolls up the per-department §3 Capability Registries into one agency view.

> Purpose: view the agency as **capabilities** (what it can do) rather than departments (who does
> it). This exposes capabilities that are duplicated across departments, and capabilities that have
> no real owner. Every capability names one **primary owner**; multiple owners = a reconciliation
> item (see `AEIT_04`/`AEIT_05`).

---

## 1. Capability → owner → consumers

### Intelligence capabilities (the future IntOS surface)
| Capability | Primary owner | Consumers | State |
|---|---|---|---|
| Acquire market/sector intelligence | Sector (01) | Offer, Marketing, Sales | Real (owner-curated xlsx + agents) |
| Map a sector (360° / audience / linguistics) | Sector (01) | Marketing, Offer, Branding | Real |
| Classify ICP fit (Tier 1/2/3/Anti-ICP) | Sector (01) | Sales, Marketing | Real — **but CRM field owner mis-assigned, see AEIT_04** |
| Score a prospect (90-pt signal scorecard) | Sector (01) | Sales, Marketing | Real |
| **Validate / verify / trust-score information** | **— none —** | all | **MISSING → IntOS (`AEIT_07`)** |
| **Resolve entities / dedupe across sources** | **— none —** | all | **MISSING → IntOS** |
| **Maintain a knowledge graph** | **— none —** (Branding `bois` is local only) | all | **MISSING → `AEIT_06`** |

### Commercial capabilities
| Capability | Primary owner | Consumers | State |
|---|---|---|---|
| Package/price offers | Offer (02) | Marketing, Sales | Real (Offer Engineering Registry) |
| Generate demand | Marketing (03) | Sales | Structure; thin OS |
| Produce content | Content (04) | Marketing, Sales | Real |
| Qualify leads | Sales (05) *(consumes Sector's ICP)* | — | Real; ownership overlap w/ Sector, Marketing, ClientPartner |
| Close deals | Sales (05) | Client Success, Finance | Real pattern |
| Partner/referral acquisition | ClientPartner Acq (06) | Sales | Real |
| Diagnose / audit (Gateway Offer) | Audits (14) | Sales, delivery offers | Chain built, never delivered |
| Advise (executive) | Consulting (15) *(the Owner delivers)* | client | By design, not delegated |

### Delivery & production capabilities
| Capability | Primary owner | Consumers | State |
|---|---|---|---|
| Onboard / retain clients | Client Success (07) | Operations, Sales | Real (lifecycle states) |
| Deliver engagements | Operations (08) | Finance | Thin (no raw source) |
| Build automations | Automation (16) | all | Real dept; estate mostly inert |
| AI enablement / readiness | AI Enablement (17) | Automation, client | Class-3 gate blocked (Legal) |
| Express brand identity | Branding (12) | Content, Design, Experience Eng, Marketing | Real + `bois` |
| Produce creative assets | Design (19) | Content, Marketing, Experience Eng | Real; ~2 images runway |
| Produce interactive experiences | Experience Eng (20) | Marketing, Offer (future) | Real Spec System |

### Enterprise / support capabilities
| Capability | Primary owner | Consumers | State |
|---|---|---|---|
| Manage money / cashflow / forecast | Finance (09) | Governance | Thin OS + `finos-plugin` |
| Manage legal / compliance / IP | Legal (10) | all client-facing | 🔴 nothing lawyer-reviewed |
| People doctrine / hiring trigger | HR (11) | Owner | Doctrine only (solo+AI) |
| Manage tool stack + verify it | Tech Stack (13) | all | Real inventory + verifier |
| Govern (constitution, risk, approvals) | Governance (00) | all | Backbone |
| **Orchestrate / execute agents** | Governance (00) / `arika-runtime` | all | Built; never run persistently |
| Synchronize the 7 Cognitive Calendars | Operations (08) *(calendar-orchestrator)* | all | Real orchestrator |

---

## 2. Cross-cutting "meta" capabilities — mostly missing

The user's target list includes Validate, Learn, Optimize, Forecast, Manage Risk. Mapped honestly:

| Meta-capability | Owner today | Reality |
|---|---|---|
| Validate / verify intelligence | none | **Missing** — the core IntOS gap (`AEIT_07`) |
| Learn (feedback → improvement) | per-dept `_memory/runtime.jsonl` | **Mostly fictional** — only Branding + Design have real streams (`AEIT_04`) |
| Optimize | none formal | Aspirational; depends on Learn, which depends on runs that haven't happened |
| Forecast | Finance (09) + 7 calendars | Structure exists; no data (0 clients) |
| Manage risk | Governance (00) + per-dept §9 | Real structure; risk vocabulary inconsistent (`AEIT_04`) |

**Reading:** the agency is strong at *doing* capabilities (produce, close, deliver) and weak at
*intelligence* meta-capabilities (validate, learn, optimize). That asymmetry is precisely what IntOS
is meant to close — and confirms IntOS is the right next platform, once activation is unblocked.

---

## 3. Duplicated / contested capabilities (hand-off to AEIT_04)

- **Lead/prospect scoring** is claimed by **four** departments: Sector (01, the real scorecard),
  Sales (05, CRM `ICP_fit_score` owner), Marketing (03, "lead scoring" capability), ClientPartner
  (06, its own 5-domain scoring). → reconcile ownership in `AEIT_05`.
- **CRM** appears as a capability in three places: Governance (00, the canonical schema), Tech Stack
  (13, a dead duplicate ClickUp template), ClientPartner (06, a *client-facing* CRM they sell).
  → distinguish/deprecate in `AEIT_04`.

---

## 4. Decision Log
- **2026-07-22 — Capability map rolled up.** Surfaced the produce-strong / validate-weak asymmetry
  and 2 contested capability clusters (scoring, CRM). — Claude Code (Opus 4.8)

## 5. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
