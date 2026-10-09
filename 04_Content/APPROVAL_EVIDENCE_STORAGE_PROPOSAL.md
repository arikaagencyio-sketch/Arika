# Approval evidence storage and content fingerprint — proposal

**Department:** Content (04) · **Prepared:** 2026-10-09 (hardening unit) · **Status: PROPOSAL ONLY.** No Notion property, no code, no formula has been added.

Applying it needs three things, in this order:
1. Owner approval of this document.
2. A separate, human-invoked Notion session.
3. The contract, gate and tests changed in the same change.

Rules it builds on: [`CONTENT_WRITE_CONTRACT.md`](CONTENT_WRITE_CONTRACT.md) §0.2, §8 and §8.1.

## 1. The problem, stated narrowly

Three things today live only in conventions or in evidence handed to the gate:

| What | Where it lives now | Consequence |
|---|---|---|
| **G1** (decision, reviewer, date, revision, path) | A page-body line on the brief | The routine cannot read it, and nothing in Notion shows a stale G1. A human must carry it into the gate snapshot by hand |
| **The G2-approved asset set** | A list in the G2 packet on the page body | Publication compares against whatever the publisher copies across. Nothing in Notion records which assets were approved |
| **Whether the approved copy is still the copy** | Nowhere | A direct Notion edit to `Caption` without a `Version` bump is invisible. `Approval Integrity` compares revision numbers, not content |

## 2. Minimal storage: six additive DB7 properties

None of these is trigger-read: the six frozen properties (R17) are untouched, and the routine is unaffected. Writer classes follow `content-databases.json`.

| Property | Type | Writer | Values / meaning |
|---|---|---|---|
| `G1 Decision` | select | `human_only` | `Passed (design)` · `Passed (text-only)` · `Returned`. Empty means not reviewed. Decision and path are one human choice, so they share one property |
| `G1 Reviewer` | text | `human_only` | The named reviewer |
| `G1 Decided At` | date | `human_only` | |
| `G1 Revision` | number | `human_only` | The `Version` the G1 covers. Any later bump makes it stale |
| `G2 Asset Set` | text | `C06` (at submission) | Canonical JSON: `[{"asset_id", "version", "provenance": {"brief_id", "brief_revision"}}]`, sorted by `asset_id`. Empty for text-only |
| `G2 Submitted Fingerprint` | text | `C06` (at submission) | `sha256:<hex>` of the canonical content (§3), computed by the gate from a fresh read-back of the page |

**How approval binds.** The human approves by setting `G2 Decision = Approved` and `G2 Approved Revision = Version`, as today. An approval covers the submitted revision, asset set and fingerprint together. **No new human field is needed for G2.**

**`Approval Integrity` formula extension (proposal).** Turn the cell red in any of these cases:
- `G1 Revision ≠ Version` while `Publishing Status` is past `In progress`;
- `Publishing Status = Ready for Design` while `G1 Decision ≠ Passed (design)`;
- `G2 Approved Revision ≠ G1 Revision`.

A formula can only *show* this. It cannot stop a person changing the select.

DB7 would go from **49 to 55 fields**. `LIVE_FIELD_COUNTS`, the contract JSON and the gate change in the same change (rollback dependency: `CONTENT_UNIT_ROLLBACK_PROPOSAL.md` §2).

## 3. Content fingerprint: specification (not implemented)

- **Algorithm.** SHA-256, lowercase hex, prefixed `sha256:`.
- **Input.** Canonical JSON (UTF-8, keys sorted, no insignificant whitespace, non-ASCII kept) of:
  ```
  {"brief_id": <page id>, "revision": <Version as int>,
   "fields": {<every DB7 field marked publication_affecting in content-databases.json>},
   "assets": [[asset_id, version], ...] sorted}
  ```
  The `publication_affecting` fields are `Script`, `Caption`, `Visual Direction`, `Canva Instructions`, `Engagement Follow-up`, `Evidence`, `Platform` (sorted), `Translation` and `Offer` (sorted page IDs). The fingerprint follows that flag automatically, so there is one definition, not two.
- **Normalisation.**
  - Rich text becomes Notion's concatenated `plain_text`.
  - Unicode NFC; `\r\n` becomes `\n`.
  - **No trimming:** a whitespace change is a change.
  - An empty field is `""`, never omitted.
- **Computed by.** The gate (a future `content_fingerprint()` with tests), from a page read back in the same session. **Never by the routine:** an LLM computing SHA-256 is not reliable. Notion formulas have no hash function.
- **Checked by.**
  - **At submission:** C06 computes and writes it.
  - **At publication:** `validate_publication` recomputes it from a fresh read. A mismatch would be a new refusal, `R26_FINGERPRINT_MISMATCH`.
  - **On re-submission:** a changed fingerprint at the same `Version` means copy changed without a bump. Refuse, and require a VERSION.

## 4. Direct Notion edits: what this would and would not catch

**It would catch, the next time someone runs the check:**
- a copy edit after submission without a `Version` bump;
- an asset swapped after approval;
- a changed `Translation` or `Offer` relation;
- a `G1 Revision` left behind by a bump.

**It would not catch:**
1. **Anything while no one runs the check.** The gate runs only when a skill or person invokes it. No scheduled verifier exists. `automation-reliability-monitor` is not scheduled, and scheduling anything is an activation that needs its own approval.
2. **Edits between the last check and the moment of publishing.** Publication is manual, so the publisher should copy from the G2 packet's text, not from the live page. Even then, the gap is human discipline.
3. **A person editing a `human_only` field.** "Human-only" is this contract's convention. Notion does not enforce per-property write permissions for workspace editors. Whether page-level permissions on the current plan could narrow this is **not verified**.
4. **A person editing the fingerprint itself.** The publication check recomputes from content, so a forged fingerprint would still mismatch the content. But a person who edits both content and fingerprint consistently is not detectable by design.
5. **Formatting-only rich-text changes**, because of `plain_text` extraction, and **non-publication-affecting fields**, by design.
6. **History.** Notion page history is the only native audit trail. Its retention depends on the plan and is not verified here.

**Optional cheap signal (not part of the minimal set).** A `Last edited time` property plus a formula flag when it is later than `G2 Decided At`. It is page-level, so it also trips on benign edits. **Whether adding a comment, such as the routine's, changes `Last edited time` is not verified.** Test that before relying on it.

## 5. What else would change when applied

- **Gate:** read G1 from the four properties, not the page-body line. Add `content_fingerprint()` and R26. Snapshot keys change accordingly.
- **Routine v2 (a separate prompt amendment and approval):** it could then block a brief whose `G1 Decision ≠ Passed (design)` or whose `G1 Revision ≠ Version`, as a new BLOCKED reason. Until then, CHANGE_PROPOSAL step T2a is the human hold.
- **No approval-matrix row** is needed for the properties themselves (manual apply). The routine change would amend its existing row.

## 6. Apply steps (later; each needs approval)

1. Read-only fetch of DB7. Confirm 49 properties and the six trigger-read properties unchanged.
2. Add the six properties. Each Notion `COMMENT` must be 280 characters or fewer, or the DDL is rejected (observed 2026-10-09).
3. Read back. Record the `G1 Decision` option names and IDs in `content-databases.json`, and pin them in tests.
4. In the same change: update the contract JSON (55 fields, writers as §2), the gate (G1 from properties, fingerprint, R26), the tests and `CONTENT_INTELLIGENCE_SCHEMA.md` §10.
5. **No backfill.** No G1 has been given yet; the two existing briefs stay empty, meaning not reviewed.
6. **Rollback:** drop the six properties. Nothing depends on them while they are empty.

## 7. Owner choices this proposal needs

- **G1 Decision options.** Merge decision and path into one select (proposed), or keep two fields.
- **Reviewers.** Who may record G1 and G2. Only the owner, or named reviewers?
- **Last-edited signal.** Whether it is wanted, after verifying the comment behaviour.

## 8. Changelog

- **2026-10-09** — Prepared under the owner's hardening brief ("Prepare, but do not implement, the minimal G1/approved-asset storage and content-fingerprint proposal. Explain direct-Notion-edit limits."). — Claude Code (Opus 5.5)
