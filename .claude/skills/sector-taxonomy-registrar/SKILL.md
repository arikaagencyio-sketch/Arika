---
name: sector-taxonomy-registrar
description: Skill S07 of Sector (01). The only sanctioned way to add or re-classify a vertical or an industry, and the only skill that may promote a Lifecycle State. Writes DB 1 Sectors Master and DB 2 Sub-Sectors — a 37-field hub carrying 14 relations, so it runs the tightest gate in the library. Use when a new market enters the universe, at activation Gates A/B, or on any lifecycle promotion. Runs FIRST — everything else needs its sub-sector to exist.
---

# S07 · Sector Taxonomy Registrar

You are performing the **apply** step of Sector's write layer, at its root.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** Gate definitions and the state machine: [`SECTOR_ACTIVATION_PROTOCOL.md`](../../../01_Sector/SECTOR_ACTIVATION_PROTOCOL.md) §3. Field truth: [`contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB1, DB2. Contract row: `SECTOR_SKILL_MATRIX.md` §2.

> **This skill owns the two tables everything else hangs from.** DB 2 is a **37-field hub carrying 14 relations** — a careless write propagates into every other database in the department. It runs **first** logically, because nothing can be written about a sub-sector that does not exist.
>
> **It is also the only skill that may set a `Lifecycle State`**, and that is the power it must be most careful with.

---

## Step 0 · The write path

| | Data source |
|---|---|
| DB1 Sectors Master | `collection://68a5d070-58de-4b4d-8293-0fab0849a4b9` |
| DB2 Sub-Sectors | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |
| Plugin **P1** *(the ontology)* | `sector_plugins/<sector>/` |

## Step 1 · No self-promotion. Ever.

**A `Lifecycle State` may only be advanced when the rows that justify it already exist.** `SECTOR_ACTIVATION_PROTOCOL.md` §3 gives each gate an **exit evidence** column; that column is the whole test.

| Gate | State it justifies | Exit evidence you must verify |
|---|---|---|
| A · Qualify | `Discovered` | `Priority Band = P1/P2`; regulated verticals flagged |
| B · Scope | `Mapped` | **one** `Target` sub-sector; geography scope named |
| C · Author the plugin | `Intelligence-Rich` | every slot filled-and-cited or explicitly ⬜ |
| D · Register sources | — | **zero `active` sources without a verification call** |
| E · Load | `Validated` | rows exist, cited, `Confidence` matching evidence |
| F · Resolve | `Offer-Ready` | **outputs structurally different per validation place** |
| G · Route | `Content-Ready` / `Acquisition-Ready` | downstream rows exist **and resolve upstream** |
| H · Live-loop | `Campaign-Ready` | a change record naming its invalidation set |

**Write the evidence into the page body as you promote.** A promotion whose justification lives only in a changelog is a self-promotion with extra steps — *the row must carry its own proof*, because the row is what a reader finds.

> **State plainly what the new state does NOT assert.** `Offer-Ready` means the model resolves differently for structurally different places. It does not mean the intelligence is complete. **A lifecycle state is a claim about a gate, not a claim about quality** — and downstream departments will read it as the latter unless you say otherwise.

**Never skip a state.** If the evidence supports `Offer-Ready` but `Validated` was never set, that is not a shortcut to take quietly — record that the earlier gates passed unrecorded, and say when.

## Step 2 · No black-box numbers

**A `Sector Priority Score` without its 8-dimension rationale is a refusal.** The score is a `number` field and the rationale is free text; nothing in the schema forces them to agree, so **you** are the enforcement.

Write the dimensions explicitly — `Rev · CapFit · Growth · Pain · BuyCap · DM-Access · CompGap · Recur` — and their values. *A reader who cannot reconstruct the number cannot challenge it, and a number that cannot be challenged will be repeated forever.*

## Step 3 · A vertical is not a category

`Category` (`Horizontal SaaS` · `Vertical SaaS` · `AI-Native` · `Multi-Location Vertical` · `Industry Vertical`) describes **what kind of market this is**. The vertical itself is the **row**.

Filing a vertical as a category, or inventing a category to hold one market, corrupts the axis that DB 2's 321 rows classify against.

**Every Sub-Sector needs a `Parent Sector`.** An orphan sub-sector is invisible to every resolution, because scope resolves *through* the hub.

## Step 4 · The hub is dangerous — read before you write

DB 2 carries **14 relations**. Before changing any of them, read what points at the row. A re-classification that silently drops a relation removes evidence from databases this skill does not own.

**Re-classification is a supersession, not an edit.** Record what the row was, what it became, and **what that invalidates** — the same 5-step change-history discipline DB 7 uses. `SECTOR_WRITE_CONTRACT.md` §5 generalises it to every Sector database, and this is the one where it matters most.

## Step 5 · Fields

**DB 1 — yours:** `Sector Name` · `Sector ID` · `Definition` · `Category` · `Industry Type` · `Atlas Layer` · `Portfolio Mode` · `Strategic Priority` · `Priority Tier` · `Priority Band` · `Priority Scoring Rationale` · `Sector Priority Score` · `Lifecycle State` · `Status` · `Readiness` · `Intelligence Confidence` · `Last Intelligence Update` · `Next Review` · `Sub-Sectors` · `Related Clients (CRM)`.

**DB 2 — yours:** all 37, including `Parent Sector`, `Status`, `Readiness`, `GTM Motion`, `Industry Type`, `Tool-Stack Chaos Risk`, `Fragmentation Type`, `Opportunity Score`, `Intelligence Confidence`.

**`Status` and `Lifecycle State` are different questions.** `Status` (`Active` · `Target` · `Reference` · `Dormant`) is *what we are doing about this market*. `Lifecycle State` is *how far the activation protocol has got*. A sector can be `Reference` and `Offer-Ready` at once — that is not a contradiction, and collapsing the two loses both.

## Step 6 · Verify, log

Read each write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S07"`, recording **which gate justified the promotion and which evidence you checked** — not merely the new value.

Loop: `activation`. Hands off `SECTOR_READINESS_SET` → Marketing (03).

> ⚠️ **Check the route before claiming the handoff.** Per [`AEIT_11`](../../../00_Agency_Governance/enterprise_architecture/AEIT_11_RUNTIME_TRUTH_STANDARD.md), `SECTOR_READINESS_SET` is `CONNECTED` — a subscriber is verified — and **not `LIVE`**: nothing publishes agent-to-agent. Report it the way S10 does, as a route that does not deliver today.

---

## Refuse

- **A lifecycle promotion without the underlying rows.** No self-promotion.
- A promotion whose evidence is not written onto the row itself.
- A `Sector Priority Score` without its 8-dimension rationale.
- A vertical filed as a `Category`.
- A Sub-Sector with no `Parent Sector`.
- Re-classifying a hub row without recording what it invalidates.
- Collapsing `Status` into `Lifecycle State`.
- Writing a sector's taxonomy from a plugin that has not authored **P1**.

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-28.** DB 1 held **25** verticals, DB 2 **321** sub-sectors. Exactly **one** sub-sector was `Target` — Accommodation (Hotels) under Hospitality.

⚠️ **A write this skill should have made was made without it.** On 2026-08-28 Hospitality was promoted to **`Offer-Ready`** — an S07 write, performed while S07 was unbuilt. The substance held: gate-by-gate exit evidence was written onto the DB 1 row, which is exactly what the no-self-promotion refusal demands. **The sequence did not.** Re-read that row before the next promotion; it is the worked example of this skill's own standard, produced before the skill existed.

**The taxonomy is already loaded, which is why this skill is built late despite running first.** It governs *future* writes. Its first real test is the next market entering the universe — or the next promotion, which is due at Gate G.
