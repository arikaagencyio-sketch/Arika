# -*- coding: utf-8 -*-
"""SECTOR-DELIVERY-P10 - focused offline tests for the Offer (02) inbox receiver.

EVERY test works in a TEMPORARY directory created outside the repository, outside OneDrive and
outside every git working tree. No test touches the real SYNCO-01 or SYNCO-02 sandbox, and the suite
asserts that by hashing both sandboxes before and after the whole run. No test makes a network
attempt - the receiver imports nothing that could.

    python 00_Agency_Governance/offline_guard/run_offline.py -- \
        python -m unittest discover -s 01_Sector/delivery -p "test_offer_inbox_receiver.py"
"""
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile
import threading
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import offer_inbox_receiver as rx  # noqa: E402

SYNCO1 = r"C:\Users\USER\Arika_Sandboxes\SYNCO-01"
SYNCO2 = r"C:\Users\USER\Arika_Sandboxes\SYNCO-02"


def tree_hash(root):
    """A stable digest of every file under `root`, for the untouched-sandbox proof."""
    if not os.path.isdir(root):
        return "ABSENT"
    acc = hashlib.sha256()
    for base, dirs, files in os.walk(root):
        dirs.sort()
        for name in sorted(files):
            p = os.path.join(base, name)
            acc.update(os.path.relpath(p, root).replace("\\", "/").encode("utf-8"))
            with io.open(p, "rb") as fh:
                acc.update(hashlib.sha256(fh.read()).digest())
    return acc.hexdigest()


SANDBOX_BEFORE = {"SYNCO-01": tree_hash(SYNCO1), "SYNCO-02": tree_hash(SYNCO2)}

GOOD_PACKET = {
    "classification": "TEST_FIXTURE",
    "_marker": "TEST_FIXTURE - NOT REAL - NOT EVIDENCE",
    "handoff_id": "sector->offer:test",
    "producer": "Sector (01)",
    "consumer": "Offer (02)",
    "confidence_threshold": "Medium",
    "freshness_requirement": "2026-12-01",
    "downstream_authorization": "NONE",
}


class Harness(unittest.TestCase):
    """Builds a disposable sandbox in the OS temp area and tears it down afterwards."""

    def setUp(self):
        # Deliberately NOT the repository, NOT OneDrive, NOT a SYNCO sandbox.
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="p10-test-"))
        self.sandbox = os.path.join(self.tmp, "sandbox")
        os.makedirs(self.sandbox)
        self.registry = os.path.join(self.tmp, "delivery-authorisations.json")
        self.packet = os.path.join(self.sandbox, "packet.json")
        self.write_packet(GOOD_PACKET)
        self.write_registry(status="approved")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # ---- builders -------------------------------------------------------
    def write_packet(self, obj, path=None):
        path = path or self.packet
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
        with io.open(path, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()

    def packet_hash(self):
        with io.open(self.packet, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()

    def write_registry(self, status="approved", **over):
        row = {"id": "AUTH-1", "status": status, "destination": "Offer (02)",
               "fixture_id": "TMP-FIXTURE", "delivery_id": "D1",
               "packet_path": self.packet, "packet_sha256": self.packet_hash(),
               "sandbox_root": self.sandbox, "max_deliveries": 1}
        row.update(over)
        with io.open(self.registry, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"delivery_authorisations": [row]}, indent=2) + "\n")
        return row

    def ref(self, **over):
        r = {"classification": "TEST_FIXTURE", "fixture_id": "TMP-FIXTURE", "delivery_id": "D1",
             "packet_path": self.packet, "packet_sha256": self.packet_hash(),
             "destination": "Offer (02)", "authorization_id": "AUTH-1",
             "authorization_status": "approved", "downstream_authorization": "NONE"}
        r.update(over)
        return r

    def acks(self):
        return sorted(f for f in os.listdir(self.sandbox) if f.endswith(".ack.json"))


class HappyPath(Harness):
    def test_a_valid_approved_delivery_writes_exactly_one_acknowledgement(self):
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_ACK, res.get("refusal_code"))
        self.assertEqual(self.acks(), ["D1.ack.json"], "exactly one acknowledgement")
        self.assertTrue(os.path.isfile(res["acknowledgement_path"]))

    def test_the_acknowledgement_carries_no_payload_no_url_no_contact_data(self):
        rx.receive(self.ref(), self.registry)
        with io.open(os.path.join(self.sandbox, "D1.ack.json"), encoding="utf-8") as fh:
            raw = fh.read()
        ack = json.loads(raw)
        self.assertEqual(ack["classification"], "TEST_FIXTURE")
        self.assertEqual(ack["delivery_id"], "D1")
        self.assertEqual(ack["packet_sha256"], self.packet_hash())
        self.assertIn("offer-inbox-receiver", ack["receiver"])
        self.assertIn("received_at", ack)
        self.assertEqual(ack["outcome"], rx.OUTCOME_ACK)
        self.assertIs(ack["external_write"], False)
        self.assertEqual(ack["downstream_authorization"], "NONE")
        # no packet payload leaked
        for key in ("handoff_id", "producer", "consumer", "payload", "packet"):
            self.assertNotIn(key, ack, "packet field %r leaked into the acknowledgement" % key)
        self.assertNotIn("sector->offer:test", raw, "packet content leaked")
        self.assertNotRegex(raw, r"https?://|\bwww\.")
        self.assertNotRegex(raw, r"[\w.+-]+@[\w-]+\.[\w.]+")

    def test_an_unresolved_floor_is_acknowledged_but_marked(self):
        p = dict(GOOD_PACKET, confidence_threshold="UNRESOLVED")
        self.write_packet(p)
        self.write_registry()
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_ACK_UNRESOLVED)
        with io.open(os.path.join(self.sandbox, "D1.ack.json"), encoding="utf-8") as fh:
            ack = json.loads(fh.read())
        self.assertEqual(ack["outcome"], rx.OUTCOME_ACK_UNRESOLVED,
                         "an unresolved floor must never read as a clean acknowledgement")

    def test_the_row_is_marked_spent_so_there_is_one_attempt(self):
        res = rx.receive(self.ref(), self.registry)
        self.assertTrue(res["registry_marked_spent"])
        with io.open(self.registry, encoding="utf-8") as fh:
            reg = json.loads(fh.read())
        self.assertEqual(reg["delivery_authorisations"][0]["status"], "spent")


class Idempotency(Harness):
    def test_a_second_attempt_fails_and_writes_nothing_new(self):
        first = rx.receive(self.ref(), self.registry)
        self.assertEqual(first["outcome"], rx.OUTCOME_ACK)
        with io.open(os.path.join(self.sandbox, "D1.ack.json"), encoding="utf-8") as fh:
            before = fh.read()
        self.write_registry(status="approved")       # re-approve: the ack must still stop it
        second = rx.receive(self.ref(), self.registry)
        self.assertEqual(second["outcome"], rx.OUTCOME_REFUSED)
        self.assertEqual(second["refusal_code"], "ACKNOWLEDGEMENT_EXISTS")
        self.assertEqual(self.acks(), ["D1.ack.json"])
        with io.open(os.path.join(self.sandbox, "D1.ack.json"), encoding="utf-8") as fh:
            self.assertEqual(fh.read(), before, "the first ack is untouched")

    def test_concurrent_attempts_produce_at_most_one_acknowledgement(self):
        results, lock = [], threading.Lock()
        start = threading.Event()

        def attempt():
            start.wait()
            r = rx.receive(self.ref(), self.registry)
            with lock:
                results.append(r)

        threads = [threading.Thread(target=attempt) for _ in range(8)]
        for t in threads:
            t.start()
        start.set()
        for t in threads:
            t.join()

        self.assertEqual(self.acks(), ["D1.ack.json"], "at most one acknowledgement may exist")
        won = [r for r in results if r["outcome"] in (rx.OUTCOME_ACK, rx.OUTCOME_ACK_UNRESOLVED)]
        self.assertEqual(len(won), 1, "exactly one invocation may claim the acknowledgement")
        for r in results:
            if r not in won:
                self.assertIn(r["refusal_code"], ("ACKNOWLEDGEMENT_EXISTS",
                                                  "AUTHORISATION_NOT_APPROVED"))
        with io.open(os.path.join(self.sandbox, "D1.ack.json"), encoding="utf-8") as fh:
            ack = json.loads(fh.read())
        self.assertEqual(ack["delivery_id"], "D1", "the single ack is well formed, not interleaved")


class AuthorisationFailsClosed(Harness):
    def assert_refused(self, ref, code, registry=None):
        res = rx.receive(ref, registry or self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_REFUSED, res)
        self.assertEqual(res["refusal_code"], code, res)
        self.assertEqual(self.acks(), [], "a refusal must write nothing")
        self.assertIsNone(res["acknowledgement_path"])
        return res

    def test_draft_authorisation_fails(self):
        self.write_registry(status="draft")
        self.assert_refused(self.ref(), "AUTHORISATION_NOT_APPROVED")

    def test_spent_authorisation_fails(self):
        self.write_registry(status="spent")
        self.assert_refused(self.ref(), "AUTHORISATION_NOT_APPROVED")

    def test_self_describing_claims_match_the_rows(self):
        """The CLASS fix. Added 2026-10-03 by PK2-P4-PREP.

        `_no_approved_delivery` is prose sitting beside the rows it describes. On 2026-10-02 it
        still said "and no SYNCO-02 row of any status" while SECTOR-DELIVERY-P10-D1 (fixture_id
        SYNCO-02) sat two keys above it, approved, invoked and spent the same day. The governing
        TEST had already been re-baselined for that exact reason - see
        test_no_shipped_row_is_approved_and_the_template_cannot_pass - but nothing checked the
        FILE'S OWN PROSE against its rows, so the note drifted for a day while every test passed.

        This test checks the claim against the data rather than against a remembered sentence, so
        the same class of drift fails here next time instead of being discovered by reading.
        """
        shipped = os.path.join(HERE, "delivery-authorisations.json")
        with io.open(shipped, encoding="utf-8") as fh:
            reg = json.loads(fh.read())
        rows = reg["delivery_authorisations"]
        note = reg["_no_approved_delivery"]
        approved = [r["id"] for r in rows if r["status"] == "approved"]

        # 1. the claim the note still makes must be true of the rows
        self.assertIn("no `approved` delivery row", note)
        self.assertEqual(approved, [],
                         "the note claims no approved row; found %s" % approved)

        # 2. the note must NOT re-assert the absence of any fixture row, because rows persist
        self.assertNotIn("no SYNCO-02 row", note,
                         "a spent row is retained history; the note must not deny its existence")
        for row in rows:
            fid = row.get("fixture_id", "")
            if row["status"] == "spent" and fid and not fid.startswith("<"):
                self.assertNotIn("no %s row" % fid, note,
                                 "the note denies %s, which is present and spent" % fid)

        # 3. the superseded claim must be preserved rather than deleted
        sup = reg["_no_approved_delivery_superseded_claim"]
        self.assertIn("NO SYNCO-02 ROW OF ANY STATUS", sup["was"].upper())
        self.assertIn("2026-10-02", sup["was_true_when_written"])
        self.assertIn("2026-10-02", sup["became_false_on"])
        self.assertIn("NOT WRONG", sup["verdict"].upper())
        self.assertIs(sup["preserved_not_rewritten"], True)

    def test_the_spent_p10_row_is_retained_and_still_admits_nothing(self):
        """A spent row must stay in the file AND stay inert. Both halves matter.

        Deleting it would orphan the SYNCO-02 acknowledgement it explains; re-approving it would
        allow a second delivery on a one-attempt authorisation.
        """
        shipped = os.path.join(HERE, "delivery-authorisations.json")
        with io.open(shipped, encoding="utf-8") as fh:
            rows = json.loads(fh.read())["delivery_authorisations"]
        d1 = [r for r in rows if r["id"] == "SECTOR-DELIVERY-P10-D1"]
        self.assertEqual(len(d1), 1, "the spent P10 delivery row must be retained, exactly once")
        self.assertEqual(d1[0]["status"], "spent")
        self.assertEqual(d1[0]["fixture_id"], "SYNCO-02")
        self.assertEqual(d1[0]["max_deliveries"], 1)
        self.assertEqual(d1[0]["spent_by_delivery_id"], d1[0]["delivery_id"])
        res = rx.receive(self.ref(authorization_id="SECTOR-DELIVERY-P10-D1"), shipped)
        self.assertEqual(res["refusal_code"], "AUTHORISATION_NOT_APPROVED")
        self.assertEqual(self.acks(), [])

    def test_missing_authorisation_id_fails(self):
        self.assert_refused(self.ref(authorization_id="NOPE"), "AUTHORISATION_NOT_FOUND")

    def test_missing_registry_file_fails(self):
        res = rx.receive(self.ref(), os.path.join(self.tmp, "absent.json"))
        self.assertEqual(res["refusal_code"], "REGISTRY_MISSING")
        self.assertEqual(self.acks(), [])

    def test_a_reference_not_claiming_approved_fails(self):
        self.assert_refused(self.ref(authorization_status="draft"), "REFERENCE_STATUS_MISMATCH")

    def test_no_shipped_row_is_approved_and_the_template_cannot_pass(self):
        """The durable invariant: the shipped registry carries NO `approved` row.

        Re-baselined 2026-10-02. This test previously also asserted that no SYNCO-02 row was
        shipped, which encoded "no delivery has ever been authorised" - true while the mechanism
        was unused, and deliberately false once SECTOR-DELIVERY-P10-D1 was approved, invoked once
        and spent by owner decision. A `spent` row is RETAINED HISTORY that explains an existing
        acknowledgement and admits nothing, so the invariant that matters is `approved`, not the
        absence of any row. Entries are never deleted, so this had to change rather than the file.
        """
        shipped = os.path.join(HERE, "delivery-authorisations.json")
        with io.open(shipped, encoding="utf-8") as fh:
            reg = json.loads(fh.read())
        rows = reg["delivery_authorisations"]
        self.assertTrue(all(r["status"] != "approved" for r in rows),
                        "no shipped row may be approved: %s"
                        % [(r["id"], r["status"]) for r in rows])
        tpl = [r for r in rows if r["id"] == "TEMPLATE-DO-NOT-APPROVE"]
        self.assertEqual(len(tpl), 1, "the template row must still be present, exactly once")
        self.assertEqual(tpl[0]["status"], "draft", "the template must stay draft")
        # the template refuses before touching anything
        res = rx.receive(self.ref(authorization_id="TEMPLATE-DO-NOT-APPROVE"), shipped)
        self.assertEqual(res["refusal_code"], "AUTHORISATION_NOT_APPROVED")
        self.assertEqual(self.acks(), [])
        # and so does every spent row, so a spent authorisation can never be reused
        for row in (r for r in rows if r["status"] == "spent"):
            spent = rx.receive(self.ref(authorization_id=row["id"]), shipped)
            self.assertEqual(spent["refusal_code"], "AUTHORISATION_NOT_APPROVED",
                             "a spent row must admit nothing: %s" % row["id"])
            self.assertEqual(self.acks(), [])


class FieldMismatchFailsClosed(Harness):
    def refuse(self, ref, code):
        res = rx.receive(ref, self.registry)
        self.assertEqual(res["refusal_code"], code, res)
        self.assertEqual(self.acks(), [])

    def test_wrong_fixture_id_fails(self):
        self.refuse(self.ref(fixture_id="OTHER"), "AUTHORISATION_FIELD_MISMATCH")

    def test_wrong_delivery_id_fails(self):
        self.refuse(self.ref(delivery_id="D2"), "AUTHORISATION_FIELD_MISMATCH")

    def test_wrong_packet_path_fails(self):
        other = os.path.join(self.sandbox, "other.json")
        self.write_packet(GOOD_PACKET, other)
        self.refuse(self.ref(packet_path=other), "AUTHORISATION_FIELD_MISMATCH")

    def test_wrong_packet_hash_fails(self):
        self.refuse(self.ref(packet_sha256="0" * 64), "AUTHORISATION_FIELD_MISMATCH")

    def test_wrong_destination_fails(self):
        self.refuse(self.ref(destination="Sales (05)"), "WRONG_DESTINATION")

    def test_a_non_fixture_reference_fails(self):
        self.refuse(self.ref(classification="PRODUCTION"), "NOT_A_FIXTURE")

    def test_downstream_authorization_other_than_none_fails(self):
        self.refuse(self.ref(downstream_authorization="GRANTED"), "DOWNSTREAM_NOT_NONE")
        self.refuse(self.ref(downstream_authorization="none"), "DOWNSTREAM_NOT_NONE")

    def test_a_reference_of_the_wrong_shape_fails(self):
        extra = self.ref()
        extra["surprise"] = True
        self.refuse(extra, "REFERENCE_SHAPE")
        missing = self.ref()
        del missing["packet_sha256"]
        self.refuse(missing, "REFERENCE_SHAPE")

    def test_an_unsafe_identifier_fails(self):
        self.refuse(self.ref(delivery_id="../escape"), "UNSAFE_IDENTIFIER")


class PacketFailsClosed(Harness):
    def refuse(self, code):
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["refusal_code"], code, res)
        self.assertEqual(self.acks(), [])

    def test_a_missing_packet_fails(self):
        # Capture the reference BEFORE deleting, since building one needs to hash the file.
        ref = self.ref()
        os.remove(self.packet)
        res = rx.receive(ref, self.registry)
        self.assertEqual(res["refusal_code"], "PACKET_MISSING", res)
        self.assertEqual(self.acks(), [])

    def test_a_modified_packet_fails_on_its_hash(self):
        # The registry pins the ORIGINAL hash; change the file after authorisation.
        with io.open(self.packet, "a", encoding="utf-8") as fh:
            fh.write("\n")
        res = rx.receive(self.ref(packet_sha256=self.packet_hash()), self.registry)
        self.assertEqual(res["refusal_code"], "AUTHORISATION_FIELD_MISMATCH")
        self.assertEqual(self.acks(), [])

    def test_a_non_fixture_packet_fails(self):
        self.write_packet(dict(GOOD_PACKET, classification="PRODUCTION"))
        self.write_registry()
        self.refuse("PACKET_NOT_FIXTURE")

    def test_a_packet_granting_downstream_action_fails(self):
        self.write_packet(dict(GOOD_PACKET, downstream_authorization="GRANTED"))
        self.write_registry()
        self.refuse("PACKET_GRANTS_DOWNSTREAM")

    def test_a_packet_carrying_a_url_fails(self):
        self.write_packet(dict(GOOD_PACKET, website="https://example.invalid"))
        self.write_registry()
        self.refuse("PACKET_CARRIES_URL")

    def test_a_packet_claiming_an_external_write_fails(self):
        self.write_packet(dict(GOOD_PACKET, external_writes=["a clickup task"]))
        self.write_registry()
        self.refuse("PACKET_CLAIMS_EXTERNAL_WRITE")

    def test_a_packet_already_claiming_delivery_fails(self):
        self.write_packet(dict(GOOD_PACKET, destinations=[{"name": "Offer (02)",
                                                           "outcome": "delivered"}]))
        self.write_registry()
        self.refuse("PACKET_CLAIMS_DELIVERED")

    def test_an_unreadable_packet_fails(self):
        with io.open(self.packet, "w", encoding="utf-8") as fh:
            fh.write("{not json")
        self.write_registry(packet_sha256=self.packet_hash())
        self.refuse("PACKET_UNREADABLE")


class PathSafety(Harness):
    def refuse_root(self, root, code):
        self.write_registry(sandbox_root=root)
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["refusal_code"], code, res)

    def test_a_repository_destination_fails(self):
        self.refuse_root(os.path.join(ROOT, "01_Sector"), "PATH_FORBIDDEN_LOCATION")

    def test_a_git_worktree_destination_fails(self):
        # A temp dir made to look like a work tree, so the git check is exercised on its own.
        fake = os.path.join(self.tmp, "worktree")
        os.makedirs(os.path.join(fake, ".git"))
        self.refuse_root(fake, "PATH_IN_GIT_WORKTREE")

    def test_a_onedrive_destination_fails(self):
        fake = os.path.join(self.tmp, "OneDrive", "x")
        os.makedirs(fake)
        self.refuse_root(fake, "PATH_FORBIDDEN_LOCATION")

    def test_a_runtime_memory_stream_destination_fails(self):
        fake = os.path.join(self.tmp, "_memory")
        os.makedirs(fake)
        self.refuse_root(fake, "PATH_FORBIDDEN_LOCATION")

    def test_a_repository_fixture_log_destination_fails(self):
        fake = os.path.join(self.tmp, "skill_runs")
        os.makedirs(fake)
        self.refuse_root(fake, "PATH_FORBIDDEN_LOCATION")

    def test_a_traversal_root_fails(self):
        self.refuse_root(os.path.join(self.sandbox, "..", "sandbox"), "PATH_TRAVERSAL")

    def test_a_relative_root_fails(self):
        self.refuse_root("sandbox", "PATH_NOT_ABSOLUTE")

    def test_a_packet_outside_the_sandbox_fails(self):
        outside = os.path.join(self.tmp, "outside.json")
        self.write_packet(GOOD_PACKET, outside)
        self.write_registry(packet_path=outside,
                            packet_sha256=self.write_packet(GOOD_PACKET, outside))
        res = rx.receive(self.ref(packet_path=outside,
                                  packet_sha256=self.write_packet(GOOD_PACKET, outside)),
                         self.registry)
        self.assertEqual(res["refusal_code"], "PATH_OUTSIDE_SANDBOX")
        self.assertEqual(self.acks(), [])

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unsupported")
    def test_a_symlink_escape_fails_where_supported(self):
        real = os.path.join(self.tmp, "real")
        os.makedirs(real, exist_ok=True)
        link = os.path.join(self.tmp, "link")
        try:
            os.symlink(real, link, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest("symlink creation not permitted here: %s" % exc)
        self.write_registry(sandbox_root=link)
        res = rx.receive(self.ref(), self.registry)
        self.assertIn(res["refusal_code"], ("PATH_LINK_ESCAPE", "PATH_OUTSIDE_SANDBOX",
                                            "AUTHORISATION_FIELD_MISMATCH"))
        self.assertEqual(self.acks(), [])


class ApprovalPrecedesSideEffects(Harness):
    def test_no_directory_is_created_when_authorisation_fails(self):
        missing = os.path.join(self.tmp, "never-created")
        self.write_registry(status="draft", sandbox_root=missing)
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["refusal_code"], "AUTHORISATION_NOT_APPROVED")
        self.assertFalse(os.path.exists(missing), "a refused delivery must create no directory")

    def test_the_registry_is_untouched_by_a_refusal(self):
        with io.open(self.registry, encoding="utf-8") as fh:
            before = fh.read()
        rx.receive(self.ref(authorization_id="NOPE"), self.registry)
        with io.open(self.registry, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), before)

    def test_validate_is_pure_and_creates_nothing(self):
        listing = sorted(os.listdir(self.sandbox))
        try:
            rx.validate(self.ref(authorization_status="draft"), self.registry)
        except rx.Refusal:
            pass
        self.assertEqual(sorted(os.listdir(self.sandbox)), listing)

    def test_a_failed_delivery_is_reported_only_in_the_result(self):
        res = rx.receive(self.ref(fixture_id="WRONG"), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_REFUSED)
        self.assertIsNotNone(res["refusal_code"])
        self.assertEqual(os.listdir(self.sandbox), ["packet.json"],
                         "no acknowledgement and no failure file may be written")

    def test_the_receiver_does_not_consult_the_runtime_approval_flag(self):
        with io.open(os.path.join(HERE, "offer_inbox_receiver.py"), encoding="utf-8") as fh:
            src = fh.read()
        for banned in ("humanGate", "requiresHumanApproval", "requires_human_approval"):
            self.assertNotIn(banned, src.replace("approval flag", ""),
                             "must enforce its own approval, not inherit %r" % banned)


class SeparateReadRoot(unittest.TestCase):
    """`packet_root` separates the authorised READ root from the authorised WRITE root.

    Every test builds a fixture-shaped tree in the OS temp area:
        <tmp>/<fixture_id>/04_fixture_inputs/   <- read root
        <tmp>/<fixture_id>/05_outputs/          <- write root
    Neither real SYNCO sandbox is touched.
    """

    FIXTURE = "TMPFIX-01"

    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp(prefix="p10-root-"))
        self.fixture_root = os.path.join(self.tmp, self.FIXTURE)
        self.inputs = os.path.join(self.fixture_root, "04_fixture_inputs")
        self.outputs = os.path.join(self.fixture_root, "05_outputs")
        os.makedirs(self.inputs)
        os.makedirs(self.outputs)
        self.packet = os.path.join(self.inputs, "control-packet.json")
        self.hash = self.write_packet(GOOD_PACKET)
        self.registry = os.path.join(self.tmp, "delivery-authorisations.json")
        self.write_registry()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_packet(self, obj, path=None):
        path = path or self.packet
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
        with io.open(path, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()

    def write_registry(self, **over):
        row = {"id": "AUTH-R", "status": "approved", "destination": "Offer (02)",
               "fixture_id": self.FIXTURE, "delivery_id": "R1",
               "packet_path": self.packet, "packet_sha256": self.hash,
               "sandbox_root": self.outputs, "packet_root": self.inputs, "max_deliveries": 1}
        row.update(over)
        self.row = row
        with io.open(self.registry, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"delivery_authorisations": [row]}, indent=2) + "\n")
        return row

    def ref(self, **over):
        r = {"classification": "TEST_FIXTURE", "fixture_id": self.row["fixture_id"],
             "delivery_id": self.row["delivery_id"], "packet_path": self.row["packet_path"],
             "packet_sha256": self.row["packet_sha256"], "destination": "Offer (02)",
             "authorization_id": "AUTH-R", "authorization_status": "approved",
             "downstream_authorization": "NONE"}
        r.update(over)
        return r

    def acks(self, where=None):
        d = where or self.outputs
        return sorted(f for f in os.listdir(d) if f.endswith(".ack.json"))

    def refuse(self, code, ref=None):
        """Assert a refusal with no side effect.

        The read root is checked for ADDED FILES only: several tests legitimately create a
        subdirectory or a stray packet there themselves to set the scenario up, so the invariant
        is that the RECEIVER added nothing - not that the directory is pristine.
        """
        before = sorted(os.listdir(self.inputs))
        res = rx.receive(ref or self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_REFUSED, res)
        self.assertEqual(res["refusal_code"], code, res)
        self.assertEqual(self.acks(), [], "a refusal must write no acknowledgement")
        self.assertEqual(sorted(os.listdir(self.inputs)), before,
                         "a refusal must not add anything to the read root")
        with io.open(self.registry, encoding="utf-8") as fh:
            self.assertNotEqual(json.loads(fh.read())["delivery_authorisations"][0]["status"],
                                "spent", "a refusal must not spend the row")
        return res

    # ---- the happy path this amendment exists for ------------------------
    def test_valid_sibling_roots_read_from_inputs_and_write_to_outputs(self):
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_ACK, res.get("refusal_code"))
        self.assertEqual(self.acks(), ["R1.ack.json"], "exactly one acknowledgement")
        self.assertEqual(os.path.dirname(res["acknowledgement_path"]), self.outputs,
                         "the acknowledgement must land in 05_outputs")
        self.assertEqual(sorted(os.listdir(self.inputs)), ["control-packet.json"],
                         "04_fixture_inputs still holds only the packet")
        with io.open(res["acknowledgement_path"], encoding="utf-8") as fh:
            ack = json.loads(fh.read())
        self.assertEqual(ack["packet_sha256"], self.hash, "the packet in 04_ was the one read")
        self.assertIs(ack["external_write"], False)
        self.assertEqual(ack["downstream_authorization"], "NONE")

    def test_the_row_is_spent_after_a_separated_root_delivery(self):
        rx.receive(self.ref(), self.registry)
        with io.open(self.registry, encoding="utf-8") as fh:
            reg = json.loads(fh.read())
        self.assertEqual(reg["delivery_authorisations"][0]["status"], "spent")

    # ---- the old behaviour is preserved exactly --------------------------
    def test_absent_packet_root_preserves_the_original_single_root_behaviour(self):
        """With no packet_root, the packet must be inside sandbox_root - as before."""
        inside = os.path.join(self.outputs, "p.json")
        h2 = self.write_packet(GOOD_PACKET, inside)
        self.write_registry(packet_root=None, packet_path=inside, packet_sha256=h2)
        del self.row["packet_root"]
        with io.open(self.registry, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"delivery_authorisations": [self.row]}, indent=2) + "\n")
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_ACK, res.get("refusal_code"))
        self.assertEqual(self.acks(), ["R1.ack.json"])

    def test_absent_packet_root_still_refuses_a_packet_outside_sandbox_root(self):
        self.write_registry(packet_root=None)
        del self.row["packet_root"]
        with io.open(self.registry, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"delivery_authorisations": [self.row]}, indent=2) + "\n")
        # the packet lives in 04_fixture_inputs, which is NOT inside 05_outputs
        self.refuse("PATH_OUTSIDE_SANDBOX")

    # ---- containment ----------------------------------------------------
    def test_a_packet_outside_packet_root_is_refused(self):
        elsewhere = os.path.join(self.fixture_root, "stray.json")
        h2 = self.write_packet(GOOD_PACKET, elsewhere)
        self.write_registry(packet_path=elsewhere, packet_sha256=h2)
        self.refuse("PATH_OUTSIDE_SANDBOX")

    def test_a_nested_packet_path_is_refused(self):
        nested = os.path.join(self.inputs, "sub", "p.json")
        h2 = self.write_packet(GOOD_PACKET, nested)
        self.write_registry(packet_path=nested, packet_sha256=h2)
        self.refuse("PATH_NOT_DIRECT_CHILD")

    # ---- the same-fixture relationship ---------------------------------
    def test_cross_fixture_roots_are_refused(self):
        other = os.path.join(self.tmp, "TMPFIX-02", "04_fixture_inputs")
        os.makedirs(other)
        p = os.path.join(other, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=other, packet_path=p, packet_sha256=h2)
        self.refuse("ROOTS_NOT_SIBLINGS")

    def test_non_sibling_roots_are_refused(self):
        deeper = os.path.join(self.fixture_root, "nest", "04_fixture_inputs")
        os.makedirs(deeper)
        p = os.path.join(deeper, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=deeper, packet_path=p, packet_sha256=h2)
        self.refuse("ROOTS_NOT_SIBLINGS")

    def test_a_wrongly_named_read_root_is_refused(self):
        wrong = os.path.join(self.fixture_root, "inputs")
        os.makedirs(wrong)
        p = os.path.join(wrong, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=wrong, packet_path=p, packet_sha256=h2)
        self.refuse("PACKET_ROOT_NAME")

    def test_a_wrongly_named_write_root_is_refused(self):
        wrong = os.path.join(self.fixture_root, "outputs")
        os.makedirs(wrong)
        self.write_registry(sandbox_root=wrong)
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["refusal_code"], "SANDBOX_ROOT_NAME", res)
        self.assertEqual(self.acks(wrong), [])

    def test_a_fixture_id_not_matching_the_shared_root_is_refused(self):
        self.write_registry(fixture_id="NOT-THE-ROOT-NAME")
        self.refuse("FIXTURE_ID_ROOT_MISMATCH")

    def test_the_normalization_rule_is_the_root_directory_name(self):
        """A fixture root's directory NAME is its fixture id - the established rule."""
        self.assertEqual(os.path.basename(self.fixture_root), self.FIXTURE)
        res = rx.receive(self.ref(), self.registry)
        self.assertEqual(res["outcome"], rx.OUTCOME_ACK, res.get("refusal_code"))

    # ---- both roots pass every safe-root check independently -------------
    def test_a_relative_read_root_is_refused(self):
        self.write_registry(packet_root="04_fixture_inputs")
        self.refuse("PATH_NOT_ABSOLUTE")

    def test_a_traversed_read_root_is_refused(self):
        self.write_registry(packet_root=os.path.join(self.fixture_root, "..", self.FIXTURE,
                                                     "04_fixture_inputs"))
        self.refuse("PATH_TRAVERSAL")

    def test_a_git_worktree_read_root_is_refused(self):
        gitfix = os.path.join(self.tmp, "GITFIX")
        inputs = os.path.join(gitfix, "04_fixture_inputs")
        os.makedirs(os.path.join(gitfix, ".git"))
        os.makedirs(inputs)
        p = os.path.join(inputs, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=inputs, packet_path=p, packet_sha256=h2)
        self.refuse("PATH_IN_GIT_WORKTREE")

    def test_a_onedrive_read_root_is_refused(self):
        od = os.path.join(self.tmp, "OneDrive", self.FIXTURE, "04_fixture_inputs")
        os.makedirs(od)
        p = os.path.join(od, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=od, packet_path=p, packet_sha256=h2)
        self.refuse("PATH_FORBIDDEN_LOCATION")

    def test_a_runtime_memory_read_root_is_refused(self):
        mem = os.path.join(self.tmp, "_memory", self.FIXTURE, "04_fixture_inputs")
        os.makedirs(mem)
        p = os.path.join(mem, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=mem, packet_path=p, packet_sha256=h2)
        self.refuse("PATH_FORBIDDEN_LOCATION")

    def test_a_fixture_log_read_root_is_refused(self):
        log = os.path.join(self.tmp, "skill_runs", self.FIXTURE, "04_fixture_inputs")
        os.makedirs(log)
        p = os.path.join(log, "control-packet.json")
        h2 = self.write_packet(GOOD_PACKET, p)
        self.write_registry(packet_root=log, packet_path=p, packet_sha256=h2)
        self.refuse("PATH_FORBIDDEN_LOCATION")

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unsupported")
    def test_a_symlinked_read_root_is_refused_where_supported(self):
        link = os.path.join(self.fixture_root, "04_fixture_inputs_link")
        try:
            os.symlink(self.inputs, link, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest("symlink creation not permitted here: %s" % exc)
        self.write_registry(packet_root=link)
        res = rx.receive(self.ref(), self.registry)
        self.assertIn(res["refusal_code"], ("PATH_LINK_ESCAPE", "PACKET_ROOT_NAME"))
        self.assertEqual(self.acks(), [])

    # ---- order, and unchanged guarantees --------------------------------
    def test_every_relationship_failure_precedes_any_side_effect(self):
        for kwargs, code in [({"fixture_id": "WRONG-ROOT"}, "FIXTURE_ID_ROOT_MISMATCH"),
                             ({"status": "draft"}, "AUTHORISATION_NOT_APPROVED")]:
            self.write_registry(**kwargs)
            res = rx.receive(self.ref(), self.registry)
            self.assertEqual(res["refusal_code"], code, res)
            self.assertEqual(self.acks(), [], "no acknowledgement for %s" % code)
            self.assertEqual(sorted(os.listdir(self.inputs)), ["control-packet.json"])
            with io.open(self.registry, encoding="utf-8") as fh:
                self.assertNotEqual(json.loads(fh.read())["delivery_authorisations"][0]["status"],
                                    "spent", "a refusal must not spend the row")

    def test_validate_remains_pure_with_separated_roots(self):
        before_in = sorted(os.listdir(self.inputs))
        before_out = sorted(os.listdir(self.outputs))
        self.write_registry(fixture_id="WRONG-ROOT")
        try:
            rx.validate(self.ref(), self.registry)
        except rx.Refusal:
            pass
        self.assertEqual(sorted(os.listdir(self.inputs)), before_in)
        self.assertEqual(sorted(os.listdir(self.outputs)), before_out)

    def test_concurrency_and_atomicity_are_unchanged_with_separated_roots(self):
        results, lock = [], threading.Lock()
        start = threading.Event()

        def attempt():
            start.wait()
            r = rx.receive(self.ref(), self.registry)
            with lock:
                results.append(r)

        threads = [threading.Thread(target=attempt) for _ in range(8)]
        for t in threads:
            t.start()
        start.set()
        for t in threads:
            t.join()

        self.assertEqual(self.acks(), ["R1.ack.json"], "at most one acknowledgement")
        won = [r for r in results if r["outcome"] in (rx.OUTCOME_ACK, rx.OUTCOME_ACK_UNRESOLVED)]
        self.assertEqual(len(won), 1, "exactly one invocation may claim the acknowledgement")

    def test_the_packet_hash_is_still_enforced_against_the_read_root(self):
        """Changing the packet AFTER authorisation is caught by re-hashing the file.

        The reference still carries the hash the row pins, so this is not a field mismatch - the
        receiver recomputes the file's hash and reports PACKET_HASH_MISMATCH, which is the more
        precise refusal of the two.
        """
        self.write_packet(dict(GOOD_PACKET, extra="changed"))
        self.refuse("PACKET_HASH_MISMATCH")

    def test_a_missing_packet_in_the_read_root_is_refused(self):
        ref = self.ref()
        os.remove(self.packet)
        res = rx.receive(ref, self.registry)
        self.assertEqual(res["refusal_code"], "PACKET_MISSING", res)
        self.assertEqual(self.acks(), [])


class Isolation(unittest.TestCase):
    def test_the_receiver_imports_no_connector_network_bus_or_sdk_module(self):
        with io.open(os.path.join(HERE, "offer_inbox_receiver.py"), encoding="utf-8") as fh:
            src = fh.read()
        import_lines = "\n".join(l for l in src.splitlines()
                                 if l.startswith("import ") or l.startswith("from "))
        for banned in ("socket", "http", "urllib", "requests", "httpx", "urllib3", "ssl",
                       "anthropic", "event-bus", "event_bus", "arika", "clickup", "notion",
                       "subprocess"):
            self.assertNotIn(banned, import_lines, "receiver imports %r" % banned)

    def test_the_receiver_only_imports_the_allowed_standard_library(self):
        with io.open(os.path.join(HERE, "offer_inbox_receiver.py"), encoding="utf-8") as fh:
            src = fh.read()
        mods = set()
        for line in src.splitlines():
            if line.startswith("import ") and " " in line:
                mods.add(line.split()[1].split(".")[0])
        self.assertTrue(mods <= {"datetime", "hashlib", "io", "json", "os", "re", "sys"},
                        "unexpected import(s): %s" % sorted(mods))

    def test_executor_still_neither_publishes_nor_references_the_bus(self):
        with io.open(os.path.join(ROOT, "arika-runtime", "src", "executor.ts"),
                     encoding="utf-8") as fh:
            ex = fh.read()
        self.assertNotIn("publish(", ex)
        self.assertNotIn("event-bus", ex)

    def test_the_real_synco_sandboxes_were_not_touched_by_this_suite(self):
        self.assertEqual(tree_hash(SYNCO1), SANDBOX_BEFORE["SYNCO-01"],
                         "the SYNCO-01 sandbox changed during the test run")
        self.assertEqual(tree_hash(SYNCO2), SANDBOX_BEFORE["SYNCO-02"],
                         "the SYNCO-02 sandbox changed during the test run")

    def test_production_runtime_files_are_unchanged(self):
        base = os.path.join(ROOT, "arika-runtime", "src")
        for name in ("executor.ts", "index.ts", os.path.join("triggers", "event-bus.ts")):
            self.assertTrue(os.path.isfile(os.path.join(base, name)), name)
        # the mechanism adds no runtime file
        self.assertFalse(os.path.exists(os.path.join(base, "delivery.ts")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
