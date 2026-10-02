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
# Re-baselined again 2026-09-22: the CRM note called `ICP Fit Score` Sales-set, repeating a line
# that AEIT_05 R1 (ratified 2026-07-22) supersedes - Sector sets it, Sales consumes. The note now
# says it is a score, not a tier, and no substitute for icp_tier.
# Was 4b854d4c633b5f5b27e3d300dc47fe009eeb5dfa782fd444184320393159b69f (2026-09-22, mid-day).
# Re-baselined 2026-09-29: the four Lead tag fields were created and verified, so the CRM row moves
# from "no target" to CONNECTED - while still reporting HANDOFF_FAILURE until SECTOR-CW2 passes.
# Was 9a25200ab4fb2c8f0b2416cdb9134c86fde365c9c50e9989646209ba82ee1ed2 (2026-09-22, evening).
# Re-baselined 2026-09-29 after SECTOR-CW2: the CRM row now records that a direct connector write
# round-tripped, while S10 itself has still never written a tag - so a run must read its own write
# back before recording anything but HANDOFF_FAILURE.
# Was 55d6d868c2a8bc51b430db395e4ff18a7999f5772071754126407e68afa927f2 (2026-09-29, earlier).
# Re-baselined 2026-09-29 after SECTOR-SF2: the CRM row now records that S10 itself wrote, read
# back and deleted one disposable fixture task - while no real Lead has ever been tagged.
# Was a30d91d57428d7bcbddaad8b47fba071fd3387d329fd45e6efd63083247f7c4d (2026-09-29, post-CW2).
# Re-baselined 2026-10-02 by DB9-PROV-1 (owner-approved): Step 4 gained the COMPUTED fail-closed
# floors. `confidence_threshold` is UNRESOLVED whenever any contributing item's Confidence is null
# (null is weaker than Low, never equal to it); otherwise it is the weakest value on
# Low < Medium < High. `freshness_requirement` takes the earliest non-null `Next Review` and states
# the oldest non-null `Last Verified` beside it, is UNRESOLVED when any date is absent, and may
# never substitute the assembly date. The live DB 9 field name is `Next Review`, not DB7/DB14's
# `Next Verification`. Before this, neither floor could be expressed for the audience element at
# all, because DB 9 carried no provenance in-schema - so S10 now reports UNRESOLVED on an
# Accommodation packet where it previously expressed nothing. That is stricter, not a regression.
# Was 337a0ba7d9acfdb790ef01059e896c1a84d135df785f77258c57b51ef49ee07a (2026-09-29, post-SF2).
S10_ORDINARY_SHA = "7acd495e29fbd73c9aaf32db75b838402349d55388123a2de0903ebd9942d581"

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
# One line per spent authorisation, pinned individually so a later fixture can append without
# breaking the pins - and so a rewrite of an earlier line is caught.
SF1_LINE_SHA = "4670109698ba328ade36489b251e0394eaf012b6e9711d5123f2e0f0e09ad9f5"
SF2_LINE_SHA = "5a3f639de2ea211c727da65c2602f011999bb23fbf987403469611223976d565"
PACKET_SHA = "7554729f114d737dc4f365847dd336c0606e9fbc776d5e339a94671acb2f1798"
SF2_PACKET_SHA = "a4e0ff7ce334dcf4fc4c834821ce1e4322be484e313628aa741e2f179c6bb673"
SF1_EXECUTION_ID = "s10-2026-09-22-sector-sf1-syn-s10-01-fixture-1"
SF2_EXECUTION_ID = "s10-2026-09-29-sector-sf2-syn-s10-01-crm-tag-1"


class SpentState(unittest.TestCase):
    def test_both_authorisations_are_spent_and_nothing_is_approved(self):
        reg = json.loads(rd(REGISTRY))["authorisations"]
        self.assertEqual([(a["id"], a["status"]) for a in reg],
                         [("SECTOR-SF1", "spent"), ("SECTOR-SF2", "spent")])
        self.assertFalse(any(a["status"] == "approved" for a in reg), "nothing may sit approved")
        self.assertIn(SF1_EXECUTION_ID, reg[0]["spent"])

    def test_sf1s_own_artifacts_are_unaltered_by_the_later_run(self):
        self.assertEqual(hashlib.sha256(rd(os.path.join(ROOT, PACKET_REL), "rb")).hexdigest(), PACKET_SHA,
                         "SF1's packet must survive every later fixture untouched")
        lines = [l for l in rd(SANDBOX_LOG, "rb").splitlines(keepends=True) if l.strip()]
        self.assertEqual(len(lines), 2, "one record per spent authorisation, appended in order")
        self.assertEqual(hashlib.sha256(lines[0]).hexdigest(), SF1_LINE_SHA,
                         "SF1's record changed - the fixture log is append-only")

    def test_the_fixture_record_is_marked_isolated_and_delivers_nothing(self):
        r = json.loads(rd(SANDBOX_LOG, "rb").splitlines(keepends=True)[0])  # SF1's own line
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


# --------------------------------------------------- SECTOR-SF2: prepared, NOT enacted --
# SF2 would have S10 exercise the CRM tag write itself: one disposable ClickUp task, tagged,
# read back, deleted. These tests pin the prepared mechanism while it is still a draft.
SF2_PACKET_REL = "01_Sector/fixtures/SYN-S10-01.s10-packet-sf2.json"


def sf2_record(eid="s10-sf2-test-1", ts="2026-01-01T00:00:00Z", verified=True, crm="delivered_fixture_verified"):
    r = fixture_record(eid, ts)
    r["payload"]["fixture"] = {
        "authorisation_id": "SECTOR-SF2", "synthetic_record": RECORD_REL, "packet": SF2_PACKET_REL,
        "not_read_fixture": ["DB3", "DB4", "DB6", "DB7", "DB8", "DB9", "DB10", "DB15", "DB16"],
    }
    if verified:
        r["payload"]["fixture"]["external_writes"] = [
            "ClickUp: one disposable task 'TEST_FIXTURE SECTOR-SF2 S10 CRM TAG' created, tagged, "
            "read back, deleted, absence confirmed"]
        r["payload"]["fixture"]["readback_verified"] = True
    r["payload"]["destinations"] = [dict(d) for d in r["payload"]["destinations"]]
    for d in r["payload"]["destinations"]:
        if d["destination"] == "ClickUp CRM":
            d["outcome"] = crm
    return r


class SF2Spent(unittest.TestCase):
    """SF2 ran once on 2026-09-29: S10 wrote the CRM tags itself, read them back and cleaned up."""

    def test_the_authorisation_is_spent_distinct_and_admits_nothing_further(self):
        reg = {a["id"]: a for a in json.loads(rd(REGISTRY))["authorisations"]}
        a = reg["SECTOR-SF2"]
        self.assertEqual(a["status"], "spent", "SF2 was one attempt; it must not sit re-usable")
        self.assertIn(SF2_EXECUTION_ID, a["spent"])
        self.assertEqual(a["max_records"], 1)
        self.assertEqual((a["skill"], a["skill_id"]), ("sector-handoff-packet", "S10"))
        self.assertNotEqual(a["packet"], reg["SECTOR-SF1"]["packet"], "SF2 has its own packet path")
        self.assertEqual(a["synthetic_record_sha256"], reg["SECTOR-SF1"]["synthetic_record_sha256"],
                         "both authorisations pin the same reviewed input")

    def test_the_pinned_input_is_the_one_the_owner_reviewed(self):
        self.assertEqual(hashlib.sha256(rd(os.path.join(ROOT, RECORD_REL), "rb")).hexdigest(),
                         "8247eefd3b84d1f4a64f385637eabb2dc617b1b76a43c2466a1b99ae7e62d94f")

    def test_the_run_left_exactly_its_two_artifacts(self):
        self.assertEqual(hashlib.sha256(rd(os.path.join(ROOT, SF2_PACKET_REL), "rb")).hexdigest(),
                         SF2_PACKET_SHA)
        line = rd(SANDBOX_LOG, "rb").splitlines(keepends=True)[1]
        self.assertEqual(hashlib.sha256(line).hexdigest(), SF2_LINE_SHA)

    def test_the_record_claims_a_verified_write_and_earns_it(self):
        r = json.loads(rd(SANDBOX_LOG, "rb").splitlines(keepends=True)[1])
        V.validate(r)
        self.assertEqual(r["classification"], "TEST_FIXTURE")
        self.assertEqual(r["payload"]["execution_id"], SF2_EXECUTION_ID)
        self.assertEqual((r["payload"]["writes"], r["payload"]["events"], r["payload"]["decision"]),
                         ([], [], "NO_OP"), "a fixture writes no Notion database and emits no event")
        crm = [d for d in r["payload"]["destinations"] if d["destination"] == "ClickUp CRM"][0]
        self.assertEqual(crm["outcome"], "delivered_fixture_verified")
        self.assertIs(r["payload"]["fixture"]["readback_verified"], True)
        self.assertTrue(r["payload"]["fixture"]["external_writes"])
        self.assertNotIn("delivered", [d["outcome"] for d in r["payload"]["destinations"]],
                         "a fixture may never claim a real delivery")

    def test_the_tag_values_written_were_explicit_fixtures(self):
        p = json.loads(rd(os.path.join(ROOT, SF2_PACKET_REL)))
        tags = p["payload"]["crm_tags_written"]
        self.assertEqual(tags, p["payload"]["crm_tags_read_back"], "written and read-back must match")
        self.assertTrue(tags["sector"].startswith("TEST_FIXTURE"))
        self.assertTrue(tags["sub_sector"].startswith("TEST_FIXTURE"))
        self.assertTrue(tags["offer_id"].startswith("TEST_FIXTURE"))
        self.assertEqual(tags["icp_tier"], "Out-of-scope",
                         "the only approved option that asserts nothing about a real company")
        self.assertIsNone(p["payload"]["fit_verdict"])

    # ---- schema: the new outcome is fixture-only, and `delivered` stays impossible ----
    def test_the_verified_outcome_is_valid_on_a_fixture_record(self):
        self.assertTrue(valid(sf2_record()))

    def test_a_fixture_record_still_cannot_claim_plain_delivered(self):
        self.assertFalse(valid(sf2_record(crm="delivered")))

    def test_an_ordinary_record_cannot_claim_the_verified_outcome(self):
        r = ordinary_record()
        r["payload"]["destinations"] = [{"destination": "ClickUp CRM", "mechanism": "tags",
                                         "outcome": "delivered_fixture_verified"}]
        self.assertFalse(valid(r), "delivered_fixture_verified is fixture-only")

    def test_ordinary_records_are_unaffected_by_the_extension(self):
        n = 0
        for line in rd(REAL_LOG).splitlines():
            if line.strip():
                V.validate(json.loads(line)); n += 1
        self.assertGreaterEqual(n, 15)
        r = ordinary_record()
        r["payload"]["destinations"] = [{"destination": "Offer (02)", "mechanism": "text", "outcome": "delivered"}]
        self.assertTrue(valid(r), "an ordinary run may still record a real delivery")


class SF2GateRules(GateIsolation):
    """Same temp-repo harness; the registry copy is re-pointed at SF2."""

    def use_sf2(self, status):
        reg = json.loads(rd(REGISTRY))
        for a in reg["authorisations"]:
            if a["id"] == "SECTOR-SF2":
                a["status"] = status
        reg["authorisations"] = [a for a in reg["authorisations"] if a["id"] == "SECTOR-SF2"]
        self.reg = os.path.join(self.root, "reg-sf2.json")
        with io.open(self.reg, "w", encoding="utf-8") as fh:
            json.dump(reg, fh)
        shutil.copy(os.path.join(self.root, PACKET_REL), os.path.join(self.root, SF2_PACKET_REL))

    def test_a_draft_sf2_admits_nothing(self):
        self.use_sf2("draft")
        self.write(self.fxlog, [sf2_record()])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("DRAFT authorisation", out)

    def test_an_approved_sf2_run_passes(self):
        self.use_sf2("approved")
        self.write(self.fxlog, [sf2_record()])
        rc, out = self.run_gate()
        self.assertEqual(rc, 0, out)

    def test_a_spent_sf2_admits_no_second_record(self):
        self.use_sf2("spent")
        self.write(self.fxlog, [sf2_record("a"), sf2_record("b", "2026-01-01T00:00:01Z")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("exceeds SECTOR-SF2's limit", out)

    def test_the_verified_outcome_requires_a_recorded_readback(self):
        self.use_sf2("approved")
        self.write(self.fxlog, [sf2_record(verified=False)])
        rc, out = self.run_gate()
        self.assertEqual(rc, 1); self.assertIn("without a recorded read-back", out)

    def test_an_unverified_run_may_still_report_a_failure_honestly(self):
        self.use_sf2("approved")
        self.write(self.fxlog, [sf2_record(verified=False, crm="HANDOFF_FAILURE")])
        rc, out = self.run_gate()
        self.assertEqual(rc, 0, out)


class SF1RecordIsPreserved(unittest.TestCase):
    """SF1's line must survive SF2 byte-for-byte - the fixture log is append-only too."""
    # The whole-file pin above holds only until SF2 appends; this one holds afterwards too.
    SF1_LINE_SHA = "4670109698ba328ade36489b251e0394eaf012b6e9711d5123f2e0f0e09ad9f5"

    def test_the_first_line_is_sf1_and_is_byte_identical(self):
        first = rd(SANDBOX_LOG, "rb").splitlines(keepends=True)[0]
        self.assertEqual(hashlib.sha256(first).hexdigest(), self.SF1_LINE_SHA,
                         "SF1's record changed - the fixture log is append-only")
        self.assertEqual(json.loads(first)["payload"]["fixture"]["authorisation_id"], "SECTOR-SF1")


if __name__ == "__main__":
    unittest.main()
