# -*- coding: utf-8 -*-
"""
Sector skill-execution-record gate.

    python 01_Sector/contracts/skill_run_gate.py

`01_Sector/_memory/skill_runs.jsonl` is the department's observability store, and
under AEIT_11 a **dated execution record is the named test for `LIVE`**. That makes
its timestamps load-bearing: if they are composed rather than read, the test for the
strongest reality state is unreliable.

On 2026-09-12, 8 of the 14 records were found to claim times **up to 17.3 hours after
the file was last written** - the ids said 2026-08-28 while the timestamps walked past
midnight into a 2026-08-29 that never happened. They were written by hand, by an agent
incrementing a clock rather than reading one.

Those 8 are **grandfathered, not rewritten**. An observability log is append-only; a
store you edit when it embarrasses you is not evidence. They stay, with this gate
naming them, and nothing new may join them.

Checks:
  1  SCHEMA         every record validates against skill-execution-record.schema.json
  2  NO FUTURE      no record may be timestamped after the file was last written,
                    except the grandfathered ids below
  3  APPEND ORDER   timestamps must not go backwards
  4  UNIQUE IDS     execution_id must be unique
  5  SKILL EXISTS   every skill named must have a SKILL.md on disk

TEST_FIXTURE isolation (added 2026-09-22, prepared for draft decision SECTOR-SF1):
  6  REAL LOG CLEAN  no record in skill_runs.jsonl may carry the TEST_FIXTURE marker
                     or fixture fields. A fixture record there would be counted as
                     real evidence.
  7  FIXTURE LOG     every record in skill_runs-sandbox.jsonl must be marked, must
                     name an authorisation that is approved or spent (a DRAFT admits
                     nothing), must match that authorisation's skill, synthetic input
                     and packet, must stay within its record limit, and must not name
                     A001 (deferred under A001 D6) or a real pilot ID. Checks 1-5 apply
                     to it too, and execution ids must be unique across BOTH logs.
  8  REGISTRY        skill-fixture-authorisations.json is well-formed, and every
                     authorisation's synthetic record exists, is marked SYNTHETIC and
                     matches its pinned sha256 - so the input the owner reviewed is the
                     input that would run.

Enforcement is detective, not preventive: a skill is run by Claude Code following
SKILL.md, so no code can stop a run. This gate fails on any record that breaks the
rules, which is what makes a violation visible.
"""
import io, os, re, sys, glob, json, hashlib, datetime


def _read(path, mode="r"):
    with (io.open(path, "rb") if mode == "rb" else io.open(path, encoding="utf-8")) as fh:
        return fh.read()

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOG = os.path.join(ROOT, "01_Sector", "_memory", "skill_runs.jsonl")
FIXTURE_LOG = os.path.join(ROOT, "01_Sector", "_memory", "skill_runs-sandbox.jsonl")
SCHEMA = os.path.join(os.path.dirname(__file__), "skill-execution-record.schema.json")
AUTHS = os.path.join(os.path.dirname(__file__), "skill-fixture-authorisations.json")

FIXTURE = "TEST_FIXTURE"
STATUSES = {"draft", "approved", "spent"}
PACKET_FIELDS = ["handoff_id", "producer", "consumer", "trigger", "payload", "validation_rules",
                 "confidence_threshold", "freshness_requirement", "owner", "sla_cadence",
                 "failure_modes"]  # AEIT_09 section 1
FORBIDDEN = [(re.compile(r"\bA001\b"), "names A001, whose skill records stay deferred under A001 D6"),
             (re.compile(r"PILOT-H-\d"), "names a real pilot ID")]

# Composed, not read. Found 2026-09-12; kept because the log is append-only.
UNVERIFIABLE_TIMESTAMPS = {
    "s09-2026-08-28-gate-f-falsification-run-1",
    "s03-2026-08-28-bulk-backing-run-1",
    "s03-2026-08-28-kenya-authority-pack-1",
    "s05-2026-08-28-db16-first-profiles-1",
    "s05-2026-08-28-db15-market-routes-1",
    "s09-2026-08-28-owner-rulings-31d-31h",
    "s10-2026-08-28-offer-ready-promotion-and-exit-built",
    "s07-2026-08-29-authored-after-ownership-audit",
}


def load(path, fail, label):
    recs = []
    for i, line in enumerate(_read(path).splitlines(), 1):
        if not line.strip():
            continue
        try:
            recs.append((i, json.loads(line)))
        except ValueError as e:
            fail.append("%sLINE %d IS NOT JSON: %s" % (label, i, e))
    return recs


def check_records(recs, path, schema, fail, warn, label="", grandfathered=frozenset(), seen=None):
    """Checks 1-4 for one log. Returns {execution_id: line}."""
    if schema is not None:
        import jsonschema
        for i, r in recs:
            try:
                jsonschema.validate(r, schema)
            except jsonschema.ValidationError as e:
                fail.append("%sSCHEMA line %d (%s): %s" % (label, i, r.get("skill_id", "?"), e.message))
    written = datetime.datetime.fromtimestamp(os.path.getmtime(path), datetime.timezone.utc)
    prev, own = None, {}
    seen = {} if seen is None else seen
    for i, r in recs:
        eid = r.get("payload", {}).get("execution_id", "")
        try:
            ts = datetime.datetime.strptime(r["timestamp"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=datetime.timezone.utc)
        except Exception:
            fail.append("%sBAD TIMESTAMP line %d: %r is not YYYY-MM-DDTHH:MM:SSZ" % (label, i, r.get("timestamp")))
            continue
        if ts > written and eid not in grandfathered:
            fail.append("%sFUTURE-DATED line %d (%s): claims %s, but the log was last written %s "
                        "- %.1fh earlier. A timestamp must be READ, not composed (AEIT_11 R1)."
                        % (label, i, eid or r.get("skill_id", "?"), r["timestamp"],
                           written.strftime("%Y-%m-%dT%H:%M:%SZ"),
                           (ts - written).total_seconds() / 3600.0))
        if prev is not None and ts < prev:
            fail.append("%sOUT OF ORDER line %d (%s): %s precedes the record above it. "
                        "The log is append-only." % (label, i, eid, r["timestamp"]))
        prev = ts
        if eid in seen:
            fail.append("%sDUPLICATE execution_id %r (line %d; already used%s)."
                        % (label, eid, i, "" if eid in own else " in the other log"))
        seen[eid] = i
        own[eid] = i
    return own


def check_skills_exist(recs, root, fail, label=""):
    built = {os.path.basename(os.path.dirname(p)) for p in
             glob.glob(os.path.join(root, ".claude", "skills", "*", "SKILL.md"))}
    for i, r in recs:
        if r.get("skill") and r["skill"] not in built:
            fail.append("%sNO SUCH SKILL line %d: %r has no SKILL.md. A record of a run by a "
                        "skill that does not exist is not evidence." % (label, i, r["skill"]))


def check_real_log_clean(recs, fail):
    """Check 6."""
    for i, r in recs:
        if "classification" in r or "fixture" in r.get("payload", {}):
            fail.append("MARKED RECORD IN THE REAL LOG line %d (%s): a TEST_FIXTURE record belongs "
                        "in skill_runs-sandbox.jsonl. Here it would be counted as real evidence."
                        % (i, r.get("payload", {}).get("execution_id", "?")))


def load_auths(path, fail):
    if not os.path.exists(path):
        return None
    try:
        return json.loads(_read(path)).get("authorisations", [])
    except ValueError as e:
        fail.append("REGISTRY is not JSON: %s" % e)
        return []


def check_registry(auths, root, fail):
    """Check 8."""
    ids = set()
    for a in auths:
        aid = a.get("id", "?")
        if aid in ids:
            fail.append("REGISTRY duplicate authorisation id %r." % aid)
        ids.add(aid)
        if a.get("status") not in STATUSES:
            fail.append("REGISTRY %s: status %r is not one of %s." % (aid, a.get("status"), sorted(STATUSES)))
        rec = os.path.join(root, a.get("synthetic_record", ""))
        if not os.path.isfile(rec):
            fail.append("REGISTRY %s: synthetic record %r does not exist." % (aid, a.get("synthetic_record")))
            continue
        raw = _read(rec, "rb")
        if hashlib.sha256(raw).hexdigest() != a.get("synthetic_record_sha256"):
            fail.append("REGISTRY %s: synthetic record %r does not match its pinned sha256. "
                        "The input the owner reviewed is not the input that would run."
                        % (aid, a.get("synthetic_record")))
        try:
            body = json.loads(raw.decode("utf-8"))
        except ValueError:
            fail.append("REGISTRY %s: synthetic record is not JSON." % aid)
            continue
        if body.get("classification") != FIXTURE or body.get("synthetic") is not True:
            fail.append("REGISTRY %s: synthetic record is not marked TEST_FIXTURE and synthetic." % aid)
        for pat, why in FORBIDDEN:
            if pat.search(raw.decode("utf-8")):
                fail.append("REGISTRY %s: synthetic record %s." % (aid, why))
        if not a.get("packet", "").replace("\\", "/").startswith("01_Sector/fixtures/"):
            fail.append("REGISTRY %s: packet must live under 01_Sector/fixtures/." % aid)


def check_fixture_log(recs, auths, root, fail):
    """Check 7."""
    by_id = {a.get("id"): a for a in (auths or [])}
    counts = {}
    for i, r in recs:
        where = "FIXTURE LOG line %d" % i
        if r.get("classification") != FIXTURE:
            fail.append("%s: UNMARKED record in the fixture log. Every record here must carry "
                        "classification TEST_FIXTURE." % where)
            continue
        fx = r.get("payload", {}).get("fixture", {})
        a = by_id.get(fx.get("authorisation_id"))
        if a is None:
            fail.append("%s: names no known authorisation (%r)." % (where, fx.get("authorisation_id")))
            continue
        if a.get("status") == "draft":
            fail.append("%s: written under %s, a DRAFT authorisation. The fixture path is disabled "
                        "until the owner approves it." % (where, a["id"]))
        if a.get("status") not in ("approved", "spent"):
            continue
        if r.get("skill") != a.get("skill") or r.get("skill_id") != a.get("skill_id"):
            fail.append("%s: skill %s/%s is not the one %s authorises (%s/%s)."
                        % (where, r.get("skill"), r.get("skill_id"), a["id"], a.get("skill"), a.get("skill_id")))
        if fx.get("synthetic_record") != a.get("synthetic_record") or fx.get("packet") != a.get("packet"):
            fail.append("%s: synthetic record or packet differs from %s's." % (where, a["id"]))
        counts[a["id"]] = counts.get(a["id"], 0) + 1
        if counts[a["id"]] > a.get("max_records", 1):
            fail.append("%s: exceeds %s's limit of %d record(s)." % (where, a["id"], a.get("max_records", 1)))
        text = json.dumps(r, ensure_ascii=False)
        pkt = os.path.join(root, a.get("packet", ""))
        if not os.path.isfile(pkt):
            fail.append("%s: packet %r does not exist." % (where, a.get("packet")))
        else:
            ptext = _read(pkt)
            text += ptext
            try:
                p = json.loads(ptext)
                if p.get("classification") != FIXTURE:
                    fail.append("%s: packet is not marked TEST_FIXTURE." % where)
                missing = [f for f in PACKET_FIELDS if f not in p]
                if missing:
                    fail.append("%s: packet lacks AEIT_09 section 1 field(s): %s." % (where, ", ".join(missing)))
            except ValueError:
                fail.append("%s: packet is not JSON." % where)
        for pat, why in FORBIDDEN:
            if pat.search(text):
                fail.append("%s: record or packet %s." % (where, why))


def main(log=LOG, fixture_log=FIXTURE_LOG, auths_path=AUTHS, root=ROOT, out=print):
    fail, warn = [], []
    if not os.path.exists(log):
        out("no skill_runs.jsonl - nothing to check")
        return 0

    try:
        import jsonschema  # noqa: F401
        schema = json.loads(_read(SCHEMA))
    except ImportError:
        schema = None
        warn.append("jsonschema not installed - check 1 did not run.")

    recs = load(log, fail, "")
    seen = check_records(recs, log, schema, fail, warn, "", UNVERIFIABLE_TIMESTAMPS)
    check_skills_exist(recs, root, fail)
    check_real_log_clean(recs, fail)

    auths = load_auths(auths_path, fail)
    if auths is not None:
        check_registry(auths, root, fail)

    frecs = []
    if os.path.exists(fixture_log):
        if auths is None:
            fail.append("FIXTURE LOG exists but skill-fixture-authorisations.json does not.")
        frecs = load(fixture_log, fail, "FIXTURE LOG ")
        check_records(frecs, fixture_log, schema, fail, warn, "FIXTURE LOG ", frozenset(), dict(seen))
        check_skills_exist(frecs, root, fail, "FIXTURE LOG ")
        check_fixture_log(frecs, auths, root, fail)

    stale = UNVERIFIABLE_TIMESTAMPS - set(seen)
    if stale:
        warn.append("grandfather list names %d id(s) no longer in the log: %s"
                    % (len(stale), ", ".join(sorted(stale))))

    written = datetime.datetime.fromtimestamp(os.path.getmtime(log), datetime.timezone.utc)
    out("SECTOR SKILL-RUN GATE")
    out("=" * 66)
    out("records %d | skills referenced %d | log last written %s"
        % (len(recs), len({r.get("skill") for _, r in recs}),
           written.strftime("%Y-%m-%d %H:%M:%SZ")))
    out("  timestamps grandfathered as UNVERIFIABLE: %d of %d"
        % (len(UNVERIFIABLE_TIMESTAMPS & set(seen)), len(recs)))
    if auths is not None:
        out("  fixture authorisations: %d (%s)"
            % (len(auths), ", ".join("%s %s" % (a.get("id"), a.get("status")) for a in auths)))
    out("  fixture log: %s" % ("%d record(s)" % len(frecs) if os.path.exists(fixture_log)
                              else "absent - no TEST_FIXTURE skill run has happened"))
    out("")
    for w in warn:
        out("  WARN  " + w)
    if fail:
        out("")
        for f in fail:
            out("  FAIL  " + f)
        out("\nGATE FAILED (%d)" % len(fail))
        return 1
    out("GATE PASSED - every record validates, is uniquely identified, in order, "
        "and names a skill that exists.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
