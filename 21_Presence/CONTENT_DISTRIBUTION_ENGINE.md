# Content Distribution Engine — Specification (Presence 21)

**Version:** v0.1.0
**Last updated:** 2026-08-02
**Owner:** Mary Thuo (Agency Governance, 00) · coordinated by Presence (21)
**Status:** **Design ratified by owner 2026-08-02 (platform set, executor, host, gate model all decided).** Reality-gated, pre-build — zero social accounts exist, no instance deployed. This is the design the engine gets built to, not a record of a running system.

> Read `GLOBAL_OS.md`, then `21_Presence/PRESENCE_OS.md` and `00_Agency_Governance/AGENCY_COMMERCIAL_DOCTRINE.md`. This spec is the executable elaboration of Presence's §4 Workflow Index. Rich visual companions (owner-facing): the **Vision Map** (https://claude.ai/code/artifact/36a207db-9453-4f63-a8d2-51614f786c52) and the **Workflow Runbook** (https://claude.ai/code/artifact/f9c4e557-7236-46eb-b5b2-473294c42757).

---

## 1. What this is

The system that turns produced content into consistent, high-volume, **doctrine-compliant** presence across every confirmed platform. It is **decoupled** — a Reservoir buffer sits between production and publishing so volume never breaks the chain: a generation outage can't create a posting gap, and a platform outage can't back up production.

**Ownership (one-owner discipline preserved — a coordinator was added, no capability moved):**
- **Presence (21)** coordinates the engine + owns the economics gate.
- **Content (04)** produces the multiplication tree (`content-multiplication-engine`).
- **Design (19)** supplies assets (Production Engine).
- **Marketing (03)** owns distribution strategy + measurement truth.
- **Automation (16)** owns the runtime/orchestration + the approval-matrix rows + reliability monitoring.
- **TechStack (13)** registers + verifies the tools.

**Core principle (PIL §1):** *one strategic narrative → many native executions.* This is what makes high output both possible and doctrine-compliant — volume comes from multiplying a few strategic assets, never from filling a calendar.

---

## 2. Confirmed decisions (owner, 2026-08-02)

| Decision | Confirmed value |
|---|---|
| **Platform set (10, launch-priority order)** | 1·LinkedIn · 2·Facebook · 3·Instagram · 4·Threads · 5·TikTok · 6·Pinterest · 7·Website (owned hub) · 8·X · 9·Newsletter · 10·YouTube. **Tumblr out of scope.** |
| **First-test platform** | LinkedIn (position 1) — the full body runs end-to-end here before scaling. |
| **Executor (L6)** | **Postiz, self-hosted** — posts natively to all 10 via one API; chosen over per-post platform-API builds and over paid per-channel SaaS (flat cost, uncapped volume). |
| **Host (L0)** | **Hostinger KVM 2 (8GB) + Coolify** — Ubuntu 24.04, running Coolify (free self-hosted PaaS); Postiz + Postgres + Redis deployed and **Running (healthy)** 2026-08-07. Paid by card (Hostinger accepted the virtual card Railway/Stripe rejected; the M-Pesa Kenyan-VPS fallback was unneeded). Render retained as candidate for the L5 orchestrator. |
| **Gate model** | **Two gates** — a Concept Gate (pre-production) + a Pre-Publish Check (pre-queue) + an automated pre-flight at the publish moment. |

All 10 platforms are already PIL-profiled. This resolves PIL's open `[OWNER: confirm the canonical in-scope set]` flag (`04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md` §4).

---

## 3. Architecture — the 8 layers (decoupled)

| Layer | Role | Owner · tool |
|---|---|---|
| **L0 Foundation** | Host + token vault + the identity spine | **Hostinger KVM 2 (8GB) + Coolify** (Postiz stack, live) · Render (L5 orchestrator, later) |
| **L1 Supply** | Assets produced in batches, ahead of demand | Design (19) · OpenArt/KIE.ai/Canva |
| **L2 Multiply** | 1 asset → many native variants; wrapped as a packet | Content (04) · `content-multiplication-engine` |
| **L3 Reservoir** | Buffer + queue-of-record (packet state) | Content/Presence · Notion brief DB (extended) |
| **L4 Governance** | The two gates, approved at template level | Presence (21) `presence-economics-gate` + Content `content-publishing-gate` |
| **L5 Orchestration** | Cadence engine + rate governor + retry/dead-letter | Automation (16) · orchestrator on Render |
| **L6 Executor** | Per-platform adapters → post natively | **Postiz (self-hosted)** |
| **L7 Monitor** | Token/connector health, gap sentinel, results | `automation-reliability-monitor` (16) + `techstack-connection-verifier` (13) + Marketing attribution (03) |

**The spine (through every layer):** `packet_id · variant_id · publish_record(packet × platform × timestamp × status × external_post_id)` — makes retries idempotent (no double-post) and failures a state (nothing vanishes).

---

## 4. The workflow — 12 stages (plan-first, owner-adopted sequence)

Adopted order maps from the original as `1→5→9→3→4→2→[new]→6→7→8→[+11]→10`. Phases: **PLAN → PRODUCE & PUSH → CLOSE.**

| # | Stage | Phase | Owner | Trigger | Exit → state |
|---|---|---|---|---|---|
| 01 | Conceived | plan | Content · `content-brief-builder` | Scored opportunity / manual idea | Brief exists → `conceived` |
| 02 | **◇ Concept Gate (G1)** | gate | Presence + Content (advisory) → human · Class 2 | Brief complete | Pass → `planned` · Fail → `concept_rejected` |
| 03 | Define Success | plan | Marketing attribution + Presence | Passed G1 | Success spec attached |
| 04 | Plan the Tree | plan | Content · `content-multiplication-engine` | Success defined | Variant plan attached |
| 05 | Package | plan | Content → Reservoir | Tree planned | Packet persisted → `planned` |
| 06 | Produce | produce | Design (19) + Content variants | Human marks **"Ready for Design"** | Variants rendered → `produced` |
| 07 | **◇ Pre-Publish Check (G2)** | gate | Content gate + **human Class 3** | Variants produced | Pass → `approved` · Fail → `publish_rejected` → rework |
| 08 | Schedule | push | Orchestrator (L5) | Approved | Slotted per cadence + rate ceiling → `scheduled` |
| 09 | Publish | push | Executor (Postiz, L6) | Slot time | Pre-flight → post → `publish_record` → `published` |
| 10 | Verify | push | Monitor (L7) | Publish returned | Confirmed live, or retry → dead-letter |
| 11 | Measure | close | Marketing attribution | Measurement window elapsed | Results vs. target → `measured` |
| 12 | Archive | close | Reservoir (L3) | Measured | `archived`, or `evergreen` → re-enters at Schedule |

---

## 5. The two gates

- **Gate 1 — Concept (pre-production).** *"Should this exist at all?"* Checks: economic job + ≥1 of the five movements · Presence Intelligence Filter · on-narrative · worth the scarce credits. Fail = nothing is produced (the credit-protecting move).
- **Gate 2 — Pre-Publish (pre-queue, NEW 2026-08-02).** *"Is the finished asset safe to send?"* Checks: platform-native (PIL profile) · narrative preserved · every claim substantiated (Legal Class C ban) · on-brand. Requires **human Class 3 sign-off** (public-facing). A final **automated pre-flight** (token valid? media present? link resolves?) also runs at the publish moment.

At volume, both gates approve at the **template level** (approve a content *type* once; only new/flagged items need a fresh human look) so neither becomes the bottleneck.

---

## 6. Packet state machine

```
conceived → ◇G1 → planned → in_production → produced → ◇G2 → approved
          → scheduled → publishing → published → measured → archived
off-ramps: concept_rejected · publish_rejected→rework · failed→retry→dead-letter · evergreen→re-enters at scheduled
```

---

## 7. Disconnect resolutions

| Gap | Resolution | Status |
|---|---|---|
| Volume vs. doctrine | Volume from the multiplication tree; economic job set once (stage 03), inherited by every variant; cadence caps per-platform | resolved by spec |
| Canonical platform set | The 10 confirmed in §2 | **resolved (owner 2026-08-02)** |
| Executor / host | Postiz self-hosted on Render | **resolved (owner 2026-08-02)** |
| Zero social accounts | Phase-0 task: create accounts in priority order, register each in TechStack with `verified_at` | owner action (Phase 0) |
| Runtime declared-not-scheduled | v1 orchestrator runs on Render, **not** the un-booted arika-runtime; write 3 approval-matrix rows before any cron fires | resolved by spec |
| Silent connector death | L7 monitor: token-expiry watch (alert 7 days out), heartbeat, gap sentinel, `verified_at` everywhere; monitor lives on the always-on host | resolved by spec |
| Supply is the real ceiling | Build supply (L1/L2) first; min buffer depth (7–14 days/platform) is the go-live gate; owner action: re-auth OpenArt + top up credits | resolved by spec + owner action |

---

## 8. Build order

- **Phase 0 — Decide & connect.** ✅ platform set / executor / host decided. Remaining: provision a Kenyan KVM VPS (≥4GB RAM, M-Pesa) + install Coolify + deploy Postiz, create the 10 accounts (priority order), register connectors with `verified_at`.
- **Phase 1 — Reservoir.** Extend the Notion packet schema + state machine (the queue-of-record).
- **Phase 2 — Gates.** Wire G1 + G2 as template-level checkpoints.
- **Phase 3 — Executor.** Deploy Postiz via Coolify on the VPS; connect LinkedIn first.
- **Phase 4 — First test (LinkedIn, end-to-end).** One real packet through all 12 stages. The "first test of the full body."
- **Phase 5 — Orchestrator + Monitor.** Cadence engine, rate governor, retry/dead-letter, L7 monitor; write the 3 approval-matrix rows.
- **Phase 6 — Scale.** Fill the Reservoir to min depth; turn on platforms 2–10; go live, watched.

---

## 9. Governance

- **Approval-matrix rows required before any live automation** (`00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`): (1) publish orchestrator, (2) L7 monitor, (3) recycle loop. No cron fires without a row (Automation 16 rule).
- **Class 3 human sign-off** on all public-facing publishing (Gate 2).
- **Presence Economics** enforced: every packet carries an economic job; **excluded metrics: impressions, followers, likes, reach** (Presence Constitution §8 / KPI §7).

---

## 10. Decision Log

- **2026-08-07 — Host LIVE: Hostinger KVM 2 (8GB) + Coolify.** The M-Pesa Kenyan-VPS plan was dropped (Novahost out of stock); the owner's virtual card succeeded at Hostinger (Railway/Stripe had rejected it). Coolify + Postiz v2.10.1 + Postgres + Redis **Running (healthy)**; admin login confirmed. IPv4 191.215.36.69. Executor host verified; full-engine verification pending first live post. — Claude Code (Opus 4.8)
- **2026-08-07 — Host switched Railway → self-hosted VPS + Coolify (M-Pesa).** Railway/Stripe rejected the owner's virtual card (no PayPal/M-Pesa), and Railway's free Trial RAM cap OOM-killed Postiz (exit 137) regardless. Kenyan VPS providers accept M-Pesa; executor moves to a KVM VPS (≥4GB RAM, Ubuntu) + Coolify. **≥4GB RAM is a hard requirement** (the OOM lesson). — Claude Code (Opus 4.8)
- **2026-08-02 — Executor host switched Render → Railway.** Postiz v2.12+ requires a Temporal service Render can't host managed; Railway's official one-click template side-steps it (pins v2.11.3, ~$5/mo, auto-wires Postgres+Redis+secrets). Render retained as candidate for the L5 orchestrator. — Claude Code (Opus 4.8)
- **2026-08-02 — Content Distribution Engine design ratified (owner).** Confirmed the 10-platform canonical set (LinkedIn → Facebook → Instagram → Threads → TikTok → Pinterest → Website → X → Newsletter → YouTube; Tumblr dropped), **Postiz self-hosted** as executor, **Render** as host, and the **two-gate** model (Concept + Pre-Publish, +automated pre-flight). Adopted the owner's plan-first 12-stage sequence (`1→5→9→3→4→2→new→6→7→8→+11→10`) with two relabels (09→Define Success, 03→Plan the Tree) and results-capture re-added. Resolves PIL's open in-scope-set flag. Reality-gated: no accounts, no deployment yet — design of record, not a live system. — Claude Code (Opus 4.8)

## 11. Reality note

Nothing here is live. Every account, tool, cron, and host named is a target the presence gets built to — stated so plainly because the alternative is exactly the doc-vs-reality drift the repo has caught before (the 11-day Creative Pipeline outage; TechStack's 4 rotted rows). No `verified_at` reads true until first deploy.
