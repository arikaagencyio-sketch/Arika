# Hospitality Revenue Content OS — Full Push Readiness Packet

> ⚠️ **PREPARATION ONLY · NOT A RUN · NOT QUOTABLE · NOT A COMMERCIAL LAUNCH ARTIFACT.**
> This packet prepares the first full **manual** push from Sector (01) into Offer (02) and on to downstream departments, for one real hospitality property. **It runs nothing.** Writing it ran no agent, published no event, started no scheduler or daemon, read no `.env`, and wrote no memory log. It contains **no price, fee, rate, currency, floor or quote language**, and it does not change the Offer Engineering Registry. The Hospitality Revenue Content OS remains **Working Hypothesis / Not Quotable**.

## 0. Status

| Field | Value |
|---|---|
| **Type** | Readiness packet — Offer (02), crossing Sector (01) → Offer (02) → Content (04) · Marketing (03) · Sales (05) |
| **Date** | 2026-09-14 |
| **Readiness** | ❌ **NOT READY TO EXECUTE** — waiting on owner inputs OI1–OI9 (§4) and pre-run decisions **RD2 and RD7** (§9.1). *RD1, RD3, RD4, RD5 and RD6 decided 2026-09-20 — but **RD3's rotation is not yet performed**, **RD2's storage question is open**, and **RD4 settles method only, with no property checked**, so **PG0 and PG1 are both still unmet**.* |
| **Offer** | Hospitality Revenue Content OS · "Direct Booking Engine" (gateway: OTA Leakage & Direct-Booking Audit) — Working Hypothesis / Not Quotable, not registered |
| **Parent documents** | `Draft 41` (structural OEOS, §12 control test) · `Hospitality Revenue Content OS - Delivery Capacity and Cost Model Worksheet.md` · `OFFER_OS.md` §3, §5, §12 · `01_Sector/SECTOR_OS.md` §5–§6 · `01_Sector/sector_plugins/hospitality/HOSPITALITY_PLUGIN.md` · `.claude/skills/sector-handoff-packet/SKILL.md` (S10) |
| **Tracker** | `00_Agency_Governance/OWNER_INPUT_NEEDED.md` item 72 (this packet's owner inputs); items 59, 71, 57, 58 (blockers, §7) |

**How this differs from the control test.** The 2026-09-13 Hospitality Sector → Offer Control Test (`Draft 41` §12) validated control flow on **test fixtures**. This push uses **one real, owner-supplied property** and **public data only**. It is still manual and advisory, and every hand-off is still carried by a person.

### Readiness at a glance

| Step | Ready? | What blocks it |
|---|---|---|
| **PG0 · Session preconditions** | ❌ | ~~RD1 pilot identity~~ ✅ *decided 2026-09-20* · ◐ **RD2 — workspace location set 2026-09-20, but its storage, access and retention questions are still open** · ◐ **RD3 — decided 2026-09-20 (rotate first), but the rotation is not yet performed or verified** |
| **PG1 · Before Sector** | ❌ | OI1–OI8 *(none supplied)* · ~~RD4 Sector fit method~~ ✅ *decided 2026-09-20 — method only; **no property checked or classified*** |
| **PG2 · Before `offer-orchestrator`** | ❌ | Sector fit record and S10 packet, owner-reviewed |
| **PG3 · Before `offer-oeos-engineer`** | ❌ | Orchestrator output, owner-reviewed · RD7 |
| **PG4 · Before `offer-pricing-floor-analyst`** | ⛔ **Skipped — RD5 decided 2026-09-20** | Not run, and **no negative re-test**. **Skipped, not passed** — **no hotel floor, price, pricing band, cost figure or positive pricing verdict is approved or inferred**. A positive pricing run remains impossible: no hotel floors, no H-band support, no approved test prices |
| **PG5 · Before Content / Marketing / Sales** | ❌ | Offer output, owner-reviewed *(none exists)* · ~~RD6 downstream scope~~ ✅ *decided 2026-09-20 — notes only;* **PG5 has not passed** |

---

## 1. Source of truth

| | |
|---|---|
| **Repository** | `C:\Users\USER\OneDrive\Documents\The Agency Drafts` — branch `master`, remote `git@github.com-arikaagency:arikaagencyio-sketch/Arika.git` |
| **State when this packet was written** | Working tree clean, level with its last-fetched `origin/master` at `f8feba5`; Batches 1–3 and the estate-count reconciliation committed; `estate_event_gate.py` passing (115 agents · 75 waits with no emitter: 4 external, 62 manual, 9 unassigned) |
| **Runtime** | `arika-runtime/` inside this repository. Every `arika run` in §8 runs from here |
| **Stale clone — out of scope** | `C:\Users\USER\OneDrive\Documents\ChatGPT\Agency.Repo` is a stale clone of the same GitHub repository: HEAD `acbbd9f` (2026-09-12), 36 commits behind, 6 uncommitted files, and none of `Draft 41`, the worksheet, or the Batch 1–3 fixes. **Do not run from it, read from it, write to it, pull into it or copy from it.** Its only unique work — corrected estate counts — was re-derived into this repository on 2026-09-14 |

> 🔴 **Name collision — resolve before any client data exists (RD2).** Worksheet §5.2 records the owner's tool decision as *"a dedicated client folder outside this git repository (called Agency.Repo in the decision)"*. **The existing `ChatGPT\Agency.Repo` is a git clone of this repository, not a client folder.** Anything saved inside it sits in a working tree of the agency repository and could be committed and pushed. The client folder must be a different location, outside every git working tree.

**Every operator session — Claude Code, Codex, ChatGPT or a person — starts in the repository path above.**

---

## 2. Push objective

| | |
|---|---|
| **What** | The first full manual push: Sector (01) → Offer (02) → prepared downstream hand-offs to Content (04), Marketing (03) and Sales (05) |
| **Sector** | Hospitality → Accommodation (Hotels) — Sector Plugin #001, `Offer-Ready` since 2026-08-28, geography scope **Kenya-inbound** (plugin P4) |
| **Pilot** | **One real company or property, supplied by the owner** (§4). None is named in this packet |
| **Mode** | Manual and advisory end to end. Each agent runs once, by hand (`arika run`). Each hand-off is carried by a person and reviewed at a gate (§6) before the next step |
| **Data** | Public information and clearly labelled owner-supplied notes only (§3) |

**What the push produces:** a Sector fit record and Sector hand-off packet for the pilot; an orchestrator intake and a structural, non-pricing OEOS run grounded in that property's public footprint; an owner review of both; and, only after that review, draft hand-off notes for Content, Marketing and Sales.

**What the push cannot produce — by design:**
- **No audit verdict.** The diagnostic gate needs the client's own data (`Draft 41` §3.2 G2–G3; worksheet §1.4 MD1, MD4 required). Public observation can raise a **pre-audit hypothesis** about leakage; it can never classify it. Every Offer output is labelled that way.
- **No price, quote, proposal, outreach, publication, CRM lead or client engagement.**
- **No event chaining.** Nothing is published; no agent triggers another.

**This packet prepares the run only.** It does not run agents.

---

## 3. Allowed data

### 3.1 What may be used

| Data | Allowed | Conditions | Label |
|---|---|---|---|
| **Public company / property information** — name, location, property type, published room count, published brand or group affiliation | ✅ | Record the source URL and the date viewed. Never infer a figure the source does not state | `[PUBLIC · url · date]` |
| **Public website and booking-path observations** | ✅ | Viewed manually by a person or an interactive session — **no automated crawling or scraping** (the scraping gate is closed: `01_Sector/FIELD_POPULATION_PLAN.md` item 5). **Stop at the public boundary:** no account creation, no test or partial booking, no personal details entered into any form | `[PUBLIC · url · date]` |
| **Public OTA presence** | ◐ **Only if OI7 = yes** | Manual viewing only; record listing facts (present or absent, listed property type). **Never copy guest reviews or reviewer names.** OTA terms of use are not assessed here | `[PUBLIC-OTA · url · date]` |
| **Screenshots of public pages** | ◐ **Only if OI8 = screenshots** | Public pages only, stored **in the client folder, never in this repository**. Default is **text notes only** | `[PUBLIC · screenshot · date]` |
| **Owner-supplied notes** | ✅ | Business context only. Unverified by definition — never presented as a Sector finding or a client fact | `[OWNER-SUPPLIED · date]` |
| **Sector intelligence** (plugin, Notion DBs) | ✅ | Benchmarks stay benchmarks — never a claim about this property (`Draft 41` QG3) | `[SECTOR · Medium]` |
| **Reviewer inference** | ✅ | Clearly marked as a hypothesis to test in an audit, never a finding | `[INFERENCE]` |
| **Anything not known** | — | Recorded as unknown. **No estimated room count, direct share, commission or occupancy** | `UNKNOWN` |

### 3.2 What may not be used

- ❌ **Guest personal data** of any kind — names, contact details, booking records, identifiable reviews.
- ❌ **Client private exports** (worksheet MD1–MD3, real sent messages from MD5). There is no engagement and no legal review path (item 59).
- ❌ **Named individuals' contact details** — emails, phone numbers. Decision-maker **titles only**; people-data stays gated (plugin P9).
- ❌ **Secrets or API keys** — never in inputs, notes or outputs. Nobody opens or prints `arika-runtime/.env`.
- ❌ **Sector benchmarks presented as facts about the property**, or unratified plugin rules cited as client evidence (item 31i: the P2 matrix is internal operating use only).

### 3.3 What reaches the repository — read before any run

> 🔴 **Every `arika run` appends its full `--input` and its recommendation to the agent's memory log** (`arika-runtime/src/memory-writer.ts`). Those logs are **tracked by git**, and the auto-sync hook **commits and pushes within minutes**. Memory logs are append-only and are not edited afterwards.
>
> **So anything placed in `--input` becomes permanent repository history** — including the property's name, if it is typed there. The input is also sent to the model provider (Anthropic) as part of the prompt.

**Identity rule — ✅ decided 2026-09-20 (RD1).** `--input` carries a **pilot ID only**, plus public-derived descriptors at the level the step needs (archetype, H-band, destination, labelled observations) and nothing personal. **Use only the pilot ID in repository logs and runtime inputs.** The real **name ↔ pilot ID mapping** and every full note live in the **client folder, outside every git working tree** — never in this repository, and never in a runtime input.

| Identity | Rule |
|---|---|
| **`A001`, and `A001-P01`…`A001-P09`** | The internal **simulation** group and its existing simulated units. **Preserve these IDs.** They are not part of the `PILOT-H-*` series, and they **do not satisfy item 72's real-property requirement** |
| **`PILOT-H-001`** | **Reserved** for the **first real, owner-supplied property** |
| **`PILOT-H-002`, `-003`, …** | Sequential IDs for **additional real properties only**, and only **as each one is separately approved** |
| **A real group ID** | ⏳ **Not assigned, deliberately.** Document the group structure first; decide its ID as a **separate** decision (RD1a, §9.1) |

| Where | Holds |
|---|---|
| **Client folder** — `C:\Users\USER\Arika_Pilots\PILOT-H-001` *(provisional workspace, RD2, 2026-09-20: created **empty**; verified outside every git working tree and outside OneDrive; **not** an approved storage platform)* | Pilot name ↔ ID key · observation notes · screenshots (if allowed) · Sector fit record · S10 packet · seed brief · full stdout of every run · owner review notes · downstream hand-off drafts |
| **This repository** | Memory-log lines written by the runs (automatic) · the S10 skill-run record (`01_Sector/_memory/skill_runs.jsonl`) · this packet's pseudonymous run log (§11) · changelog entries |

---

## 4. Required owner inputs before the full push

| # | Input | Required | Format | Used for | If missing or out of range |
|---|---|---|---|---|---|
| **OI1** | **Pilot company / property name** | ✅ | Text; stored only in the client folder | Every step; replaced by the pilot ID in any `--input` (RD1) | **Stop — nothing to push** |
| **OI2** | **Website URL** | ✅ | URL | Public observation; anti-ICP check | **Stop.** A property with no website is anti-ICP (`OFFER_OS.md` §3 seed: it needs a build first) |
| **OI3** | **Booking path URL or instructions** | ✅ | URL, or steps from the homepage | Booking-path observation (the public side of MD4) | **Stop** if no direct booking path exists — anti-ICP. If the path needs a login or a booking to see, observe up to that boundary only |
| **OI4** | **Geography / market** | ✅ | Country, destination, town | Sector scope and Destination Fit | **Stop** outside Kenya-inbound (plugin P4). Nairobi, Maasai Mara and Diani have Destination Profiles. **Mombasa and any unprofiled place are blocked by Destination Fit** — stop, or the owner commissions a profile first (skill S05, a separate Sector job) |
| **OI5** | **Property type** — plus brand, chain or group affiliation, if public | ✅ | One plugin P2 archetype | Archetype rules; anti-ICP; H3 condition | City / Conference Hotel · Safari Lodge · Beach Resort are ruled in live geography. Other archetypes: flag, continue with reduced Sector grounding. `Destination Property` is unruled. **Stop** for a `Hospitality Group` (unresolvable today, item 31i) or a chain with a central brand.com / direct-booking team (anti-ICP; Decision 71) |
| **OI6** | **Approximate room count — only if public or owner-supplied** | Optional | Number with its label | H-band | **H1 30–60 · H2 61–120** are the MVP scope. **Stop** for H3 (121–250, or 2–5 properties) or under 30 — both outside the approved MVP. Unknown: continue with `H-band: UNKNOWN`, and MVP fit stays unconfirmed |
| **OI7** | **May OTA pages be inspected?** | ✅ | Yes / No | §3.1 | Treated as **No** |
| **OI8** | **Public screenshots, or text notes only?** | ✅ | Screenshots / Text only | §3.1 | Treated as **text notes only** |
| **OI9** | **Known owner-supplied business context** | Optional | Labelled notes | Seed brief context | None assumed. **Label every line `[OWNER-SUPPLIED]`.** Useful: relationship status (cold / known contact / referral), any past approach, what the owner believes about OTA dependency. **Not:** guest data, private exports, personal contact details |

---

## 5. Department sequence

| # | Department | Job in this push | Mechanism | Not in this push |
|---|---|---|---|---|
| 1 | **Sector (01)** | Validate **sector fit** (Hospitality → Accommodation, plugin #001) and **company fit** (archetype, geography, H-band, anti-ICP), then produce the **Sector hand-off packet** | **Manual, not agent-run.** Fit is checked against plugin P1, P2, P4 and the H-bands. The packet follows skill **S10** `sector-handoff-packet` and reaches Offer by **text reference** (S10: Offer route works) | `sector-icp-fit` and `sector-signal-scorer` (see note) · any Notion or CRM write |
| 2 | **Offer (02) — intake** | `offer-orchestrator` on the reviewed seed brief | `arika run offer-orchestrator` — the **manual equivalent of the human-invoked `OFFER_INTAKE_REQUESTED` intake**. The event itself is **not** published | Registry change of any kind |
| 3 | **Offer (02) — engineering** | `offer-oeos-engineer`, structural and **non-pricing**; Phase 11 stays BLOCKED | `arika run offer-oeos-engineer` — the brief is **carried by hand**, not by `OFFER_BRIEF_RECEIVED` | Any tier figure |
| 4 | **Offer (02) — pricing advisory** | ⛔ **Skipped — RD5 decided 2026-09-20.** Not run, and **no negative re-test** | `arika run offer-pricing-floor-analyst` | A positive floor check — impossible today (§7) |
| 5 | **Content (04) · Marketing (03) · Sales (05)** | **Prepare later hand-offs only after the Offer output is reviewed** (PG5) | ✅ **RD6 decided 2026-09-20 — hand-off notes only**: the *angle*, never the artifact (S10 boundary law), and **no downstream agent runs** — not `content-intelligence-hub`, not `marketing-market-intelligence`, not `sales-lead-qualification`, and no other | Publication · outreach · CRM lead · **Notion or ClickUp write** · `sales-lead-qualification` · any downstream agent run |

> 🔴 **Surfaced while preparing this packet — no Sector agent can check a hotel's company fit today.** `sector-icp-fit` classifies only against the **B2B SaaS** three-tier ICP (a hotel would return `out_of_scope` or `anti_icp`). `sector-signal-scorer`'s service match is limited to `marketing · sales · partner_acquisition · automation`. `sector-intelligence-mapper`'s grounding names B2B SaaS as the real sector, and the runtime has no Notion client, so it cannot read the Accommodation intelligence that lives in Notion and the plugin. The skill that would classify a prospect, **S12 `sector-prospect-classifier`, is not built** (scraping gate). Hence step 1 is manual — decided by RD4. No existing record of this mismatch was found in the repository (searched 2026-09-14).

**No event chaining, at any step.** Only one-shot `arika run` processes. **Never** `npm start`, `npm run dev` or `node dist/index.js` — those boot the scheduler, webhook server and event bus (item 58: 30 declared schedule triggers, scheduler not approved). An `arika run` result's declared `emits` are **not published** (`executor.ts` does not publish — estate gate check 4).

---

## 6. Gate conditions before each step

**Global stop rules — apply at every step:**
- A run fails, or reports truncation — stop; do not re-run blind.
- Any output or input contains a **price, amount, fee, floor or quote language**, an outcome guarantee, or a claim that the offer is quotable — stop; do not carry it forward.
- **Personal data or a secret appears** in an input or output — stop at once and tell the owner. The memory line cannot be edited, so it is an owner-level incident, not a clean-up task.
- The working tree shows changes other than the expected memory-log lines, or the estate gate fails — stop.
- Any step would require publishing an event, booting the runtime, creating a CRM lead, writing to Notion, or contacting the property — stop.
- The owner has not reviewed the previous step's output — stop.

| Gate | Before | Must be true | Stop if | Human review |
|---|---|---|---|---|
| **PG0** | The session starts | Operating in this repository (§1), not `ChatGPT\Agency.Repo` · `git status` clean and not behind · `estate_event_gate.py` passes · RD1, RD2, RD3 decided · client folder exists **outside every git working tree** · `arika-runtime/dist/` built (`npm run build` — compiles only) · nobody opens `.env` | Any item false | Owner confirms RD1–RD3 in writing |
| **PG1** | **Sector** | OI1–OI8 answered · RD4 decided · public observation notes captured (R1) with labels · no guest data captured | No website or no direct booking path (anti-ICP) · outside Kenya-inbound · unprofiled destination (incl. Mombasa) · `Hospitality Group` · chain with a central brand.com team · H3 or under-30 rooms | — |
| **PG2** | **`offer-orchestrator`** | Sector fit record says **in scope**, with every basis labelled · S10 packet assembled; confidence carries the **weakest** item (Sector findings are Medium) · packet and seed brief contain no personal data, secret, private export or invented figure · seed brief uses the pilot ID (RD1) and states: public data only, pre-audit, H1/H2 MVP, non-pricing, not quotable | Fit record says out of scope · the owner has not approved the **exact** seed-brief text — it becomes permanent repository history | ✅ **Owner approves the seed brief character for character** |
| **PG3** | **`offer-oeos-engineer`** | Orchestrator output reviewed: `registry_action`, `misaligned_assumptions`, `control_questions` · top-level `requiresHumanApproval` honoured | `registry_action: reject` · `needs_more_seed_data` **and** the owner has not approved a structural-only continuation (RD7) · `add_new_offer` or `update_existing_offer` read as permission to change the registry — **it is not; the registry stays unchanged** | ✅ Owner review note saved |
| **PG4** | **`offer-pricing-floor-analyst`** | ⛔ **Do not run — RD5 decided 2026-09-20: skip, with no negative re-test.** **Skipped, not passed.** *Reference only, not authorised — a re-test would have required:* input `arr_band: "unknown"`, a statement that no hospitality floor exists and B2B SaaS floors must not be applied, and **no `proposed_price`** | RD5 not approved · anything but `insufficient_data` with `setup_floor` and `retainer_floor` null — **record the failure; never use a returned band or floor** | ✅ **RD5 decided 2026-09-20 — skip** |
| **PG5** | **Content / Marketing / Sales** | OEOS output reviewed and accepted **as an internal structural hypothesis only** · ✅ **RD6 decided 2026-09-20 — notes only**, and the notes are drafted **only after the Offer output is reviewed by the owner, and then each proposed hand-off is reviewed individually** · every hand-off labelled *pre-audit · Working Hypothesis · Not Quotable* · no price, outcome claim, or unlabelled benchmark | Offer output carries a price, guarantee or client-specific claim · the owner has not reviewed it · a hand-off would publish, contact, create a lead, write to **Notion or ClickUp**, or run any downstream agent | ✅ Owner approves each hand-off note |

---

## 7. Known blockers

| Blocker | Effect on this push | Blocks the push? | Source |
|---|---|---|---|
| **Legal review path** — counsel named, both letters unsigned, scope not agreed | No client data, engagement, contract, audit or claim review. OTA terms of use and screenshot handling are **not** assessed | ◐ Not a public-data internal push; **blocks every client-facing step** after it | Item 59; worksheet §11 |
| **Offer is Working Hypothesis / Not Quotable** | Every output is internal; no proposal, outreach or publication | ◐ Shapes the outputs | `Draft 41` §0; `OFFER_OS.md` §3 |
| **No money / cost conversion** | Planning hours exist (worksheet §12); cost in money does not | ❌ Blocks any positive pricing step | Worksheet §12.6; item 71 |
| **No hotel pricing floors** | `offer-pricing-floor-analyst` must return `insufficient_data` | ❌ Blocks pricing | `Draft 41` §11.4; item 71 |
| **Pricing agent has no H-band support** | Its `arr_band` accepts only `A`–`D` or `unknown` | ❌ Blocks a positive pricing test | Worksheet §7; item 71 |
| **Test prices not approved** | No `proposed_price` in any input | ❌ Blocks pricing | Decision 71; worksheet G7 |
| **API key rotation — decided, not done** | Every run would still use the key whose value was displayed in a session transcript on 2026-09-13 | ✅ **RD3 decided 2026-09-20: rotate first.** ❌ **Still blocks PG0** — **the rotation itself is not performed and not verified** — and AG-19's condition is that the rotation be **recorded as done**, so the act and the record are both still outstanding | Item 57 · A001 D16 / AG-19 |
| **Scheduler not approved** | Never boot the runtime; `arika run` only | ◐ Constrains the method | Item 58; `GLOBAL_OS.md` v0.28.3 |
| **Stale clone exists** | Must not be used. ✅ **The name collision is resolved 2026-09-20** — the pilot workspace is `Arika_Pilots\PILOT-H-001`, a different name in a different tree | ◐ **RD2's storage question** before PG0 | §1 |
| **No Sector agent fits a hotel company** *(surfaced here)* | Sector fit is manual; S12 is unbuilt | ✅ **RD4 decided 2026-09-20 — manual, by design.** The capability gap is **accepted, not closed**: `sector-icp-fit` stays B2B-SaaS-only and S12 stays unbuilt | §5 note |
| **Runs write inputs to git-tracked, auto-synced logs** *(surfaced here)* | A real name in `--input` becomes permanent history | ✅ **RD1 decided 2026-09-20** — pilot ID only; the mapping stays in the client folder. **The log behaviour itself is unchanged** | §3.3 |
| **Downstream routes** | Marketing (03) has **no route** from Sector (item 31k); Sales (05) is event-only with **no delivery**; Content (04)'s relation route works but is held at PG5 | ◐ Hand-offs are carried by hand | S10 Step 0; item 31k |
| **Public data cannot pass the diagnostic gate** | Offer output is a pre-audit hypothesis, never a verdict | ◐ Shapes the outputs | `Draft 41` §3.2 |

---

## 8. Proposed manual run sequence — not executed

**Conventions.** Commands assume Git Bash, run from `arika-runtime/`. `<CLIENT>` is the client folder (RD2). `--input` takes a JSON string; keep the JSON in a file in `<CLIENT>` and pass it with `$(cat …)`. `tee` keeps the full stdout in `<CLIENT>`; the memory-log line is written automatically.

| # | Step | How | Expected output | Saved to | Stops the sequence |
|---|---|---|---|---|---|
| **R0** | **Preflight** (PG0) | `git status --short --branch` · `python 00_Agency_Governance/enterprise_architecture/estate_event_gate.py` · `npm run build` · confirm RD1–RD3 and `<CLIENT>` | Preflight checklist, all ✅ | §11 run log (repo, no pilot data) | Any PG0 item false |
| **R1** | **Public observation capture** — no agent | Person or interactive session views the website, booking path (OI2–OI3) and, if OI7 = yes, OTA listings; labels every line (§3.1) | `R1_public_observations.md` | `<CLIENT>` | No website or booking path · the public boundary needs a login or booking · guest data encountered (do not capture it) |
| **R2** | **Sector fit check** (PG1) — **manual, no agent (RD4)** | Session reads plugin P1, P2, P4, P9–P11 and checks the OI4 destination's profile, read-only | `R2_sector_fit_record.md` — sector fit, then **a cited basis for each of**: archetype (P2) · destination profile (P4) · size band / H-band · website · direct booking path · group or chain anti-ICP; then verdict `in scope` / `out of scope`. **a required check that fails or is unknown takes the PG1 stop rule, or stays `unresolved` — it may never be written up as an `in scope` verdict** | `<CLIENT>`; verdict only in §11 | Any PG1 stop rule |
| **R3** | **Sector hand-off packet** — skill S10, manual apply | Assemble per S10 and `AEIT_09` §1: finding, timing, language, audience titles, offer match (Hospitality Revenue Content OS entry), destination profile. Re-measure the route table from `01_Sector/contracts/event-catalog.json`. Record each destination's outcome: **Offer — delivered by text reference** · **Content — held at PG5** · **CRM — held (no lead in this push)** · **Sales, Marketing, Operations — `HANDOFF_FAILURE`** | `R3_sector_handoff_packet.md` · one S10 record in `01_Sector/_memory/skill_runs.jsonl`, then `python 01_Sector/contracts/skill_run_gate.py` | Packet `<CLIENT>`; skill-run record in the repo, per the S10 contract | Out-of-scope verdict in R2 · a `Needs verification` signal handed off as settled · the skill-run gate fails |
| **R4** | **Seed brief** (PG2) — no agent | Draft `{"seed_brief": "…"}`: pilot ID; labelled public observations; S10 summary; constraints — public data only, pre-audit hypothesis, H1/H2 MVP, audit-gated two stages, non-pricing, Phase 11 BLOCKED, Not Quotable | `R4_seed_brief.json`, **owner-approved text** | `<CLIENT>` | Owner has not approved the exact text · personal data, secret or invented figure present |
| **R5** | **`offer-orchestrator`** | `node dist/triggers/cli.js run offer-orchestrator --input "$(cat "<CLIENT>/R4_seed_brief.json")" \| tee "<CLIENT>/R5_offer-orchestrator.json"` | Intent (strategic, commercial, execution), misaligned assumptions, control questions, routing plan, `registry_action` · next line of `02_Offer/_memory/runtime.jsonl` | stdout `<CLIENT>`; memory line in the repo (automatic) | Run fails or truncates · `reject` · `needs_more_seed_data` without RD7 approval · any price or claim |
| **R6** | **`offer-oeos-engineer`** (PG3) | Build `R6_oeos_input.json` from the approved brief plus the orchestrator's routing plan and control-question answers; restate *non-pricing, Phase 11 BLOCKED, no figure in any tier*. Run `node dist/triggers/cli.js run offer-oeos-engineer --input "$(cat "<CLIENT>/R6_oeos_input.json")" \| tee "<CLIENT>/R6_offer-oeos-engineer.json"` | Structural phases, immutable and customizable components, risks, tiers with investment **BLOCKED** · next memory line | stdout `<CLIENT>`; memory line in the repo | Any figure in a tier's `investment` · outcome claim · truncation |
| **R7** | **`offer-pricing-floor-analyst`** (PG4) — ⛔ **SKIPPED.** RD5 decided 2026-09-20: not run, and no negative re-test | *Retained for reference only and **not authorised** — any future run needs its own decision:* `R7_pricing_input.json` = `{"arr_band": "unknown", "context": "Hospitality pilot. No hospitality pricing floor exists. Do not apply B2B SaaS ARR floors. No proposed price."}` · `node dist/triggers/cli.js run offer-pricing-floor-analyst --input "$(cat "<CLIENT>/R7_pricing_input.json")" \| tee "<CLIENT>/R7_pricing.json"` | `floor_check: insufficient_data`, `arr_band: unknown`, both floors `null` | stdout `<CLIENT>`; memory line in the repo | Any band `A`–`D` or non-null floor → record as a failed test, use nothing |
| **R8** | **Offer review** — no agent | Owner compares R5–R6 with `Draft 41`: what is property-specific, what is generic, what is wrong; decides accept-as-hypothesis or reject | `R8_offer_review.md` | `<CLIENT>`; decision only in §11 | Rejected · owner not available to review |
| **R9** | **Downstream hand-off drafts** (PG5) — ⛔ **no agent at all (RD6, decided 2026-09-20)** | Three notes, *angle not artifact*, each labelled pre-audit · Not Quotable: **Content (04)** content-angle brief · **Marketing (03)** market-angle note (carried by hand — no route, item 31k) · **Sales (05)** pre-qualification note (carried by hand — no delivery). ⛔ **Declined by RD6 (2026-09-20) — no downstream agent runs.** *(Reference only: `content-intelligence-hub` and `marketing-market-intelligence` would each **create a new tracked memory log** — `04_Content/_memory/runtime.jsonl`, `03_Marketing/_memory/runtime.jsonl` — which is part of why they are declined.)* | `R9_handoff_content.md` · `R9_handoff_marketing.md` · `R9_handoff_sales.md` | `<CLIENT>` | PG5 not passed · anything would publish, contact the property, create a CRM lead, or write to Notion or ClickUp · `sales-lead-qualification` requested (it needs a CRM `lead_id`; no lead is created in this push) |
| **R10** | **Close-out** — no agent | `git status` (expect only memory-log lines, the S10 record and the §11 log) · estate gate · confirm no runtime process is running · fill §11 · changelog entries in `OFFER_OS.md` §15 and `SECTOR_OS.md` §15 · update the memory-log line counts the repo states (`AEIT_04` §C4; item 57 cites Offer lines 1–5) | Run log complete | Repo (pseudonymous) | Unexpected file changes · gate failure |

---

## 9. Open decisions

### 9.1 Needed before this packet is complete — before the push can execute

| # | Decision | Recommended | Blocks |
|---|---|---|---|
| ~~**RD1**~~ | ✅ **DECIDED 2026-09-20 — pseudonymous pilot IDs in repository-logged inputs.** Full rule in §3.3 | **Pilot ID only.** `PILOT-H-001` reserved for the first real property; sequential `PILOT-H` IDs for further real properties as each is approved; `A001`/`A001-P0n` preserved as simulation IDs that do **not** satisfy item 72; the name ↔ ID mapping stays in the client folder | ~~PG0~~ — **RD1 no longer blocks PG0; RD2 and RD3 still do** |
| **RD1a** *(new 2026-09-20)* | **The real group ID** — what identifies a real multi-property group, if one is ever pushed | ⏳ **Undecided by design.** Document the group structure first, then decide the ID separately. Not required for a single-property push | Nothing today |
| **RD2** | ◐ **PARTLY DECIDED 2026-09-20 — the workspace *location* only.** `C:\Users\USER\Arika_Pilots\PILOT-H-001`, **created empty**. Verified: no ancestor is a git repository; it sits outside **all five** git working trees under `Documents` (including `ChatGPT\Agency.Repo` and this repository); no junction or symlink; and **outside OneDrive entirely**, which removes the sync exposure worksheet §5.2 flagged. It holds an **ID-named folder and nothing else** — no property name, no name ↔ ID mapping, no intake, no screenshot, no client data | ⏳ **RD2 is NOT passed.** Still open: the storage **platform** is still unregistered and unreviewed (`TECHSTACK_OS.md` §3) · **legal/privacy review of client-data handling is still blocked by G5** (worksheet §11.5; LQ2 — hosting location, access control, retention, deletion at close) · **access control** · **retention and deletion** · **backup and durability** — a local-only folder trades OneDrive sync exposure for **no redundancy** · and whether real client data may be placed there **at all**. **The storage platform is not approved** | PG0 — **still blocks** |
| ~~**RD3**~~ | ✅ **DECIDED 2026-09-20 — rotate the exposed API key before the first runtime-backed pilot run.** The question is settled; running on the current key is **not** an option | ⏳ **Execution condition, still outstanding:** **the rotation itself is not performed and not verified** — and AG-19's condition is that the rotation be **recorded as done**, so the act and the record are both still outstanding. Nothing was read, printed, tested or changed here. **The same rotation also clears A001's D16 / AG-19**, which blocks runtime-backed Phase 3 work — one rotation, two blockers, but neither clears until it is done **and** recorded | PG0 — **still blocks** |
| ~~**RD4**~~ | ✅ **DECIDED 2026-09-20 — a manual Sector fit check**, against the existing Hospitality rules and this packet's **PG1 / R2** procedure. **`sector-icp-fit` is not extended and S12 is not built** as part of this decision — both stay unbuilt work, not push prerequisites | ⏳ **Method only. No property has been checked or classified, and no fit record exists.** A later record must cite a **basis for each** of: archetype (P2) · destination profile (P4) · size band / H-band · website · direct booking path · group or chain anti-ICP. And **a required check that fails or is unknown takes the PG1 stop rule, or stays `unresolved` — it may never be written up as an `in scope` verdict**. **A001's `SIMULATED_VERDICT` lines establish nothing about a real property** — they show only that the gates ran | PG1 — **still blocks** |
| ~~**RD5**~~ | ✅ **DECIDED 2026-09-20 — SKIP the pricing step.** R7 / `offer-pricing-floor-analyst` is **not run** in this push, and **no negative re-test is run either** | ⏳ **Skipping approves nothing:** **no hotel floor, price, pricing band, cost figure or positive pricing verdict is approved or inferred**, and the Offer stays **Working Hypothesis / Not Quotable**. It **closes none** of the separate pricing and commercial blockers (§7; item 71 — hotel floors, pricing-agent H-band support, test prices, cost-to-deliver in money) and **authorises no later pricing run**: any future run needs its own decision | PG4 — **skipped, not passed** |
| ~~**RD6**~~ | ✅ **DECIDED 2026-09-20 — downstream hand-off NOTES ONLY** for Content (04), Marketing (03) and Sales (05). The notes are drafted **only after the Offer output is reviewed by the owner, and then each proposed hand-off is reviewed individually** | ⏳ **Bounded:** each note stays **pre-audit · Working Hypothesis · Not Quotable** and carries **an angle, never a publishable artifact and never a performance claim**; **no downstream agent runs** — not `content-intelligence-hub`, not `marketing-market-intelligence`, not `sales-lead-qualification`, and no other; and **nothing is published, the property is not contacted, no CRM lead is created, and nothing is written to Notion or ClickUp**. **RD6 approves no wider test.** Any later exercise of further departments, agents, skills or plugins needs **its own scope and gate decisions** | PG5 — **has not passed** |
| **RD7** | If the orchestrator returns `needs_more_seed_data`, may OEOS still run **structurally**, as the control test did? | **Yes, structural only, with the orchestrator's questions carried into R6** — owner confirms | PG3 |
| **OI1–OI9** | **The pilot itself** (§4) | — | PG1 |

### 9.2 Needed before quoting or commercial launch — not needed for this push

| Decision | Source |
|---|---|
| Engage counsel with an agreed scope: contract, DPA and NDA templates, audit-data terms, sub-processor register, and — if ever client-facing — OTA and screenshot handling | Item 59; worksheet §11; G5 |
| Cost-to-deliver in money | Worksheet §12.6; `Draft 41` §9 #1 |
| Hotel floor derivation method | Worksheet §8 #10 |
| Pricing-agent H-band support | Worksheet §8 #11 |
| Approval of test figures | Decision 71; worksheet G7 |
| Price band · audit-fee credit policy · proof-generation method | `Draft 41` §9 #3–#5 |
| Launch ICP reconciliation (seed vs plugin vs H-bands) | `Draft 41` §9 #7 |
| Definition of "dominant" and the mixed-finding rule · L2/L3 thresholds | `Draft 41` §9 #9; worksheet §8 #12 |
| Redirect destinations for (c), (d) and technical (b) | `Draft 41` §9 #10 |
| Registry decision — enter as #13 once priced | `Draft 41` §9 #19 |
| A Marketing (03) route and Sales (05) delivery mechanism from Sector | Item 31k; S10 |
| Governance rows before anything is automated or the scheduler starts | Item 58 |

---

## 10. How this packet was prepared

Written on 2026-09-14 from repository documents only: `AGENTS.md`, `GLOBAL_OS.md`, `SECTOR_OS.md`, `OFFER_OS.md`, `Draft 41`, the delivery/cost worksheet, `OWNER_INPUT_NEEDED.md` items 57, 58, 59, 71, 31i and 31k, the Hospitality plugin, the S10 skill, the eight relevant agent specs, and the runtime's CLI and memory-writer source.

**No agent was run, no event was published, the scheduler and daemon were not started, `.env` was not read, and no memory log was written.** No price, fee, rate, currency or quote language was added, and the Offer registry table was not changed.

---

## 11. Run log — pseudonymous, filled during the push

| Step | Date | Operator | Gate | Result | Memory-log lines written | Client-folder artifact |
|---|---|---|---|---|---|---|
| R0 Preflight | — | — | PG0 | — | — | — |
| R1 Public observation | — | — | — | — | — | — |
| R2 Sector fit | — | — | PG1 | — | — | — |
| R3 S10 packet | — | — | — | — | — | — |
| R4 Seed brief | — | — | PG2 | — | — | — |
| R5 `offer-orchestrator` | — | — | — | — | — | — |
| R6 `offer-oeos-engineer` | — | — | PG3 | — | — | — |
| R7 Pricing (default skip) | — | — | PG4 | — | — | — |
| R8 Offer review | — | — | — | — | — | — |
| R9 Downstream hand-offs | — | — | PG5 | — | — | — |
| R10 Close-out | — | — | — | — | — | — |

---

## 12. Changelog

- **2026-09-20 — RD6 decided: downstream hand-off notes only.** Content (04), Marketing (03) and Sales (05) receive **three drafted notes and nothing else**, and the notes are drafted **only after the Offer output is reviewed by the owner, and then each proposed hand-off is reviewed individually**. **Bounded:** each note stays **pre-audit · Working Hypothesis · Not Quotable** and carries **an angle, never a publishable artifact and never a performance claim**; **no downstream agent runs** — not `content-intelligence-hub`, not `marketing-market-intelligence`, not `sales-lead-qualification`, and no other; and **nothing is published, the property is not contacted, no CRM lead is created, and nothing is written to Notion or ClickUp**. §8's R9 optional-agent branch is **declined** and kept as reference only, noting that each such run would create a **new tracked memory log**. **RD6 approves no wider test.** Any later exercise of further departments, agents, skills or plugins needs **its own scope and gate decisions**. **Also closed a half-stated rule:** §5, §6 and §8 barred a Notion write but not a ClickUp write — RD6 bars both, and all three now say so. **🔴 PG5 has not passed**, **PG0 and PG1 remain unmet** (RD3's outstanding rotation, RD2's open storage question, OI1–OI8 unsupplied), and the packet is **still NOT READY TO EXECUTE** — no Offer output exists for the owner to review. RD2's storage half, RD7, RD1a and OI1–OI9 are untouched. No property researched, no client data used, no `.env` or key read, no agent or skill run. — Claude Code (Opus 5)
- **2026-09-20 — RD5 decided: SKIP the pricing step in this push.** R7 / `offer-pricing-floor-analyst` is **not run**, and **no negative re-test is run either** — the earlier `insufficient_data` result already stands, and a re-run would add a pilot line to a git-tracked memory log for no new evidence. **🔴 Skipping approves and infers nothing:** **no hotel floor, price, pricing band, cost figure or positive pricing verdict is approved or inferred**, and the Offer remains **Working Hypothesis / Not Quotable**. It **closes none** of the separate pricing and commercial blockers (§7; item 71 — hotel floors, pricing-agent H-band support, test prices, cost-to-deliver in money) and **authorises no later pricing run**: any future run needs its own decision. §0, §5, §6, §8 and §9.1 now read **skipped, not passed**; the re-test procedure is retained as **reference only, not authorised**. **Item 71 is deliberately untouched** — a decision not to run a pricing agent changes none of its pricing blockers. **PG0 and PG1 remain unmet** (RD3's outstanding rotation, RD2's open storage question, OI1–OI8 unsupplied), and the packet is **still NOT READY TO EXECUTE**. RD2's storage half, RD6–RD7, RD1a and OI1–OI9 are untouched. No property researched, no key or `.env` read, no agent or skill run, no runtime code changed. — Claude Code (Opus 5)
- **2026-09-20 — RD4 decided: a manual Sector fit check for the first real single-property pilot.** The check runs against the existing Hospitality rules and this packet's **PG1 / R2** procedure. **`sector-icp-fit` is not extended and S12 is not built** — the capability gap is **accepted, not closed**. **🔴 Method only: no property has been checked or classified, and no fit record exists.** §8's R2 row now requires a **cited basis for each** of archetype (P2) · destination profile (P4) · size band / H-band · website · direct booking path · group or chain anti-ICP — it previously named four of the six, omitting website and direct booking path — and records that **a required check that fails or is unknown takes the PG1 stop rule, or stays `unresolved` — it may never be written up as an `in scope` verdict**. **A001's `SIMULATED_VERDICT` lines establish nothing about a real property.** §0, §7, §8 and §9.1 updated. **PG1 remains unmet** (OI1–OI8 unsupplied), **PG0 remains unmet** (RD3's outstanding rotation, RD2's open storage question), and the packet is **still NOT READY TO EXECUTE**. RD2's storage half, RD5–RD7, RD1a and OI1–OI9 are untouched. No property was chosen or researched, no fit record created, no agent or skill run, no client data used, and no runtime code changed. — Claude Code (Opus 5)
- **2026-09-20 — RD3 decided: rotate the exposed API key before the first runtime-backed pilot run.** Running on the current key is **not** an option; the key whose value appeared in a session transcript on 2026-09-13 is to be replaced first. **🔴 The decision is all that changed:** **the rotation itself is not performed and not verified** — and AG-19's condition is that the rotation be **recorded as done**, so the act and the record are both still outstanding, and **no `.env` or key value was read, printed, tested or changed** in recording it. §0, §7 and §9.1 updated. **The same rotation also clears A001's D16 / AG-19**, which gates runtime-backed Phase 3 work — one rotation answers both, and neither clears until it is performed **and** recorded. **PG0 remains unmet** on two counts — the outstanding rotation **and** RD2's open storage question — and the packet is **still NOT READY TO EXECUTE**. OI1–OI9, RD2's storage half, RD4–RD7 and RD1a are untouched. No agent, skill or runtime was run, and no key was rotated. — Claude Code (Opus 5)
- **2026-09-20 — RD2 partly decided: the pilot workspace *location* only.** `C:\Users\USER\Arika_Pilots\PILOT-H-001` was **created empty** after checks: no ancestor is a git repository, it lies outside **all five** git working trees found under `Documents` (including the stale `ChatGPT\Agency.Repo` clone and this repository), there is no junction or symlink on the path, and it is **outside OneDrive**, which removes the sync exposure worksheet §5.2 flagged. **It contains nothing** — no property name, name ↔ ID mapping, intake, screenshot or client data, and none may be placed there yet. §0, §3.3, §7 and §9.1 updated; the stale-clone **name collision is resolved**. **🔴 RD2 is NOT passed and the storage platform is NOT approved.** Still open: the storage **platform** is still unregistered and unreviewed (`TECHSTACK_OS.md` §3) · **legal/privacy review of client-data handling is still blocked by G5** (worksheet §11.5; LQ2 — hosting location, access control, retention, deletion at close) · **access control** · **retention and deletion** · **backup and durability** — a local-only folder trades OneDrive sync exposure for **no redundancy** · and whether real client data may be placed there **at all**. **PG0 remains unmet** (RD2's storage question, RD3), the packet is **still NOT READY TO EXECUTE**, and OI1–OI9 with RD3–RD7 and RD1a are untouched. No property was researched, no key or `.env` read, no key rotated, no agent or skill run, nobody contacted, and no client data copied. — Claude Code (Opus 5)
- **2026-09-20 — RD1 decided: pseudonymous pilot IDs in repository-logged inputs.** §3.3's "default rule (pending RD1)" becomes the **identity rule**: pilot ID only in repository logs and runtime inputs; the real **name ↔ ID mapping lives in the client folder outside every git working tree**, never in this repository. `PILOT-H-001` stays **reserved for the first real, owner-supplied property**; further real properties take **sequential `PILOT-H` IDs only as each is approved**; and `A001` with `A001-P01`…`A001-P09` are **preserved** as simulation IDs which **still do not satisfy item 72**. **A real group ID is deliberately not assigned** — recorded as new open decision **RD1a**: document the group structure first, decide the ID separately. §0, §7 and §9.1 updated. **🔴 Nothing else moves:** **PG0 is still not met** (RD2 and RD3 open), the packet is **still NOT READY TO EXECUTE**, RD2–RD7 and OI1–OI9 are untouched, no property was chosen or researched, no client folder was created, no key was read or rotated, and no agent or skill was run. — Claude Code (Opus 5)
- **2026-09-14 — Created (preparation only).** Readiness packet for the first full manual Hospitality push — Sector (01) → Offer (02) → Content (04) · Marketing (03) · Sales (05) — on one real, owner-supplied property, public data only. Defines the source of truth and the out-of-scope stale clone; the push objective and what it cannot produce (no audit verdict — public data cannot pass the diagnostic gate); allowed and forbidden data; nine owner inputs with stop rules; the department sequence; six gates (PG0–PG5) and global stop rules; known blockers; an eleven-step manual run sequence with outputs, save locations and stop conditions; and seven pre-run decisions separated from the launch-level ones. **Surfaced while preparing it:** (1) every `arika run` writes its full input to a git-tracked, auto-synced memory log, so a property name in `--input` becomes permanent history — RD1; (2) no Sector agent can check a hotel's company fit — `sector-icp-fit` and `sector-signal-scorer` are B2B SaaS-only and S12 is unbuilt — RD4; (3) worksheet §5.2 names the client folder "Agency.Repo", the same name as the stale git clone — RD2. **Not ready to execute.** No agent run, no event published, no scheduler, no `.env`, no memory-log write; no prices; registry table unchanged; still **Working Hypothesis / Not Quotable**. — Claude Code (Opus 5)
