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

    def test_db9_prov_1_added_evidence_to_db9_only(self):
        # GENERALISED 2026-10-02 by DB6-DB10-PROV-1. This test previously also asserted that DB6's
        # and DB10's MISSING_FIELD severity stayed "flagged, not fixed". That assertion PINNED A
        # FALSE CLAIM: DB6-DB10-PROV-AUDIT-1 proved both notes wrong, so the test was protecting
        # the defect it should have caught. The durable invariant is narrower and is kept here -
        # DB9-PROV-1's live write touched DB9 alone, so `Evidence` must still be absent from the
        # other two. Whether to add it is open decision OD3.
        rows = {r["db_id"]: r for r in json.loads(read(DBJSON))["databases"]}
        self.assertIn("Evidence", [f["name"] for f in rows["DB9"]["fields"]],
                      "DB9 keeps the one field DB9-PROV-1 added")
        for other in ("DB6", "DB10"):
            names = [f["name"] for f in rows[other]["fields"]]
            self.assertNotIn("Evidence", names,
                             "%s must not have gained Evidence - no live write was authorised"
                             % other)
            # Replaces the old severity pin: the note must now carry its own superseded history
            # rather than repeat a claim the audit disproved.
            mf = rows[other]["MISSING_FIELD"]
            self.assertIn("superseded_claim", mf,
                          "%s must preserve the claim it supersedes" % other)
            self.assertNotIn("flagged, not fixed", mf["severity"],
                             "%s's severity must no longer repeat the superseded framing" % other)

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
# The six provenance properties observed live in BOTH DB6 and DB10. `Evidence` is deliberately
# NOT in this list: it exists in DB9 only.
OBSERVED_SIX = ["Confidence", "Source", "Source Tier", "Source URL", "Last Verified",
                "Next Review"]
EXPECTED_COUNT = {"DB6": 18, "DB10": 15}


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

    def test_the_six_observed_provenance_fields_are_recorded(self):
        for db_id in EXPECTED_COUNT:
            names = [f["name"] for f in dbrow(db_id)["fields"]]
            for p in OBSERVED_SIX:
                self.assertIn(p, names, "%s must record provenance field %r" % (db_id, p))

    def test_provenance_field_types_match_the_audit(self):
        want = {"Confidence": "select", "Source": "text", "Source Tier": "select",
                "Source URL": "url", "Last Verified": "date", "Next Review": "date"}
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
        added = ["Source", "Source Tier", "Source URL", "Last Verified", "Next Review"]
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

    def test_evidence_is_recorded_absent_from_both(self):
        for db_id in EXPECTED_COUNT:
            names = [f["name"] for f in dbrow(db_id)["fields"]]
            self.assertNotIn("Evidence", names,
                             "%s must NOT record Evidence - it is absent live" % db_id)
        blob = flat(json.dumps(dbrow("DB6")) + json.dumps(dbrow("DB10")))
        self.assertIn("Evidence", blob,
                      "absence of Evidence must be stated somewhere, not merely implied")

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
            for p in OBSERVED_SIX:
                if p == "Confidence" and db_id == "DB6":
                    continue  # DB6 always had Confidence; 31e did not add it
                self.assertIn(AUDIT_ID, by[p].get("provenance_of_record", ""),
                              "%s %s must name its snapshot source" % (db_id, p))

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
            self.assertIn("SUPERSEDES", mf["note"],
                          "%s note must say it supersedes, not silently replace" % db_id)

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

    def test_the_schema_description_is_not_called_complete(self):
        # Checks that EVERY occurrence of the phrase is negated, rather than stripping one exact
        # negation string - the two entries word it differently ("does NOT make DB6 ..." vs
        # "DB10 is NOT ..."), and a literal replace() silently misses the other.
        for db_id in EXPECTED_COUNT:
            blob = flat(json.dumps(dbrow(db_id)))
            hits = list(re.finditer(r"provenance-complete", blob))
            self.assertTrue(hits, "%s must address provenance-completeness explicitly" % db_id)
            for m in hits:
                window = blob[max(0, m.start() - 45):m.start()]
                self.assertIn("NOT", window,
                              "%s claims provenance-completeness without negation: ...%s"
                              % (db_id, window[-60:]))


class DB6DB10RowLevelStatus(unittest.TestCase):

    def test_db6_row_level_counts(self):
        st = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]
        self.assertEqual((st["rows"], st["cells"], st["non_null_cells"]), (4, 24, 4))
        self.assertIs(st["backfill_authorised"], False)

    def test_db10_row_level_counts(self):
        st = dbrow("DB10")["MISSING_FIELD"]["row_level_status"]
        self.assertEqual((st["rows"], st["cells"], st["non_null_cells"]), (57, 342, 0))
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
        self.assertTrue(note, "DB6's Confidence must carry the open conflict")
        self.assertIn("OD1", note)
        for must in ("V3", "NOT extended", "separate owner decision"):
            self.assertIn(must, note, "DB6 Confidence note must state %r" % must)

    def test_rule_v3_is_not_extended_to_db6(self):
        by = {f["name"]: f for f in dbrow("DB6")["fields"]}
        self.assertNotIn("validation", by["Confidence"],
                         "adding a V3-style validation to DB6 would legislate the open decision")

    def test_the_four_values_are_not_cleared_or_downgraded(self):
        st = dbrow("DB6")["MISSING_FIELD"]["row_level_status"]
        self.assertIn("Medium", st["non_null_detail"],
                      "the four populated Medium values must still be recorded as populated")
        self.assertEqual(st["non_null_cells"], 4)


class StepOneOpenDecisions(unittest.TestCase):

    def test_all_five_open_decisions_are_recorded_and_unresolved(self):
        od = json.loads(read(DBJSON))["_open_decisions"]
        for k in ("OD1", "OD2", "OD3", "OD4", "OD5"):
            self.assertIn(k, od, "%s must be recorded" % k)
            self.assertIn("OPEN", od[k]["status"], "%s must remain OPEN" % k)
        self.assertIn("NOT RESOLVED", od["_note"])

    def test_no_multi_source_convention_is_defined(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD2"]
        self.assertIn("OPEN", od["status"])
        self.assertIn("No convention is defined", od["status"])
        for db_id in EXPECTED_COUNT:
            by = {f["name"]: f for f in dbrow(db_id)["fields"]}
            self.assertIn("OD2", by["Source Tier"]["validation"],
                          "%s Source Tier must point at the undefined mapping" % db_id)

    def test_no_repository_wide_standard_is_ratified(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD4"]
        self.assertIn("NOT ratified", od["status"])
        self.assertIn("BY OBSERVATION", od["status"])

    def test_adding_evidence_remains_a_decision_not_an_action(self):
        od = json.loads(read(DBJSON))["_open_decisions"]["OD3"]
        self.assertIn("OPEN", od["status"])
        for db_id in EXPECTED_COUNT:
            self.assertNotIn("Evidence", [f["name"] for f in dbrow(db_id)["fields"]])


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

    def test_all_three_contributing_databases_are_named(self):
        for db_id in ("DB 6", "DB 9", "DB 10"):
            self.assertIn(db_id, self.txt, "Step 4 must name %s as a contributing element" % db_id)

    def test_db6_populated_confidence_is_described_as_unsupported(self):
        self.assertIn("populated `Confidence` with an EMPTY `Source`", self.txt)
        self.assertIn("OD1", self.txt)

    def test_db10_is_described_as_empty(self):
        self.assertTrue(re.search(r"DB 10.{0,120}null on all 57", self.txt),
                        "Step 4 must state DB10's provenance is empty")

    def test_evidence_absence_is_stated_for_both(self):
        self.assertIn("`Evidence` does not exist in DB 6's or DB 10's live schema", self.txt)

    def test_the_undefined_multi_source_mapping_is_stated(self):
        self.assertIn("no convention", self.txt.lower())
        self.assertIn("OD2", self.txt)

    def test_rule_v3_is_not_extended_to_db6_in_the_skill(self):
        self.assertIn("rule V3 is deliberately NOT extended to DB 6", self.txt)

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
        self.assertIn("18 properties, verified live 2026-10-02", self.txt)
        self.assertIn("15 properties, verified live 2026-10-02", self.txt)

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

    def test_evidence_absence_recorded_for_both(self):
        self.assertIn("`Evidence` is absent from DB 6", self.txt)
        self.assertIn("`Evidence` is absent from DB 10", self.txt)


if __name__ == "__main__":
    unittest.main(verbosity=2)
