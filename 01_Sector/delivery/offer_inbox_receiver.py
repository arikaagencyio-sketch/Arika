# -*- coding: utf-8 -*-
"""SECTOR-DELIVERY-P10 - the offline Offer (02) inbox receiver.

The smallest mechanism that can prove a Sector handoff was RECEIVED: a packet reference is handed
directly to this module, which validates it, invokes receiver logic, and records one durable,
idempotent acknowledgement. Against the proposal's A-D ladder it proves A (transport), B (receiver
invoked) and C (acknowledgement recorded) while keeping D (external destination changed) FALSE.

WHAT THIS IS NOT
----------------
This is an OFFLINE FAKE Offer-side receiver and says so in every acknowledgement it writes. It does
not write Offer's registry, Offer's runtime memory log, or any other production store. It is not an
agent, has no spec, declares no trigger, is wired into no boot path, and is invoked only by an
explicit owner-authorised command.

NO EVENT, NO BUS, NO RUNTIME
----------------------------
The Sector -> Offer route is "relation + text reference" (S10 Step 0), not an event route. Nothing
here publishes an event, instantiates an event bus, boots the runtime, starts a scheduler or a
webhook server, or touches `arika-runtime` at all. `executor.ts` is unmodified, so the estate event
gate's check 4 - which FAILS the build if `executor.ts` ever contains `publish(` or `event-bus` -
keeps passing unaltered.

APPROVAL IS ENFORCED HERE, NOT INHERITED
----------------------------------------
This module deliberately does NOT consult the runtime's approval flag. That flag is computed after an
agent answers and is only REPORTED - no runtime code branches on it - so inheriting it would inherit
a bypass. Every authorisation condition below is checked by this module, and ALL of them are checked
BEFORE any directory is created, any file is opened, any registry state is changed, any receiver
logic runs, and before any delivered outcome is recorded.

NO RETRIES. A refused or failed attempt stays refused. There is no back-off, no second attempt and no
repair path: a further attempt needs a new owner decision and a new authorisation.
"""
import datetime
import hashlib
import io
import json
import os
import re

# Only the standard library, and only these. No connector, HTTP, DNS, socket, event-bus, runtime or
# SDK module is imported here, and `test_offer_inbox_receiver.py` asserts that by source inspection.

RECEIVER_ID = "offer-inbox-receiver/1 (OFFLINE FAKE Offer-side receiver - writes no production store)"
FIXTURE_CLASSIFICATION = "TEST_FIXTURE"
DESTINATION = "Offer (02)"
DOWNSTREAM_NONE = "NONE"

#: The exact keys a packet reference must carry - no more, no fewer.
REFERENCE_KEYS = frozenset({
    "classification", "fixture_id", "delivery_id", "packet_path", "packet_sha256",
    "destination", "authorization_id", "authorization_status", "downstream_authorization",
})

OUTCOME_ACK = "ACKNOWLEDGED"
OUTCOME_ACK_UNRESOLVED = "ACKNOWLEDGED_WITH_UNRESOLVED_FLOOR"
OUTCOME_REFUSED = "REFUSED"
OUTCOME_DUPLICATE = "DUPLICATE_REFUSED"

_URLISH = re.compile(r"https?://|\bwww\.", re.I)
_CONTACTISH = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+|\+\d{7,}")
_SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,80}$")


class Refusal(Exception):
    """Raised internally when a condition fails. Never escapes: it becomes a REFUSED result."""

    def __init__(self, code, detail=""):
        super().__init__(code)
        self.code = code
        self.detail = detail


# ---------------------------------------------------------------- path safety
def _resolved(path):
    return os.path.realpath(os.path.abspath(path))


def _has_traversal(raw):
    return ".." in str(raw).replace("\\", "/").split("/")


def _links_on_chain(resolved):
    """True if any existing ancestor (or the path itself) is a symlink or junction."""
    p = resolved
    seen = set()
    while p and p not in seen:
        seen.add(p)
        if os.path.exists(p) and os.path.islink(p):
            return True
        parent = os.path.dirname(p)
        if parent == p:
            break
        p = parent
    return False


def _inside_git_worktree(resolved):
    p = resolved
    while True:
        if os.path.isdir(os.path.join(p, ".git")) or os.path.isfile(os.path.join(p, ".git")):
            return True
        parent = os.path.dirname(p)
        if parent == p:
            return False
        p = parent


FORBIDDEN_SEGMENTS = ("onedrive",)
FORBIDDEN_MARKERS = ("_memory", "arika-runtime", "skill_runs", "runtime.jsonl",
                     "the agency drafts")

#: When an authorisation separates its read root from its write root, the two must be these exact
#: sibling directories of one fixture root. Hard-coded rather than configurable: a free choice of
#: directory names would let an authorisation point the read root anywhere that happens to be safe.
PACKET_ROOT_NAME = "04_fixture_inputs"
ACK_ROOT_NAME = "05_outputs"


def assert_safe_root(raw, label):
    """A destination root must be absolute, link-free, outside git and OneDrive, and not a
    production or runtime-log location. Checked BEFORE anything is created."""
    if not raw or not isinstance(raw, str):
        raise Refusal("PATH_NOT_A_STRING", label)
    if _has_traversal(raw):
        raise Refusal("PATH_TRAVERSAL", "%s contains a '..' segment" % label)
    if not os.path.isabs(raw):
        raise Refusal("PATH_NOT_ABSOLUTE", label)
    res = _resolved(raw)
    if res != os.path.abspath(raw):
        raise Refusal("PATH_LINK_ESCAPE", "%s does not resolve to itself" % label)
    if _links_on_chain(res):
        raise Refusal("PATH_LINK_ESCAPE", "%s has a symlink or junction on its chain" % label)
    low = res.replace("\\", "/").lower()
    for seg in FORBIDDEN_SEGMENTS:
        if seg in low:
            raise Refusal("PATH_FORBIDDEN_LOCATION", "%s is under %r" % (label, seg))
    for marker in FORBIDDEN_MARKERS:
        if marker in low:
            raise Refusal("PATH_FORBIDDEN_LOCATION", "%s names a production or runtime-log "
                                                     "location (%r)" % (label, marker))
    if _inside_git_worktree(res):
        raise Refusal("PATH_IN_GIT_WORKTREE", label)
    return res


def assert_within(child_raw, root_resolved, label):
    """`child` must resolve to a location inside `root`, with no traversal or link escape."""
    if _has_traversal(child_raw):
        raise Refusal("PATH_TRAVERSAL", label)
    if not os.path.isabs(child_raw):
        raise Refusal("PATH_NOT_ABSOLUTE", label)
    res = _resolved(child_raw)
    if res != os.path.abspath(child_raw):
        raise Refusal("PATH_LINK_ESCAPE", label)
    if _links_on_chain(res):
        raise Refusal("PATH_LINK_ESCAPE", label)
    root = root_resolved.rstrip("\\/")
    if not (res == root or res.startswith(root + os.sep)):
        raise Refusal("PATH_OUTSIDE_SANDBOX", "%s is not inside the authorised root" % label)
    return res


def assert_direct_child(child_resolved, root_resolved, label):
    """`child` must sit DIRECTLY in `root`, not in a subdirectory of it."""
    if os.path.dirname(child_resolved) != root_resolved.rstrip("\\/"):
        raise Refusal("PATH_NOT_DIRECT_CHILD",
                      "%s must be a direct file inside its authorised root, not nested" % label)
    return child_resolved


def assert_sibling_fixture_roots(packet_root, sandbox_root, fixture_id):
    """Both roots must be the two named sibling directories of ONE authorised fixture root.

    This is what refuses a cross-fixture read or write even when both paths are independently
    safe: a read root under one fixture and a write root under another have different parents, and
    a parent whose name is not the authorisation's fixture id is not that authorisation's fixture.

    NORMALIZATION RULE, established here because the mechanism had none: a fixture root's
    directory NAME is its fixture id. The sandboxes are already named this way, so the rule
    records existing practice rather than inventing a mapping.
    """
    if os.path.basename(packet_root) != PACKET_ROOT_NAME:
        raise Refusal("PACKET_ROOT_NAME", "packet_root must be named %r, not %r"
                      % (PACKET_ROOT_NAME, os.path.basename(packet_root)))
    if os.path.basename(sandbox_root) != ACK_ROOT_NAME:
        raise Refusal("SANDBOX_ROOT_NAME", "sandbox_root must be named %r, not %r"
                      % (ACK_ROOT_NAME, os.path.basename(sandbox_root)))
    packet_parent = os.path.dirname(packet_root)
    ack_parent = os.path.dirname(sandbox_root)
    if packet_parent != ack_parent:
        raise Refusal("ROOTS_NOT_SIBLINGS",
                      "packet_root and sandbox_root do not share one resolved parent - a "
                      "cross-fixture read or write is refused")
    fixture_root = packet_parent
    if os.path.basename(fixture_root) != fixture_id:
        raise Refusal("FIXTURE_ID_ROOT_MISMATCH",
                      "the shared parent is named %r but the authorisation's fixture_id is %r"
                      % (os.path.basename(fixture_root), fixture_id))
    return fixture_root


# ---------------------------------------------------------------- validation
def _sha256_file(path):
    with io.open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _load_registry(registry_path):
    if not os.path.isfile(registry_path):
        raise Refusal("REGISTRY_MISSING", registry_path)
    try:
        with io.open(registry_path, encoding="utf-8") as fh:
            return json.loads(fh.read())
    except Exception as exc:
        raise Refusal("REGISTRY_UNREADABLE", type(exc).__name__)


def _find_authorisation(registry, auth_id):
    for row in registry.get("delivery_authorisations", []):
        if row.get("id") == auth_id:
            return row
    raise Refusal("AUTHORISATION_NOT_FOUND", "no row with the given id")


def _assert_packet_grants_nothing(packet):
    """The packet must not itself grant an external or downstream action."""
    if packet.get("classification") != FIXTURE_CLASSIFICATION:
        raise Refusal("PACKET_NOT_FIXTURE", "packet classification is not TEST_FIXTURE")
    if packet.get("downstream_authorization") != DOWNSTREAM_NONE:
        raise Refusal("PACKET_GRANTS_DOWNSTREAM",
                      "packet downstream_authorization is not NONE")
    blob = json.dumps(packet, ensure_ascii=False)
    if _URLISH.search(blob):
        raise Refusal("PACKET_CARRIES_URL", "a URL-shaped string is present")
    if _CONTACTISH.search(blob):
        raise Refusal("PACKET_CARRIES_CONTACT_DATA", "contact-shaped data is present")
    for key in ("external_write", "external_writes"):
        if packet.get(key):
            raise Refusal("PACKET_CLAIMS_EXTERNAL_WRITE", key)
    for row in packet.get("destinations", []) or []:
        if str(row.get("outcome", "")).lower() == "delivered":
            raise Refusal("PACKET_CLAIMS_DELIVERED", "a destination already claims delivery")
    return True


def _floor_unresolved(packet):
    for key in ("confidence_threshold", "freshness_requirement"):
        value = packet.get(key)
        if value is None:
            continue
        text = json.dumps(value) if not isinstance(value, str) else value
        if "UNRESOLVED" in text.upper():
            return True
    return False


def validate(reference, registry_path):
    """Pure validation. Touches nothing, creates nothing, changes nothing.

    Returns (authorisation_row, sandbox_root_resolved, ack_path, packet) on success.
    Raises Refusal on the first failed condition.
    """
    if not isinstance(reference, dict):
        raise Refusal("REFERENCE_NOT_AN_OBJECT")
    keys = set(reference)
    if keys != REFERENCE_KEYS:
        raise Refusal("REFERENCE_SHAPE",
                      "expected exactly %d keys; missing=%s unexpected=%s"
                      % (len(REFERENCE_KEYS), sorted(REFERENCE_KEYS - keys), sorted(keys - REFERENCE_KEYS)))

    if reference["classification"] != FIXTURE_CLASSIFICATION:
        raise Refusal("NOT_A_FIXTURE", "classification must be TEST_FIXTURE")
    if reference["destination"] != DESTINATION:
        raise Refusal("WRONG_DESTINATION", "only %r is implemented" % DESTINATION)
    if reference["downstream_authorization"] != DOWNSTREAM_NONE:
        raise Refusal("DOWNSTREAM_NOT_NONE", "must be exactly %r" % DOWNSTREAM_NONE)
    for field in ("fixture_id", "delivery_id", "authorization_id"):
        if not _SAFE_ID.match(str(reference[field] or "")):
            raise Refusal("UNSAFE_IDENTIFIER", field)

    registry = _load_registry(registry_path)
    row = _find_authorisation(registry, reference["authorization_id"])

    if row.get("status") != "approved":
        raise Refusal("AUTHORISATION_NOT_APPROVED", "status is %r" % row.get("status"))
    if reference["authorization_status"] != "approved":
        raise Refusal("REFERENCE_STATUS_MISMATCH", "reference does not claim approved")
    if row.get("destination") != DESTINATION:
        raise Refusal("AUTHORISATION_DESTINATION_MISMATCH")
    for field in ("fixture_id", "delivery_id", "packet_path", "packet_sha256"):
        if row.get(field) != reference[field]:
            raise Refusal("AUTHORISATION_FIELD_MISMATCH", field)

    sandbox = assert_safe_root(row.get("sandbox_root"), "sandbox_root")

    # `packet_root` separates the authorised READ root from the authorised WRITE root. Absent, the
    # original single-root behaviour is preserved EXACTLY: one root bounds both.
    packet_root_raw = row.get("packet_root")
    if packet_root_raw is None:
        packet_root = sandbox
        fixture_root = None
    else:
        packet_root = assert_safe_root(packet_root_raw, "packet_root")
        fixture_root = assert_sibling_fixture_roots(packet_root, sandbox, reference["fixture_id"])

    packet_path = assert_within(reference["packet_path"], packet_root, "packet_path")
    if packet_root_raw is not None:
        assert_direct_child(packet_path, packet_root, "packet_path")

    if not os.path.isfile(packet_path):
        raise Refusal("PACKET_MISSING", "no file at the authorised packet path")
    actual = _sha256_file(packet_path)
    if actual != reference["packet_sha256"]:
        raise Refusal("PACKET_HASH_MISMATCH", "the packet changed since authorisation")

    try:
        with io.open(packet_path, encoding="utf-8") as fh:
            packet = json.loads(fh.read())
    except Exception as exc:
        raise Refusal("PACKET_UNREADABLE", type(exc).__name__)
    if not isinstance(packet, dict):
        raise Refusal("PACKET_NOT_AN_OBJECT")
    _assert_packet_grants_nothing(packet)

    # The acknowledgement stays confined to `sandbox_root` whether or not a read root was given,
    # and must sit directly in it.
    ack_path = assert_within(os.path.join(sandbox, "%s.ack.json" % reference["delivery_id"]),
                             sandbox, "acknowledgement_path")
    assert_direct_child(ack_path, sandbox, "acknowledgement_path")
    if os.path.exists(ack_path):
        raise Refusal("ACKNOWLEDGEMENT_EXISTS", "this delivery_id is already acknowledged")

    return row, sandbox, ack_path, packet


# ---------------------------------------------------------------- receive
def receive(reference, registry_path, now=None):
    """Validate, then invoke receiver logic, then write ONE durable acknowledgement.

    Returns a result dict. A refusal is REPORTED in the result and writes nothing at all - there is
    no failure file, so a refusal can never be mistaken for an acknowledgement.
    """
    result = {
        "mechanism": "SECTOR-DELIVERY-P10",
        "receiver": RECEIVER_ID,
        "classification": FIXTURE_CLASSIFICATION,
        "delivery_id": (reference or {}).get("delivery_id") if isinstance(reference, dict) else None,
        "outcome": OUTCOME_REFUSED,
        "refusal_code": None,
        "refusal_detail": None,
        "acknowledgement_path": None,
        "external_write": False,
        "downstream_authorization": DOWNSTREAM_NONE,
        "side_effects_before_validation": False,
        "registry_marked_spent": False,
    }
    try:
        row, sandbox, ack_path, packet = validate(reference, registry_path)
    except Refusal as refusal:
        result["refusal_code"] = refusal.code
        result["refusal_detail"] = refusal.detail
        return result

    # ---- every condition passed. ONLY NOW may anything be created or changed. ----
    stamp = now or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    outcome = OUTCOME_ACK_UNRESOLVED if _floor_unresolved(packet) else OUTCOME_ACK

    acknowledgement = {
        "classification": FIXTURE_CLASSIFICATION,
        "_marker": "TEST_FIXTURE - NOT REAL - NOT EVIDENCE",
        "mechanism": "SECTOR-DELIVERY-P10",
        "delivery_id": reference["delivery_id"],
        "fixture_id": reference["fixture_id"],
        "authorization_id": reference["authorization_id"],
        "destination": DESTINATION,
        "packet_sha256": reference["packet_sha256"],
        "receiver": RECEIVER_ID,
        "received_at": stamp,
        "outcome": outcome,
        "external_write": False,
        "downstream_authorization": DOWNSTREAM_NONE,
        "_this_is_not": [
            "a delivered production handoff", "an Offer registry entry",
            "an Offer runtime memory line", "a CRM or Notion write", "a Lead or pipeline entry",
            "evidence that any external destination received anything",
        ],
        "_no_packet_payload": "This acknowledgement records THAT a packet was received and its "
                              "hash. It deliberately carries no packet content, no URL and no "
                              "personal data.",
    }

    # Atomic create-if-absent. Two concurrent invocations race here and exactly one wins; the loser
    # gets FileExistsError and is refused, so at most one acknowledgement can ever exist.
    blob = json.dumps(acknowledgement, ensure_ascii=False, indent=2) + "\n"
    try:
        fd = os.open(ack_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        result["outcome"] = OUTCOME_DUPLICATE
        result["refusal_code"] = "ACKNOWLEDGEMENT_EXISTS"
        result["refusal_detail"] = "lost the create race; the acknowledgement already exists"
        return result
    try:
        with io.open(fd, "w", encoding="utf-8", newline="\n", closefd=True) as fh:
            fh.write(blob)
    except Exception:
        # The file exists but is incomplete. Do NOT retry and do NOT remove it: a partial
        # acknowledgement is a fact that needs an owner decision, not a silent repair.
        result["outcome"] = OUTCOME_REFUSED
        result["refusal_code"] = "ACKNOWLEDGEMENT_WRITE_INCOMPLETE"
        result["refusal_detail"] = "the acknowledgement file exists but may be incomplete"
        result["acknowledgement_path"] = ack_path
        return result

    result["outcome"] = outcome
    result["acknowledgement_path"] = ack_path
    result["acknowledgement_sha256"] = hashlib.sha256(blob.encode("utf-8")).hexdigest()

    # One-attempt model: the row is consumed now that the delivery happened. Recorded as
    # best-effort - the acknowledgement above is the authoritative record, not the registry.
    try:
        registry = _load_registry(registry_path)
        for candidate in registry.get("delivery_authorisations", []):
            if candidate.get("id") == reference["authorization_id"]:
                candidate["status"] = "spent"
                candidate["spent_at"] = stamp
                candidate["spent_by_delivery_id"] = reference["delivery_id"]
        with io.open(registry_path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
        result["registry_marked_spent"] = True
    except Exception as exc:
        result["registry_marked_spent"] = False
        result["registry_note"] = "could not mark the row spent (%s); the acknowledgement stands " \
                                  "and no retry is permitted" % type(exc).__name__
    return result


if __name__ == "__main__":
    import sys

    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print("SECTOR-DELIVERY-P10 - Offer (02) offline inbox receiver")
    print("  receiver        :", RECEIVER_ID)
    print("  destination     :", DESTINATION)
    print("  reference keys  :", ", ".join(sorted(REFERENCE_KEYS)))
    print("  outcomes        :", ", ".join([OUTCOME_ACK, OUTCOME_ACK_UNRESOLVED,
                                            OUTCOME_REFUSED, OUTCOME_DUPLICATE]))
    print("  retries         : none, ever")
    print("  external writes : none - this receiver can reach no external system")
    print()
    print("  Self-report only. No delivery was attempted and no file was written.")
    print("  A delivery needs an approved row in a delivery-authorisations registry,")
    print("  and no delivery authorisation is approved.")
