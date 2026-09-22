# -*- coding: utf-8 -*-
"""Offline tests for the Sector S10 TEST_FIXTURE path (decision SECTOR-SF1, enacted and spent 2026-09-22).

    python -m unittest discover -s 01_Sector/contracts -p "test_*.py"

No network, no connector, no skill run. Every gate scenario runs against a temp
directory; the real logs are only ever READ.
"""
import copy, hashlib, importlib.util, io, json, os, re, shutil, tempfile, unittest

import jsonschema


def rd(path, mode="r"):
    with (io.open(path, "rb") if mode == "rb" else io.open(path, encoding="utf-8")) as fh:
        return fh.read()

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCHEMA = json.loads(rd(os.path.join(HERE, "skill-execution-record.schema.json")))
V = jsonschema.Draft202012Validator(SCHEMA)
REAL_LOG = os.path.join(ROOT, "01_Sector", "_memory", "skill_runs.jsonl")
SANDBOX_LOG = os.path.join(ROOT, "01_Sector", "_memory", "skill_runs-sandbox.jsonl")
REGISTRY = os.path.join(HERE, "skill-fixture-authorisations.json")
RECORD_REL = "01_Sector/fixtures/SYN-S10-01.sector-record.json"
PACKET_REL = "01_Sector/fixtures/SYN-S10-01.s10-packet.json"
SKILL_MD = os.path.join(ROOT, ".claude", "skills", "sector-handoff-packet", "SKILL.md")

# Baselines captured 2026-09-22, before the fixture path was prepared.
REAL_LOG_FIRST_15_SHA = "9b0183657e1e33c1633d37357e8a193730d69468773f8d4a34e8d29f58169652"
# Re-baselined 2026-09-22, deliberately: an owner-authorised read-only schema call found that
# none of the four `Lead` tag fields exists live, so S10's Step 0 table now records the ClickUp
# CRM route as DESIGNED / no target instead of CONNECTED, with the dated note and appendix
# re-measurement that go with it. SECTOR_OS.md section 8 and section 15 carry the record.
# Was 1261834be05d5160c1263c47748a931bde7bdeb1699baddc7fb3dd8817878f84 (2026-09-22, pre-correction).
S10_ORDINARY_SHA = "4b854d4c633b5f5b27e3d300dc47fe009eeb5dfa782fd444184320393159b69f"

spec = importlib.util.spec_from_file_location("skill_run_gate", os.path.join(HERE, "skill_run_gate.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

DESTS = [
    ("Offer (02)", "relation + text reference", "not_attempted_fixture"),
    ("Content (04)", "native relation", "not_attempted_fixture"),
    ("ClickUp CRM", "free-text ID tags", "not_attempted_fixture"),
    ("Sales (05)", "event only", "HANDOFF_FAILURE"),
    ("Marketing (03)", "event only (DEMAND_SHIFT, DESIGNED)", "HANDOFF_FAILURE"),
    ("Operations (08)", "event only (DEMAND_SHIFT, DESIGNED)", "HANDOFF_FAILURE"),
]


def fixture_record(eid="s10-fx-test-1", ts="2026-01-01T00:00:00Z"):
    return {
        "timestamp": ts, "skill": "sector-handoff-packet", "skill_id": "S10", "department": "01",
        "stream": "skill", "event_type": "skill_run", "source": "claude-code",
        "classification": "TEST_FIXTURE",
        "payload": {
            "execution_id": eid, "trigger": {"kind": "manual"}, "context": {"resolved": True},
            "decision": "NO_OP", "writes": [], "events": [],
            "fixture": {"authorisation_id": "SECTOR-SF1", "synthetic_record": RECORD_REL,
                        "packet": PACKET_REL, "not_read_fixture": ["DB3", "DB6", "DB7", "DB9", "DB10"]},
            "destinations": [{"destination": d, "mechanism": m, "outcome": o} for d, m, o in DESTS],
        },
    }


def ordinary_record(eid="s10-ordinary-1", ts="2026-01-01T00:00:00Z"):
    r = fixture_record(eid, ts)
    del r["classification"]
    del r["payload"]["fixture"]
    del r["payload"]["destinations"]
    return r


def valid(r):
    return not list(V.iter_errors(r))


# ------------------------------------------------------------ ordinary path --
class OrdinaryPath(unittest.TestCase):
    def test_every_existing_record_still_validates(self):
        n = 0
        for line in rd(REAL_LOG).splitlines():
            if line.strip():
                V.validate(json.loads(line)); n += 1
        self.assertGreaterEqual(n, 15)

    def test_existing_records_are_byte_for_byte_unchanged(self):
        lines = rd(REAL_LOG, "rb").splitlines(keepends=True)
        self.assertEqual(hashlib.sha256(b"".join(lines[:15])).hexdigest(), REAL_LOG_FIRST_15_SHA,
                         "the first 15 real records changed - the log is append-only")

    def test_s10_ordinary_instructions_are_byte_for_byte_unchanged(self):
        t = rd(SKILL_MD, "rb").decode("utf-8")
        self.assertEqual(t.count("<!-- FIXTURE-MODE:BEGIN -->"), 1)
        stripped = re.sub(r"<!-- FIXTURE-MODE:BEGIN -->.*?<!-- FIXTURE-MODE:END -->\n\n", "", t, flags=re.S)
        self.assertEqual(hashlib.sha256(stripped.encode("utf-8")).hexdigest(), S10_ORDINARY_SHA,
                         "ordinary S10 text changed; if intentional, re-baseline with a dated changelog")

    def test_ordinary_record_is_valid_and_may_record_delivered(self):
        r = ordinary_record()
        self.assertTrue(valid(r))
        r["payload"]["destinations"] = [{"destination": "Offer (02)", "mechanism": "text", "outcome": "delivered"}]
        self.assertTrue(valid(r))

    def test_ordinary_record_cannot_carry_fixture_fields(self):
        r = ordinary_record(); r["payload"]["fixture"] = fixture_record()["payload"]["fixture"]
        self.assertFalse(valid(r))
        r = ordinary_record()
        r["payload"]["destinations"] = [{"destination": "x", "mechanism": "y", "outcome": "not_attempted_fixture"}]
        self.assertFalse(valid(r), "not_attempted_fixture is a fixture-only outcome")


# -------------------------------------------------------------- schema ------
class FixtureSchema(unittest.TestCase):
    def test_well_formed_fixture_record_validates(self):
        self.assertTrue(valid(fixture_record()))

    def test_a_fixture_record_cannot_claim_a_write_an_event_or_a_delivery(self):
        r = fixture_record(); r["payload"]["writes"] = [{"db_id": "DB1", "record_id": "x", "fields_changed": []}]
        self.assertFalse(valid(r))
        r = fixture_record(); r["payload"]["events"] = [{"event": "SECTOR_MAPPED", "subscriber_check": "has_subscribers"}]
        self.assertFalse(valid(r))
        r = fixture_record(); r["payload"]["destinations"][0]["outcome"] = "delivered"
        self.assertFalse(valid(r))

    def test_a_fixture_record_must_name_its_authorisation_and_destinations(self):
        r = fixture_record(); del r["payload"]["fixture"]
        self.assertFalse(valid(r))
        r = fixture_record(); del r["payload"]["destinations"]
        self.assertFalse(valid(r))
        r = fixture_record(); r["payload"]["fixture"]["authorisation_id"] = "OFFER-F2"
        self.assertFalse(valid(r))
        r = fixture_record(); r["classification"] = "SIMULATED"
        self.assertFalse(valid(r))


# ------------------------------------------------------------ gate isolation --
class GateIsolation(unittest.TestCase):
    """A self-contained temp repository, so the real logs are never touched."""

    def setUp(self):
        self.root = tempfile.mkdtemp(prefix="sf1-")
        os.makedirs(os.path.join(self.root, ".claude", "skills", "sector-handoff-packet"))
        shutil.copy(SKILL_MD, os.path.join(self.root, ".claude", "skills", "sector-handoff-packet", "SKILL.md"))
        os.makedirs(os.path.join(self.root, "01_Sector", "fixtures"))
        os.makedirs(os.path.join(self.root, "01_Sector", "_memory"))
        shutil.copy(os.path.join(ROOT, RECORD_REL), os.path.join(self.root, RECORD_REL))
        self.write_packet({f: "x" for f in gate.PACKET_FIELDS} | {"classification": "TEST_FIXTURE"})
        self.log = os.path.join(self.root, "01_Sector", "_memory", "skill_runs.jsonl")
        self.fxlog = os.path.join(self.root, "01_Sector", "_memory", "skill_runs-sandbox.jsonl")
        self.write(self.log, [ordinary_record()])
        self.set_status("approved")

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def write(self, path, recs):
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("".join(json.dumps(r) + "\n" for r in recs))

    def write_packet(self, obj):
        with io.open(os.path.join(self.root, PACKET_REL), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(obj))

    def set_status(self, status, **over):
        reg = json.loads(rd(REGISTRY))
        reg["authorisations"][0]["status"] = status
        reg["authorisations"][0].update(over)
        self.reg = os.path.join(self.root, "reg.json")
        with io.open(self.reg, "w", encoding="utf-8") as fh:
            json.dump(reg, fh)

    def run_gate(self):
        lines = []
        rc = gate.main(log=self.log, fixture_log=self.fxlog, auths_path=self.reg, root=self.root, out=lines.append)
        return rc, "\n".join(lines)

    def test_clean_state_passes(self):
        self.assertEqual(self.run_gate()[0], 0)

    def test_an_approved_well_formed_fixture_run_passes(self):
        self.write(self.fxlog, [fixture_record()])
        rc, out = self.run_gate()
        self.assertEqual(rc, 0, out)

    def test_a_marked_record_in_the_real_log_fails(self):
        self.write(self.log, [ordinary_record(), fixture_record("s10-fx-leaked")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("MARKED RECORD IN THE REAL LOG", out)

    def test_an_unmarked_record_in_the_fixture_log_fails(self):
        self.write(self.fxlog, [ordinary_record("s10-unmarked")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("UNMARKED record in the fixture log", out)

    def test_a_fixture_record_under_a_draft_authorisation_fails(self):
        self.set_status("draft")
        self.write(self.fxlog, [fixture_record()])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("DRAFT authorisation", out)

    def test_the_one_record_limit_is_enforced(self):
        self.write(self.fxlog, [fixture_record("a"), fixture_record("b", "2026-01-01T00:00:01Z")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("exceeds SECTOR-SF1's limit", out)

    def test_a001_is_refused_in_a_fixture_record(self):
        r = fixture_record(); r["payload"]["decision_reason"] = "used A001-P07"
        self.write(self.fxlog, [r])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("A001 D6", out)

    def test_the_packet_must_exist_be_marked_and_carry_aeit09_fields(self):
        self.write(self.fxlog, [fixture_record()])
        self.write_packet({"classification": "TEST_FIXTURE", "handoff_id": "x"})
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("lacks AEIT_09", out)
        os.remove(os.path.join(self.root, PACKET_REL))
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("does not exist", out)

    def test_a_changed_synthetic_record_fails_its_pin(self):
        p = os.path.join(self.root, RECORD_REL)
        with io.open(p, "ab") as fh:
            fh.write(b" ")
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("does not match its pinned sha256", out)

    def test_execution_ids_are_unique_across_both_logs(self):
        self.write(self.fxlog, [fixture_record("s10-ordinary-1")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("already used in the other log", out)

    def test_a_future_dated_fixture_record_fails(self):
        self.write(self.fxlog, [fixture_record(ts="2999-01-01T00:00:00Z")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("FUTURE-DATED", out)


    def test_a_spent_authorisation_admits_no_second_record(self):
        self.set_status("spent")
        self.write(self.fxlog, [fixture_record("a"), fixture_record("b", "2026-01-01T00:00:01Z")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("exceeds SECTOR-SF1's limit", out)


# ------------------------------------------------------- the real spent state --
# Until 2026-09-22 this class was PreparedStateIsDisabled and asserted the pre-run state
# (SF1 draft, no artifacts). SECTOR-SF1 was then enacted, its ONE attempt made and the
# authorisation SPENT (SECTOR_OS.md section 8). These tests pin what that attempt left.
SANDBOX_LOG_SHA = "4670109698ba328ade36489b251e0394eaf012b6e9711d5123f2e0f0e09ad9f5"
PACKET_SHA = "7554729f114d737dc4f365847dd336c0606e9fbc776d5e339a94671acb2f1798"
SF1_EXECUTION_ID = "s10-2026-09-22-sector-sf1-syn-s10-01-fixture-1"


class SpentState(unittest.TestCase):
    def test_sf1_is_spent_and_nothing_is_approved(self):
        reg = json.loads(rd(REGISTRY))["authorisations"]
        self.assertEqual([(a["id"], a["status"]) for a in reg], [("SECTOR-SF1", "spent")])
        self.assertFalse(any(a["status"] == "approved" for a in reg))
        self.assertIn(SF1_EXECUTION_ID, reg[0]["spent"])

    def test_the_one_attempt_left_exactly_its_two_artifacts_unaltered(self):
        self.assertEqual(hashlib.sha256(rd(SANDBOX_LOG, "rb")).hexdigest(), SANDBOX_LOG_SHA,
                         "the fixture log changed - it is append-only and SF1 admits one record")
        self.assertEqual(hashlib.sha256(rd(os.path.join(ROOT, PACKET_REL), "rb")).hexdigest(), PACKET_SHA)
        self.assertEqual(len([l for l in rd(SANDBOX_LOG).splitlines() if l.strip()]), 1)

    def test_the_fixture_record_is_marked_isolated_and_delivers_nothing(self):
        r = json.loads(rd(SANDBOX_LOG))
        V.validate(r)
        self.assertEqual(r["classification"], "TEST_FIXTURE")
        self.assertEqual(r["payload"]["execution_id"], SF1_EXECUTION_ID)
        self.assertEqual((r["payload"]["writes"], r["payload"]["events"], r["payload"]["decision"]), ([], [], "NO_OP"))
        self.assertEqual([(d["destination"], d["outcome"]) for d in r["payload"]["destinations"]],
                         [(d, o) for d, _, o in DESTS])

    def test_the_real_log_holds_no_fixture_record(self):
        for line in rd(REAL_LOG).splitlines():
            if line.strip():
                self.assertNotIn("classification", json.loads(line))
                self.assertNotEqual(json.loads(line)["payload"]["execution_id"], SF1_EXECUTION_ID)

    def test_the_real_gate_passes(self):
        self.assertEqual(gate.main(out=lambda *_: None), 0)


# ------------------------------------------------------ the synthetic record --
class SyntheticRecord(unittest.TestCase):
    """Every rule result the record states is recomputed from the repository's sources."""

    @classmethod
    def setUpClass(cls):
        cls.raw = rd(os.path.join(ROOT, RECORD_REL), "rb")
        cls.rec = json.loads(cls.raw.decode("utf-8"))
        cls.cfg = json.loads(rd(os.path.join(ROOT, "01_Sector", "sector_plugins", "hospitality",
                                             "plugin.config.json")))
        cls.packet = rd(os.path.join(ROOT, "02_Offer", "Hospitality Revenue Content OS - Full Push "
                                          "Readiness Packet.md"))
        cls.offer = rd(os.path.join(ROOT, "02_Offer", "OFFER_OS.md"))

    def attr(self, k):
        return self.rec["attributes"][k]["value"]

    def recomputed(self):
        icp = [l for l in self.offer.replace("\r\n", "\n").split("\n") if l.startswith("| **ICP** |")]
        self.assertEqual(len(icp), 1, "the OFFER_OS section 3 ICP row the anti-ICP rules cite is missing")
        self.assertIn("no website", icp[0]); self.assertIn("central brand.com", icp[0])
        mvp = "**H1 30–60 · H2 61–120** are the MVP scope" in self.packet
        self.assertTrue(mvp, "the readiness packet OI6 MVP-scope rule is missing")
        tier1 = self.cfg["P2"]["property_type_rule"]["tier1_scope"]["archetypes"]
        db16 = self.cfg["P5"]["proposed_assignments"].get(self.attr("destination"), {}).get("db16")
        return {
            "R-ARCHETYPE": "pass" if self.attr("archetype") in tier1 else "fail",
            "R-DESTINATION": "pass" if db16 == "profiled" else "fail",
            "R-SIZE-BAND": "pass" if self.attr("size_band") in ("H1", "H2") else "fail",
            "R-ANTI-ICP-WEB": "not_fired" if (self.attr("website") == "present"
                                              and self.attr("direct_booking_path") == "present") else "fired",
            "R-ANTI-ICP-GROUP": "not_fired" if (self.attr("group_or_chain") == "none"
                                                and self.attr("archetype") != "Hospitality Group") else "fired",
        }

    def test_every_stated_rule_result_is_recomputed_from_sources(self):
        calc = self.recomputed()
        stated = {c["id"]: c["result"] for c in self.rec["rule_checks"]}
        self.assertEqual(stated, calc)
        self.assertEqual(self.rec["stop_rules_fired"], [])

    def test_it_is_labelled_synthetic_and_independent(self):
        self.assertEqual(self.rec["classification"], "TEST_FIXTURE")
        self.assertIs(self.rec["synthetic"], True)
        self.assertEqual(self.rec["unit_id"], "SYN-S10-01")
        self.assertIn("SIMULATED_VERDICT", self.rec["verdict_label"])
        self.assertNotIn("seed_brief", self.rec, "an S10 input is a Sector record, not an Offer seed")
        for v in self.rec["attributes"].values():
            self.assertTrue(v["status"].startswith("SYNTHETIC"))

    def test_it_carries_no_a001_pilot_id_or_figure(self):
        t = self.raw.decode("utf-8")
        self.assertIsNone(re.search(r"\bA001\b", t))
        self.assertIsNone(re.search(r"PILOT-H-\d", t))
        self.assertIsNone(re.search(r"[$€£%]|\b(?:USD|KES|KSh)\b|\d+\s*rooms?", t))
        for k, v in self.rec["attributes"].items():
            if k != "size_band":
                self.assertIsNone(re.search(r"\d", v["value"]), k)

    def test_it_matches_the_pin_the_owner_would_approve(self):
        reg = json.loads(rd(REGISTRY))["authorisations"][0]
        self.assertEqual(hashlib.sha256(self.raw).hexdigest(), reg["synthetic_record_sha256"])


if __name__ == "__main__":
    unittest.main()
