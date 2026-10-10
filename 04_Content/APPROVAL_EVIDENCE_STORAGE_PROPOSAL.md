# Approval evidence storage and content fingerprint — proposal

**Department:** Content (04) · **Prepared:** 2026-10-09 (hardening unit) · **Amended:** 2026-10-10 (follow-up unit: resolved publishing context, §3.1) · **Status: PROPOSAL ONLY.** No Notion property, no code, no formula has been added.

Applying it needs three things, in this order:
1. Owner approval of this document, including the choices in §7.
2. A separate, human-invoked Notion session.
3. The contract, gate and tests changed in the same change.

Rules it builds on: [`CONTENT_WRITE_CONTRACT.md`](CONTENT_WRITE_CONTRACT.md) §0.2, §7.1, §8 and §8.1.

## 1. The problem, stated narrowly

Four things today live only in conventions or in evidence handed to the gate:

| What | Where it lives now | Consequence |
|---|---|---|
| **G1** (decision, reviewer, date, revision, path) | A page-body line on the brief | The routine cannot read it, and nothing in Notion shows a stale G1. A human must carry it into the gate snapshot by hand |
| **The G2-approved asset set** | A list in the G2 packet on the page body | Publication compares against whatever the publisher copies across. Nothing in Notion records which assets were approved |
| **Whether the approved copy is still the copy** | Nowhere | A direct Notion edit to `Caption` without a `Version` bump is invisible. `Approval Integrity` compares revision numbers, not content |
| **The resolved publishing context**: Surface, Audience Role and Format *(added 2026-10-10)* | On the linked DB6 translation page, reached through DB7's `Translation` relation | The relation can keep the same page ID while that page's `Surface` changes (founder profile → Company Page), or its `Audience Role` or `Format`. **Today the approval silently carries over.** The publication check compares the published surface with the surface read *at publication*, not with the surface that was approved |

## 2. Minimal storage: six additive DB7 properties

None of these is trigger-read: the six frozen properties (R17) are untouched, and the routine is unaffected. Writer classes follow `content-databases.json`.

| Property | Type | Writer | Values / meaning |
|---|---|---|---|
| `G1 Decision` | select | `human_only` | `Passed (design)` · `Passed (text-only)` · `Returned`. Empty means not reviewed. Decision and path are one human choice, so they share one property |
| `G1 Reviewer` | text | `human_only` | The named reviewer |
| `G1 Decided At` | date | `human_only` | |
| `G1 Revision` | number | `human_only` | The `Version` the G1 covers. Any later bump makes it stale |
| **Option A (recommended, 2026-10-10):** `G2 Packet Manifest` — or **Option B (as first proposed, 2026-10-09):** `G2 Asset Set` | text | `C06` (at submission) | **A:** canonical JSON `{"assets": [...], "resolved": {...}}` (§3, §3.1). **B:** canonical JSON `[{"asset_id", "version", "provenance": {"brief_id", "brief_revision"}}]`, sorted by `asset_id`, empty for text-only. Under B, the resolved context lives only inside the fingerprint input and the page-body G2 packet |
| `G2 Submitted Fingerprint` | text | `C06` (at submission) | `sha256:<hex>` of the canonical content (§3), computed by the gate from a fresh read-back |

**The field count is unchanged: six properties under either option** (DB7: 49 → 55).

Option A changes the *name and content* of one proposed property, not the count. It is presented for owner approval, not assumed. Why A:
- with the resolved values stored next to the assets, a fingerprint mismatch can be **explained from Notion data alone** (for example, "`surface` changed from `LinkedIn - Founder profile` to `LinkedIn - Company Page`");
- under B, the reason has to be dug out of the page body.

Both options detect the change equally, because both feed the same fingerprint.

**How approval binds.** The human approves by setting `G2 Decision = Approved` and `G2 Approved Revision = Version`, as today. An approval covers the submitted revision, the asset set, the resolved context and the fingerprint together. **No new human field is needed for G2.**

**`Approval Integrity` formula extension (proposal).** Turn the cell red in any of these cases:
- `G1 Revision ≠ Version` while `Publishing Status` is past `In progress`;
- `Publishing Status = Ready for Design` while `G1 Decision ≠ Passed (design)`;
- `G2 Approved Revision ≠ G1 Revision`.

A formula can only *show* this. It cannot stop a person changing the select, and it cannot see a linked page change (no hash, no cross-page compare).

DB7 would go from **49 to 55 fields**. `LIVE_FIELD_COUNTS`, the contract JSON and the gate change in the same change (rollback dependency: `CONTENT_UNIT_ROLLBACK_PROPOSAL.md` §2).

## 3. Content fingerprint: specification (not implemented)

- **Algorithm.** SHA-256, lowercase hex, prefixed `sha256:`.
- **Input.** Canonical JSON (UTF-8, keys sorted, separators `,` and `:` with no spaces, non-ASCII kept) of:
  ```
  {"brief_id": <canonical page id>, "revision": <Version as int>,
   "fields":   {<every DB7 field marked publication_affecting in content-databases.json>},
   "assets":   [[asset_id, version], ...]  sorted,
   "resolved": {"translation_id": <canonical page id>,
                "surface":        <exact Notion option name | null>,
                "audience_role":  <exact Notion option name | null>,
                "format":         <exact Notion option name | null>}}
  ```
  The `publication_affecting` fields are `Script`, `Caption`, `Visual Direction`, `Canva Instructions`, `Engagement Follow-up`, `Evidence`, `Platform` (sorted), `Translation` and `Offer` (sorted page IDs). The fingerprint follows that flag automatically, so there is one definition, not two. `resolved` was added 2026-10-10 (§3.1).
- **Normalisation.**
  - Rich text becomes Notion's concatenated `plain_text`.
  - Unicode NFC; `\r\n` becomes `\n`.
  - **No trimming:** a whitespace change is a change.
  - An empty text field is `""`, never omitted.
  - An empty select inside `resolved` is `null` (§3.1).
- **Computed by.** The gate (a future `content_fingerprint()` with tests), from pages read back in the same session. **Never by the routine:** an LLM computing SHA-256 is not reliable. Notion formulas have no hash function.
- **Checked by.**
  - **At submission:** C06 computes and writes it.
  - **At publication:** `validate_publication` recomputes it from fresh reads. A mismatch would be a new refusal, `R26_FINGERPRINT_MISMATCH`.
  - **On re-submission:** a changed fingerprint at the same `Version` means something publishable changed without a bump. Refuse, and require a VERSION.

### 3.1 Resolved publishing context: capture, normalise, compare (amendment 2026-10-10)

**What is captured.** The `Surface`, `Audience Role` and `Format` select values on the **one** DB6 page that the brief's `Translation` relation points to. These are the values that decide where the piece is published, in what voice, for whom and in what shape. None of them is a DB7 field.

**How it is read (deterministic):**
1. Read the DB7 brief page. Then fetch the translation page **by the ID in its `Translation` relation**, in the same session.
2. The relation must hold **exactly one** page ID. Zero or several means no fingerprint, and C06 does not submit; the brief is malformed for G2.
3. Each value is the **exact Notion option name** as returned, normalised to Unicode NFC and nothing else: no case-folding, no dash or space normalisation. Agent enums (`linkedin_company_page`) never appear. A value outside `content-databases.json` → `vocabularies` means no fingerprint (unknown fails closed: R09_SURFACE_UNKNOWN, R23).
4. An **empty** select becomes JSON `null`. `null` always means "read, and empty". It never stands in for "could not read". The G2 submission check already refuses an unassigned surface, and an empty audience or format fails the same way.
5. **Page IDs** go into the input in one canonical form: 32 lowercase hex characters, no dashes. A dashed UUID is converted; anything else means no fingerprint.

   This is a fingerprint rule. The gate's current rule for write targets (follow-up unit, 2026-10-10) compares IDs **exactly as given** and refuses a dashed/undashed mix rather than converting it. When this proposal is applied, skills canonicalise IDs at read time, and the gate keeps comparing the canonical strings exactly.

**Unreadable context (never inherited, never "unchanged"):**
- The translation fetch fails (error, timeout, permission, quota), or returns without one of the three properties (for example, a renamed property). The state is **`context_unreadable`**:
  - no fingerprint is computed;
  - the stored manifest or fingerprint is **not** reused in its place;
  - C06 does not submit;
  - the publication check refuses, as a new `R27_CONTEXT_UNREADABLE`.
- The operation is **incomplete**, not passed. Retry later. A failed read is never treated as a match, and never as empty.

**Comparison, and what happens on a change:**
- **Recompute from fresh reads** at publication and at any re-check. Compare with `G2 Submitted Fingerprint`.
  - Equal: the approved copy, assets and context all still hold.
  - Different: R26, publication refused.
  - Under Option A, the gate also diffs the stored manifest against the fresh one and names the component that moved (`resolved.surface`, `resolved.audience_role`, `resolved.format`, an asset, or copy).
- **A context change is publication-affecting even though no DB7 field changed.** The approval does not carry over:
  1. C04 records a **VERSION** on the brief: `Version + 1`, plus a change line naming the context change and the prior value.
  2. That bump makes G1 and G2 stale, because both bind to `Version`. `Approval Integrity` goes red (`G2 Approved Revision ≠ Version`).
  3. Both gates are re-done on the new Version.

  Pointing `Translation` at a different page is already a `Translation` field change, so the existing VERSION rule applies.
- **Order of reads matters for honesty, not for the hash.** Both pages are read before computing. A change made to either page between the two reads shows up at the next check. It can never be averaged away.

**Not covered by `resolved` (stated, not solved):**
- the translation's `Platform` relation and `Translation Family ID`;
- the linked Offer page's `Offer Status`;
- the wording of the linked Narrative Position;
- the opportunity's DRAGON status after G2;
- any other attribute of a linked page.

The extension options are in §7. Each is the same mechanism with no new property.

## 4. Direct Notion edits: what this would and would not catch

**It would catch, the next time someone runs the check:**
- a copy edit after submission without a `Version` bump;
- an asset swapped after approval;
- a changed `Translation` or `Offer` relation;
- a `G1 Revision` left behind by a bump;
- **a `Surface`, `Audience Role` or `Format` changed on the linked translation page while no DB7 field moved** (2026-10-10);
- **an unreadable translation passed off as "unchanged"**: it refuses instead (2026-10-10).

**It would not catch:**
1. **Anything while no one runs the check.** The gate runs only when a skill or person invokes it. No scheduled verifier exists. `automation-reliability-monitor` is not scheduled, and scheduling anything is an activation that needs its own approval.
2. **Edits between the last check and the moment of publishing.** Publication is manual, so the publisher should copy from the G2 packet's text, not from the live page. Even then, the gap is human discipline.
3. **A person editing a `human_only` field.** "Human-only" is this contract's convention. Notion does not enforce per-property write permissions for workspace editors. Whether page-level permissions on the current plan could narrow this is **not verified**.
4. **A person editing the fingerprint itself.** The publication check recomputes from content, so a forged fingerprint would still mismatch the content. But a person who edits both content and fingerprint consistently is not detectable by design. The same goes for the manifest under Option A.
5. **Formatting-only rich-text changes**, because of `plain_text` extraction, and **non-publication-affecting fields**, by design.
6. **Linked-page attributes outside `resolved`** (§3.1), unless the owner extends it.
7. **History.** Notion page history is the only native audit trail. Its retention depends on the plan and is not verified here.

**Optional cheap signal (not part of the minimal set).** A `Last edited time` property plus a formula flag when it is later than `G2 Decided At`. It is page-level, so it also trips on benign edits. It also does not see edits to *linked* pages. **Whether adding a comment, such as the routine's, changes `Last edited time` is not verified.** Test that before relying on it.

## 5. What else would change when applied

- **Gate:**
  - read G1 from the four properties, not the page-body line;
  - add `content_fingerprint()`, R26 and R27;
  - **stop trusting the surface read at publication time.** Compare the published surface, audience and format with the approved `resolved` values instead.

  Snapshot keys change accordingly.
- **Routine v2 (a separate prompt amendment and approval):** it could then block a brief whose `G1 Decision ≠ Passed (design)` or whose `G1 Revision ≠ Version`, as a new BLOCKED reason. Until then, CHANGE_PROPOSAL step T2a is the human hold.
- **No approval-matrix row** is needed for the properties themselves (manual apply). The routine change would amend its existing row.

## 6. Apply steps (later; each needs approval)

1. Read-only fetch of DB7. Confirm 49 properties and the six trigger-read properties unchanged.
2. Add the six properties, using the fifth property's name from the option the owner chose (§2). Each Notion `COMMENT` must be 280 characters or fewer, or the DDL is rejected (observed 2026-10-09).
3. Read back. Record the `G1 Decision` option names and IDs in `content-databases.json`, and pin them in tests.
4. In the same change, update:
   - the contract JSON (55 fields, writers as §2);
   - the gate (G1 from properties, fingerprint with `resolved`, R26, R27);
   - the tests;
   - `CONTENT_INTELLIGENCE_SCHEMA.md` §10.
5. **No backfill.** No G1 has been given yet; the two existing briefs stay empty, meaning not reviewed.
6. **Rollback:** drop the six properties. Nothing depends on them while they are empty.

## 7. Owner choices this proposal needs

- **G1 Decision options.** Merge decision and path into one select (proposed), or keep two fields. Keeping two would add one field: an alternative, not the recommendation.
- **Fifth property (2026-10-10).** Option A, `G2 Packet Manifest` (recommended), or Option B, `G2 Asset Set`. Both have six properties.
- **Scope of `resolved` (2026-10-10).** Keep the three values (proposed), or extend it to the translation's `Platform` relation IDs and the linked Offer's `Offer Status`. That is the same mechanism with no new property.
- **Reviewers.** Who may record G1 and G2. Only the owner, or named reviewers?
- **Last-edited signal.** Whether it is wanted, after verifying the comment behaviour.

## 8. Changelog

- **2026-10-10** — Amended under the owner's follow-up brief. Changes:
  - The resolved publishing context (Surface, Audience Role, Format) is captured and compared through the fingerprint (§3.1), so a linked page changing beneath an unchanged relation ID cannot inherit the previous approval.
  - Deterministic normalisation and unreadable-context handling are defined (R27).
  - Option A (`G2 Packet Manifest`) is presented for approval against Option B, the original `G2 Asset Set`. The field count stays at six either way.
  - Not implemented. — Claude Code (Opus 5.5)
- **2026-10-09** — Prepared under the owner's hardening brief ("Prepare, but do not implement, the minimal G1/approved-asset storage and content-fingerprint proposal. Explain direct-Notion-edit limits."). — Claude Code (Opus 5.5)
