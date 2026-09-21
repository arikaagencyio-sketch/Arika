# A001 — Hospitality Sector Sandbox

**Department:** Sector (01) — owns this record. Offer (02) consumes it.
**Owner:** Mary Thuo
**Status:** ✅ Approved by the owner 2026-09-15 as a sandbox and architecture specimen · ✅ Ratified 2026-09-16 (D17) as an **internal simulation sandbox only** — not a prospect, not a CRM record, not offer evidence · 🔴 **Not runtime-runnable.** Phase 3 runs document-only first (D15), and any runtime-backed work stays blocked until the API key is rotated (D16 · AG-19). Phase 3 document-only execution is under way: `A001-P07` has reached S2 (§9). No runtime-backed work has started.
**Version:** v0.15

> A001 is a **fictional** hospitality group. It exists to test the agency's architecture against a company with several properties. It is **not evidence** about any market, property or buyer. Read §2 before using an A001 value anywhere.

> See [`SECTOR_OS.md`](SECTOR_OS.md) §8 for the decision entry, and [`OWNER_INPUT_NEEDED.md`](../00_Agency_Governance/OWNER_INPUT_NEEDED.md) item 74 for what is still undecided.

---

## 1. Status and decision

**Owner decision, 2026-09-15:**
- A001 is approved as the **group-level simulated Hospitality Sector Sandbox** and pilot-company architecture specimen.
- It is **not** a real client, prospect, lead, CRM company, or the item 72 real-property pilot.
- `PILOT-H-001` stays reserved for a real single-property pilot unless it is later re-scoped.
- The child units are `A001-P01` to `A001-P09`. `A001-P08` is linked to `A001-P07`.
- `A001-P07` may become the first property test slice, **but only inside the A001 group context**.

**What this decision does not change** (also recorded in [`02_Offer/OFFER_OS.md`](../02_Offer/OFFER_OS.md) §8):
- Owner Decision 71 and its H-bands.
- The H1/H2 MVP.
- The seed ICP and the anti-ICP.
- The pricing gates (capacity worksheet G7, `Draft 41` Phase 11).
- Item 72.

**Still open, under item 74:**
- The Tier-1 changes in §8 — **deferred 2026-09-15 (D6)**; none is needed while no runtime is used.
- The run mode for Phase 3. *(Phases 0–2: M0, no runtime — decided 2026-09-15, D5.)*
- ~~The archetype mapping in §6.~~ Decided 2026-09-15 (D13).
- ~~Geography.~~ Decided 2026-09-15 (D14).
- API key rotation and full A001 ratification (Phase 3 entry gate).
- ~~The sandbox folder path.~~ Decided 2026-09-15 (D1; §5.1).
- The AG-4 build. *(AG-1/AG-3 deferred under a manual workaround, D7; AG-16 done.)*

**Named risk: `AEIT_10` RK-2, "architecture keeps outrunning reality."** A sandbox is structure with no real run behind it. This file records gaps and gates, not capability. Writing something down here does not make it `BUILT` (`AEIT_11`).

## 2. What A001 is and is not

| A001 is | A001 is not |
|---|---|
| A fictional group company, supplied by the owner as a simulation package kept outside the repository | A real client, prospect, lead, partner or competitor |
| A test of whether intake, Sector fit, the Offer flow, the entity model, provenance and runtime rules can handle a group with child properties | A CRM `Company`, a ClickUp record, or a Notion row of any kind |
| A source of **structural** findings: what breaks, what is missing, what stops correctly | Evidence for any Sector finding, P2 cell, destination profile, KPI, price, floor, capacity figure or delivery actual |
| Deliberately outside the current offer's ICP: it has a central brand and direct-booking team, and it is above H3 | A reason to amend Decision 71, the MVP or the anti-ICP. When A001 fails the ICP check, **the check is working** |
| A group whose child `A001-P07` may be the first property test slice, inside group context | A standalone H1/H2 pilot, or a substitute for item 72 |

## 3. ID scheme

| ID | Meaning | Rule |
|---|---|---|
| `A001` | The group (parent). Archetype `Hospitality Group`, "a parent, not a bookable unit" (`HOSPITALITY_PLUGIN.md` P1) | Always written in full. Never paired with a name in a repository file or a runtime input |
| `A001-P01` … `A001-P09` | Child property units, numbered in the simulation package's own order | Numbers are fixed once assigned. A withdrawn unit keeps its number and is marked `withdrawn` |
| `A001-P08 → A001-P07` | `linked_to`: P08 runs as a linked sub-property of P07 | A declared link only. No canonical edge exists for it yet (§7 AG-9) |
| `A001-P07` slice | The first property test slice | Every slice artifact carries both `A001` and `A001-P07` |

**Names.** The fictional names for these IDs live **only** in the sandbox key file (§5). Repository files use IDs, archetype class, destination status, size band and stop-rule status. Nothing else.

**Not a pilot ID.** `A001` is not part of the `PILOT-H-*` series. Never write it into a field or template that expects a pilot ID. `intake_gate.py --template` currently hard-codes `pilot_id: "PILOT-H-001"` (`00_Agency_Governance/intake/intake_gate.py:134`); see AG-1.

## 4. Provenance mapping

Every A001 value carries **`[TEST_FIXTURE · A001]`**. This reuses `Draft 41`'s existing label ("A test assumption supplied for the structural run. Not real, not validated, not quotable.") rather than adding a new one. The sandbox ID is added so an A001 value is never mistaken for one of `Draft 41`'s own structural-run fixtures.

| Simulation-package class | Repository label | May enter the repository? | May enter a runtime input? |
|---|---|---|---|
| **Reference-public:** facts about the real brand the package was modelled on | **None. Excluded** | ❌ Never | ❌ Never. Kept in the key file only, so scans can catch them |
| Simulated | `[TEST_FIXTURE · A001]` | Only as ID, archetype class, destination status, size band or stop-rule status | Only after Phase 0, with the §5 markers and a passing scan |
| Derived | `[TEST_FIXTURE · A001 · DERIVED]` | As simulated | As simulated |
| Assumed | `[TEST_FIXTURE · A001 · ASSUMED]` | As simulated | As simulated |

**Rules:**
1. **The weakest label wins.** An output that uses any A001 value takes its label, whatever else it draws on. A Sector finding combined with an A001 value is `[TEST_FIXTURE · A001]`.
2. **One-way.** No A001 value or output counts as evidence anywhere. Excluded in particular:
   - all 16 Sector Notion databases, Content DB 5 and the ClickUp CRM;
   - `HOSPITALITY_PLUGIN.md` and `plugin.config.json`, including moving any P2 cell toward `observed`;
   - KPI thresholds and the Offer Engineering Registry;
   - hotel pricing floors, test prices and worksheet gate G7;
   - delivery-capacity or hours evidence.
3. **No public or client labels.** `PUBLIC`, `PUBLIC-OTA`, `CLIENT-SUPPLIED` and `CLIENT-SYSTEM` are never valid for A001. An A001 answer can be `OWNER-SUPPLIED` in form at most, and is always `[TEST_FIXTURE · A001]` in substance.
4. **Simulated verdicts are not verdicts.** Anything computed from A001 data is recorded as **`SIMULATED_VERDICT`**: a diagnostic class (a)–(d), a QG1 result, a size-band placement or an ICP result. It shows that the gate ran, never what a real property's answer would be.
5. **`AEIT_05` has no value for this yet.** Its `trust` state attribute has no test-fixture value (AG-11). Until a Tier-1 change adds one, these labels live in text only.

## 5. Storage rules

| What | Where | Never |
|---|---|---|
| This record, the decision entries, the tracker item and the gap register | Repository: this file, `SECTOR_OS.md` §8, `OFFER_OS.md` §8, item 74 | Names, URLs, exact inventory counts, room-size or venue-capacity tables, currency amounts, synthetic KPIs or reference fingerprints |
| Group and child answer files, the simulation package, per-unit notes, slice seed briefs | **A sandbox folder outside every git working tree.** The path is supplied under item 74 | Inside this repository, the stale `ChatGPT\Agency.Repo` clone, any other git tree, or a synced folder that commits |
| **Key file** (`00_admin\a001_key.json`): the ID → name map, real names and domains, reference fingerprints | Sandbox folder only | Anywhere else. Inputs are scanned **against** it, so nothing from it may be copied **into** them. Never opened in a Claude session; validated by counts only (D3) |
| Runtime inputs for A001 (Phase 3 only, if approved) | Typed by the owner after review | Sent without the three markers and a passing scan |

**Key file rules.**
- **The current scan reads only `real_names` and `domains`.** `intake_gate.py --scan` ignores every other field. A string held only under `id_map`, `reference` or `fingerprints` is **not checked**, and the scan still prints PASS.
- **Superset rule.** Every name, domain and distinctive string held anywhere in the key must also appear in `real_names` (web addresses in `domains`), with its variants: spaced, unspaced, hyphenated, with and without "The", possessive, abbreviated, accented and unaccented.
- **Keep generic tokens out of `real_names`.** The match is a case-insensitive substring, so an entry under 5 characters, a bare number, or a fragment of a repository place or archetype name causes false hits. Hold those in a manual-check field and check them by eye.
- **Numbers are manual.** The scan does not catch inventory counts, room sizes, venue capacities, synthetic KPIs or currency figures without a code. Unit-bearing strings may go in `real_names`; bare numbers may not.

**Runtime marker convention.** This is documentation only; nothing enforces it yet (AG-3, AG-12). Every A001 `--input` must carry, at top level:

```json
{ "sandbox_id": "A001", "unit_id": "A001-P07", "provenance": "TEST_FIXTURE" }
```

**Why the markers matter:** `writeMemory` appends each run's entry, including the full `input`, to the agent's memory stream (`arika-runtime/src/memory-writer.ts:22-38`). That stream is git-tracked and auto-synced, and **a memory line cannot be cleaned up afterwards.** The markers make an A001 line identifiable. They do not make it removable.

**Not permitted for A001 today:**
- agent runs, event publication and the scheduler;
- Notion or ClickUp writes;
- skill execution records (`01_Sector/_memory/skill_runs.jsonl`; AG-13);
- Branding (12) BOIS runs, because they write client workspaces inside this repository (AG-15);
- reading `.env`.

### 5.1 Operating mode (owner decisions D1–D20: D1–D14 for Phases 0–2, 2026-09-15 · D15–D19 for Phase 3 entry, 2026-09-16 · D20 on the use of simulated evidence, 2026-09-16)

**Mode M0: no runtime.** Phases 0, 1 and 2 use none of the following: `arika run`, `npm`, skills, skill execution records, events, the scheduler, Notion, ClickUp or BOIS. Nobody reads `.env`.

The only tool is the local intake gate, run from the repository root:
- lint;
- `--template … --out <sandbox path>`;
- `--answers`;
- `--scan`.

**Phase 3's run mode is undecided:** M1, the shared stream with the §5 markers, or M2, a separate stream (T1-5). The Tier-1 changes T1-1…T1-5 are deferred.

| # | Decision | Rule |
|---|---|---|
| D1 | Sandbox root | `C:\Users\USER\Arika_Sandboxes\A001\` — local, not in OneDrive, outside every git tree |
| D2 | Key file | `00_admin\a001_key.json`, created by the owner. ✅ **In place and validated 2026-09-15** by a counts-only script; no key value was read into a session. The IDs-only scan test and the intake gate lint pass. *It was not yet in place at the first setup check the same day.* |
| D3 | Key custody | Key values never enter a Claude session. The file is validated by a script that prints counts only |
| D4 | Package custody | The simulation package stays where the owner holds it for now; nothing is extracted |
| D5 | Run mode | M0 for Phases 0–2 |
| D6 | Tier-1 | T1-1…T1-5 deferred |
| D7 | Intake tooling | Manual workaround; AG-1/AG-3 builds deferred |
| D8 | Answer label | `[OWNER-SUPPLIED · TEST_FIXTURE · A001 · YYYY-MM-DD]`, plus `· DERIVED` / `· ASSUMED` where applicable |
| D9 | Stage cap | S2. S3–S5 rows are `BLOCKED` with the note "A001 sandbox — no client system". Synthetic data stays in source custody, never in answers |
| D10 | Write-back | Only IDs-only verdict lines leave the sandbox, after `--scan` and the manual checks |
| D11 | Answer source | Values derived from rules and from this sandbox record are drafted by Claude. Values that come from the simulation package are typed by the owner into the worksheet. **Claude does not read the package** |
| D12 | Value granularity | Bands, categories, statuses and unit IDs only. No counts except the owner-decided unit count; no URLs, verbatim copy, prices, ratings, KPI values, shares or named competitors |
| D13 | Unit archetypes (sandbox use only) | `A001-P01` `City / Conference Hotel` · `A001-P02` main `City / Conference Hotel`, secondary `Serviced Apartment` (`secondary_unruled`) · `A001-P03` `Beach Resort` · `A001-P04` `City / Conference Hotel` · `A001-P05` `City / Conference Hotel` · `A001-P06` `Safari Lodge` · `A001-P07` `Tented Camp`, inheriting `Safari Lodge` · `A001-P08` `Tented Camp`, inheriting `Safari Lodge`, linked to `A001-P07` · `A001-P09` `Safari Lodge`.<br>**Two-archetype rule:** a unit with two archetypes records one main archetype for resolution and marks the other `secondary_unruled`. Resolution uses the main archetype only. The secondary is a declared sandbox gap, **not a Sector rule** |
| D14 | Geography policy | **Commission nothing for A001:** no new geography rows, destination profiles, place-profiling skill run or Notion writes.<br>Each unit records one status: `profiled`, `in_DB11_not_profiled` or `not_in_DB11`.<br>Only currently profiled destinations pass Destination Fit. Blocked statuses are recorded as `SIMULATED_VERDICT · destination_fit: blocked`.<br>No place names for `not_in_DB11` units outside the key file and owner source material |

**Phase 3 entry decisions (owner, 2026-09-16).** Recorded as B1–B5 in §9 "Phase 3 readiness". **Recording these decisions does not start Phase 3.**

| # | Decision | Rule |
|---|---|---|
| D15 (B1) | Phase 3 run mode | **No-runtime, document-only first.** Phase 3 work is written by hand in the sandbox folder. No `arika run`, agent, skill, scheduler or event activity, and no runtime memory write. This supersedes D5 for Phase 3 only; D5 still governs Phases 0–2 |
| D16 (B2) | API key rotation | ✅ **Credential condition met 2026-09-21** — rotation and revocation **owner-attested 2026-09-21** — the replacement key was installed in the intended secret location and the exposed old key was **revoked in the Anthropic Console** (AG-19 recorded done). ⚠️ **Replacement not yet verified by use**, and runtime-backed Phase 3 work still needs its own authorisation (AG-19 · item 57). It does **not** block the document-only work D15 permits, because that work needs no key. Any later move from document-only to runtime-backed re-enters this gate |
| D17 (B3) | A001 ratification | **Ratified as an internal simulation sandbox only.** A001 is **not** a prospect, **not** a CRM record and **not** offer evidence. It may not enter the Offer runtime, the Sector store, the CRM or any shared store, and no A001 output may be cited as evidence about a market, property or buyer (§2, §4 rule 4).<br>This ratifies the sandbox's standing, **not** the §8 Tier-1 changes, which stay deferred under D6 |
| D18 (B4) | Phase 3 slice | **`A001-P07` only.** Confirmed against the Phase 2 evidence: it is the only unit passing archetype, Destination Fit and the H-band together. The slice still runs as a group-architecture test carrying the group flags, never as an MVP audit |
| D19 (B5) | S2 input format | **S2 switches to a block-per-question input format before any owner fill.** One field per line, so a dropped cell is not possible. Adopted because owner fill silently lost cells twice at S1 (42 rows) and S2 is 65 rows per unit. The format is not built yet; no S2 worksheet exists |

**Use of simulated evidence (owner decision, 2026-09-16).** This governs what A001 output may justify anywhere in the repository, in every department, permanently — not only during the phases.

| # | Decision | Rule |
|---|---|---|
| D20 | Use of simulated evidence | **May be used to improve mechanisms only:** schemas · gates · intake formats · validators · routing logic · documentation · safe workflow design.<br>**May not be used as** market evidence · demand evidence · pricing evidence · proof evidence · buyer evidence · capacity evidence · or any claim about real hotels.<br>**The test:** A001 output may justify changing *how the system works*. It may never describe *how the market behaves*. A finding that a rule is missing, a profile unauthored, an edge undefined or a format unsafe is a mechanism finding and may be acted on. Anything that would read as a fact about demand, guests, prices, competitors or a real property is barred, however it is phrased.<br>Applies to every A001 output, including the Phase 2 close-out, the document-only pilot close-out and every `SIMULATED_VERDICT` (§4 rule 4) |

**Sandbox layout** (IDs only in every folder and file name):

| Folder | Holds |
|---|---|
| `00_admin` | The key file, the decisions record and the git-check record |
| `01_source` | Source material |
| `02_group` | Group files |
| `03_units\A001-P01` … `A001-P09` | One folder per unit |
| `04_slice_P07` | The first property slice |
| `05_diagnostics` | Group diagnostics |
| `06_downstream_notes` | Downstream notes |
| `90_scan` | Repo-bound drafts and scan output |

**Answer conventions under the manual workaround (D7):**
- **Generate blank files** with `--template` into the sandbox, then hand-edit `pilot_id` to `A001` or `A001-Pnn`, because the template writes `PILOT-H-001`.
- **Unit files** add three top-level keys: `"parent_id": "A001"`, `"sandbox_id": "A001"` and `"provenance": "TEST_FIXTURE"`. The gate ignores extra top-level keys.
- **Every `ANSWERED` value uses the D8 label.** It starts with `OWNER-SUPPLIED` because `--answers` checks only a label's first word and rejects one beginning `TEST_FIXTURE`. The label still obeys §4 rule 3. `PUBLIC`, `PUBLIC-OTA` and `CLIENT-*` labels are never used.
- **Never add answer IDs.** The gate fails any ID outside the question bank. Group questions therefore live in `02_group\A001_group_notes.md` until AG-2: portfolio, linked units, central systems, decision rights, group channels.

**Git-tree check.**
- **Before** creating or writing into any sandbox folder, `git -C <path> rev-parse --show-toplevel` must fail for the sandbox root and its parent. The output is saved in `00_admin\preflight_git_check.txt`.
- **After every Phase 0–2 step,** `git status --short` in this repository must show nothing but intended documentation, because the auto-sync job commits within minutes.

**Write-back rule (D10).** Nothing leaves the sandbox except IDs-only verdict lines for §6 and changelog lines. Each one:
1. is drafted in `90_scan\`;
2. passes `intake_gate.py --scan` with `--key 00_admin\a001_key.json`;
3. is checked by eye for what the scan cannot see: numbers, URLs, name variants and labels.

## 6. Child register

**IDs only.** How to read the columns:
- **Archetype class** uses the `HOSPITALITY_PLUGIN.md` P1 vocabulary. It is **confirmed for sandbox use only (D13, 2026-09-15).** A unit with two archetypes resolves on its main archetype and marks the other `secondary_unruled`.
- **Destination status** comes from `SECTOR_OS.md` §3 (DB 16 profiled: Nairobi · Maasai Mara · Diani; Mombasa not profiled). Plugin P5 now agrees with it (AG-16, resolved 2026-09-15 and gated by `sector_truth_gate.py` check 6). Places with no DB 11 row are not named here; their names are in the key file. Under D14, each unit file records one status: `profiled`, `in_DB11_not_profiled` or `not_in_DB11`.
- **Size band** uses Owner Decision 71's H-bands **as a label only**. A band does not bring any unit into MVP scope or capacity.

| Unit | Archetype class (confirmed, D13) | Destination status | Size band | Stop-rule status |
|---|---|---|---|---|
| **`A001`** (group) | `Hospitality Group` | Multi-destination | **Above H3** on property count and on keys | 🔴 Group archetype unresolvable (union operator not built) · 🔴 anti-ICP: central brand, reservations and direct-booking team · 🔴 above every H-band |
| `A001-P01` | `City / Conference Hotel` | ✅ Nairobi, DB 16 profiled | H3 | 🟡 H3 is outside MVP scope and capacity · group flags |
| `A001-P02` | **Main:** `City / Conference Hotel` · **secondary:** `Serviced Apartment` (`secondary_unruled`) | ✅ Nairobi, DB 16 profiled | H3 (hotel keys), plus serviced apartments | 🟡 H3 · 🟡 resolves on its main archetype only; the secondary is a declared sandbox gap, not a Sector rule (D13, AG-5) · group flags |
| `A001-P03` | `Beach Resort` | 🔴 Mombasa: in DB 11 with **no DB 16 profile**, so Destination Fit blocks it (31h) | **Above H3** | 🔴 Destination Fit · 🔴 above every H-band · group flags |
| `A001-P04` | `City / Conference Hotel` | 🔴 Not in DB 11 | H3 | 🔴 geography unresolvable · 🟡 H3 · group flags |
| `A001-P05` | `City / Conference Hotel` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |
| `A001-P06` | `Safari Lodge` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |
| **`A001-P07`** | `Tented Camp`, inheriting `Safari Lodge` | ✅ Maasai Mara, DB 16 profiled | **H2** | ✅ **No unit-level stop rule** · 🔴 group flags still apply, so the slice runs as a **group-architecture test**, not an MVP audit |
| `A001-P08` → P07 | `Tented Camp`, inheriting `Safari Lodge`; linked to `A001-P07` | ✅ Maasai Mara, DB 16 profiled | **Below H1** | 🔴 below every H-band · 🔴 linked-unit meaning undefined (AG-9) · group flags |
| `A001-P09` | `Safari Lodge` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |

**What the register shows:**
- **Destination:** 4 of 9 units resolve (P01, P02, P07, P08).
- **Band:** 4 of 9 fall inside H1/H2 (P05, P06, P07, P09).
- **Every unit-level check:** only `A001-P07` passes destination, band and archetype together.
- **Group flags:** every unit carries them. The sandbox exists to show what the system does with those flags, not to hide them.

### Phase verdicts

IDs only. Each line is written here only after three steps (D10):
1. It is drafted in the sandbox's `90_scan\` folder.
2. It passes `intake_gate.py --scan` with the A001 key.
3. It passes a manual check.

A `SIMULATED_VERDICT` shows that the gates ran. It is never a verdict about a real property (§4 rule 4).

| Phase · stage | Scope | Verdict | Conditions | Recorded |
|---|---|---|---|---|
| 1 · S1 | `A001` | `SIMULATED_VERDICT` · `group_outside_current_offer_icp_by_design` · `blocked_for_current_H1_H2_MVP` | may_continue_to_phase_2: yes, after item 74 points (3) and (4) · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-15 |
| 2 · S1 | `A001-P07` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_pass · H_band_pass` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: yes, after Phase 3 entry gate · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-15 |
| 2 · S1 | `A001-P08` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_pass · size_stop_rule_fires_below_H1` · group_flags: `apply` · link: `A001-P07 link recorded · AG-9 unresolved` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; A001-P07 remains the Phase 3 slice · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-15 |
| 2 · S1 | `A001-P03` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_fires_in_DB11_not_profiled · size_stop_rule_fires_above_H3` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by destination profile and size · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P04` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_fires_not_in_DB11 · size_stop_rule_fires_H3_outside_MVP` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by destination status and size · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P05` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_fires_not_in_DB11 · H_band_pass` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by destination status · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P01` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_pass · size_stop_rule_fires_H3_outside_MVP` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by size · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P02` | `SIMULATED_VERDICT` · unit_check: `main_archetype_pass · secondary_unruled · destination_fit_pass · size_stop_rule_fires_H3_plus_serviced_apartments` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by size and secondary-rule gap · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P06` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_fires_not_in_DB11 · H_band_pass` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by destination status · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |
| 2 · S1 | `A001-P09` | `SIMULATED_VERDICT` · unit_check: `archetype_pass · destination_fit_fires_not_in_DB11 · H_band_pass` · group_flags: `apply` · `outside_current_offer_icp_by_design` | may_continue_to_phase_3_planning: no; blocked by destination status · may_enter_offer_runtime: no · may_enter_sector_store_or_crm: no · pricing: skipped | 2026-09-16 |

### Phase 2 close-out (2026-09-16)

Phase 2 is complete: all nine units hold a declared `SIMULATED_VERDICT` above, and the §9 Phase 2 exit gate is marked met. IDs, statuses and band labels only — no place name for a `not_in_DB11` unit (D14), and no counts, sizes or capacities (D12).

**Archetype — all nine resolve.**

| How it resolves | Units |
|---|---|
| Directly, on a plugin P2 Tier 1 archetype | `A001-P01` · `A001-P03` · `A001-P04` · `A001-P05` · `A001-P06` · `A001-P09` |
| By inheritance (`Tented Camp`, inheriting `Safari Lodge`) | `A001-P07` · `A001-P08` |
| On the main archetype only, secondary marked `secondary_unruled` (D13; a declared sandbox gap, AG-5, not a Sector rule) | `A001-P02` |

**Destination Fit.**

| Result | Units | Reason, by status only |
|---|---|---|
| ✅ Passes | `A001-P01` · `A001-P02` · `A001-P07` · `A001-P08` | Status `profiled` |
| 🔴 Fires | `A001-P03` | Status `in_DB11_not_profiled` — a DB 11 row exists, the DB 16 profile does not |
| 🔴 Fires | `A001-P04` · `A001-P05` · `A001-P06` · `A001-P09` | Status `not_in_DB11` — no DB 11 row, so no profile can exist |

**H-band.**

| Result | Units | Reason, by band only |
|---|---|---|
| ✅ Passes | `A001-P05` · `A001-P06` · `A001-P07` · `A001-P09` | H2, inside the H1/H2 MVP |
| 🔴 Fires | `A001-P01` · `A001-P04` | H3, outside the MVP |
| 🔴 Fires | `A001-P02` | H3, plus an unbanded serviced-apartment component |
| 🔴 Fires | `A001-P03` | Above H3 |
| 🔴 Fires | `A001-P08` | Below H1 |

**Deterministic rule checks.** The unit set was built so that units differ on one axis at a time, which is what makes these comparisons readable:

| Pair | Held constant | Varied | What it showed |
|---|---|---|---|
| `A001-P06` · `A001-P09` | archetype, destination status, band | nothing | Identical verdicts. The rules are deterministic for identically-shaped units |
| `A001-P04` · `A001-P05` | archetype, status `not_in_DB11` | band (H3 · H2) | Only the size outcome changed, so the size rule is independent of the geography rule |
| `A001-P01` · `A001-P08` | archetype pass, destination pass | band (H3 · below H1) | Both fail on size from opposite sides, bounding the MVP band at both ends |
| `A001-P03` · `A001-P04` | both fire destination and size | destination status | `in_DB11_not_profiled` is recoverable by authoring a profile; `not_in_DB11` is not, and commissioning is barred for A001 (D14) |
| `A001-P07` · `A001-P08` | archetype, destination, the declared link | band | `A001-P07` is the only unit passing all three unit checks. P08's link is recorded, but its meaning stays undefined (AG-9) |

**Why the group and every unit stay outside the current H1/H2 Offer MVP.**

- **The group (`A001`) carries three stop rules.** SR-1: its archetype is unresolvable, because the `Hospitality Group` union operator is not built (AG-4). SR-2: it has a central brand, reservations and direct-booking team, which Owner Decision 71 treats as anti-ICP. SR-3: it sits above every H-band.
- **Every unit inherits those three flags by design.** They are not suppressed at unit level, so no unit is assessed as though it were independent.
- **Only `A001-P07` passes every unit-level check**, and it still carries the group flags. The other three in-band units — `A001-P05`, `A001-P06` and `A001-P09` — each fail Destination Fit.
- **Recorded for all nine:** no offer runtime, no Sector store or CRM, pricing skipped. The sandbox returned the expected result, **outside the current offer ICP by design**, rather than a fit.

## 7. Architecture-gap register

**Class key:**
- **DOC:** documentation that can be written now.
- **BUILD:** a code or skill change. Needs owner approval; not Tier-1.
- **T1:** a Tier-1 architecture change (§8).
- **OWNER:** an owner decision that is not an architecture change.

| ID | Gap | Evidence | Class | Blocks |
|---|---|---|---|---|
| AG-1 | The answers file is one flat map per company, with no group/child structure and no `parent_id`. The template hard-codes `PILOT-H-001` | `intake_gate.py:126-134` | BUILD | Phases 1, 2 |
| AG-2 | No group or portfolio question rows exist: portfolio and linked units, central systems, group vs property decision rights, group channels, cross-property accounts | `CLIENT_INTAKE_PROFILE.md` §8; overlay §3 | DOC (draft rows), then item 73 ratification | Phase 1 |
| AG-3 | The gate:<br>• reads one overlay at a time;<br>• checks only the first word of a label;<br>• has no test-fixture mode, fingerprint key or sandbox-marker check;<br>• refuses an output path only inside the current repository, not inside other git trees | `intake_gate.py:131`; the `answers` and `scan` functions | BUILD | Phases 1, 3 |
| AG-4 | The `Hospitality Group` union operator is not built. A resolver must report a group as unresolvable | `HOSPITALITY_PLUGIN.md:157`; item 31i | BUILD (S09) | Phase 4 group resolution |
| AG-5 | No Sector rule covers a property that mixes archetypes. `Business Hotel` and `Serviced Apartment` are still in the older, unruled table.<br>✅ *Sandbox convention, 2026-09-15 (D13):* `A001-P02` resolves on its main archetype and marks the secondary `secondary_unruled`. It is a declared sandbox gap, **not a Sector rule** | `HOSPITALITY_PLUGIN.md:145-150` | OWNER (sector reasoning, 31i) for real sectors; the sandbox is covered by D13 | Nothing in the sandbox. A real mixed property still needs a Sector rule |
| AG-6 | Mombasa has no DB 16 profile, and four units sit in places with no DB 11 row. The plugin says routes are built "when a real engagement requires them"; A001 is not a real engagement.<br>✅ *Decided 2026-09-15 (D14):* commission nothing. Each unit records `profiled`, `in_DB11_not_profiled` or `not_in_DB11`, and blocked statuses are simulated verdicts | `SECTOR_OS.md` §3, Destination Intelligence row; `HOSPITALITY_PLUGIN.md:180` | ✅ Decided (D14) | Not scaffolding. Five units record `destination_fit: blocked` as their Phase 2 result |
| AG-7 | The Offer flow handles one property:<br>• `Draft 41` scopes a single property;<br>• the H-bands stop at H3 and exclude groups with a central team;<br>• no group or portfolio offer exists;<br>• no redirect destination is engineered | `OFFER_OS.md` §8 (Decision 71); capacity worksheet §2, P4 row | OWNER. A001 changes none of it | Phase 4 offer diagnostics. Expected result: `reject` / `needs_more_seed_data` |
| AG-8 | The audit's diagnostic gate needs client data, and synthetic data cannot produce a verdict | `Draft 41` diagnostic gate; capacity worksheet §1.4 | DOC. Closed in this file by `SIMULATED_VERDICT` (§4 rule 4) | Phases 3, 4 |
| AG-9 | The CRM has no `Company` object. The `AEIT_06` `Company` is not built, has no Company→Company parent/child or linked-unit edge, and has no sandbox role | `CRM_SCHEMA.md` Core Objects; `AEIT_06` lines 103-106 | **T1** | Any CRM-shaped representation of A001 (none planned) |
| AG-10 | Undecided whether a property is a `Company`, a Geography place at `Property` level, or both | `AEIT_06` line 79 | **T1** (decide with AG-9) | Phase 2 entity meaning |
| AG-11 | The `AEIT_05` knowledge-state `trust` attribute has no simulated or test-fixture value | `AEIT_05` line 117 | **T1** | Any knowledge object carrying A001 data (none planned) |
| AG-12 | The runtime appends each run's full `--input` to a git-tracked, auto-synced memory stream. No sandbox stream exists | `memory-writer.ts:22-38` | **T1** for a separate stream (a new store). DOC for the shared stream with markers | Phase 3 runs |
| AG-13 | Skill execution records forbid extra fields, so they cannot carry a sandbox marker | `skill-execution-record.schema.json` lines 16, 30 | **T1** | Any S10 hand-off record or skill record for A001 |
| AG-14 | Audits (14) agents cannot scope a hotel audit (offer #10 enums) | `CLIENT_INTAKE_PROFILE.md` §9 G-4 | OWNER / BUILD. Outside A001 scope | Nothing planned |
| AG-15 | Branding (12) BOIS writes client workspaces inside this repository | `CLIENT_INTAKE_PROFILE.md` §9 G-1; §10 ID2 | OWNER | Branding (12) is excluded from A001 |
| AG-16 | ✅ **RESOLVED 2026-09-15 — destination drift corrected and gated.** Plugin P4/P5, `plugin.config.json` P5, `SECTOR_NOTION_SCHEMA.md` and `FIELD_POPULATION_PLAN.md` now match DB 16: Nairobi · Maasai Mara · Diani profiled; Mombasa not profiled. `sector_truth_gate.py` **check 6** now fails if:<br>• plugin P5 and its sidecar disagree;<br>• either drifts from DB 16's verified row count;<br>• a P4 validation destination has no profile.<br>*Was:* those files predated the 2026-08-28 profiles, and the gate did not scan the plugin files | `HOSPITALITY_PLUGIN.md` v0.2 changelog; `sector_truth_gate.py` check 6; `SECTOR_OS.md` §15, 2026-09-15 | ~~DOC + BUILD~~ done | Nothing. Destination status may be read from plugin P5 or `SECTOR_OS.md` §3 |
| AG-17 | No Sector agent can check a hotel's company fit: `sector-icp-fit` and `sector-signal-scorer` are B2B SaaS-only, and S12 is not built | `SECTOR_OS.md` §15, 2026-09-14 entry | OWNER. Check fit by hand, as in item 72 RD4 | Phases 2, 3 (by hand only) |
| AG-18 | Marketing (03) and Operations (08) have no route from Sector | Item 31k | OWNER | Phase 5 (notes written by hand only) |
| AG-19 | ~~The API key should be rotated, and the rotation is not recorded as done~~ ✅ **Closed 2026-09-21 — rotation and revocation owner-attested and recorded done.** ⚠️ Replacement **not yet verified by use** | Item 57 (Resolved table) | OWNER | Any Phase 3 run — **still needs its own authorisation** |

## 8. Tier-1 changes needing ratification

Each change below either needs a new store or field (`SECTOR_ACTIVATION_PROTOCOL.md` I4: "ESCALATE") or adds a canonical entity, edge or attribute under `AEIT_06`. Each must pass the `AEIT_00` §5 Architecture Review Checklist before it is built. **The A001 decision approves none of them.**

| # | Change | Gap | Needed for | If not ratified |
|---|---|---|---|---|
| T1-1 | Build the `AEIT_06` `Company`, with a Company→Company `parent_of` edge and defined property-unit meaning, including `linked_to` | AG-9, AG-10 | Any entity-model test of A001 | A001's group structure lives only in the sandbox folder, and Phase 2 records the gap as its result |
| T1-2 | A non-commercial **sandbox** role for `Company` | AG-9 | Telling A001 apart from real companies in any shared store | A001 never enters a shared store |
| T1-3 | A test-fixture value for `AEIT_05`'s `trust` state attribute | AG-11 | Knowledge objects that carry A001 values | Labels are carried in text only (§4) |
| T1-4 | A sandbox marker field in `skill-execution-record.schema.json` | AG-13 | S10 hand-offs and any skill record for A001 | No skill records for A001; hand-offs by text note only |
| T1-5 | A separate sandbox memory stream in the runtime | AG-12 | Keeping A001 runs out of department memory streams | The owner chooses under item 74: no A001 runs, or runs into the shared stream with the §5 markers |

**T1-1…T1-5 were deferred on 2026-09-15 (D6).** None is needed while Phases 0–2 use no runtime (§5.1). Revisit before Phase 3.

**Owner decisions under item 74 that are not Tier-1:**
- ~~Confirm the archetype mapping in §6.~~ Decided 2026-09-15 (D13).
- Choose the run mode for Phase 3: no runs, the shared stream with markers, or T1-5. *(Phases 0–2: M0, decided 2026-09-15.)*
- ~~Decide whether to commission any geography for A001.~~ Decided 2026-09-15 (D14): commission nothing.
- ~~Supply the sandbox folder path.~~ Decided 2026-09-15 (D1).
- Approve the AG-4 build. *(AG-1/AG-3 deferred under the manual workaround, D7; AG-16's gate-scope build was completed 2026-09-15.)*

## 9. Phased run plan

Each phase starts only after the previous phase passes its exit gate **and its own entry gate below**. **No phase writes to Notion, ClickUp, a skill record, the plugin or the Offer registry.**

**Entry gates (owner ruling G1, 2026-09-15).** The Phase 0 exit gate was re-scoped. Item 74 decisions that only later phases need now gate those phases:

| Phase | Entry gate |
|---|---|
| 1 | Phase 0 complete: D1–D10 recorded and the key file validated. D11–D12 govern how Phase 1 answers are filled |
| 2 | ✅ **Met 2026-09-15:** item 74 point (3) archetype mapping (D13) and point (4) geography (D14) decided |
| 3 | ◐ **Partly met 2026-09-16:** run mode decided (D15, document-only first) and A001 ratified as a simulation sandbox only (D17). ✅ **API key rotation (AG-19 · D16) — owner-attested done 2026-09-21**, so the credential no longer gates runtime-backed Phase 3 work. ⚠️ The replacement is **not yet verified by use**, and runtime-backed work still needs its own authorisation. Document-only Phase 3 work may proceed and has begun — `A001-P07` reached S2 on 2026-09-16 (see "Phase 3 document-only progress") |
| 4 | AG-4 (S09 union operator) decided under item 74 point (6) |

| Phase | Scope | Work | Exit gate | Writes |
|---|---|---|---|---|
| **0 · Preconditions** | Repository and owner | 1. ~~Ratify item 74.~~ Re-scoped by G1 (2026-09-15): D1–D10 are recorded (§5.1). Archetype mapping and geography now gate Phase 2; the Phase 3 run mode and full ratification gate Phase 3.<br>2. ~~Fix the destination drift (AG-16).~~ ✅ Done 2026-09-15.<br>3. ~~Supply the sandbox folder path and confirm it is outside every git tree.~~ ✅ Path decided 2026-09-15 (D1). The git-tree check runs at creation and is saved in `00_admin\preflight_git_check.txt`.<br>4. ~~Build the key file: names, domains, fingerprints.~~ ✅ Done 2026-09-15 — key in place and validated by counts only; IDs-only scan test PASS; intake gate lint PASS.<br>5. ~~Choose the run mode (AG-12).~~ ✅ M0 for Phases 0–2 (D5); Phase 3 still open.<br>6. Rotate the API key (AG-19) — moved to the Phase 3 entry gate (G1). | ✅ **Met 2026-09-15 (G1):** D1–D10 recorded and the key file validated. *Was: every precondition marked done in item 74 — the remaining decisions now gate later phases (entry gates above).* | Repository documentation only |
| **1 · A001 group intake** | `A001` | A group answers file in the sandbox folder, every value `[TEST_FIXTURE · A001]`. Record the group's stop rules | Gate check once AG-1, AG-2 and AG-3 exist; until then a manual checklist against §4–§5. Expected verdict: **outside the current offer ICP, by design** | Sandbox folder; one verdict line in §6 |
| **2 · Child profiles** | `A001-P01` … `P09` | One answers file per unit with `parent_id: "A001"`. A fit record per unit: archetype, destination status, band, stop rules. Declare the P08→P07 link | ✅ **Met 2026-09-16:** all nine units hold a declared verdict in the §6 "Phase verdicts" table. *Was: every unit has a declared verdict in §6.* | Sandbox folder; §6 updates |
| **3 · First property slice** | `A001-P07`, inside A001 | 1. Simulated S1 profile.<br>2. Sector fit checked by hand, **carrying the group flags**.<br>3. Hand-off as a text note (no S10 record; AG-13).<br>4. Seed brief with IDs and the §5 markers.<br>5. `intake_gate.py --scan` against the key file.<br>6. Owner approves the exact input text.<br>7. **Only then**, and only if the run mode allows: a manual `offer-orchestrator` run and a structural `offer-oeos-engineer` run.<br>Skip pricing. | Stop on any name, URL, fingerprint, currency amount, synthetic KPI or missing marker | Sandbox folder. Runtime memory lines only if runs are approved |
| **4 · Group diagnostics** | `A001` and all units | Resolve the Nairobi and Maasai Mara units by hand, following S09's steps, with nothing emitted. Map each unit against P11 and the `Draft 41` (a)–(d) classes as `SIMULATED_VERDICT`. Output: a **structural gap list** covering the union operator, above-H3 size, no group offer, unengineered redirects, the entity edge and cross-property opportunities | Owner reviews the gap list | Sandbox folder; §7 updates |
| **5 · Downstream notes** | Content (04), Marketing (03), Sales (05) | Short notes labelled `[TEST_FIXTURE · A001] · not evidence · not publishable`. Each gives the angle only, never the artifact. No Content DB 5 rows, no briefs, no Design (19) generation, no CRM leads | Owner approves each note | Sandbox folder only |

### Phase 3 readiness — ◐ ENTRY DECISIONS RECORDED · DOCUMENT-ONLY EXECUTION UNDER WAY (updated 2026-09-16)

The owner recorded all five entry decisions on 2026-09-16, as **D15–D19** in §5.1. **Document-only Phase 3 work has since begun** — `A001-P07` reached S2, recorded under "Phase 3 document-only progress" below. **Anything runtime-backed stays blocked until the API key is rotated** (D16 · AG-19), and none has been attempted. *Was: "Phase 3 execution has not started, and no Phase 3 work of any kind has been performed" — true only until the S2 work began.*

| # | Entry decision | State | Recorded as |
|---|---|---|---|
| B1 | **Phase 3 run mode** | ✅ Decided 2026-09-16 — **no-runtime, document-only first** | D15 |
| B2 | **API key rotation** | ✅ **Owner-attested done 2026-09-21** — recorded as done. ⚠️ Replacement **not verified by use**; runtime-backed Phase 3 work still needs its own authorisation | D16 · AG-19 · item 57 |
| B3 | **A001 ratification** | ✅ Decided 2026-09-16 — **internal simulation sandbox only**: not a prospect, not a CRM record, not offer evidence | D17 |
| B4 | **Phase 3 slice** | ✅ Decided 2026-09-16 — stays **`A001-P07` only** | D18 |
| B5 | **S2 input format** | ✅ Decided 2026-09-16 — **switch to block-per-question before any owner fill** | D19 |

**What this opens, and what it does not.** Under D15, document-only Phase 3 work is permitted: hand-written simulated profiles, hand checks that carry the group flags, and hand-offs as text notes. **Still not permitted:** any `arika run`, agent, skill, scheduler or event activity · any runtime memory write · anything needing the API key, all of which wait on D16. §8 T1-1…T1-5 stay deferred under D6, and D17 ratifies the sandbox's standing, not those Tier-1 changes.

**B4 — what the Phase 2 evidence says.** `A001-P07` is still the only unit passing archetype, Destination Fit and the H-band together, so nothing in Phase 2 displaces it as the slice. `A001-P05`, `A001-P06` and `A001-P09` pass archetype and band but fail Destination Fit, and D14 bars commissioning a destination for A001, so none can be substituted without reopening D14. That is evidence for keeping Phase 3 `A001-P07`-only. ✅ **Decided 2026-09-16 (D18): the slice stays `A001-P07` only.**

### Phase 3 document-only progress (2026-09-16)

`A001-P07` — the Phase 3 slice under D18 — has completed **S2 intake** inside the sandbox, document-only under D15.

| Item | State |
|---|---|
| Stage reached | `S2` · `intake_gate.py --answers` passes at S2 |
| S2 required rows | Complete — every required row is declared |
| S2 optional rows | Some remain `NOT_ASKED`; they do not block the stage and never did |
| Phase 2 S1 verdict | Unchanged |
| S3–S5 | `BLOCKED` under D9 — the sandbox has no client system |
| Runtime-backed work | Blocked under D16 (AG-19) until the API key is rotated |

**What this is not.** It is **not** a new Offer verdict · **not** runtime output · **not** CRM or Sector-store evidence · **not** pricing. No `SIMULATED_VERDICT` line changed and none was added: reaching a stage is an intake milestone, not a classification, so §6 "Phase verdicts" — which holds verdict lines only — is untouched. The unit's Phase 2 verdict there stands as written.

**How the stage moved.** `intake_gate.py` fails any required row at or below `stage_reached` left `NOT_ASKED`. The stage was set only after a guard re-checked that rule, and the move was immediately followed by `--answers` at S2, with an automatic revert had it failed. It did not fail, so the stage rests on a passing gate rather than an assertion.

**Where the detail lives.** The unit's sandbox fit record holds the full checkpoint. Nothing beyond this IDs-only note has left the sandbox (D10).

**B5 — what the Phase 2 evidence says.** S1 worksheets are pipe tables of 42 rows. Cells were lost twice during owner fill: one trailing cell in `A001-P08`, and four cells across three rows in each of `A001-P01`, `A001-P02`, `A001-P06` and `A001-P09`. Both were caught by the apply script's cell-count guard before anything was written, and both needed owner-authorised repairs. S2 is 65 rows per unit, so the same format carries more exposure, and a format where each field is its own line cannot lose a cell. ✅ **Decided 2026-09-16 (D19): S2 switches to a block-per-question format before any owner fill.** The format itself is not built yet, and no S2 worksheet exists.

## 10. Changelog

- 2026-09-21 — **Correction to the pointer below.** It said runtime tests are *“blocked until B2-adjacent items R2/R3 give A001 a marked, isolated stream”*. That **understated the bar**: **D15 (B1)** forbids all A001 agent, skill, scheduler and event activity for Phase 3, and **D6** keeps T1-1…T1-5 — including R2 — deferred. **A build cannot lift either; only an owner decision can.** R2 and R3 matter only afterwards. Corrected in `A001_AGENCY_SYSTEMS_TEST_PLAN.md` v0.2 §3. No decision, flag or stop rule in this record changed. — Claude Code (Opus 5)
- 2026-09-21 — **Pointer: bounded agency-systems test plan created** — `01_Sector/A001_AGENCY_SYSTEMS_TEST_PLAN.md` (planning only, approves and runs nothing). It uses this record’s existing group flags and unit verdicts as **read-only** fixtures. **No unit is relabelled `PILOT-H-001`**, group flags and stop rules are preserved, and **P07’s unit-level passes are explicitly not Offer eligibility**. Every runtime test is blocked until B2-adjacent items **R2/R3** give A001 a marked, isolated stream. This record is otherwise unchanged. — Claude Code (Opus 5)
- 2026-09-21 — **B2 / D16 / AG-19: the API key rotation is recorded as done, from OWNER ATTESTATION.** Rotation and revocation are **owner-attested 2026-09-21** — the replacement key was installed in the intended secret location and the exposed old key was **revoked in the Anthropic Console**. ⚠️ **The replacement's validity is NOT verified by use** — that needs a runtime call and **none was made**. Nothing was read, printed or tested: no `.env`, no key, no key fragment, no secret log. §5.1's D16 row, §7's AG-19 row, §9's Phase 3 readiness row and the B2 blocker row are updated; **dated progress records are left as written**. 🔴 **This does not start Phase 3 runtime work:** the replacement is unverified, and **Closing the credential blocker authorises nothing further** — **not** A001 runtime-backed work, and **not** the real pilot run; each needs its own decision. — Claude Code (Opus 5)
- **v0.15 — 2026-09-16** — **D20 recorded: how A001 simulated evidence may and may not be used.** The open decision surfaced by the document-only pilot close-out is now settled and written into §5.1.
  - **Permitted — mechanisms only:** schemas, gates, intake formats, validators, routing logic, documentation and safe workflow design.
  - **Barred:** market, demand, pricing, proof, buyer and capacity evidence, and any claim about real hotels.
  - **The test:** A001 output may justify changing *how the system works*, never *how the market behaves*.

  It applies to every A001 output — both close-outs and every `SIMULATED_VERDICT` — in every department, permanently, not only during the phases. Recorded because this was the pilot's most likely route to misuse: the findings are genuinely useful about mechanisms and worthless about markets, and nothing previously stated the permitted half. The §5.1 heading now spans D1–D20. No verdict, register row, gap entry or gate changed. — Claude Code (Opus 5)
- **v0.14 — 2026-09-16** — **Phase 3 document-only progress recorded: `A001-P07` reached S2.** The Phase 3 slice (D18) completed S2 intake in the sandbox under the document-only run mode (D15). Every required S2 row is declared, `stage_reached` moved to S2, and `intake_gate.py --answers` passes at S2.
  - **Recorded as a checkpoint, not a verdict.** §6 "Phase verdicts" is defined as a table of `SIMULATED_VERDICT` lines showing that the gates ran. Reaching a stage produces no classification, so **no verdict line was added or changed**, and the note went to §9, where phase execution is tracked. The unit's Phase 2 verdict stands as written.
  - **What it is not:** not a new Offer verdict · not runtime output · not CRM or Sector-store evidence · not pricing.
  - **Still closed:** S3–S5 stay `BLOCKED` under D9 (the sandbox has no client system), and runtime-backed work stays blocked under D16 (API key rotation, AG-19) — now the only remaining Phase 3 entry blocker. Remaining optional S2 rows do not block the stage.

  **Two stale statements corrected.** §1 and the §9 Phase 3 entry-gate cell both said Phase 3 execution had not started, which stopped being true when S2 work began; the §9 readiness heading was renamed from "execution not started" to "document-only execution under way". No unit verdict, register row, decision or gap entry changed. No place name for a `not_in_DB11` unit (D14); no counts, sizes, capacities, currency, ratings or KPI values (D12). — Claude Code (Opus 5)
- **v0.13 — 2026-09-16** — **Phase 3 entry decisions recorded (D15–D19). Phase 3 execution has not started.**
  - **D15 (B1) run mode:** no-runtime, **document-only first**. Supersedes D5 for Phase 3 only.
  - **D16 (B2) API key rotation:** still required before any **runtime-backed** Phase 3 work (AG-19 · item 57). It does not block document-only work, which needs no key.
  - **D17 (B3) ratification:** A001 is ratified as an **internal simulation sandbox only** — not a prospect, not a CRM record, not offer evidence. It ratifies the sandbox's standing, **not** the §8 Tier-1 changes, which stay deferred under D6.
  - **D18 (B4) slice:** Phase 3 stays **`A001-P07` only**, confirmed against the Phase 2 evidence.
  - **D19 (B5) S2 input format:** S2 switches to **block-per-question** before any owner fill. The format is not built yet and no S2 worksheet exists.

  **Sections updated:** §1 status (no longer "not runnable" without qualification — now ratified, document-only, runtime-blocked) · §5.1 (the five decisions, and its heading now covers D1–D19) · §9 Phase 3 entry gate (◐ partly met) and "Phase 3 readiness" (renamed from 🔴 NOT READY to ◐ entry decisions recorded · execution not started), including the B4 and B5 paragraphs that previously said the decision was outstanding.

  **Unchanged:** every unit verdict, the child register, the gap register and §8. No place name for a `not_in_DB11` unit (D14); no counts, sizes, capacities, currency, ratings or KPI values (D12). — Claude Code (Opus 5)
- **v0.12 — 2026-09-16** — **Phase 2 closed out; Phase 3 readiness recorded as NOT READY.** Two new subsections. No verdict, register row, decision or gap entry changed.
  - **§6 "Phase 2 close-out"** — an IDs-and-statuses-only summary: which units pass archetype (all nine, two by inheritance and one on its main archetype only), which pass Destination Fit and which fire it by status only, which pass the H-band and which fire it by band only, the five deterministic rule checks the unit set was built to produce, and why the group and every unit stay outside the current H1/H2 Offer MVP.
  - **§9 "Phase 3 readiness"** — Phase 3 marked 🔴 NOT READY behind five named blockers: the Phase 3 run mode (B1), API key rotation (B2, AG-19), full A001 ratification (B3), whether Phase 3 stays `A001-P07`-only (B4), and whether S2 switches to a block-per-question input format before any owner fill (B5). B4 and B5 record what the Phase 2 evidence says and explicitly decide nothing.

  **Why B5 exists.** Owner fill silently dropped cells twice — one trailing cell in `A001-P08`, then four cells across three rows in each of four units. The apply script's cell-count guard caught both before any write, and both needed owner-authorised repairs. S2 is 65 rows per unit against S1's 42.

  **Content kept out:** no place name for a `not_in_DB11` unit (D14), and no counts, sizes, capacities, currency, ratings or KPI values (D12). — Claude Code (Opus 5)
- **v0.11 — 2026-09-16** — **Phase 2 verdicts for `A001-P01`, `A001-P02`, `A001-P06` and `A001-P09` written back (S1), and the Phase 2 exit gate marked met.** Four IDs-only rows added to the §6 "Phase verdicts" table:
  - `A001-P01` — archetype and Destination Fit pass; the size stop rule fires because H3 is outside the MVP;
  - `A001-P02` — the main archetype passes and the secondary stays `secondary_unruled` (AG-5); Destination Fit passes; the size stop rule fires on H3 plus serviced apartments;
  - `A001-P06` and `A001-P09` — archetype passes; Destination Fit fires because the destination is not in DB 11; the H-band passes at H2;
  - all four: group flags apply, each unit stays outside the current offer ICP by design, no Phase 3 planning, no offer runtime, Sector store or CRM, and pricing skipped.

  **Phase 2 exit gate (§9).** Its rule is that every unit has a declared verdict in §6. Five units qualified before these rows and four did not; with them, all nine do, so the gate is marked met. Phase 3 is unaffected and still waits on its own entry gate: the run mode, the API key rotation (AG-19) and full A001 ratification.

  **Basis:** each unit's validated S1 answers (`--answers` PASS at S1) and its fit record. `A001-P06` and `A001-P09` are structurally identical and returned the same verdict, which is the determinism check that pair exists for. `A001-P02` is the only unit that exercised the two-archetype rule, and its size rule fired on the hotel band alone, so the unbanded serviced-apartment component never had to be resolved to reach a verdict.

  **How it got here:** drafted in `90_scan\`, scanned with the A001 key and checked by hand before being written (D10). Owner-authorised worksheet repairs preceded the apply: in all four worksheets `U-C01`, `U-C04` and `U-D03` had lost their state, label, note and source-class cells, and were restored with every owner value unchanged. No other section changed. — Claude Code (Opus 5)
- **v0.10 — 2026-09-16** — **Phase 2 verdicts for `A001-P03`, `A001-P04` and `A001-P05` written back (S1).** Three IDs-only rows added to the §6 "Phase verdicts" table:
  - `A001-P03` — archetype passes; Destination Fit fires because the destination sits in DB 11 with no DB 16 profile; the size stop rule fires above H3;
  - `A001-P04` — archetype passes; Destination Fit fires because the destination is not in DB 11; the size stop rule fires because H3 is outside the MVP;
  - `A001-P05` — archetype passes; Destination Fit fires because the destination is not in DB 11; the H-band passes;
  - all three: group flags apply, each unit stays outside the current offer ICP by design, no Phase 3 planning, no offer runtime, Sector store or CRM, and pricing skipped.

  **Basis:** each unit's validated S1 answers (`--answers` PASS at S1) and its fit record. `A001-P05` is the only unit so far whose sole unit-level block is geography, and `A001-P04` is its H3 counterpart, so the pair separates the size rule from the geography rule. `A001-P03` differs from both: its destination has a DB 11 row and lacks only a DB 16 profile, which authoring would clear, while the other two have no DB 11 row at all.

  **How it got here:** drafted in `90_scan\`, scanned with the A001 key and checked by hand before being written (D10). No other section changed. Five of the nine units now hold a declared verdict; `A001-P01`, `A001-P02`, `A001-P06` and `A001-P09` remain scaffolds, so the Phase 2 exit gate is not yet met. — Claude Code (Opus 5)
- **v0.9 — 2026-09-15** — **Phase 2 verdict for `A001-P08` written back (S1).** One IDs-only row added to the §6 "Phase verdicts" table:
  - `A001-P08` · S1 · `SIMULATED_VERDICT`;
  - archetype and Destination Fit pass, and the size stop rule fires because the unit is below H1;
  - group flags apply;
  - the link to `A001-P07` is recorded, with AG-9 unresolved;
  - outside the current offer ICP by design;
  - no Phase 3 planning, because `A001-P07` remains the Phase 3 slice;
  - no offer runtime, Sector store or CRM; pricing skipped.

  **Basis:** the unit's validated S1 answers (`--answers` PASS at S1) and its fit record. The owner-authorised worksheet repairs (the source-class cell, the unit ID in six labels, and the optional H-A07 set to `NOT_ASKED`) were made in the sandbox before the apply.

  **How it got here:** drafted in `90_scan\`, scanned with the A001 key and checked by hand before being written (D10). No other section changed. — Claude Code (Opus 5)
- **v0.8 — 2026-09-15** — **Phase 2 verdict for `A001-P07` written back (S1).** One IDs-only row added to the §6 "Phase verdicts" table:
  - `A001-P07` · S1 · `SIMULATED_VERDICT`;
  - unit checks pass: archetype, Destination Fit and H-band;
  - group flags apply, so the unit stays outside the current offer ICP by design;
  - Phase 3 planning only after the Phase 3 entry gate;
  - no offer runtime, Sector store or CRM; pricing skipped.

  **Basis:** the unit's validated S1 answers (`--answers` PASS at S1) and its fit record. In that record the no-website and no-direct-path rules don't fire, and the link from `A001-P08` is recorded without blocking this unit (AG-9).

  **How it got here:** drafted in `90_scan\`, scanned with the A001 key and checked by hand before being written (D10). No other section changed. — Claude Code (Opus 5)
- **v0.7 — 2026-09-15** — **Phase 2 entry gate met: D13 and D14 recorded.**
  - **D13:** unit archetypes confirmed for sandbox use only, with a two-archetype rule. The main archetype resolves; the secondary is marked `secondary_unruled`, a declared sandbox gap, not a Sector rule.
  - **D14:** commission nothing for A001. Each unit records one status (`profiled`, `in_DB11_not_profiled`, `not_in_DB11`). Only currently profiled destinations pass Destination Fit, and blocked statuses are simulated verdicts.
  - **Updated to match:**
    - the §5.1 table and heading;
    - the §6 register: archetype column confirmed, `A001-P02` split into main and secondary, `A001-P08`'s link shown;
    - AG-5 and AG-6 (AG-6 now counts units rather than places);
    - the Phase 2 entry gate in §9;
    - the open lists in §1 and §8.
  - **No plugin or gate change.** D13's rule stays in the sandbox (§4 rule 2), and Destination Fit is the existing rule (31h).

  Documentation only; no unit file created, no answer filled. — Claude Code (Opus 5)
- **v0.6 — 2026-09-15** — **Phase 1 group verdict written back (S1).** One IDs-only line added under a new "Phase verdicts" table at the end of §6:
  - `A001` · S1 · `SIMULATED_VERDICT`;
  - outside the current offer ICP by design, and blocked for the current H1/H2 MVP;
  - Phase 2 only after item 74 points (3) and (4);
  - no offer runtime, Sector store or CRM; pricing skipped.

  **Basis:** the sandbox's validated S1 answers (`--answers` PASS at S1), with stop rules SR-1 to SR-3 firing by design and SR-4 to SR-6 not firing.

  **How it got here:** drafted in `90_scan\`, scanned with the A001 key and checked by hand before being written (D10). No other section changed. — Claude Code (Opus 5)
- **v0.5 — 2026-09-15** — **Owner rulings G1, D11 and D12 recorded.**
  - **G1:** the Phase 0 exit gate is re-scoped and now met (D1–D10 plus key validation). §9 gains an entry gate per phase: item 74 points (3) archetype and (4) geography gate Phase 2; the Phase 3 run mode, API key rotation and full ratification gate Phase 3; AG-4 gates Phase 4.
  - **D11:** Claude drafts values derived from rules and this record; the owner types values that come from the package; Claude does not read the package.
  - **D12:** values are bands, categories, statuses and unit IDs only.
  - §5.1 table and heading and §9 Phase 0 row updated to match.

  Documentation only; no answer filled, no package or key value read. — Claude Code (Opus 5)
- **v0.4 — 2026-09-15** — **Phase 0 setup checks passed.** The owner placed `00_admin\a001_key.json`. A counts-only script, which read no key value into the session and printed none, found it well-formed:
  - every expected field present;
  - a complete `id_map`;
  - no placeholder left and no entry shorter than 5 characters;
  - no entry that would fire on an ordinary place or archetype mention.

  The IDs-only scan test and the intake gate lint both pass. D2 (§5.1) and Phase 0 step 4 (§9) updated.

  ⚠️ **Phase 1 is not yet cleared to start.** Phase 0's exit gate still reads *every precondition marked done in item 74*, and archetype mapping, geography, the Phase 3 run mode and API key rotation remain open. Phase 1 needs either those decisions or an owner ruling that they belong to later phases. — Claude Code (Opus 5)
- **v0.3 — 2026-09-15** — **Phase 0 decisions D1–D10 recorded (Batch 3).**
  - **§5:** the key file is `00_admin\a001_key.json`. New key file rules: the current scan reads only `real_names` and `domains`; the superset rule; generic tokens and bare numbers are kept for manual checks.
  - **New §5.1:** Phase 0–2 operating mode M0 (no runtime), the D1–D10 table, the sandbox layout, answer conventions under the manual workaround, the git-tree check and the write-back rule.
  - **§1, §8 and §9 Phase 0 updated to match:** the Tier-1 changes are deferred, and the Phases 0–2 run mode and sandbox path are decided. Archetype mapping, geography, the Phase 3 run mode and AG-4 stay open.
  - ⚠️ **The owner-created key file was not in place at the setup check,** so its counts-only validation and the scan test are still to run.

  Documentation only. No answer filled, no package content read, no runtime used. — Claude Code (Opus 5)
- **v0.2 — 2026-09-15** — **AG-16 resolved.** The Hospitality destination drift was corrected in plugin P4/P5, `plugin.config.json` P5, `SECTOR_NOTION_SCHEMA.md` and `FIELD_POPULATION_PLAN.md`, and is now gated by `sector_truth_gate.py` check 6 (record: `SECTOR_OS.md` §15). Updated with it, so the file stays consistent: the §6 destination-status note, the §8 owner-decision bullet, and Phase 0 step 2 in §9. No other gap, phase or register row changed; A001 remains unratified and not runnable. — Claude Code (Opus 5)
- **v0.1 — 2026-09-15** — File created when the owner approved A001 as the group-level simulated Hospitality Sector Sandbox. Contents:
  - status and decision (§1), and what A001 is and is not (§2);
  - the ID scheme (§3);
  - provenance mapping to `[TEST_FIXTURE · A001]`, including a `SIMULATED_VERDICT` rule (§4);
  - storage rules and a runtime marker convention (§5);
  - a nine-unit child register using IDs only (§6);
  - a 19-item architecture-gap register (§7);
  - five Tier-1 changes for ratification (§8);
  - a six-phase run plan (§9).

  Documentation only. Nothing was imported from the simulation package. No agent run, event, scheduler start, Notion or ClickUp write, memory-log write, or `.env` read. Decision recorded in `SECTOR_OS.md` §8 and `OFFER_OS.md` §8; tracker item 74. — Claude Code (Opus 5)
