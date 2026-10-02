# -*- coding: utf-8 -*-
"""DB9-PROV-1 focused offline tests.

Covers the recorded DB 9 schema, the S10 fail-closed aggregation rules, and the validation rules
that keep an unsupported Confidence out of the store. Every test is OFFLINE: nothing here calls
Notion, and the aggregation functions below are REFERENCE IMPLEMENTATIONS of the rules written into
S10's Step 4 - they are what the rules mean, expressed executably, not a second source of truth.

    python -m unittest discover -s 01_Sector/contracts -p "test_db9_provenance.py"
"""
import io
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DBJSON = os.path.join(HERE, "sector-databases.json")
IOJSON = os.path.join(HERE, "intelligence-object.schema.json")
S10 = os.path.join(ROOT, ".claude", "skills", "sector-handoff-packet", "SKILL.md")
NSCHEMA = os.path.join(ROOT, "01_Sector", "SECTOR_NOTION_SCHEMA.md")

PROVENANCE = ["Confidence", "Source", "Source Tier", "Source URL", "Evidence", "Last Verified",
              "Next Review"]
CONF_OPTS = ["High", "Medium", "Low"]
TIER_OPTS = ["T1 Primary", "T2 Institutional", "T3 Commercial-intel", "T4 Secondary"]
ORDER = {"Low": 0, "Medium": 1, "High": 2}
UNRESOLVED = "UNRESOLVED"


def read(p):
    with io.open(p, encoding="utf-8") as fh:
        return fh.read()


def db9():
    for r in json.loads(read(DBJSON))["databases"]:
        if r["db_id"] == "DB9":
            return r
    raise AssertionError("DB9 not recorded")


# ---------------------------------------------------------------- reference implementations
def confidence_threshold(items):
    """S10 Step 4. A null Confidence is UNASSESSED and DOMINATES: null is weaker than Low."""
    if any(i.get("Confidence") is None for i in items):
        return UNRESOLVED, [i["id"] for i in items if i.get("Confidence") is None]
    return min((i["Confidence"] for i in items), key=lambda c: ORDER[c]), []


def freshness_requirement(items, assembly_date=None):
    """S10 Step 4. Absent dates stay UNRESOLVED; the assembly date may never substitute."""
    missing = [i["id"] for i in items if i.get("Last Verified") is None]
    if missing:
        return {"state": UNRESOLVED, "offending": missing}, missing
    reviews = [i["Next Review"] for i in items if i.get("Next Review") is not None]
    return {"state": "RESOLVED",
            "oldest_last_verified": min(i["Last Verified"] for i in items),
            "earliest_next_review": min(reviews) if reviews else None}, []


def validate_row(row):
    """Validation rules V1-V7 as recorded in the contract's field-level validation text."""
    errs = []
    c = row.get("Confidence")
    if c is not None:
        if c not in CONF_OPTS:
            errs.append("V1 Confidence not in the option set")
        if not row.get("Source"):
            errs.append("V3 Confidence without Source")
        if not row.get("Evidence"):
            errs.append("V3 Confidence without Evidence")
    if row.get("Source") and not row.get("Source Tier"):
        errs.append("V4 Source without Source Tier")
    if row.get("Source Tier") and row["Source Tier"] not in TIER_OPTS:
        errs.append("V2 Source Tier not in the option set")
    lv, nr = row.get("Last Verified"), row.get("Next Review")
    if lv and not nr:
        errs.append("V6 Last Verified without Next Review")
    if nr and not lv:
        errs.append("V7 Next Review without Last Verified")
    if lv and nr and nr <= lv:
        errs.append("V6 Next Review must be strictly later than Last Verified")
    return errs


class RecordedSchema(unittest.TestCase):
    def test_db9_records_twenty_one_fields(self):
        names = [f["name"] for f in db9()["fields"]]
        self.assertEqual(len(names), 21, "the audited live schema has 21 properties")
        self.assertEqual(db9()["field_count_verified"], 21)

    def test_no_duplicate_field_and_evidence_appears_once(self):
        names = [f["name"] for f in db9()["fields"]]
        self.assertEqual(len(names), len(set(names)), "no duplicate field name")
        self.assertEqual(names.count("Evidence"), 1, "Evidence recorded exactly once")

    def test_every_provenance_field_is_recorded_nullable_with_its_established_type(self):
        by = {f["name"]: f for f in db9()["fields"]}
        expect = {"Confidence": "select", "Source": "text", "Source Tier": "select",
                  "Source URL": "url", "Evidence": "text", "Last Verified": "date",
                  "Next Review": "date"}
        for name, ntype in expect.items():
            self.assertIn(name, by, name)
            self.assertEqual(by[name]["notion_type"], ntype, name)
            self.assertIs(by[name]["required"], False, "%s must be nullable" % name)

    def test_option_sets_match_the_established_vocabularies(self):
        by = {f["name"]: f for f in db9()["fields"]}
        self.assertEqual(by["Confidence"]["allowed_values"], CONF_OPTS)
        self.assertEqual(by["Source Tier"]["allowed_values"], TIER_OPTS)

    def test_the_live_field_name_is_next_review_not_next_verification(self):
        names = [f["name"] for f in db9()["fields"]]
        self.assertIn("Next Review", names)
        self.assertNotIn("Next Verification", names,
                         "DB7/DB14 use Next Verification; DB9's live name is Next Review")

    def test_the_superseded_false_claim_is_marked_corrected(self):
        mf = db9()["MISSING_FIELD"]
        self.assertIn("FACTUALLY WRONG", mf["note"])
        self.assertIn("Evidence", mf["note"])

    def test_row_level_provenance_is_recorded_unresolved_and_unbackfilled(self):
        rl = db9()["MISSING_FIELD"]["row_level_status"]
        self.assertEqual(rl["non_null_cells"], 0)
        self.assertIs(rl["backfill_authorised"], False)
        self.assertEqual(rl["rows"], 4)

    def test_intelligence_object_maps_db9_for_q2_q3_q4(self):
        props = json.loads(read(IOJSON))["properties"]
        for q in ("source", "when_observed", "reliability"):
            nf = props[q]["notion_field"]
            self.assertIn("DB9", nf, q)
            self.assertIn("DB3", nf, "%s keeps DB3" % q)
            self.assertIn("DB7", nf, "%s keeps DB7" % q)
        self.assertNotIn("Next Verification", props["when_observed"]["notion_field"]["DB9"])

    def test_the_human_readable_schema_doc_agrees(self):
        seg = read(NSCHEMA).split("### DB 9 — Audience Roles", 1)[1].split("### DB 10", 1)[0]
        for name in PROVENANCE:
            self.assertIn(name, seg, name)
        self.assertIn("21 properties", seg)
        self.assertIn("UNRESOLVED", seg)


class ConfidenceAggregation(unittest.TestCase):
    def test_a_single_null_confidence_makes_the_threshold_unresolved(self):
        items = [{"id": "finding", "Confidence": "Medium"},
                 {"id": "signal", "Confidence": "High"},
                 {"id": "audience", "Confidence": None}]
        value, offenders = confidence_threshold(items)
        self.assertEqual(value, UNRESOLVED)
        self.assertEqual(offenders, ["audience"])

    def test_null_is_not_read_as_low(self):
        items = [{"id": "a", "Confidence": "Low"}, {"id": "b", "Confidence": None}]
        self.assertEqual(confidence_threshold(items)[0], UNRESOLVED,
                         "null must dominate, not collapse to the Low that is already present")

    def test_assessed_values_aggregate_to_the_weakest(self):
        self.assertEqual(confidence_threshold(
            [{"id": "a", "Confidence": "High"}, {"id": "b", "Confidence": "Medium"},
             {"id": "c", "Confidence": "High"}])[0], "Medium")
        self.assertEqual(confidence_threshold(
            [{"id": "a", "Confidence": "High"}, {"id": "b", "Confidence": "Low"}])[0], "Low")
        self.assertEqual(confidence_threshold(
            [{"id": "a", "Confidence": "High"}, {"id": "b", "Confidence": "High"}])[0], "High")

    def test_every_offending_element_is_named(self):
        items = [{"id": "audience", "Confidence": None}, {"id": "language", "Confidence": None},
                 {"id": "finding", "Confidence": "Medium"}]
        self.assertEqual(sorted(confidence_threshold(items)[1]), ["audience", "language"])

    def test_the_accommodation_case_as_it_stands_today(self):
        """All four DB9 rows are null, so a real Accommodation packet resolves to UNRESOLVED."""
        items = [{"id": "finding", "Confidence": "Medium"},
                 {"id": "signal", "Confidence": "Medium"},
                 {"id": "language", "Confidence": "Medium"},
                 {"id": "audience", "Confidence": None}]
        self.assertEqual(confidence_threshold(items)[0], UNRESOLVED,
                         "must not fall back to the Medium the other elements would have set")


class FreshnessAggregation(unittest.TestCase):
    def test_all_dates_absent_is_unresolved(self):
        items = [{"id": "a", "Last Verified": None, "Next Review": None},
                 {"id": "b", "Last Verified": None, "Next Review": None}]
        res, offenders = freshness_requirement(items)
        self.assertEqual(res["state"], UNRESOLVED)
        self.assertEqual(sorted(offenders), ["a", "b"])

    def test_one_absent_date_fails_closed_for_the_whole_packet(self):
        items = [{"id": "a", "Last Verified": "2026-08-01", "Next Review": "2026-11-01"},
                 {"id": "audience", "Last Verified": None, "Next Review": None}]
        self.assertEqual(freshness_requirement(items)[0]["state"], UNRESOLVED)

    def test_earliest_next_review_is_selected(self):
        items = [{"id": "a", "Last Verified": "2026-08-01", "Next Review": "2026-12-01"},
                 {"id": "b", "Last Verified": "2026-09-01", "Next Review": "2026-10-15"},
                 {"id": "c", "Last Verified": "2026-07-01", "Next Review": "2027-01-01"}]
        self.assertEqual(freshness_requirement(items)[0]["earliest_next_review"], "2026-10-15")

    def test_oldest_last_verified_is_reported_alongside(self):
        items = [{"id": "a", "Last Verified": "2026-08-01", "Next Review": "2026-12-01"},
                 {"id": "b", "Last Verified": "2026-09-01", "Next Review": "2026-10-15"},
                 {"id": "c", "Last Verified": "2026-07-01", "Next Review": "2027-01-01"}]
        self.assertEqual(freshness_requirement(items)[0]["oldest_last_verified"], "2026-07-01")

    def test_no_assembly_date_substitutes_for_a_missing_last_verified(self):
        items = [{"id": "audience", "Last Verified": None, "Next Review": None}]
        res, _ = freshness_requirement(items, assembly_date="2026-10-02")
        self.assertEqual(res["state"], UNRESOLVED)
        self.assertNotIn("2026-10-02", json.dumps(res),
                         "the assembly date must not leak into the result")

    def test_mixed_null_and_non_null_provenance_fails_closed(self):
        items = [{"id": "a", "Confidence": "High", "Last Verified": "2026-08-01",
                  "Next Review": "2026-11-01"},
                 {"id": "b", "Confidence": None, "Last Verified": None, "Next Review": None}]
        self.assertEqual(confidence_threshold(items)[0], UNRESOLVED)
        self.assertEqual(freshness_requirement(items)[0]["state"], UNRESOLVED)


class ValidationRules(unittest.TestCase):
    def test_confidence_without_source_is_rejected(self):
        errs = validate_row({"Confidence": "Medium", "Source": None, "Evidence": "something"})
        self.assertTrue(any("V3" in e and "Source" in e for e in errs))

    def test_confidence_without_evidence_is_rejected(self):
        errs = validate_row({"Confidence": "Medium", "Source": "A named authority",
                             "Source Tier": "T2 Institutional", "Evidence": None})
        self.assertTrue(any("V3" in e and "Evidence" in e for e in errs))

    def test_a_fully_supported_confidence_passes(self):
        self.assertEqual(validate_row({
            "Confidence": "Medium", "Source": "A named authority",
            "Source Tier": "T2 Institutional", "Evidence": "the specific passage",
            "Last Verified": "2026-08-19", "Next Review": "2026-11-19"}), [])

    def test_source_without_tier_is_rejected(self):
        self.assertTrue(any("V4" in e for e in validate_row({"Source": "A named authority"})))

    def test_a_date_pair_must_be_complete_and_ordered(self):
        self.assertTrue(any("V6" in e for e in validate_row({"Last Verified": "2026-08-19"})))
        self.assertTrue(any("V7" in e for e in validate_row({"Next Review": "2026-11-19"})))
        self.assertTrue(any("V6" in e for e in validate_row(
            {"Last Verified": "2026-08-19", "Next Review": "2026-08-19"})))

    def test_an_all_null_row_is_valid(self):
        """The four live rows are all-null today; that must not be a validation error."""
        self.assertEqual(validate_row({k: None for k in PROVENANCE}), [])


class S10Contract(unittest.TestCase):
    def test_s10_states_every_fail_closed_rule(self):
        s = read(S10)
        for needle in ["Low < Medium < High", "null is weaker than", "UNRESOLVED",
                       "Next Review", "assembly date", "naming each such element"]:
            self.assertIn(needle, s, needle)

    def test_s10_forbids_falling_back_to_the_other_elements_floor(self):
        self.assertIn("Do not fall back", read(S10))

    def test_s10_does_not_use_the_wrong_field_name(self):
        seg = read(S10).split("### The two floors are computed", 1)[1]
        self.assertNotIn("Next Verification", seg.split("> **The live field name")[0])


class OrdinaryBehaviourUnchanged(unittest.TestCase):
    def test_db9_keeps_its_original_fourteen_recorded_fields(self):
        names = [f["name"] for f in db9()["fields"]]
        for original in ["Audience Profile", "Sub-Sector", "Role", "Wants", "Fears", "Beliefs",
                         "Rejects", "Access Paths", "Content Persona", "Primary Signal Type",
                         "CRM Lead/Person", "Content Opportunities",
                         "Destination Profiles (Primary)", "Destination Profiles (Secondary)"]:
            self.assertIn(original, names, original)

    def test_the_substantive_vocabularies_are_untouched(self):
        by = {f["name"]: f for f in db9()["fields"]}
        self.assertEqual(by["Role"]["allowed_values"],
                         ["Operator", "Buyer", "Amplifier", "Enabler"])
        self.assertEqual(by["Primary Signal Type"]["allowed_values"],
                         ["Authority", "Market", "Conversion"])

    def test_all_three_databases_now_carry_evidence_each_by_its_own_authorisation(self):
        # Rewritten twice, both times by a real change rather than a correction:
        #   Step 1 removed an assertion that PINNED A FALSE CLAIM (DB6/DB10 severity
        #     "flagged, not fixed", which DB6-DB10-PROV-AUDIT-1 disproved).
        #   Step 2 then added Evidence to DB6 and DB10 under its own owner approval, so the
        #     "DB9 only" invariant retired honestly instead of being asserted into the ground.
        # What remains durable: each database's Evidence is attributed to the task that added it,
        # and DB9's row-level status is untouched by either DB6/DB10 task.
        rows = {r["db_id"]: r for r in json.loads(read(DBJSON))["databases"]}
        for db_id in ("DB6", "DB9", "DB10"):
            by = {f["name"]: f for f in rows[db_id]["fields"]}
            self.assertIn("Evidence", by, "%s carries Evidence" % db_id)
            self.assertEqual(by["Evidence"]["notion_type"], "text")
        self.assertIn("DB9-PROV-1", by9_evidence_source(rows),
                      "DB9's Evidence stays attributed to DB9-PROV-1")
        for other in ("DB6", "DB10"):
            by = {f["name"]: f for f in rows[other]["fields"]}
            self.assertIn("DB6-DB10-PROV-1 Step 2", by["Evidence"]["provenance_of_record"],
                          "%s's Evidence is attributed to Step 2" % other)
            mf = rows[other]["MISSING_FIELD"]
            self.assertIn("superseded_claim", mf,
                          "%s must preserve the claim it supersedes" % other)
            self.assertNotIn("flagged, not fixed", mf["severity"],
                             "%s's severity must not repeat the superseded framing" % other)
        self.assertEqual(
            rows["DB9"]["MISSING_FIELD"]["row_level_status"]["non_null_cells"], 0,
            "DB9's row-level status must be untouched by the DB6/DB10 work")

    def test_other_databases_keep_their_own_provenance_shape(self):
        rows = {r["db_id"]: r for r in json.loads(read(DBJSON))["databases"]}
        db7 = {f["name"] for f in rows["DB7"]["fields"]}
        self.assertIn("Next Verification", db7, "DB7 keeps its own naming")
        db16 = {f["name"] for f in rows["DB16"]["fields"]}
        self.assertIn("Next Review", db16, "DB16 keeps its own naming")


# --------------------------------------------------------------------------------------------
# DB6-DB10-PROV-1 Step 1 (2026-10-02) - repository synchronisation to DB6-DB10-PROV-AUDIT-1.
# Offline and deterministic. These tests check what the REPOSITORY RECORDS. They cannot and do
# not check the live Notion schema; live drift needs another separately authorised audit.
# --------------------------------------------------------------------------------------------

AUDIT_ID = "DB6-DB10-PROV-AUDIT-1"
# The SEVEN provenance properties now live in BOTH DB6 and DB10. Six were added 2026-09-13 by
# owner item 31e; `Evidence` was added 2026-10-02 by DB6-DB10-PROV-1 Step 2 and is the only field
# that task created. Attribution is kept distinct on purpose - see ADDED_BY_31E below.
OBSERVED_SEVEN = ["Confidence", "Source", "Source Tier", "Source URL", "Last Verified",
                  "Next Review", "Evidence"]
ADDED_BY_31E = ["Source", "Source Tier", "Source URL", "Last Verified", "Next Review"]
ADDED_BY_STEP2 = "Evidence"
EXPECTED_COUNT = {"DB6": 19, "DB10": 16}
# DB6 went 4 -> 17 populated on 2026-10-02 when DB6-OD1-OD2-1 wrote 13 cells.
EXPECTED_CELLS = {"DB6": (4, 28, 17), "DB10": (57, 399, 0)}  # rows, cells, non_null
OD1 = "DB6-OD1-OD2-1"
BACKFILL_CELLS = 13
EXCEPTION_EXPIRY = "2026-11-24"
STEP2 = "DB6-DB10-PROV-1 Step 2"


def by9_evidence_source(rows):
    """DB9's Evidence provenance string, for the attribution check above."""
    for f in rows["DB9"]["fields"]:
        if f["name"] == "Evidence":
            return f.get("provenance_of_record", "")
    return ""


def dbrow(db_id):
    for r in json.loads(read(DBJSON))["databases"]:
        if r["db_id"] == db_id:
            return r
    raise AssertionError("no %s entry" % db_id)


def flat(text):
    """Whitespace-normalised copy. The markdown is hard-wrapped, so a phrase can span a newline."""
    return re.sub(r"\s+", " ", text)


class DB6DB10RecordedSchema(unittest.TestCase):

    def test_recorded_field_counts_match_the_audit(self):
        for db_id, n in EXPECTED_COUNT.items():
            row = dbrow(db_id)
            self.assertEqual(len(row["fields"]), n,
                             "%s must record %d fields" % (db_id, n))
            self.assertEqual(row.get("field_count_verified"), n,
                             "%s field_count_verified must be %d" % (db_id, n))

    def test_no_duplicate_field_names(self):
        for db_id in EXPECTED_COUNT:
            names = [f["name"] for f in dbrow(db_id)["fields"]]
            dupes = sorted({n for n in names if names.count(n) > 1})
            self.assertEqual(dupes, [], "%s has duplicate field names: %s" % (db_id, dupes))

    def test_the_seven_observed_provenance_fields_are_recorded(self):
        for db_id in EXPECTED_COUNT:
            names = [f["name"] for f in dbrow(db_id)["fields"]]
            for p in OBSERVED_SEVEN:
                self.assertIn(p, names, "%s must record provenance field %r" % (db_id, p))
            self.assertEqual(len(OBSERVED_SEVEN), 7)

    def test_provenance_field_types_match_the_audit(self):
        want = {"Confidence": "select", "Source": "text", "Source Tier": "select",
                "Source URL": "url", "Last Verified": "date", "Next Review": "date",
                "Evidence": "text"}
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            for p, t in want.items():
                self.assertEqual(by[p].get("notion_type"), t,
                                 "%s %s must be %s" % (db_id, p, t))

    def test_the_fields_31e_added_are_recorded_nullable(self):
        # Scoped deliberately to the fields owner item 31e added. DB6's `Confidence` is EXCLUDED:
        # it predates 31e and carries `required: true`, a pre-existing authoring rule that says
        # S02 must always set it. This synchronisation does not weaken that rule - and the tension
        # between "always set it" and "no rule that it be supported" is part of open decision OD1.
        added = ADDED_BY_31E + [ADDED_BY_STEP2]
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            names = added + (["Confidence"] if db_id == "DB10" else [])
            for p in names:
                self.assertFalse(by[p].get("required", False),
                                 "%s %s must be recorded nullable" % (db_id, p))
        self.assertIs(
            {f["name"]: f for f in dbrow("DB6")["fields"]}["Confidence"].get("required"), True,
            "DB6's pre-existing required Confidence rule must NOT be weakened by this task")

    def test_source_tier_reuses_the_existing_four_value_enum(self):
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            self.assertEqual(by["Source Tier"]["allowed_values"], TIER_OPTS,
                             "%s Source Tier must reuse the DB7/DB9/DB14/DB16 enum" % db_id)

    def test_confidence_options_are_the_three_canonical_values(self):
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            self.assertEqual(sorted(by["Confidence"]["allowed_values"]), sorted(CONF_OPTS),
                             "%s Confidence must carry exactly Low/Medium/High" % db_id)

    def test_evidence_is_recorded_present_nullable_text_and_null_on_all_rows(self):
        # INVERTED 2026-10-02 by Step 2. This test previously asserted Evidence was ABSENT. It is
        # now live in both databases, so the invariant flips - but the ROW VALUES must still be
        # recorded null, because adding a column is not adding evidence.
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            self.assertIn("Evidence", by, "%s must record Evidence" % db_id)
            ev = by["Evidence"]
            self.assertEqual(ev["notion_type"], "text", "%s Evidence is text" % db_id)
            self.assertFalse(ev.get("required", False), "%s Evidence nullable" % db_id)
            self.assertIn("NULL", ev["row_values"],
                          "%s Evidence row values must be recorded NULL" % db_id)
            self.assertIn(STEP2, ev["provenance_of_record"],
                          "%s Evidence must be attributed to Step 2, not to 31e" % db_id)
            rl = dbrow(db_id)["MISSING_FIELD"]["row_level_status"]
            self.assertIn("NULL", rl["evidence_row_values"])

    def test_attribution_of_the_six_versus_the_one_stays_distinct(self):
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            for p in ADDED_BY_31E:
                self.assertIn("31e", by[p]["schema_history"],
                              "%s %s was added by owner item 31e" % (db_id, p))
            hist = by["Evidence"]["schema_history"]
            self.assertIn("ONLY field this task added", hist)
            self.assertIn("NOT by this task", hist,
                          "Evidence must not absorb credit for the 31e additions")

    def test_next_review_not_next_verification(self):
        for db_id in EXPECTED_COUNT:
            names = [f["name"] for f in dbrow(db_id)["fields"]]
            self.assertIn("Next Review", names)
            self.assertNotIn("Next Verification", names,
                             "%s uses Next Review; Next Verification is DB7/DB14's name" % db_id)

    def test_snapshot_is_attributed_to_the_audit(self):
        for db_id in EXPECTED_COUNT:
            row = dbrow(db_id)
            self.assertIn(AUDIT_ID, row.get("field_count_note", ""),
                          "%s must attribute its count to %s" % (db_id, AUDIT_ID))
            by = {f["name"]: f for f in row["fields"]}
            for p in OBSERVED_SEVEN:
                if p == "Confidence" and db_id == "DB6":
                    continue  # DB6 always had Confidence; 31e did not add it
                src = by[p].get("provenance_of_record", "")
                want = STEP2 if p == ADDED_BY_STEP2 else AUDIT_ID
                self.assertIn(want, src,
                              "%s %s must name its source (%s)" % (db_id, p, want))

    def test_live_drift_is_declared_undetectable(self):
        for db_id in EXPECTED_COUNT:
            row = dbrow(db_id)
            blob = flat(json.dumps(row))
            self.assertTrue(re.search(r"(?i)drift", blob),
                            "%s must warn that live drift is not detected offline" % db_id)


class DB6DB10SupersededClaims(unittest.TestCase):

    def test_both_notes_preserve_the_claim_they_supersede(self):
        for db_id in EXPECTED_COUNT:
            mf = dbrow(db_id)["MISSING_FIELD"]
            self.assertIn("superseded_claim", mf, "%s must preserve prior history" % db_id)
            sc = mf["superseded_claim"]
            self.assertTrue(sc["text"].strip(), "%s superseded text must not be blank" % db_id)
            self.assertIn("SUPERSED", mf["note"],
                          "%s note must say it supersedes/supersedED, not silently replace"
                          % db_id)

    def test_the_superseded_claims_are_the_real_prior_strings(self):
        # Guards against a future edit quietly softening what was actually claimed.
        self.assertIn("NO Source",
                      dbrow("DB6")["MISSING_FIELD"]["superseded_claim"]["text"],
                      "DB6's prior claim denied Source")
        self.assertIn("No Confidence",
                      dbrow("DB10")["MISSING_FIELD"]["superseded_claim"]["text"],
                      "DB10's prior claim denied Confidence")

    def test_each_note_dates_when_the_claim_stopped_being_true(self):
        for db_id in EXPECTED_COUNT:
            sc = dbrow(db_id)["MISSING_FIELD"]["superseded_claim"]
            self.assertIn("2026-09-13", sc["became_false_on"],
                          "%s must date the change to owner item 31e" % db_id)
            self.assertIn("31e", sc["became_false_on"], "%s must name item 31e" % db_id)
            self.assertIn("2026-08-24", sc["was_true_when_written"],
                          "%s must record the claim WAS true when written" % db_id)

    def test_f14_records_the_propagation_failure(self):
        f14 = next(e for e in json.loads(read(DBJSON))["_divergences"] if e["id"] == "F14")
        self.assertIn("resolution_update_2026_09_13", f14,
                      "the original 31e closure must be preserved")
        self.assertIn("resolution_update_2026_10_02", f14,
                      "F14 must record that the closure was never propagated")

    def test_schema_completeness_is_never_stated_as_row_completeness(self):
        # REPLACES Step 1's "not provenance-complete" phrase check. Step 2 CLOSED the schema gap,
        # so a blanket "not complete" claim would now be wrong. The invariant that actually
        # matters is the DISTINCTION: schema complete, rows not - stated, never blurred.
        for db_id in EXPECTED_COUNT:
            mf = dbrow(db_id)["MISSING_FIELD"]
            blob = flat(json.dumps(dbrow(db_id)))
            self.assertIn("SCHEMA GAP", mf["status"] + mf["note"],
                          "%s must name the schema gap as the thing that closed" % db_id)
            self.assertIn("ROW-LEVEL PROVENANCE", mf["status"] + mf["note"],
                          "%s must name row-level provenance separately" % db_id)
            # DB6's wording changed when DB6-OD1-OD2-1 resolved three of its four rows. The
            # invariant is that row-level status is stated and never claimed complete - not that
            # it uses one fixed phrase.
            self.assertTrue(
                re.search(r"(?i)row-level provenance (is not|still incomplete"
                          r"|substantially resolved)", blob),
                "%s must state its row-level provenance state explicitly" % db_id)
            self.assertTrue(re.search(r"(?i)field existence|column exists", blob),
                            "%s must warn that field existence is not evidence" % db_id)
            self.assertTrue(
                "incomplete" in mf["severity"] or "exception" in mf["severity"],
                "%s severity must record incompleteness or the named exception" % db_id)


class DB6DB10RowLevelStatus(unittest.TestCase):

    def test_row_level_counts_reflect_seven_fields(self):
        for db_id, want in EXPECTED_CELLS.items():
            st = dbrow(db_id)["MISSING_FIELD"]["row_level_status"]
            self.assertEqual((st["rows"], st["cells"], st["non_null_cells"]), want,
                             "%s row-level counts" % db_id)
            self.assertEqual(st["provenance_fields_live"], 7,
                             "%s now has seven provenance fields" % db_id)
            self.assertEqual(st["rows"] * 7, st["cells"],
                             "%s cells must equal rows x 7" % db_id)
            self.assertIs(st["backfill_authorised"], False)

    def test_db10_records_that_no_skill_run_ever_wrote_it(self):
        st = dbrow("DB10")["MISSING_FIELD"]["row_level_status"]
        self.assertIn("NO_OP", st["no_skill_run_provenance"],
                      "DB10 must record the S02 NO_OP, so its evidence_refs are not attachable")

    def test_db10_unaudited_rows_are_not_characterised(self):
        cov = dbrow("DB10")["MISSING_FIELD"]["row_level_status"]["audit_coverage"]
        self.assertEqual(cov["rows_body_read"], 4)
        self.assertEqual(cov["rows_not_body_read"], 53)
        self.assertEqual(cov["rows_body_read"] + cov["rows_not_body_read"], 57)
        self.assertIn("UNRESOLVED", cov["bodies"],
                      "the 53 unread rows must be UNRESOLVED, not verified-absent")
        self.assertIn("not", flat(cov["bodies"]).lower(),
                      "the 53 must be explicitly NOT characterised")


class DB6UnsupportedConfidenceStaysOpen(unittest.TestCase):

    def test_the_conflict_is_recorded_on_the_confidence_field(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        note = by["Confidence"].get("open_decision_2026_10_02", "")
        self.assertTrue(note, "DB6's Confidence must carry the OD1 record")
        self.assertIn("OD1", note)
        # Updated 2026-10-02: OD1 is now CLOSED with one named exception. V3 must still be
        # recorded as NOT enforced, and the four values must still be recorded as not cleared.
        for must in ("V3", "NOT extended", "required: true", "not cleared"):
            self.assertIn(must, note, "DB6 Confidence note must state %r" % must)
        self.assertIn("CLOSED", note, "OD1 is closed with an exception, not still open")

    def test_rule_v3_is_not_extended_to_db6(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        self.assertNotIn("validation", by["Confidence"],
                         "adding a V3-style validation to DB6 would legislate the open decision")

    def test_the_four_values_are_not_cleared_or_downgraded(self):
        st = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]
        self.assertIn("Medium", st["non_null_detail"],
                      "the four Medium values must still be recorded as populated")
        self.assertIn("UNCHANGED", st["non_null_detail"],
                      "and recorded as never rewritten by the backfill")
        self.assertEqual(st["non_null_cells"], 17,
                         "4 Confidence + 13 backfilled = 17 populated")


class StepOneOpenDecisions(unittest.TestCase):

    def test_od1_od2_od3_closed_and_od4_od5_od6_open(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k in ("OD1", "OD2", "OD3", "OD4", "OD5", "OD6"):
            self.assertIn(k, od, "%s must be recorded" % k)
        self.assertIn("CLOSED", od["OD3"]["status"], "OD3 closed by Step 2")
        self.assertIn(STEP2, od["OD3"]["closed_by"])
        self.assertIn("CLOSED", od["OD1"]["status"], "OD1 closed by DB6-OD1-OD2-1")
        self.assertIn("EXCEPTION", od["OD1"]["status"].upper(), "with a named exception")
        self.assertIn("CLOSED", od["OD2"]["status"], "OD2 closed locally")
        # Every closure must say what it did NOT close. OD1 and OD3 use
        # `what_it_did_not_close`; OD2 uses `scope_warning` because its limit is one of scope.
        for k in ("OD1", "OD3"):
            self.assertIn("what_it_did_not_close", od[k],
                          "%s must state what closing it did NOT close" % k)
        self.assertIn("scope_warning", od["OD2"],
                      "OD2 must state the boundary of its local closure")
        for k in ("OD4", "OD5", "OD6"):
            self.assertIn("OPEN", od[k]["status"], "%s must remain OPEN" % k)
            self.assertNotIn("CLOSED", od[k]["status"], "%s must not be closed" % k)
        self.assertIn("NOT RESOLVED", od["_note"])

    def test_the_multi_source_convention_is_local_to_db6_only(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD2"]
        self.assertIn("CLOSED LOCALLY FOR DB6 ONLY", od["status"])
        self.assertIn("NOT A SECTOR-WIDE RATIFICATION", od["status"])
        self.assertIn("V4", od["scope_warning"], "must warn that DB9's V4 is unchanged")
        d6 = {f["name"]: f for f in dbrow("DB6")["fields"]}
        for p in ("Source Tier", "Source URL"):
            self.assertIn("LOCAL TO DB6", d6[p]["row_values"],
                          "DB6 %s must record the convention as local" % p)
            self.assertIn("MUST NOT be applied to DB9", d6[p]["row_values"])
        # DB10 must NOT have acquired the convention
        d10 = {f["name"]: f for f in dbrow("DB10")["fields"]}
        self.assertNotIn("LOCAL TO DB6", d10["Source Tier"].get("row_values", ""),
                         "DB10 must not have inherited DB6's local convention")

    def test_no_repository_wide_standard_is_ratified(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD4"]
        self.assertIn("NOT ratified", od["status"])
        self.assertIn("BY OBSERVATION", od["status"])

    def test_closing_od3_did_not_ratify_a_standard(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        self.assertIn("NOT ratified", od["OD4"]["status"],
                      "the shared seven-field shape is OBSERVED, not ratified")
        self.assertTrue(any("OBSERVED convergence" in f for f in od["OD4"]["facts"]),
                        "OD4 must record the convergence as observed")
        self.assertTrue(any("Next Verification" in f for f in od["OD4"]["facts"]),
                        "OD4 must still note DB7/DB14 diverge on the date-field name")


class DB6DB10IntelligenceMapping(unittest.TestCase):

    def test_db6_and_db10_are_mapped_under_q2_q3_q4(self):
        props = json.loads(read(IOJSON))["properties"]
        for q in ("source", "when_observed", "reliability"):
            nf = props[q]["notion_field"]
            for db_id in ("DB6", "DB9", "DB10"):
                self.assertIn(db_id, nf, "%s must map %s" % (q, db_id))

    def test_q2_omits_evidence_for_db6_and_db10_but_keeps_it_for_db9(self):
        nf = json.loads(read(IOJSON))["properties"]["source"]["notion_field"]
        self.assertIn("Evidence", nf["DB9"], "DB9 has Evidence live")
        for db_id in ("DB6", "DB10"):
            self.assertNotIn("Evidence", nf[db_id],
                             "%s has no Evidence field - mapping it would be invention" % db_id)

    def test_q3_maps_next_review_for_both(self):
        nf = json.loads(read(IOJSON))["properties"]["when_observed"]["notion_field"]
        for db_id in ("DB6", "DB10"):
            self.assertIn("Next Review", nf[db_id])
            self.assertNotIn("Next Verification", nf[db_id])

    def test_pre_existing_mappings_are_preserved(self):
        props = json.loads(read(IOJSON))["properties"]
        self.assertEqual(props["source"]["notion_field"]["DB3"], "Evidence + Source")
        self.assertEqual(props["when_observed"]["notion_field"]["DB7"],
                         "Last Verified + Next Verification")
        self.assertEqual(props["reliability"]["notion_field"]["DB7"], "Confidence")


class S10StepFourNamesEveryCause(unittest.TestCase):

    def setUp(self):
        self.txt = flat(read(S10))

    def test_all_four_contributing_databases_are_named(self):
        # DB3 added 2026-10-02 by DB3-PROV-1 Step A. The table had named three of four while
        # Step 4's own prose named findings as a confidence contributor.
        for db_id in ("DB 3", "DB 6", "DB 9", "DB 10"):
            self.assertIn(db_id, self.txt, "Step 4 must name %s as a contributing element" % db_id)
        self.assertIn("four contributing elements", self.txt,
                      "the count must say four, not three")
        self.assertIn("DB 3 added as the fourth element", self.txt)

    def test_db6_populated_confidence_is_described_as_unsupported(self):
        self.assertIn("populated `Confidence` with an EMPTY `Source`", self.txt)
        self.assertIn("OD1", self.txt)

    def test_db10_is_described_as_empty(self):
        self.assertTrue(re.search(r"DB 10.{0,120}null on all 57", self.txt),
                        "Step 4 must state DB10's provenance is empty")

    def test_evidence_state_is_stated_for_all_three(self):
        # Updated 2026-10-02: Evidence is no longer null everywhere - DB6-OD1-OD2-1 populated it
        # on three DB6 rows. The rule about nulls is unchanged and must survive verbatim.
        self.assertIn("`Evidence` exists structurally in DB 6, DB 9 and DB 10", self.txt)
        self.assertIn("populated on three DB 6 rows and null everywhere else", self.txt)
        self.assertIn("null `Evidence` continues to force an UNRESOLVED provenance floor",
                      self.txt)
        self.assertIn("No confidence or freshness value may be inferred from the fact that a "
                      "field exists", self.txt)
        self.assertIn("A column is a place to put evidence, not evidence", self.txt)

    def test_the_local_multi_source_convention_is_stated_and_scoped(self):
        # OD2 closed LOCALLY 2026-10-02. S10 must describe the convention AND its boundary, so a
        # packet never reads DB6's null tier as a gap or applies the convention to DB9.
        self.assertIn("OD2 closed LOCALLY FOR DB 6 ONLY", self.txt)
        self.assertIn("not representable in a single-valued field", self.txt)
        self.assertIn("NOT ratified for DB 9, DB 10 or Sector-wide", self.txt)
        self.assertIn("do not read DB 6's null tier as a missing value to be filled", self.txt)
        self.assertIn("OD4", self.txt)

    def test_rule_v3_is_not_enforced_on_db6_in_the_skill(self):
        self.assertIn("Rule V3 is a DOCUMENTED EXPECTATION for DB 6, not an enforced validator",
                      self.txt)
        self.assertIn("A sourced row and an excepted row must never be reported the same way",
                      self.txt)

    def test_null_and_unsupported_both_fail_closed(self):
        self.assertIn("Null and unsupported both fail closed", self.txt)
        self.assertIn("weaker than `Low`", self.txt)

    def test_no_assembly_date_may_substitute(self):
        self.assertTrue(re.search(r"(?i)no assembly date may ever substitute", self.txt),
                        "the assembly-date prohibition must be restated in the corrected reason")

    def test_the_values_are_not_to_be_cleared(self):
        self.assertIn("not** to be cleared or downgraded", self.txt)


class SchemaMarkdownSynchronised(unittest.TestCase):

    def setUp(self):
        self.txt = flat(read(NSCHEMA))

    def test_both_counts_are_stated(self):
        self.assertIn("19 properties, verified live 2026-10-02", self.txt)
        self.assertIn("16 properties, verified live 2026-10-02", self.txt)

    def test_the_phantom_db6_field_is_marked_absent(self):
        self.assertIn("`Decision-language patterns` does NOT exist in the live schema", self.txt)

    def test_the_stale_52_row_claim_is_superseded_not_rewritten(self):
        self.assertIn("all **52** (buyer titles", self.txt,
                      "the dated 2026-08-11 line stays as written")
        self.assertIn("DB 10 now holds 57 rows", self.txt, "and is superseded by a dated note")

    def test_the_stale_still_to_load_claim_is_superseded(self):
        self.assertIn("Still to load", self.txt, "the dated line stays")
        self.assertIn("no longer true for the one Target sub-sector", self.txt)

    def test_the_db6_misnumbering_is_corrected(self):
        self.assertNotIn("DB 11 Sector Linguistics", self.txt,
                         "Sector Linguistics is DB 6; DB 11 is Geography")
        self.assertIn("DB 6 Sector Linguistics", self.txt)

    def test_evidence_presence_and_nullity_recorded_for_both(self):
        self.assertIn("`Evidence` now EXISTS in DB 6", self.txt)
        self.assertIn("`Evidence` now EXISTS in DB 10", self.txt)
        self.assertIn("null on all 4 rows", self.txt)
        self.assertIn("null on all 57 rows", self.txt)
        warn = len(re.findall(r"(?i)column existing is not evidence", self.txt))
        self.assertEqual(warn, 2,
                         "both sections must warn against inferring from field existence, "
                         "found %d" % warn)
        self.assertEqual(
            len(re.findall(r"(?i)no confidence or freshness value may be inferred", self.txt)), 2,
            "and both must say no value may be inferred from field existence")


# --------------------------------------------------------------------------------------------
# DB6-OD1-OD2-1 (2026-10-02) - the bounded 13-cell backfill, the DB6-local multi-source
# convention, OD1 closed with ONE named exception, and the S10 null-Next-Review fail-closed fix.
# Offline and deterministic. Checks what the REPOSITORY RECORDS, never the live store.
# --------------------------------------------------------------------------------------------


class OD1BackfillRecorded(unittest.TestCase):

    def test_thirteen_cells_recorded_as_written(self):
        bp = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]["backfill_performed"]
        self.assertEqual(bp["cells_written"], BACKFILL_CELLS)
        self.assertEqual(bp["rows_written"], 4)
        self.assertIn(OD1, bp["task"])

    def test_populated_and_null_counts_reconcile_to_28(self):
        st = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]
        self.assertEqual(st["non_null_cells"] + st["null_cells"], st["cells"])
        self.assertEqual(st["cells"], 28)
        self.assertEqual(st["non_null_cells"], 17)
        self.assertEqual(st["null_cells"], 11)
        # 4 pre-existing Confidence + 13 written = 17
        self.assertEqual(4 + BACKFILL_CELLS, st["non_null_cells"])

    def test_three_rows_satisfy_the_documented_source_evidence_expectation(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        for field in ("Source", "Evidence"):
            rv = by[field]["row_values"]
            for lens in ("Operator", "Amplifier", "Enabler"):
                self.assertIn(lens, rv, "%s must record %s as populated" % (field, lens))
            self.assertIn("NULL on Buyer", rv, "%s must record Buyer as null" % field)

    def test_evidence_values_carry_their_caveats(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        self.assertIn("caveat", by["Evidence"]["row_values"].lower(),
                      "the read-depth/inference caveats must be recorded as carried")

    def test_dates_are_from_the_bodies_not_derived(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        lv = by["Last Verified"]["row_values"]
        self.assertIn("2026-08-19", lv)
        self.assertIn("2026-08-24", lv)
        self.assertIn("No date was derived, defaulted or inferred", lv)

    def test_no_further_backfill_is_authorised(self):
        st = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]
        self.assertIs(st["backfill_authorised"], False,
                      "the fail-closed default must survive its own exercise")
        self.assertIn("no FURTHER backfill", st["backfill_authorised_note"])


class OD1NoTierNoUrlNoConfidenceWrite(unittest.TestCase):

    def test_no_source_tier_or_source_url_populated(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        for p in ("Source Tier", "Source URL"):
            self.assertIn("NULL on all four rows", by[p]["row_values"],
                          "%s must be recorded null on every row" % p)
            self.assertIn("not representable", by[p]["row_values"].lower(),
                          "%s null must mean not-representable, not unknown" % p)

    def test_confidence_unchanged_and_still_required(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        c = by["Confidence"]
        self.assertIs(c.get("required"), True, "required: true must survive")
        self.assertNotIn("validation", c, "V3 must not have been legislated as a validator")
        self.assertIn("NOT WRITTEN", c["row_values"],
                      "Confidence must be recorded as never written by the backfill")
        self.assertIn("Medium on all four rows", c["row_values"])

    def test_the_backfill_records_what_it_did_not_write(self):
        bp = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]["backfill_performed"]
        nw = bp["not_written"]
        for must in ("Confidence", "Source Tier", "Source URL", "Buyer", "schema", "DB3",
                     "DB9", "DB10"):
            self.assertIn(must, nw, "not_written must name %s" % must)


class OD1BuyerExceptionIsSingularAndExpiring(unittest.TestCase):

    def setUp(self):
        self.ex = dbrow("DB6")["od1_exception"]

    def test_the_exception_fields_are_exactly_as_approved(self):
        self.assertEqual(self.ex["database"], "DB6")
        self.assertEqual(self.ex["row_alias"], "Buyer")
        self.assertEqual(self.ex["scope"], "this row only")
        self.assertEqual(self.ex["expiry"], EXCEPTION_EXPIRY)
        self.assertEqual(
            self.ex["issue"],
            "Confidence populated while governed Source and Evidence remain absent")
        self.assertEqual(
            self.ex["reason"],
            "existing author judgement retained while re-sourcing remains incomplete")
        self.assertEqual(self.ex["consequence"],
                         "S10 confidence/freshness floors remain UNRESOLVED")

    def test_expiry_is_exact(self):
        self.assertEqual(self.ex["expiry"], "2026-11-24")

    def test_no_automatic_waiver_renewal_and_no_automatic_action(self):
        self.assertIs(self.ex["automatic_waiver_renewal"], False)
        self.assertIn("Nothing happens by itself", self.ex["no_automatic_action_on_expiry"])
        self.assertIn("separate owner-reviewed task", self.ex["no_automatic_action_on_expiry"])

    def test_buyer_alone_carries_it(self):
        self.assertEqual(self.ex["row_alias"], "Buyer")
        for other in ("DB9", "DB10"):
            self.assertNotIn("od1_exception", dbrow(other),
                             "%s must carry no exception" % other)

    def test_it_does_not_apply_to_other_or_future_rows(self):
        dna = self.ex["does_not_apply_to"]
        self.assertIn("future", dna, "must exclude future rows")
        self.assertIn("NOT an exception for historical rows generally", dna,
                      "must not be phrased as a class of rows")

    def test_the_resourcing_lead_is_a_lead_not_evidence(self):
        lead = self.ex["re_sourcing_lead"]
        self.assertIn("LEAD for", lead)
        self.assertIn("NOT evidence", lead)
        self.assertIn("another database", lead)


class OD1S10FreshnessFailsClosedOnEitherDate(unittest.TestCase):

    def setUp(self):
        self.txt = flat(read(S10))
        self.rawt = read(S10)

    def test_null_next_review_forces_unresolved(self):
        self.assertTrue(re.search(r"null Last Verified\s*OR a null Next Review\s*->\s*UNRESOLVED",
                                  self.txt),
                        "the rule must fail closed on EITHER missing date")
        self.assertIn("Both dates are required from every contributing record", self.txt)

    def test_the_unresolved_result_names_the_element(self):
        self.assertIn("UNRESOLVED, naming each such element", self.txt)
        self.assertIn("name the record or audience element", self.txt)

    def test_another_rows_date_cannot_fill_a_null(self):
        self.assertIn("may NEVER be filled from another row's", self.txt)
        for forbidden in ("Not from the earliest", "not from the latest",
                          "not from a sibling", "not from a department default"):
            self.assertIn(forbidden, self.txt,
                          "the inheritance ban must be explicit: %s" % forbidden)

    def test_no_substitute_dates(self):
        self.assertIn("No assembly date, no current date and no global decay threshold", self.txt)
        self.assertIn("a borrowed date is a fabricated one", self.txt)

    def test_db6_is_the_worked_example_and_still_unresolved(self):
        self.assertIn("the DB 6 freshness contribution is `UNRESOLVED`, naming the", self.txt)
        self.assertIn("That is the rule working, not the rule failing", self.txt)
        self.assertIn("One null is enough", self.txt)

    def test_the_backfill_did_not_change_the_verdict(self):
        self.assertIn("the backfill improved the data, not the verdict", self.txt)


class OD1ScopeBoundaries(unittest.TestCase):

    def test_od2_local_closure_is_not_sector_wide_ratification(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        self.assertIn("LOCALLY", od["OD2"]["status"])
        self.assertIn("NOT A SECTOR-WIDE RATIFICATION", od["OD2"]["status"])
        self.assertIn("NOT ratified", od["OD4"]["status"], "OD4 is where that is decided")

    def test_od4_and_od5_stay_open(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k in ("OD4", "OD5"):
            self.assertIn("OPEN", od[k]["status"])
            self.assertNotIn("CLOSED", od[k]["status"])

    def test_db3_finding_is_open_and_caused_no_db3_mutation(self):
        # UPDATED 2026-10-02: DB3-PROV-1 Step A RE-SCOPED OD6 and replaced its original facts
        # list, so the old "not acted on" / "terminates in an unsourced claim" phrases are gone
        # by design. What must survive is that OD6 is OPEN, that the original claim is preserved
        # rather than rewritten, and that DB3 itself was never mutated.
        od = json.loads(read(DBJSON))["_open_decisions"]["OD6"]
        self.assertEqual(od["db"], "DB3")
        self.assertIn("OPEN", od["status"])
        self.assertIn("RE-SCOPED", od["status"])
        self.assertIn("superseded_claim", od,
                      "the original OD6 framing must be preserved, not rewritten")
        self.assertIn("DISPROVEN", od["superseded_claim"]["verdict"])
        self.assertIs(od["superseded_claim"]["preserved_not_rewritten"], True)
        # DB3 itself must carry no backfill and no exception
        d3 = dbrow("DB3")
        self.assertIs(d3["row_level_provenance"]["backfill_authorised"], False)
        self.assertNotIn("backfill_performed", json.dumps(d3))
        self.assertNotIn("od1_exception", d3)
        # DB3's own contract entry must be untouched by this task
        d3 = dbrow("DB3")
        self.assertNotIn("od1_exception", d3)
        self.assertNotIn("backfill_performed", json.dumps(d3))

    def test_db9_and_db10_row_state_untouched(self):
        self.assertEqual(
            dbrow("DB9")["MISSING_FIELD"]["row_level_status"]["non_null_cells"], 0)
        self.assertEqual(
            dbrow("DB10")["MISSING_FIELD"]["row_level_status"]["non_null_cells"], 0)

    def test_v3_is_a_documented_expectation_not_a_validator(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD1"]
        self.assertIn("documented expectation", od["status"].lower())
        self.assertIn("not an enforced validator", od["status"].lower())


# --------------------------------------------------------------------------------------------
# DB3-PROV-1 Step A (2026-10-02) - repository synchronisation to DB3-PROV-AUDIT-1.
# Offline and deterministic. REPOSITORY-INTERNAL ONLY: these tests check what the repository
# RECORDS about DB3. They cannot and do not check the live Notion store, so THEY CANNOT DETECT
# LATER LIVE DRIFT. Re-verifying DB3's live schema needs another separately authorised audit.
# --------------------------------------------------------------------------------------------

DB3_AUDIT = "DB3-PROV-AUDIT-1"
DB3_SOURCE_OPTS = ["xlsx", "chat", "agent run", "research"]
# REWRITTEN 2026-10-02 by DB3-OD10-OD12-1. DB3_ABSENT was
#   ["Source Tier", "Source URL", "Last Verified", "Next Review", "Next Verification"]
# Two of those five were added to live DB3 as nullable dates under OD10 Option D, so asserting
# their absence would now assert something false. Split rather than shortened: the three that are
# still absent keep their ban, and the two that now exist get a POSITIVE requirement, which is
# strictly stronger than having no rule at all.
DB3_ABSENT = ["Source Tier", "Source URL", "Next Verification"]
DB3_NOW_PRESENT = ["Last Verified", "Next Review"]
DB3_OD10 = "DB3-OD10-OD12-1"


class DB3RecordedSchema(unittest.TestCase):

    def test_field_count_is_seventeen_and_anchored(self):
        # Was test_field_count_is_fifteen_and_anchored. 15 was the correct live count until
        # DB3-OD10-OD12-1 added two date properties on 2026-10-02. Renamed rather than edited in
        # place, so the diff cannot be mistaken for a loosened threshold.
        d3 = dbrow("DB3")
        self.assertEqual(len(d3["fields"]), 17)
        self.assertEqual(d3.get("field_count_verified"), 17,
                         "DB3 must carry the mechanical count anchor")
        self.assertIn(DB3_AUDIT, d3.get("field_count_note", ""),
                      "and attribute the original count to the bounded audit")
        self.assertIn(DB3_OD10, d3.get("field_count_note", ""),
                      "and attribute the change to the task that made it")

    def test_the_superseded_fifteen_field_count_is_preserved(self):
        # The point of this test: a dated claim that stops being true is SUPERSEDED, never
        # silently corrected. This is the same rule check 7b exists to enforce, applied to a
        # change I made myself.
        fcs = dbrow("DB3")["field_count_superseded"]
        self.assertEqual(fcs["was"], 15)
        self.assertIn("2026-10-02", fcs["was_true_when_written"])
        self.assertIn("2026-10-02", fcs["became_false_on"])
        self.assertIn("SUPERSEDED, NOT WRONG", fcs["verdict"])
        self.assertIs(fcs["preserved_not_rewritten"], True)

    def test_the_two_new_dates_are_recorded_nullable_and_governing(self):
        by = {f["name"]: f for f in dbrow("DB3")["fields"]}
        for n in DB3_NOW_PRESENT:
            self.assertIn(n, by, "%s was added live 2026-10-02 and must be recorded" % n)
            self.assertEqual(by[n]["notion_type"], "date")
            self.assertIs(by[n]["required"], False, "%s is nullable" % n)
            self.assertIn("GOVERN", by[n]["semantics"].upper())
            self.assertIn("FAILS CLOSED", by[n]["validation"].upper())
            self.assertIn("217", by[n]["semantics"], "must record null on all 217 rows")

    def test_next_review_not_next_verification(self):
        by = {f["name"]: f for f in dbrow("DB3")["fields"]}
        self.assertNotIn("Next Verification", by,
                         "the owner was explicit: `Next Review`, not `Next Verification`")
        self.assertIn("Next Verification", by["Next Review"]["semantics"],
                      "and the choice must be recorded, not merely made")
        self.assertIn("FIRST TRIGGER", by["Next Review"]["semantics"].upper(),
                      "Next Review is what finally gives the Stale rule a trigger")

    def test_no_duplicate_field_names(self):
        names = [f["name"] for f in dbrow("DB3")["fields"]]
        dupes = sorted({n for n in names if names.count(n) > 1})
        self.assertEqual(dupes, [], "DB3 duplicate field names: %s" % dupes)

    def test_source_is_a_four_value_process_kind_select(self):
        by = {f["name"]: f for f in dbrow("DB3")["fields"]}
        src = by["Source"]
        self.assertEqual(src["notion_type"], "select")
        self.assertEqual(src["allowed_values"], DB3_SOURCE_OPTS,
                         "the exact four options, in order")
        self.assertIn("PROCESS KIND", src["semantics"])
        self.assertIn("not authority", src["semantics"].lower())
        self.assertIn("Evidence", src["semantics"],
                      "must say the locator belongs in Evidence")

    def test_evidence_is_required_and_fully_populated(self):
        by = {f["name"]: f for f in dbrow("DB3")["fields"]}
        self.assertIs(by["Evidence"].get("required"), True)
        self.assertIn("No evidence, no row", by["Evidence"]["validation"])
        rl = dbrow("DB3")["row_level_provenance"]
        self.assertEqual(rl["Evidence"]["non_null"], 217)
        self.assertEqual(rl["Evidence"]["of"], 217)

    def test_tier_fields_are_still_recorded_absent(self):
        # Was test_temporal_and_tier_fields_are_recorded_absent, which required `Last Verified`
        # and a next-review key inside `fields_absent`. Both now EXIST, so that test would force
        # the contract to carry a false record. The TIER half of the limitation is untouched and
        # is still asserted here; the temporal half moved to the two tests below.
        d3 = dbrow("DB3")
        names = [f["name"] for f in d3["fields"]]
        for absent in DB3_ABSENT:
            self.assertNotIn(absent, names, "%s must not be recorded as a DB3 field" % absent)
        pm = d3["provenance_model"]["fields_absent"]
        for absent in ("Source Tier", "Source URL"):
            self.assertIn(absent, pm, "absence of %s must be STATED, not merely omitted" % absent)
        self.assertNotIn("Last Verified", pm, "no longer absent as of 2026-10-02")
        self.assertFalse(any("Next Review" in k for k in pm),
                         "no longer absent as of 2026-10-02")
        for k, v in pm.items():
            self.assertIn("ABSENT", v.upper(), "%s must be described as absent" % k)

    def test_the_superseded_absence_claims_are_preserved_verbatim(self):
        fmr = dbrow("DB3")["provenance_model"]["fields_formerly_absent_now_present"]
        verb = fmr["superseded_claims_verbatim"]
        self.assertEqual(len(verb), 2, "both absence claims preserved")
        for k, v in verb.items():
            self.assertIn("ABSENT", v.upper(),
                          "preserved means verbatim - %s no longer reads as an absence claim" % k)
        self.assertIs(fmr["preserved_not_rewritten"], True)

    def test_absent_and_present_but_null_are_recorded_as_different_facts(self):
        # The substantive point of the whole task. Adding the fields did NOT fix anything today;
        # it changed the KIND of failure from unfixable to merely empty.
        fmr = dbrow("DB3")["provenance_model"]["fields_formerly_absent_now_present"]
        why = fmr["why_this_distinction_matters"]
        self.assertIn("DIFFERENT FACTS", why.upper())
        self.assertIn("fail closed", why.lower())
        self.assertIn("dead end", why.lower())
        self.assertIn("did NOT make anything computable", why)
        for n in DB3_NOW_PRESENT:
            self.assertIn("NULL", fmr[n].upper())

    def test_freshness_threshold_is_recorded_undefined(self):
        by = {f["name"]: f for f in dbrow("DB3")["fields"]}
        sem = by["Freshness"]["semantics"]
        self.assertIn("DECLARED", sem.upper())
        self.assertIn("no Fresh/Aging/Stale threshold is defined", sem)
        self.assertIn("never substitute", sem.lower())
        fr = dbrow("DB3")["provenance_model"]["freshness_is_a_declaration_not_a_measurement"]
        self.assertIn("DECLARATION", fr["consequence"].upper())
        self.assertIn("OD10", fr["related_open_item"])
        self.assertIn("CLOSED BY DISSOLUTION", fr["related_open_item"],
                      "OD10 closed 2026-10-02; the pointer must say so")

    def test_freshness_is_recorded_non_governing_and_not_derived(self):
        sd = dbrow("DB3")["provenance_model"][
            "freshness_is_a_declaration_not_a_measurement"]["superseding_decision"]
        self.assertIs(sd["freshness_is_non_governing"], True)
        self.assertIn("DISSOLVED", sd["no_threshold_is_defined_or_needed"].upper())
        self.assertIn("notAvailableInQuerySql", sd["do_not_derive"],
                      "the reason is the DB5 Total Score formula precedent, not a bare ban")
        self.assertIn("not being called", sd["historical_values_are_non_governing_not_false"],
                      "the 217 Fresh values are non-governing, NOT false")

    def test_the_limitation_is_recorded_half_closed(self):
        lim = dbrow("DB3")["provenance_model"]["the_actual_limitation"]
        self.assertIn("NOT MISSING PROVENANCE", lim.upper())
        self.assertIn("SCHEMA EXPRESSIVENESS", lim.upper())
        self.assertIn("HALF CLOSED", lim.upper())
        self.assertIn("EXPRESSIBLE but UNPOPULATED", lim)
        self.assertIn("SOURCE TIER REMAINS STRUCTURALLY INEXPRESSIBLE", lim.upper(),
                      "closing the temporal half must not be read as closing the tier half")

    def test_the_limitation_is_expressiveness_not_missing_provenance(self):
        pm = dbrow("DB3")["provenance_model"]
        lim = pm["the_actual_limitation"]
        self.assertIn("NOT MISSING PROVENANCE GENERALLY", lim.upper())
        self.assertIn("SCHEMA EXPRESSIVENESS", lim.upper())
        self.assertIn("TEMPORAL", lim.upper())

    def test_drift_is_declared_undetectable(self):
        self.assertIn("drift", flat(json.dumps(dbrow("DB3"))).lower())
        dw = flat(dbrow("DB3")["provenance_model"]["drift_warning"]).lower()
        self.assertIn("no offline gate can detect later live", dw,
                      "the warning must say no gate can detect drift")


class DB3RowLevelRecorded(unittest.TestCase):

    def setUp(self):
        self.rl = dbrow("DB3")["row_level_provenance"]

    def test_row_count_and_full_population(self):
        self.assertEqual(self.rl["rows"], 217)
        for f in ("Evidence", "Confidence", "Source", "Freshness"):
            self.assertEqual(self.rl[f]["non_null"], 217, "%s populated 217/217" % f)

    def test_zero_rows_have_confidence_without_evidence(self):
        self.assertEqual(self.rl["rows_with_confidence_and_no_evidence"], 0,
                         "this is the fact that disproved the original OD6 framing")

    def test_source_values_sum_to_the_row_count(self):
        self.assertEqual(sum(self.rl["Source"]["by_value"].values()), 217)
        self.assertEqual(sum(self.rl["Confidence"]["by_value"].values()), 217)

    def test_target_set_recorded_without_overclaiming(self):
        t = self.rl["target_sector_rows"]
        self.assertEqual(t["count"], 6)
        self.assertEqual(t["evidence_naming_a_source"], 5)
        self.assertEqual(t["evidence_naming_no_source"], 1)
        self.assertEqual(t["evidence_naming_a_source"] + t["evidence_naming_no_source"], 6)
        self.assertIn("NONE", t["confidence_correction_required"],
                      "no Target-row confidence correction is required")

    def test_non_target_rows_are_not_characterised(self):
        n = self.rl["non_target_rows"]
        self.assertEqual(n["count"], 211)
        self.assertEqual(n["count"] + self.rl["target_sector_rows"]["count"], 217)
        self.assertIn("NOT READ", n["bodies"])
        self.assertIn("not characterised", n["bodies"].lower())

    def test_the_high_confidence_rows_are_now_classified(self):
        # Was test_no_claim_is_made_about_the_high_confidence_rows, which required
        # no_claim_is_made_about_them is True. Correct while the bodies were unread; the owner
        # then authorised reading all three. Refusing to characterise them now would be a FALSE
        # record, so the test is rewritten to require the classifications BY NAME - which is
        # stricter than the refusal it replaces.
        hc = self.rl["high_confidence_rows"]
        self.assertEqual(hc["count"], 3)
        self.assertEqual(hc["in_target_set"], 0)
        self.assertIn("CHARACTERISED", hc["status"].upper())
        self.assertIs(hc["no_claim_is_made_about_them"], False)
        self.assertEqual(hc["bodies_read"], 3)
        self.assertIs(hc["all_three_bodies_blank"], True)

    def test_the_earlier_refusal_to_characterise_is_preserved(self):
        sc = self.rl["high_confidence_rows"]["superseded_claim"]
        self.assertIn("NOT CHARACTERISED", sc["was"].upper())
        self.assertIs(sc["prior_no_claim_flag"], True)
        self.assertIn("NOT WRONG", sc["verdict"].upper(),
                      "declining to characterise unread bodies was correct, not an error")
        self.assertIs(sc["preserved_not_rewritten"], True)

    def test_one_overstated_two_unresolved(self):
        cls = self.rl["high_confidence_rows"]["classifications"]
        verdicts = sorted(v["verdict"] for v in cls.values() if isinstance(v, dict))
        self.assertEqual(verdicts, ["HIGH_OVERSTATED", "HIGH_UNRESOLVED", "HIGH_UNRESOLVED"])

    def test_h1_requires_a_correction_that_was_not_authorised_here(self):
        cls = self.rl["high_confidence_rows"]["classifications"]
        h1 = next(v for v in cls.values()
                  if isinstance(v, dict) and v["verdict"] == "HIGH_OVERSTATED")
        self.assertIs(h1["correction_required"], True)
        self.assertIn("NOT AUTHORISED", h1["correction_is_a_separate_decision"].upper(),
                      "the owner reserved H1's disposition")
        self.assertIn("DRAFT 15", h1["why"].upper(),
                      "the basis is self-referential: Arika's own internal draft")
        self.assertIn("triggers an agent", h1["not_inert"],
                      "H1 is not dormant: it is routed and it fires an agent")
        self.assertIn("Sales", h1["not_inert"])
        self.assertIs(h1["in_target_s10_path"], False)

    def test_h2_and_h3_need_resourcing_not_rerating(self):
        cls = self.rl["high_confidence_rows"]["classifications"]
        unres = [v for v in cls.values()
                 if isinstance(v, dict) and v["verdict"] == "HIGH_UNRESOLVED"]
        self.assertEqual(len(unres), 2)
        for v in unres:
            self.assertIs(v["correction_required"], False)
            self.assertIn("RE-SOURCING", v["needs"].upper())
            self.assertIn("NULL", v["sub_sector"].upper(), "Sub-Sector is null on both - OD13")

    def test_no_confidence_value_was_changed(self):
        cls = self.rl["high_confidence_rows"]["classifications"]
        self.assertIn("NO Confidence value was written", cls["_confidence_values_unchanged"])
        by_value = self.rl["Confidence"]["by_value"]
        self.assertEqual(by_value, {"High": 3, "Medium": 214, "Low": 0},
                         "the live distribution after the writes is identical to before")

    def test_the_two_new_columns_are_null_on_every_row(self):
        for n in DB3_NOW_PRESENT:
            cell = self.rl[n]
            self.assertEqual(cell["non_null"], 0)
            self.assertEqual(cell["of"], 217)
            self.assertIn("PRESENT BUT NULL", cell["state"].upper())
            self.assertIs(cell["backfill_authorised"], False)

    def test_the_zero_row_write_proof_is_recorded(self):
        zp = self.rl["zero_row_writes_proof"]
        self.assertEqual(zp["schema_writes"], 2)
        self.assertEqual(zp["row_value_writes"], 0)
        self.assertEqual(zp["live_calls"], 5)
        self.assertIn("identical", zp["method"], "the method, not just the conclusion")
        self.assertIn("31794", zp["result"], "a concrete before/after measure")

    def test_no_backfill_authorised(self):
        self.assertIs(self.rl["backfill_authorised"], False)


class DB3IsNotTheSevenFieldShape(unittest.TestCase):

    def test_db3_does_not_claim_the_seven_field_shape(self):
        pm = dbrow("DB3")["provenance_model"]
        self.assertIn("not the seven-field shape", pm["summary"].lower())
        self.assertIn("NOT AN INCOMPLETE COPY", pm["summary"].upper())

    def test_no_seven_field_ratification_anywhere(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        self.assertIn("NOT ratified", od["OD4"]["status"])
        self.assertIn("DIFFERENT coherent model", od["OD4"]["status"])
        self.assertTrue(any("COUNTEREXAMPLE" in f for f in od["OD4"]["facts"]),
                        "OD4 must record DB3 as a counterexample")
        self.assertTrue(any("SEMANTIC REVERSAL" in f for f in od["OD4"]["facts"]),
                        "and record why standardising would be a migration, not an addition")

    def test_the_other_three_keep_their_shape(self):
        for db_id, n in (("DB6", 19), ("DB9", 21), ("DB10", 16)):
            self.assertEqual(len(dbrow(db_id)["fields"]), n, "%s unchanged" % db_id)
            self.assertIn("Evidence", [f["name"] for f in dbrow(db_id)["fields"]])

    def test_intelligence_object_q2_mapping_is_still_unchanged(self):
        # The Q2 half of this test is unchanged and must stay that way: `Evidence + Source` was
        # already correct and three successive authorisations have said not to touch it.
        props = json.loads(read(IOJSON))["properties"]
        self.assertEqual(props["source"]["notion_field"]["DB3"], "Evidence + Source",
                         "DB3's Q2 mapping was already correct and must not be touched")
        self.assertEqual(props["reliability"]["notion_field"]["DB3"], "Confidence")

    def test_intelligence_object_q3_mapping_now_names_the_two_dates(self):
        # The Q3 half CHANGED, and this is the one repository edit of the task that went beyond
        # a straight transcription of live state. It read `Freshness` ALONE, which could not
        # satisfy when_observed.required = [last_verified, freshness]. That non-compliance was
        # one of the two reasons Option D is compliance work rather than convenience, so leaving
        # the mapping stale would have hidden the very defect the task closed.
        wo = json.loads(read(IOJSON))["properties"]["when_observed"]
        self.assertEqual(wo["notion_field"]["DB3"], "Last Verified + Next Review")
        self.assertEqual(sorted(wo["required"]), ["freshness", "last_verified"],
                         "the canonical object was NOT relaxed - DB3 was made able to satisfy it")
        self.assertIn("NON-GOVERNING", wo["notion_field_notes"])
        self.assertIn("could not satisfy", wo["notion_field_notes"],
                      "the reason for the change must be recorded next to it")
        self.assertIn("NULL", wo["notion_field_notes"].upper(),
                      "and that no DB3 row can supply a floor today")


class DB3OD6SupersededAndRescoped(unittest.TestCase):

    def setUp(self):
        self.od6 = json.loads(read(DBJSON))["_open_decisions"]["OD6"]

    def test_the_prior_claim_is_preserved_verbatim(self):
        sc = self.od6["superseded_claim"]
        self.assertIn("unsupported", sc["question_text"].lower(),
                      "the original framing must be kept as written")
        self.assertIs(sc["preserved_not_rewritten"], True)
        self.assertIn("DISPROVEN", sc["verdict"])

    def test_the_reading_error_is_recorded(self):
        sc = self.od6["superseded_claim"]
        self.assertIn("`Source` property ALONE", sc["the_reading_error"])
        self.assertIn("GOVERNED PROCESS VOCABULARY", sc["the_reading_error"])
        self.assertIn("ALREADY BEEN READ", sc["aggravating_detail"])
        self.assertIn("SECOND", sc["pattern"])

    def test_zero_of_217_is_the_disproving_fact(self):
        self.assertIn("ZERO of 217", self.od6["superseded_claim"]["why_it_was_wrong"])

    def test_od6_is_rescoped_to_four_specific_things(self):
        rs = self.od6["rescoped_to"]
        self.assertEqual(len(rs), 4)
        joined = " ".join(rs)
        for must in ("temporal", "Source Tier", "Freshness", "Body-level"):
            self.assertIn(must, joined, "re-scope must name %s" % must)
        self.assertIn("OPEN", self.od6["status"])
        self.assertIn("RE-SCOPED", self.od6["status"])
        self.assertIn("SCHEMA EXPRESSIVENESS", self.od6["status"].upper())

    def test_no_confidence_correction_claimed_as_needed(self):
        self.assertIn("No Target-row Confidence correction",
                      self.od6["what_the_audit_found_NOT_required"])

    def test_the_db6_proposal_carries_a_superseding_note_not_a_rewrite(self):
        # Strip blockquote markers BEFORE flattening: the preserved text is inside a quote block,
        # so a hard-wrapped phrase would otherwise pick up a stray "> " in the middle.
        _p = read(os.path.join(ROOT, "01_Sector", "DB6_OD1_OD2_RESOLUTION_PROPOSAL.md"))
        prop = flat(re.sub(r"(?m)^>\s?", "", _p))
        self.assertIn("SUPERSEDED 2026-10-02 by `DB3-PROV-AUDIT-1`", prop)
        self.assertIn("THE CLAIM BELOW IS DISPROVEN", prop)
        # the original wording must survive verbatim
        self.assertIn("That is the OD1 pattern exactly", prop,
                      "the disproven text is preserved, not deleted")
        self.assertIn("ORIGINAL TEXT, PRESERVED", prop)


class DB3OpenItemsRecorded(unittest.TestCase):

    def test_od7_to_od13_are_recorded_and_open_except_od10(self):
        # Was test_od7_to_od12_are_recorded_and_open. OD10 is the only one of the twelve that
        # closed, and it is NOT simply dropped from the loop - it gets a stricter dedicated test
        # below. OD13 joins.
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k in ("OD7", "OD8", "OD9", "OD11", "OD12", "OD13"):
            self.assertIn(k, od, "%s must be recorded" % k)
            self.assertIn("OPEN", od[k]["status"], "%s must be OPEN" % k)
            self.assertEqual(od[k]["db"], "DB3")
        for k in ("OD7", "OD8", "OD9", "OD11", "OD13"):
            self.assertNotIn("CLOSED", od[k]["status"])

    def test_od10_is_closed_by_dissolution_with_its_question_preserved(self):
        od10 = json.loads(read(DBJSON))["_open_decisions"]["OD10"]
        self.assertIn("CLOSED BY DISSOLUTION", od10["status"])
        self.assertIn("NOT reusable", od10["status"],
                      "the 30/90-day finding belongs in the closure, not only in the proposal")
        sq = od10["superseded_question"]
        self.assertIn("Fresh/Aging/Stale thresholds", sq["verbatim"],
                      "the original question must be preserved verbatim")
        self.assertIn("DISSOLVED, NOT ANSWERED", sq["verdict"].upper())
        self.assertIn("UNIMPLEMENTABLE", sq["verdict"].upper(),
                      "the reason it was dissolved: Option A could not be built at all")
        self.assertIs(sq["preserved_not_rewritten"], True)
        self.assertIn("NOT authorised", od10["what_remains_open"],
                      "closing OD10 did not authorise a backfill or make anything computable")

    def test_the_nine_option_d_decisions_are_recorded(self):
        odr = dbrow("DB3")["provenance_model"]["od10_decision_record"]
        self.assertEqual(len(odr["decisions"]), 9)
        joined = " ".join(odr["decisions"])
        for needle in ("NON-GOVERNING", "GOVERNING temporal fields", "NO Fresh/Aging/Stale "
                       "threshold is defined", "NOT reused", "NON-NULL `Next Review` is STALE",
                       "FAILS CLOSED", "NOT derived", "CLOSED BY DISSOLUTION"):
            self.assertIn(needle, joined, "decision missing: %s" % needle)
        self.assertEqual(
            odr["proposal_sha256"],
            "51d405e4cac3fb4c3318246646e3b0d324da6251b67c58a48d91024865abafb4",
            "the approved proposal must be pinned by hash")

    def test_options_a_and_c_are_recorded_as_impossible_not_merely_rejected(self):
        # The sharpest finding of the assessment, and the one most likely to be softened later
        # into "we preferred D". A was UNIMPLEMENTABLE; C was EXCLUDED BY CONTRACT.
        rej = dbrow("DB3")["provenance_model"]["od10_decision_record"]["options_rejected"]
        self.assertIn("UNIMPLEMENTABLE", rej["A - define a threshold"].upper())
        self.assertIn("needs a date to measure from", rej["A - define a threshold"])
        self.assertIn("EXCLUDED BY CONTRACT", rej["C - retire `Freshness`"].upper())
        self.assertIn("REQUIRED property", rej["C - retire `Freshness`"])

    def test_the_30_and_90_day_horizons_are_recorded_not_reusable(self):
        thr = dbrow("DB3")["provenance_model"]["od10_decision_record"][
            "thresholds_examined_and_rejected_as_not_reusable"]
        self.assertIn("PROSPECT-SCORE", thr["30_day"].upper())
        self.assertIn("REPOSITORY CONTRACT FILE", thr["90_day"].upper(),
                      "the 90-day rule governs repository metadata, not row content")
        self.assertIn("NEITHER IS REUSABLE", thr["verdict"].upper())
        self.assertIn("`Next Review` NAMING CONVENTION", thr["verdict"],
                      "what WAS reusable was the naming convention, not a number")

    def test_the_stale_rule_finally_has_a_trigger(self):
        odr = dbrow("DB3")["provenance_model"]["od10_decision_record"]
        trig = odr["stale_rule_now_has_a_trigger"]
        self.assertIn("MUST NOT drive downstream execution", trig)
        self.assertIn("nothing governed WHEN", trig,
                      "a consequence with no trigger - that is the defect Option D closed")
        self.assertIn("never run", trig, "the M4 stale sweep has never run")

    def test_option_d_was_not_chosen_to_make_s10_computable(self):
        # The authorisation for the assessment said in terms: do not define a threshold merely
        # to make S10 computable. This test exists so that the recorded motive cannot drift.
        odr = dbrow("DB3")["provenance_model"]["od10_decision_record"]
        cnc = odr["contract_non_compliances_this_addresses"]
        self.assertIn("intelligence-object.schema.json", cnc)
        self.assertIn("SECTOR_ACTIVATION_CONTRACT.md", cnc)
        self.assertIn("never the reason", cnc["why_this_matters"])
        self.assertIn("DOES NOT MAKE THE FRESHNESS FLOOR COMPUTABLE TODAY",
                      odr["what_this_does_NOT_do"].upper())

    def test_od12_is_characterised_but_still_open(self):
        od12 = json.loads(read(DBJSON))["_open_decisions"]["OD12"]
        self.assertIn("OPEN", od12["status"])
        self.assertIn("HIGH_OVERSTATED", od12["status"])
        self.assertIn("HIGH_UNRESOLVED", od12["status"])
        self.assertIn("SEPARATE DECISION", od12["status"].upper())
        self.assertIn("NO Confidence value was changed", od12["status"])
        self.assertIs(od12["superseded_question"]["preserved_not_rewritten"], True)

    def test_od13_records_the_subsector_nulls_as_unmeasured(self):
        od13 = json.loads(read(DBJSON))["_open_decisions"]["OD13"]
        self.assertIn("OPEN", od13["status"])
        self.assertIn("UNMEASURED", od13["status"].upper())
        self.assertIn("Sub-Sector", od13["question"])
        self.assertIs(od13["bounded_measurement_requires_its_own_authorisation"], True)
        self.assertIn("Incidentally", od13["how_it_was_found"],
                      "it was not the object of any query")
        self.assertIn("gap in my own prior audit", od13["disclosed_gap_in_the_prior_audit"],
                      "DB3-PROV-AUDIT-1 did not check Sub-Sector population - disclose it")
        self.assertIn("did NOT measure", od13["not_measured_here"])

    def test_each_open_item_names_its_subject(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k, needle in (("OD7", "Last Verified"), ("OD8", "Source Tier"),
                          ("OD9", "Source URL"), ("OD11", "re-sourced"),
                          ("OD12", "High-confidence"), ("OD13", "Sub-Sector")):
            self.assertIn(needle, od[k]["question"], "%s must concern %s" % (k, needle))
        self.assertIn("Fresh/Aging/Stale", od["OD10"]["superseded_question"]["verbatim"],
                      "OD10's subject survives in its preserved question")

    def test_earlier_decisions_keep_their_state(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k in ("OD1", "OD2", "OD3"):
            self.assertIn("CLOSED", od[k]["status"], "%s stays closed" % k)
        for k in ("OD4", "OD5"):
            self.assertIn("OPEN", od[k]["status"], "%s stays open" % k)
        self.assertEqual(dbrow("DB6")["od1_exception"]["expiry"], "2026-11-24",
                         "the DB6 Buyer exception is untouched")


class DB3S10FailsClosed(unittest.TestCase):

    def setUp(self):
        self.txt = flat(read(S10))

    def test_db3_is_the_fourth_element_with_present_but_null_date_fields(self):
        # Was test_db3_is_the_fourth_element_with_absent_date_fields, asserting
        # "FIELD DOES NOT EXIST". Both fields now exist, so S10 must no longer say that.
        self.assertIn("| **DB 3** findings |", self.txt)
        self.assertNotIn("FIELD DOES NOT EXIST", self.txt,
                         "both DB 3 date fields exist as of 2026-10-02")
        self.assertIn("| **PRESENT, null on all 217** | **PRESENT, null on all 217** |", self.txt,
                      "BOTH cells - one is not enough")
        self.assertIn("now *emptily*, no longer *structurally*", self.txt)

    def test_s10_states_three_states_not_two(self):
        self.assertIn("Three states, not two", self.txt)
        self.assertIn("present and populated", self.txt, "the third state by name")
        self.assertIn("changed the kind of failure, not the verdict", self.txt)

    def test_s10_records_freshness_as_non_governing(self):
        self.assertIn("`Freshness` is NON-GOVERNING and MUST NOT be read as a temporal signal",
                      self.txt)
        self.assertIn("A row past a **non-null** `Next Review` is **stale**", self.txt)
        self.assertIn("No Fresh/Aging/Stale threshold exists and none is needed", self.txt)

    def test_s10_does_not_claim_the_floor_is_now_computable(self):
        self.assertIn("No backfill is authorised, so nothing in DB 3 can supply a freshness "
                      "floor today", self.txt)

    def test_absent_field_is_distinguished_from_a_null_cell(self):
        self.assertIn("An absent field is a different fact from a present-but-null cell",
                      self.txt)
        self.assertIn("Both fail closed", self.txt)
        self.assertIn("only the second could ever be filled", self.txt)

    def test_freshness_may_not_substitute_for_a_verification_date(self):
        self.assertIn("No assembly date, current date, or `Freshness` label may substitute",
                      self.txt)
        self.assertIn("cannot age and carries no temporal information", self.txt)

    def test_source_must_not_be_read_as_authority(self):
        self.assertIn("`Source` is a process-kind dimension, not an authority", self.txt)
        self.assertIn("Never read `Source` as the authority", self.txt)
        self.assertIn("never report a row as unsourced because `Source` looks generic", self.txt)

    def test_the_six_target_rows_are_reported_accurately(self):
        self.assertIn("Five of the six Target rows name re-followable sources inline; one does "
                      "not", self.txt)
        self.assertIn("`Evidence` is REQUIRED and populated on 217 of 217 rows", self.txt)

    def test_body_restrictions_may_be_lost(self):
        self.assertIn("Restrictions recorded only in page bodies can be lost", self.txt)
        self.assertIn("read the body before relying on a DB 3 finding", self.txt)
        self.assertIn("do not treat property-completeness as permission", self.txt)

    def test_the_high_confidence_rows_are_classified_in_s10(self):
        # Was test_no_claim_about_the_high_confidence_rows. The bodies were read under
        # authorisation and all three are blank, so "make no claim" is no longer honest - but
        # the earlier position must be visibly SUPERSEDED, not quietly dropped.
        self.assertIn("all three bodies are blank", self.txt)
        self.assertIn("HIGH_OVERSTATED", self.txt)
        self.assertIn("HIGH_UNRESOLVED", self.txt)
        self.assertIn("*Superseded: this bullet previously said to make no claim about them",
                      self.txt)
        self.assertIn("not inert", self.txt,
                      "H1 is routed to Sales and Marketing with an agent-triggering action")
        self.assertIn("None is in a Target S10 path", self.txt)

    def test_db3_is_no_longer_the_unfixable_case(self):
        # Was test_db3_becomes_the_binding_constraint, asserting "cannot be fixed by any
        # backfill". That is exactly what stopped being true. The old sentence is kept in the
        # skill as superseded history, and this test now requires BOTH halves: the correction
        # and the preserved original.
        self.assertIn("DB 3 was the harder case until 2026-10-02", self.txt)
        self.assertIn("could not be fixed by any backfill, because the fields did "
                      "not exist", self.txt,
                      "the superseded sentence must survive verbatim in S10")
        self.assertIn("DB 3 is now an ordinary empty-cell case", self.txt)
        self.assertIn("fixable in principle", self.txt)
        self.assertIn("superseded, not deleted", self.txt)


if __name__ == "__main__":
    unittest.main(verbosity=2)
