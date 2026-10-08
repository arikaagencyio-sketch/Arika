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
# Re-baselined 2026-10-02 by DB6-DB10-PROV-1 Step 1 (owner-approved): Step 4's EXPLANATION of why
# the floors resolve to UNRESOLVED was corrected. The rules themselves are UNCHANGED - the computed
# floors, the ordering, the null-is-weaker-than-Low rule and the assembly-date ban all stand exactly
# as DB9-PROV-1 wrote them. What changed is that the text had blamed the UNRESOLVED result on DB 9
# alone, when THREE elements contribute: DB 9 (null on both), DB 10 (null on both, all 57 rows), and
# DB 6 - which carries a POPULATED `Confidence` of Medium beside an EMPTY `Source`. Step 4 now names
# all three, states that `Evidence` is absent from DB 6 and DB 10, records that the multi-source
# `Source Tier`/`Source URL` mapping is undefined (OD2), and says plainly that null AND unsupported
# both fail closed. Rule V3 is deliberately NOT extended to DB 6 and its four values are NOT
# cleared (OD1). Naming one cause of three would have let a reader think fixing DB 9 clears the
# floor. Stricter and more honest, not a behaviour change.
# Was 7acd495e29fbd73c9aaf32db75b838402349d55388123a2de0903ebd9942d581 (2026-10-02, post-DB9-PROV-1).
# Re-baselined 2026-10-02 by DB6-DB10-PROV-1 Step 2 (owner-approved, and the approval names this
# re-baseline explicitly). Step 2 added `Evidence` live to DB 6 and DB 10, so Step 4's bullet 2 had
# to stop saying the field is absent. It now states: Evidence exists STRUCTURALLY in DB 6, DB 9 and
# DB 10; every one of its row values is NULL; a null Evidence STILL forces an UNRESOLVED provenance
# floor; and no confidence or freshness value may be inferred from the fact that a field exists.
# A column is a place to put evidence, not evidence. The computed floors, the Low < Medium < High
# ordering, the null-is-weaker-than-Low rule, the assembly-date ban and the three-element table are
# all UNCHANGED. Rule V3 is still NOT extended to DB 6 and its four Confidence values are still not
# cleared (OD1 open). Closing the schema gap closed nothing about the rows - which is exactly why
# this wording change is a tightening and not a relaxation.
# Was f4ac696f182e3762621bcd1b01bf4daf768eb6f48550209feb2654c51a23e3c9 (2026-10-02, post-Step 1).
# Re-baselined 2026-10-02 by DB6-OD1-OD2-1 (owner-approved; the approval names this re-baseline
# and elected to fix the S10 gap in the same task). This change TIGHTENS the freshness floor:
# `freshness_requirement` now returns UNRESOLVED if any contributing record has EITHER a null
# `Last Verified` OR a null `Next Review`, naming each unresolved element, and only computes the
# earliest/oldest pair when every record has BOTH dates. Before this, the rule failed closed on a
# missing `Last Verified` but said nothing about a missing `Next Review` - so a row without one
# would have silently inherited the EARLIEST non-null date from its siblings, which is the exact
# substitution the rule exists to prevent. It became reachable the moment DB 6's dates were partly
# populated. Also updated, all three factual rather than behavioural: the contributing-element
# table now carries a `Next Review` column and DB 6's post-backfill state; bullet 1 records that
# three DB 6 rows are sourced and the Buyer row alone is EXCEPTED (and that an excepted row must
# never be reported as a sourced one); bullet 3 records the DB6-LOCAL multi-source convention with
# its boundary - not ratified for DB 9 or DB 10, and barred from DB 9 whose V4 still requires a
# tier whenever a source is set. The computed floors, the Low < Medium < High ordering, the
# null-is-weaker-than-Low rule and the assembly-date ban are UNCHANGED.
# Was e741c19e6d580dc4f8c91693ac2835047ee67de555a3617f275746201ab348b8 (2026-10-02, post-Step 2).
# Re-baselined 2026-10-02 by DB3-PROV-1 Step A (owner-approved; the approval names this
# re-baseline). Step 4 gained DB 3 as the FOURTH contributing provenance element. It had been
# missing from the computed-floor table while Step 4's own prose named findings as a confidence
# contributor - "A finding at `Confidence = Low` ... caps the packet" - so the table listed three
# of four. That is the same class of omission Step 1 corrected when the table named DB 9 alone,
# reproduced at smaller scale. What Step 4 now states about DB 3: its Confidence contributes
# normally (all 217 rows governed, all six Target rows Medium); `Evidence` is REQUIRED and
# populated 217/217, with five of six Target rows naming re-followable sources inline and one not;
# `Source` is a PROCESS-KIND dimension - xlsx/chat/agent run/research - and must NEVER be read as
# the authority or taken to mean a row is unsourced; its freshness contribution is UNRESOLVED
# because `Last Verified` and `Next Review` DO NOT EXIST AS FIELDS, which is a different fact from
# an empty cell - both fail closed but only an empty cell can ever be filled; no assembly date,
# current date or `Freshness` label may substitute, because `Freshness` is `Fresh` on all 217 rows
# with no threshold defined and so cannot age; payload restrictions recorded only in page bodies
# can be lost if S10 reads properties alone; and NO claim is made about the three unaudited
# High-confidence rows. The computed floors, the Low < Medium < High ordering, the
# null-is-weaker-than-Low rule, the assembly-date ban and the DB6 null-Next-Review clause are all
# UNCHANGED. DB 3 is now the binding constraint on the freshness floor, because no backfill can
# fix a field that does not exist.
# Was 8397e683ab1390c6c32c085a9fbf9f1fb1b1fe9c43f1b200ce2d7dbae6355c89 (2026-10-02, post-OD1/OD2).
# Was 52506b25793b937031ac2e3df0dcb3b5c37f11bf1ffac68765d220c49216e81c (2026-10-02, post-DB3 Step A).
# Re-baselined 2026-10-02 by DB3-OD10-OD12-1 (owner-approved; the approval names the S10
# Step 4 synchronisation). THE PRECEDING PARAGRAPH IS NOW PARTLY SUPERSEDED, and is kept
# because it is the reason this change was made: it recorded that DB 3's freshness
# contribution was UNRESOLVED because `Last Verified` and `Next Review` DO NOT EXIST AS
# FIELDS. Under OD10 Option D both were added to live DB 3 as nullable dates, so Step 4 no
# longer says that. What Step 4 now states: both fields EXIST and are NULL ON ALL 217 ROWS,
# so the freshness floor is UNRESOLVED **emptily rather than structurally**; THREE states are
# distinguished, not two - absent, present-but-null, and present-and-populated - because only
# the middle one can ever be filled; `Freshness` is NON-GOVERNING as of OD10 Option D and must
# never be read as a temporal signal, with `Last Verified` + `Next Review` governing; a row
# past a NON-NULL `Next Review` is stale and a null one is UNRESOLVED; no Fresh/Aging/Stale
# threshold exists and NONE IS NEEDED; no backfill is authorised, so nothing in DB 3 can
# supply a freshness floor today - the KIND of failure changed, not the verdict; and the three
# High-confidence rows are now CLASSIFIED (H1 HIGH_OVERSTATED, H2/H3 HIGH_UNRESOLVED, all
# three bodies blank) because the owner authorised reading them, with the earlier no-claim
# position marked SUPERSEDED rather than deleted. The computed floors, the Low < Medium < High
# ordering, the null-is-weaker-than-Low rule, the assembly-date ban and the DB6
# null-Next-Review clause are all UNCHANGED. DB 3 is NO LONGER the unfixable case: it is now
# an ordinary empty-cell element like DB 9 and DB 10.
S10_ORDINARY_SHA = "6ffdc4fc108247f1e00b034e1908c6e94c1db69aa04ed24a899156e5d198f756"

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

    def test_s10_fixture_notice_matches_the_registry(self):
        """The CLASS fix, second instance. Added 2026-10-03 by PK2-P4-PREP.

        S10's fixture-mode notice said "The only one, SECTOR-SF1, was spent on 2026-09-22" while
        the registry held TWO spent rows - SECTOR-SF2 was approved and spent on 2026-09-29. The
        operative clause ("none is approved") stayed correct, so nothing was ever wrongly
        admitted; the COUNT drifted and no test compared the sentence to the registry.

        This checks the notice against the registry instead of against a remembered sentence.
        """
        notice = rd(SKILL_MD, "rb").decode("utf-8")
        self.assertEqual(notice.count("<!-- FIXTURE-MODE:BEGIN -->"), 1)
        block = notice.split("<!-- FIXTURE-MODE:BEGIN -->", 1)[1].split("<!-- FIXTURE-MODE:END -->", 1)[0]
        # Scan the OPERATIVE notice only, split on a STABLE MACHINE-READABLE MARKER.
        #
        # This has now false-positived twice for the same reason: preserved history quotes the
        # very claim it retracts, and a scan that cannot tell history from assertion flags it.
        # The first fix split on the literal "*Corrected", which then broke the moment the note
        # was reworded on 2026-10-08 - a strip keyed to prose is itself prose-fragile.
        #
        # `<!-- NOTICE-HISTORY -->` in SKILL.md is the boundary now. It cannot drift with wording,
        # and if it is ever removed this test fails loudly rather than silently scanning history.
        # Same class as check 7c's `xlsx sheet` ban tripping on the sentence that explains it.
        MARKER = "<!-- NOTICE-HISTORY"
        self.assertIn(MARKER, block,
                      "S10's fixture notice must carry the NOTICE-HISTORY marker separating the "
                      "live notice from preserved history; without it this test cannot tell "
                      "them apart")
        operative = block.split(MARKER, 1)[0]
        auths = json.loads(rd(REGISTRY))["authorisations"]
        spent = [a["id"] for a in auths if a["status"] == "spent"]
        approved = [a["id"] for a in auths if a["status"] == "approved"]

        # every spent authorisation must be named in the notice, so the count cannot drift again
        for aid in spent:
            self.assertIn(aid, operative,
                          "%s is spent and must be named in S10's fixture notice" % aid)
        # the notice must not claim a single authorisation while several exist
        if len(spent) > 1:
            self.assertNotIn("The only one", operative,
                             "%d spent authorisations exist; the notice claims one" % len(spent))
        # the operative clause must still match the registry
        if not approved:
            self.assertIn("None is `approved`, so refuse", operative,
                          "no authorisation is approved; the notice must say so and refuse")
        else:
            self.assertNotIn("None is `approved`", operative,
                             "%s is approved; the notice must not deny it" % approved)

    def test_no_authorisation_is_currently_approved(self):
        """P4's live state, asserted rather than described.

        This is the invariant that keeps the fixture path shut: a run is admissible only while
        some row is `approved`, and none is. If a future row is approved deliberately, this test
        is the one that must be changed, which is the point - it cannot happen quietly.
        """
        auths = json.loads(rd(REGISTRY))["authorisations"]
        approved = [a["id"] for a in auths if a["status"] == "approved"]
        self.assertEqual(approved, [],
                         "no S10 fixture authorisation may ship approved; found %s" % approved)
        self.assertTrue(auths, "the registry must not be empty")
        for a in auths:
            self.assertIn(a["status"], ("draft", "spent", "approved"))

    def test_each_spent_authorisation_has_exactly_its_one_record(self):
        """A spent row is retained history. Its record count must equal its limit, so neither a
        reopened authorisation nor a deleted record can pass unnoticed."""
        auths = {a["id"]: a for a in json.loads(rd(REGISTRY))["authorisations"]}
        counts = {}
        for line in rd(SANDBOX_LOG).splitlines():
            if not line.strip():
                continue
            fx = json.loads(line)["payload"]["fixture"]
            counts[fx["authorisation_id"]] = counts.get(fx["authorisation_id"], 0) + 1
        for aid, a in auths.items():
            if a["status"] == "spent":
                self.assertEqual(counts.get(aid, 0), a.get("max_records", 1),
                                 "%s is spent: it must hold exactly its %d authorised record(s)"
                                 % (aid, a.get("max_records", 1)))
            if a["status"] == "draft":
                self.assertEqual(counts.get(aid, 0), 0,
                                 "%s is draft and must hold no record" % aid)

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
# SECTOR-SF3 enacted and spent 2026-10-08. Its attempt produced the first execution anywhere of
# S10 Step 4's four-element computed floors; both resolved UNRESOLVED, which is the designed
# answer when provenance is absent. The run was SCORED FAIL against its own section 8 checklist on
# two checks, NEITHER caused by the run - a mis-specified `Medium` confidence expectation and a
# pre-existing truth-gate defect - so these pins record a CORRECT packet from a procedurally
# failed run. See 01_Sector/PK2_P4_P5_DRY_RUN_PROPOSAL.md section 14.
SF3_LINE_SHA = "3badbd16451de02eddffae91893bbb92cf1da2a85829b0b88ad069555351ff70"
SF3_PACKET_SHA = "551a31d3e259d3d72839fa6724b95bcf7593e0d0dec7b654a2a68bd0ce28657a"
SF3_EXECUTION_ID = "s10-2026-10-08-sector-sf3-syn-s10-01-computed-floors-1"
SF3_PACKET_REL = "01_Sector/fixtures/SYN-S10-01.s10-packet-sf3.json"

# Pins keyed by authorisation id, so a new spent fixture adds a row here and nothing else.
SPENT_PINS = {
    "SECTOR-SF1": {"line": SF1_LINE_SHA, "exec": SF1_EXECUTION_ID,
                   "packet_rel": PACKET_REL, "packet": PACKET_SHA},
    "SECTOR-SF2": {"line": SF2_LINE_SHA, "exec": SF2_EXECUTION_ID,
                   "packet_rel": "01_Sector/fixtures/SYN-S10-01.s10-packet-sf2.json",
                   "packet": SF2_PACKET_SHA},
    "SECTOR-SF3": {"line": SF3_LINE_SHA, "exec": SF3_EXECUTION_ID,
                   "packet_rel": SF3_PACKET_REL, "packet": SF3_PACKET_SHA},
}


class SpentState(unittest.TestCase):
    def test_every_authorisation_is_spent_and_nothing_is_approved(self):
        """REWRITTEN 2026-10-08 after SECTOR-SF3 was enacted and spent. Not loosened.

        History of this one test is the whole argument for deriving from the registry:
          - to 2026-09-22 it asserted the pre-run state (SF1 draft, no artifacts);
          - to 2026-10-03 it asserted the exact roster [SF1 spent, SF2 spent];
          - to 2026-10-08 it asserted "the first two are spent, everything after is draft";
          - each wording was true when written and each had to be hand-edited by the next change.

        It now derives from the registry: EVERY row is either `spent` with its pinned execution
        id, or `draft` carrying `_not_enacted` and holding no record. NOTHING may be `approved` -
        that is the invariant keeping the fixture path shut, and it is the one a future enactment
        must change deliberately. A reopened spent row, a silently approved row, or a spent row
        whose pins are missing all still fail here.
        """
        reg = json.loads(rd(REGISTRY))["authorisations"]
        self.assertTrue(reg, "the registry must not be empty")
        self.assertFalse(any(a["status"] == "approved" for a in reg),
                         "nothing may sit approved: %s"
                         % [a["id"] for a in reg if a["status"] == "approved"])
        spent = [a for a in reg if a["status"] == "spent"]
        self.assertEqual([a["id"] for a in spent], sorted(SPENT_PINS),
                         "every spent authorisation must be pinned in SPENT_PINS, in order")
        for a in spent:
            self.assertIn(SPENT_PINS[a["id"]]["exec"], a["spent"],
                          "%s's spent note must name the execution id it spent" % a["id"])
        for a in reg:
            if a["status"] == "draft":
                self.assertIn("_not_enacted", a,
                              "%s is draft and must carry the _not_enacted marker" % a["id"])
            else:
                self.assertEqual(a["status"], "spent",
                                 "%s: only draft or spent may ship" % a["id"])

    def test_a_draft_row_holds_no_record_and_pins_its_inputs(self):
        """A draft row must be inert AND fully specified, so approving it adds no new decision."""
        reg = json.loads(rd(REGISTRY))["authorisations"]
        drafts = [a for a in reg if a["status"] == "draft"]
        log = rd(SANDBOX_LOG)
        for a in drafts:
            self.assertNotIn(a["id"], log, "%s is draft and must hold no record" % a["id"])
            self.assertEqual(a["skill_id"], "S10")
            self.assertTrue(a["packet"].startswith("01_Sector/fixtures/"),
                            "the packet must live under 01_Sector/fixtures/")
            self.assertEqual(a["max_records"], 1)
            rec = os.path.join(ROOT, a["synthetic_record"])
            self.assertTrue(os.path.isfile(rec), "%s names a missing record" % a["id"])
            self.assertEqual(hashlib.sha256(rd(rec, "rb")).hexdigest(),
                             a["synthetic_record_sha256"],
                             "%s's pinned hash must match the file on disk" % a["id"])

    def test_every_spent_fixtures_artifacts_are_byte_unaltered(self):
        """REWRITTEN 2026-10-08. The hard-coded `len(lines) == 2` is gone.

        That count was the fragile part: it had to be edited the moment SECTOR-SF3 appended its
        authorised record, and the failure it produced said nothing about whether an EARLIER line
        had been tampered with - which is the thing that actually matters in an append-only log.

        The line count is now DERIVED: it must equal the sum of `max_records` over the spent
        authorisations. Every spent fixture's line AND packet is pinned individually, so an
        authorised append passes while any rewrite of an earlier line or packet fails.
        """
        reg = json.loads(rd(REGISTRY))["authorisations"]
        spent = [a for a in reg if a["status"] == "spent"]
        expected = sum(a.get("max_records", 1) for a in spent)
        lines = [l for l in rd(SANDBOX_LOG, "rb").splitlines(keepends=True) if l.strip()]
        self.assertEqual(len(lines), expected,
                         "the log must hold exactly one record per spent authorisation "
                         "(derived from the registry: %d), found %d" % (expected, len(lines)))
        for i, a in enumerate(spent):
            pin = SPENT_PINS[a["id"]]
            self.assertEqual(hashlib.sha256(lines[i]).hexdigest(), pin["line"],
                             "%s's record changed - the fixture log is append-only" % a["id"])
            self.assertEqual(
                hashlib.sha256(rd(os.path.join(ROOT, pin["packet_rel"]), "rb")).hexdigest(),
                pin["packet"],
                "%s's packet must survive every later fixture untouched" % a["id"])

    def test_no_log_line_is_unapproved_or_unexplained(self):
        """Strict detection, kept and tightened. Added 2026-10-08.

        Every line must name an authorisation that EXISTS and is non-draft, and every spent
        authorisation must be accounted for by a line. An orphan record, a record under a draft,
        and a spent row whose record vanished are three different defects and all three fail.
        """
        reg = {a["id"]: a for a in json.loads(rd(REGISTRY))["authorisations"]}
        seen = {}
        for i, line in enumerate(rd(SANDBOX_LOG).splitlines(), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            self.assertEqual(r.get("classification"), "TEST_FIXTURE",
                             "line %d in the fixture log is unmarked" % i)
            aid = r["payload"]["fixture"]["authorisation_id"]
            self.assertIn(aid, reg, "line %d names unknown authorisation %r" % (i, aid))
            self.assertNotEqual(reg[aid]["status"], "draft",
                                "line %d was written under DRAFT %s" % (i, aid))
            self.assertEqual(r["payload"]["fixture"]["packet"], reg[aid]["packet"],
                             "line %d's packet differs from %s's" % (i, aid))
            seen[aid] = seen.get(aid, 0) + 1
            self.assertLessEqual(seen[aid], reg[aid].get("max_records", 1),
                                 "%s exceeds its record limit" % aid)
        for aid, a in reg.items():
            if a["status"] == "spent":
                self.assertEqual(seen.get(aid, 0), a.get("max_records", 1),
                                 "%s is spent but its record is missing" % aid)
            if a["status"] == "draft":
                self.assertEqual(seen.get(aid, 0), 0, "%s is draft and must hold no record" % aid)

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
