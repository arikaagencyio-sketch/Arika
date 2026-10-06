# 05 — Workflow Map: operational workflows and handoffs

**Protocol §4, §15, §22:** how work flows, where it is handed off, and where it does not connect.

> **One fact governs this whole file.** The runtime **never publishes an event**: `executor.ts` returns `emitted` and never calls the bus; the only `publish()` site is an inbound external webhook (`AEIT_11_RUNTIME_TRUTH_STANDARD.md` §1; `estate_event_gate.py` PASS 2026-10-06: *"the runtime still does not publish"*). Every agent-to-agent handoff below is therefore at most `CONNECTED` (both ends declared and checked), **never `LIVE`**. Every handoff that has actually happened was **carried by a person**.

---

## 1. Workflow inventory relevant to Hospitality

| # | Workflow | Owner | Trigger | Steps | Output | Reality (test) |
|---|---|---|---|---|---|---|
| W1 | **Sector Activation** (Gates A–I) | Sector (01) | Owner activates a sector on its Priority Score | Qualify → Scope → Author plugin → Register sources → Load → Resolve + falsify → Route → Live-loop → Generalize | A plugin; lifecycle promotion | A–G run for Hospitality; **H and I specified, unrun** (`SECTOR_ACTIVATION_PROTOCOL.md` header) |
| W2 | **Commercial Cross-Loop** (7 links) | Sector (01) | Sub-sector reaches `Status = Target` | WHEN → WHY → HOW → WHO → WHICH → WHAT → WHERE | Outreach-ready CRM packet | Run for Accommodation 2026-08-19 (`SECTOR_OS.md` §15) |
| W3 | **Calendar Resolution** (skill S09) | Sector (01) | Calendar requested, or a signal changes | SELECT → SCOPE → ENRICH → FILTER (archetype) → FILTER (client) → DERIVE → SCORE + 3 gates → EMIT | Layered calendar (computed) | `LIVE` — 3 dated Gate F runs; **6 of 8 steps exercised** (step 5 needs a real client) |
| W4 | **Sector handoff packet** (skill S10) | Sector (01) | Offer-Ready, Gate G, or resolver output | Assemble findings, language, audience, offer match, timing, CRM tags → route per destination | Packet; `HANDOFF_FAILURE` where a destination is unreachable | `BUILT`; spent on fixtures (SECTOR-SF1/SF2); **3 of 6 destinations deliver** (GLOBAL_OS v0.27.0) |
| W5 | **Offer engineering** (OEOS 12 phases) | Offer (02) | Seed brief | orchestrator → OEOS engineer → pricing-floor analyst | Engineered offer | Hospitality: control test **COMPLETE for control flow**, Phase 11 BLOCKED (Draft 41 §12) |
| W6 | **Full Push** (R1–R7, PG0–PG5) | Offer (02) | Owner supplies a real property (OI1–OI9) | Sector fit (by hand) → S10 → orchestrator → OEOS (conditional) → notes to 04/03/05 | Pre-audit hand-off notes | **NOT READY** — 0 of 5 required gates passed; PG0 satisfied for *public-only preparation* only |
| W7 | **Public prospecting cycle** | Sales (05) | Owner request (2026-10-03) | Verify public evidence → reserve `ORG-*` outside Git → qualify the buyer level → one coordinated touch → review → release → CRM write/read-back → follow-up from actual send | ID-only queue + drafts | `LIVE` once: 4 companies, 23 levels, 3 drafts saved; **0 sent, 0 CRM rows** |
| W8 | **Client intake** (S1–S5) | Governance (00) + overlay | Stage gates | S1 desk profile → S2 discovery → S3 audit data → S4 onboarding → S5 measurement | Answers file in the client folder | `intake_gate.py` `BUILT`; S1 allowed; S2 needs ID3; **S3–S5 blocked** |
| W9 | **MVP delivery** (2 stages) | Offer (02) → owner | Signed engagement | Stage 1: M1 audit snapshot + M2 root-cause verdict (+ M7 redirect) → Stage 2 (only on a content/journey root cause): M3–M6 | Audit + blueprint | `DESIGNED`; **never run**; capacity one H1/H2 client at a time |
| W10 | **A001 sandbox** | Sector (01) | Owner decisions D1–D21 | Phases 0–3, document-only; one fixture run | Mechanism findings only (D20) | Document-only pilot **closed** 2026-09-16; D21 spent 2026-09-21 |
| W11 | **Content production** (ACCOS 1–10) | Content (04) | Sector events / manual | Intelligence → opportunity → narrative → brief → multiplication → publishing gate | Briefs, translations | Stores `LIVE`; **no Content agent has ever run** (no memory stream) |
| W12 | **Creative pipeline** | Design (19) | `Publishing Status = "Ready for Design"` | storyboard → reuse gate → production plan → ⟨human approves + generates⟩ → brand/AI-artifact check → Canva assembly → ⟨human publishes⟩ | Finished asset | Cloud routine restored 2026-07-15 (one forced run); hourly cadence **not proven since** |
| W13 | **Client delivery chain** | Operations (08) | `SCOPE_DEFINED` | scheduler → risk → QA → `DELIVERY_COMPLETE` → Finance | Delivered engagement + billable event | `CONNECTED` on paper; never run |
| W14 | **Retention / expansion / advocacy / offboarding** | Client Success (07) | health-score / tenure / contract | 6 synthesized workflows | Renewals, referrals, exits | `DESIGNED` (Claude-synthesized, `CLIENTSUCCESS_OS.md` §10); never run |
| W15 | **Daily command + calendar sync** | Operations (08) | cron 06:00/07:00, Monday | state → ranked actions; 7 calendars → conflicts | Today's plan | Cron declared; **scheduler not approved** → never fired |

## 2. The spine — every department handoff the Hospitality pilot needs

| Handoff | From → To | Mechanism | Contract | State | Evidence |
|---|---|---|---|---|---|
| H1 | Sector → Offer | S10 packet reference → offline Offer inbox receiver; text reference | `AEIT_09` (none specific); `delivery-authorisations.json` | `CONNECTED` on a **fixture** (SYNCO-02); no real delivery | `01_Sector/delivery/` |
| H2 | Sector → CRM (Lead tags) | S10 writes 4 bridge fields | `CRM_SCHEMA.md` "Sector (01) → CRM bridge" | Round-trip **verified on disposable fixtures** 2026-09-29; **no real Lead tagged** | `CRM_SCHEMA.md` 2026-09-29 entries |
| H3 | Sector → Content | Notion relations (DB 5 ← DB 3/7/9) | `CONTENT_INTELLIGENCE_SCHEMA.md` §3 | `CONNECTED`, used 2026-08-19 | — |
| H4 | Sector → Sales | `PROSPECT_SCORED` / `ICP_CLASSIFIED` events | `AEIT_09` HP-1 | `CONNECTED`; **nothing publishes** | estate gate |
| H5 | Sector → Marketing | ~~`DEMAND_SHIFT`~~ (archived, 31d) | — | ❌ **no route** — item 31k | `OWNER_INPUT_NEEDED.md` 31k |
| H6 | Sector → Operations | ~~`COMPRESSION_EVENT`~~ (archived) | `OPERATIONS_OS.md` §12a | ❌ **no route** — item 31k | same |
| H7 | Marketing/Content/06 → Sales | `LEAD_CREATED` | `AEIT_09` HP-2; `CRM_SCHEMA.md` handoffs | `CONNECTED`; never fired | `MARKETING_OS.md` §5 |
| H8 | Sales → Client Success | `DEAL_CLOSED_WON`; Opportunity → Client | `AEIT_09` HP-3 | `CONNECTED`; never fired | — |
| H9 | Client Success → Operations | `SCOPE_DEFINED` | `AEIT_09` HP-4 | `CONNECTED`; never fired | `OPERATIONS_OS.md` §4 |
| H10 | Operations → Finance | `DELIVERY_COMPLETE` → invoice (Class 3) | `AEIT_09` HP-4 | `CONNECTED`; **invoicing has no matrix row**; USD→KES calculator unbuilt | `AUTOMATION_APPROVAL_MATRIX.md`; `AEIT_09` HP-4 failure modes |
| H11 | Content → Design | `Publishing Status = "Ready for Design"` | `AUTOMATION_APPROVAL_MATRIX.md` real row | `LIVE` once (2026-07-15 forced run) | matrix |
| H12 | Design → Presence → market | human publishes | `PRESENCE_OS.md` | ❌ nothing published; 0 connected channels | `PRESENCE_OS.md` §16 |
| H13 | Market → Measurement → Learning → Sector | performance store | — | ❌ **absent** | `SECTOR_OS_ARCHITECTURE.md` §1.3 finding 3 |
| H14 | Audit verdict → Offer redirect intake | (c)/(d)/technical (b) redirect | Draft 41 §3 | ❌ **no engineered destination** for any redirect | Draft 41 §3.1, §9 #10 |
| H15 | Offer (hospitality audit) → Audits (14) | — | — | ❌ `audits-scoping` enums cannot scope a hotel audit (A001 AG-14) | `CLIENT_INTAKE_PROFILE.md` §9 G-4 |

## 3. Missing or broken handoffs — named

1. **Measurement → Learning → Intelligence (H13)** — the loop's closing edge does not exist anywhere. `OWNED-UNBUILT` (Marketing owns performance and has no store). → `HV-18`, `HV-33`.
2. **Sector → Marketing / Operations (H5, H6)** — no route since the 31d archival. Known (item 31k). For the pilot, `RD6` already chose *hand-written notes only*, which is sufficient. → `HV-20`.
3. **Audit → redirect (H14)** — every non-content root cause (pricing/rate, tech-stack, technical booking-engine) ends in a redirect to an offer that does not exist. A redirect is a valid outcome, but the destination is `UNASSIGNED`. → `HV-27`.
4. **Hospitality audit ownership (H15)** — the Gateway Offer's department (Audits 14) cannot scope the hospitality gateway; Draft 41 runs it under Offer (02) by hand. Workable for one MVP; ambiguous ownership at scale. → `HV-30`.
5. **Offer → Proposal → Agreement** — blocked twice: no price (Phase 11) and no reviewed contract (Legal). → `HV-04`, `HV-27`.
6. **Client approval → system of record** — Draft 41 Phase 8: *"WhatsApp threads leave decisions unrecorded — approvals must be confirmed in the system of record."* There is no such record for a deliverable. → `HV-09`.
7. **Content/Design for a client** — Tier 3 outputs "land in Content DB 7 + the ClickUp CRM" (`SECTOR_OS_ARCHITECTURE.md` §2), but DB 7 cannot say which client a brief belongs to. → `HV-11`.
8. **Prospecting → CRM** — the queue is outside Git; CRM registration awaits account access and deduplication; `crm_delivery: not_verified`. → `HV-05`.
9. **Decision → enactment** — ratified decisions (R1, R3) never reached the files they amend; no register tracks "decided, not yet applied". → `HV-21`.

## 4. The protocol's loop — Information → Decision → Action → Outcome → Learning

| Transition | Where it happens today | Strength | Where it breaks |
|---|---|---|---|
| **Information** | Sector DBs with provenance (DB 3 217 findings, DB 7 signals, DB 14 sources, DB 16 profiles); intake answers | **Strong** — tiered sources, honesty states, verification dates | Row-level provenance empty on DB 9 (0/28) and DB 10 (0/399) — `sector_truth_gate.py` output |
| **Information → Decision** | Owner decisions recorded with reasoning in department §8 logs, A001 D1–D21, packet RD1–RD7, Decision 71 | **Strong** — reasoned, dated, quoted | Decisions live in ≥10 registers with ≥15 ID schemes; the consolidated tracker lags three weeks (`HV-07`, `HV-10`) |
| **Decision → Action** | Authorisation registers (draft → approved → spent) for system actions; human runs for everything else | **Strong for system actions**; informal for business work | No task entity; no enactment tracking (`HV-21`); auto-sync pushes without running gates (`HV-01`) |
| **Action → Outcome** | Execution records (`_memory/*.jsonl`), fixture outcomes, prospecting queue (`sent: 0`) | **Honest** — never claims an unverified outcome | **No client outcome exists yet**; no booking/revenue data path designed (`HV-18`) |
| **Outcome → Learning** | Changelog "lessons", memory files, `AEIT_11` rules generalised from incidents | **Rich but prose-only** | Learning is not queryable; P2 cells cannot move to `observed`; Sales `Learning_Loop_Log.md` is an empty template (`HV-33`) |
| **Learning → Information** | — | — | **Open** |

**Verdict (`CONFIRMED`):** the agency runs the first three transitions with unusual rigour — but for *its own construction*, not yet for a client. The last two transitions are designed and unbuilt, which the repository states about itself.
