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
"""
import io, os, sys, glob, json, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOG = os.path.join(ROOT, "01_Sector", "_memory", "skill_runs.jsonl")
SCHEMA = os.path.join(os.path.dirname(__file__), "skill-execution-record.schema.json")

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


def main():
    fail, warn = [], []
    if not os.path.exists(LOG):
        print("no skill_runs.jsonl - nothing to check")
        return 0

    recs = []
    for i, line in enumerate(io.open(LOG, encoding="utf-8"), 1):
        if not line.strip():
            continue
        try:
            recs.append((i, json.loads(line)))
        except ValueError as e:
            fail.append("LINE %d IS NOT JSON: %s" % (i, e))

    try:
        import jsonschema
        schema = json.load(io.open(SCHEMA, encoding="utf-8"))
        for i, r in recs:
            try:
                jsonschema.validate(r, schema)
            except jsonschema.ValidationError as e:
                fail.append("SCHEMA line %d (%s): %s" % (i, r.get("skill_id", "?"), e.message))
    except ImportError:
        warn.append("jsonschema not installed - check 1 did not run.")

    written = datetime.datetime.fromtimestamp(os.path.getmtime(LOG), datetime.timezone.utc)
    prev, seen = None, {}
    for i, r in recs:
        eid = r.get("payload", {}).get("execution_id", "")
        try:
            ts = datetime.datetime.strptime(r["timestamp"], "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=datetime.timezone.utc)
        except Exception:
            fail.append("BAD TIMESTAMP line %d: %r is not YYYY-MM-DDTHH:MM:SSZ" % (i, r.get("timestamp")))
            continue

        if ts > written and eid not in UNVERIFIABLE_TIMESTAMPS:
            fail.append("FUTURE-DATED line %d (%s): claims %s, but the log was last written %s "
                        "- %.1fh earlier. A timestamp must be READ, not composed (AEIT_11 R1)."
                        % (i, eid or r.get("skill_id", "?"), r["timestamp"],
                           written.strftime("%Y-%m-%dT%H:%M:%SZ"),
                           (ts - written).total_seconds() / 3600.0))
        if prev is not None and ts < prev:
            fail.append("OUT OF ORDER line %d (%s): %s precedes the record above it. "
                        "The log is append-only." % (i, eid, r["timestamp"]))
        prev = ts
        if eid in seen:
            fail.append("DUPLICATE execution_id %r on lines %d and %d." % (eid, seen[eid], i))
        seen[eid] = i

    built = {os.path.basename(os.path.dirname(p)) for p in
             glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "SKILL.md"))}
    for i, r in recs:
        if r.get("skill") and r["skill"] not in built:
            fail.append("NO SUCH SKILL line %d: %r has no SKILL.md. A record of a run by a "
                        "skill that does not exist is not evidence." % (i, r["skill"]))

    stale = UNVERIFIABLE_TIMESTAMPS - set(seen)
    if stale:
        warn.append("grandfather list names %d id(s) no longer in the log: %s"
                    % (len(stale), ", ".join(sorted(stale))))

    print("SECTOR SKILL-RUN GATE")
    print("=" * 66)
    print("records %d | skills referenced %d | log last written %s"
          % (len(recs), len({r.get("skill") for _, r in recs}),
             written.strftime("%Y-%m-%d %H:%M:%SZ")))
    print("  timestamps grandfathered as UNVERIFIABLE: %d of %d"
          % (len(UNVERIFIABLE_TIMESTAMPS & set(seen)), len(recs)))
    print()
    for w in warn:
        print("  WARN  " + w)
    if fail:
        print()
        for f in fail:
            print("  FAIL  " + f)
        print("\nGATE FAILED (%d)" % len(fail))
        return 1
    print("GATE PASSED - every record validates, is uniquely identified, in order, "
          "and names a skill that exists.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
