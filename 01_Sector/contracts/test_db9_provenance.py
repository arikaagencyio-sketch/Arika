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

    def test_db6_and_db10_are_untouched_by_this_remediation(self):
        rows = {r["db_id"]: r for r in json.loads(read(DBJSON))["databases"]}
        for other in ("DB6", "DB10"):
            names = [f["name"] for f in rows[other]["fields"]]
            self.assertNotIn("Evidence", names, "%s must not have gained Evidence" % other)
            # DB6 qualifies the severity ("... - a schema change is Gate 2+ work"); DB10 does not.
            # The invariant is that both stay FLAGGED AND UNFIXED, not that the strings match.
            self.assertTrue(
                rows[other]["MISSING_FIELD"]["severity"].startswith("flagged, not fixed"),
                "%s's gap stays flagged and unfixed, got %r"
                % (other, rows[other]["MISSING_FIELD"]["severity"]))

    def test_other_databases_keep_their_own_provenance_shape(self):
        rows = {r["db_id"]: r for r in json.loads(read(DBJSON))["databases"]}
        db7 = {f["name"] for f in rows["DB7"]["fields"]}
        self.assertIn("Next Verification", db7, "DB7 keeps its own naming")
        db16 = {f["name"] for f in rows["DB16"]["fields"]}
        self.assertIn("Next Review", db16, "DB16 keeps its own naming")


if __name__ == "__main__":
    unittest.main(verbosity=2)
