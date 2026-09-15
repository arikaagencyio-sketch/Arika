# A001 — Hospitality Sector Sandbox

**Department:** Sector (01) — owns this record. Offer (02) consumes it.
**Owner:** Mary Thuo
**Status:** ✅ Approved by the owner 2026-09-15 as a sandbox and architecture specimen · 🔴 **Not runnable.** No A001 run of any kind until item 74's prerequisites are ratified (§8, §9 Phase 0).
**Version:** v0.3

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
- The archetype mapping in §6.
- Geography.
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

### 5.1 Phase 0–2 operating mode (owner decisions D1–D10, 2026-09-15)

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
| D2 | Key file | `00_admin\a001_key.json`, created by the owner. **Not yet in place at the 2026-09-15 setup check**; validation by counts runs once it is |
| D3 | Key custody | Key values never enter a Claude session. The file is validated by a script that prints counts only |
| D4 | Package custody | The simulation package stays where the owner holds it for now; nothing is extracted |
| D5 | Run mode | M0 for Phases 0–2 |
| D6 | Tier-1 | T1-1…T1-5 deferred |
| D7 | Intake tooling | Manual workaround; AG-1/AG-3 builds deferred |
| D8 | Answer label | `[OWNER-SUPPLIED · TEST_FIXTURE · A001 · YYYY-MM-DD]`, plus `· DERIVED` / `· ASSUMED` where applicable |
| D9 | Stage cap | S2. S3–S5 rows are `BLOCKED` with the note "A001 sandbox — no client system". Synthetic data stays in source custody, never in answers |
| D10 | Write-back | Only IDs-only verdict lines leave the sandbox, after `--scan` and the manual checks |

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
- **Archetype class** uses the `HOSPITALITY_PLUGIN.md` P1 vocabulary. It is **proposed from the package's descriptions, for the owner to confirm under item 74.**
- **Destination status** comes from `SECTOR_OS.md` §3 (DB 16 profiled: Nairobi · Maasai Mara · Diani; Mombasa not profiled). Plugin P5 now agrees with it (AG-16, resolved 2026-09-15 and gated by `sector_truth_gate.py` check 6). Places with no DB 11 row are not named here; their names are in the key file.
- **Size band** uses Owner Decision 71's H-bands **as a label only**. A band does not bring any unit into MVP scope or capacity.

| Unit | Archetype class (proposed) | Destination status | Size band | Stop-rule status |
|---|---|---|---|---|
| **`A001`** (group) | `Hospitality Group` | Multi-destination | **Above H3** on property count and on keys | 🔴 Group archetype unresolvable (union operator not built) · 🔴 anti-ICP: central brand, reservations and direct-booking team · 🔴 above every H-band |
| `A001-P01` | `City / Conference Hotel` | ✅ Nairobi, DB 16 profiled | H3 | 🟡 H3 is outside MVP scope and capacity · group flags |
| `A001-P02` | `City / Conference Hotel` + `Serviced Apartment` (mixed) | ✅ Nairobi, DB 16 profiled | H3 (hotel keys), plus serviced apartments | 🟡 H3 · 🔴 P1/P2 cannot express a mixed archetype, and `Serviced Apartment` is still in the older, unruled table · group flags |
| `A001-P03` | `Beach Resort` | 🔴 Mombasa: in DB 11 with **no DB 16 profile**, so Destination Fit blocks it (31h) | **Above H3** | 🔴 Destination Fit · 🔴 above every H-band · group flags |
| `A001-P04` | `City / Conference Hotel` | 🔴 Not in DB 11 | H3 | 🔴 geography unresolvable · 🟡 H3 · group flags |
| `A001-P05` | `City / Conference Hotel` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |
| `A001-P06` | `Safari Lodge` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |
| **`A001-P07`** | `Tented Camp`, inheriting `Safari Lodge` | ✅ Maasai Mara, DB 16 profiled | **H2** | ✅ **No unit-level stop rule** · 🔴 group flags still apply, so the slice runs as a **group-architecture test**, not an MVP audit |
| `A001-P08` → P07 | `Tented Camp`, inheriting `Safari Lodge` | ✅ Maasai Mara, DB 16 profiled | **Below H1** | 🔴 below every H-band · 🔴 linked-unit meaning undefined (AG-9) · group flags |
| `A001-P09` | `Safari Lodge` | 🔴 Not in DB 11 | H2 | 🔴 geography unresolvable · group flags |

**What the register shows:**
- **Destination:** 4 of 9 units resolve (P01, P02, P07, P08).
- **Band:** 4 of 9 fall inside H1/H2 (P05, P06, P07, P09).
- **Every unit-level check:** only `A001-P07` passes destination, band and archetype together.
- **Group flags:** every unit carries them. The sandbox exists to show what the system does with those flags, not to hide them.

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
| AG-5 | No rule covers a property that mixes archetypes. `Business Hotel` and `Serviced Apartment` are still in the older, unruled table | `HOSPITALITY_PLUGIN.md:145-150` | OWNER (sector reasoning, 31i) | Phase 2 for P02 |
| AG-6 | Mombasa has no DB 16 profile, and four child places have no DB 11 row. The plugin says routes are built "when a real engagement requires them"; A001 is not a real engagement | `SECTOR_OS.md` §3, Destination Intelligence row; `HOSPITALITY_PLUGIN.md:180` | OWNER. **Default: commission nothing, and record "blocked by Destination Fit" as the result** | Phases 2 and 4 for five units |
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
| AG-19 | The API key should be rotated, and the rotation is not recorded as done | Item 57 (Resolved table) | OWNER | Any Phase 3 run |

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
- Confirm the archetype mapping in §6.
- Choose the run mode for Phase 3: no runs, the shared stream with markers, or T1-5. *(Phases 0–2: M0, decided 2026-09-15.)*
- Decide whether to commission any geography for A001 (default: no; AG-6).
- ~~Supply the sandbox folder path.~~ Decided 2026-09-15 (D1).
- Approve the AG-4 build. *(AG-1/AG-3 deferred under the manual workaround, D7; AG-16's gate-scope build was completed 2026-09-15.)*

## 9. Phased run plan

Each phase starts only after the previous phase passes its exit gate. **No phase writes to Notion, ClickUp, a skill record, the plugin or the Offer registry.**

| Phase | Scope | Work | Exit gate | Writes |
|---|---|---|---|---|
| **0 · Preconditions** | Repository and owner | 1. Ratify item 74 — *partly recorded 2026-09-15:* D1–D10 (§5.1). Archetype mapping, geography and the Phase 3 run mode stay open.<br>2. ~~Fix the destination drift (AG-16).~~ ✅ Done 2026-09-15.<br>3. ~~Supply the sandbox folder path and confirm it is outside every git tree.~~ ✅ Path decided 2026-09-15 (D1). The git-tree check runs at creation and is saved in `00_admin\preflight_git_check.txt`.<br>4. Build the key file: names, domains, fingerprints — ⏳ **owner**. Not in place at the 2026-09-15 check, so the counts-only validation and the scan test have not run.<br>5. ~~Choose the run mode (AG-12).~~ ✅ M0 for Phases 0–2 (D5); Phase 3 still open.<br>6. Rotate the API key (AG-19) — needed before Phase 3 only. | Every precondition marked done in item 74 | Repository documentation only |
| **1 · A001 group intake** | `A001` | A group answers file in the sandbox folder, every value `[TEST_FIXTURE · A001]`. Record the group's stop rules | Gate check once AG-1, AG-2 and AG-3 exist; until then a manual checklist against §4–§5. Expected verdict: **outside the current offer ICP, by design** | Sandbox folder; one verdict line in §6 |
| **2 · Child profiles** | `A001-P01` … `P09` | One answers file per unit with `parent_id: "A001"`. A fit record per unit: archetype, destination status, band, stop rules. Declare the P08→P07 link | Every unit has a declared verdict in §6 | Sandbox folder; §6 updates |
| **3 · First property slice** | `A001-P07`, inside A001 | 1. Simulated S1 profile.<br>2. Sector fit checked by hand, **carrying the group flags**.<br>3. Hand-off as a text note (no S10 record; AG-13).<br>4. Seed brief with IDs and the §5 markers.<br>5. `intake_gate.py --scan` against the key file.<br>6. Owner approves the exact input text.<br>7. **Only then**, and only if the run mode allows: a manual `offer-orchestrator` run and a structural `offer-oeos-engineer` run.<br>Skip pricing. | Stop on any name, URL, fingerprint, currency amount, synthetic KPI or missing marker | Sandbox folder. Runtime memory lines only if runs are approved |
| **4 · Group diagnostics** | `A001` and all units | Resolve the Nairobi and Maasai Mara units by hand, following S09's steps, with nothing emitted. Map each unit against P11 and the `Draft 41` (a)–(d) classes as `SIMULATED_VERDICT`. Output: a **structural gap list** covering the union operator, above-H3 size, no group offer, unengineered redirects, the entity edge and cross-property opportunities | Owner reviews the gap list | Sandbox folder; §7 updates |
| **5 · Downstream notes** | Content (04), Marketing (03), Sales (05) | Short notes labelled `[TEST_FIXTURE · A001] · not evidence · not publishable`. Each gives the angle only, never the artifact. No Content DB 5 rows, no briefs, no Design (19) generation, no CRM leads | Owner approves each note | Sandbox folder only |

## 10. Changelog

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
