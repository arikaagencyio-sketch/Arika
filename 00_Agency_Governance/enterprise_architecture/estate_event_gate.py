# -*- coding: utf-8 -*-
"""
AEIT_11 estate event gate.

Runs the Runtime Truth Standard against the whole agent estate and EXITS 1 when a
claim about the system's state has stopped being true. Written because the standard
was, until now, a described gate rather than a runnable one.

    python 00_Agency_Governance/enterprise_architecture/estate_event_gate.py

Checks, in order of what they protect:

  0  PARSER INTEGRITY  every agent must yield at least one parseable `emits`.
                       An `emits: [A, B]` inline list read by a block-only regex
                       silently reports zero edges and a clean estate. That bug
                       happened on 2026-08-29; this check exists because of it.
  1  ORPHAN REGISTER   every event an agent waits on that NO agent emits must be
                       classified in estate-event-register.json (AEIT_11 R7).
  2  NO STALE ENTRIES  a registered orphan that has since gained an emitter must be
                       removed, or the register is describing a repo that moved on.
  3  NO UNRULED HOLES  a `producer_unassigned` entry still carrying the UNCLASSIFIED
                       marker is a hole nobody has ruled on.
  4  RUNTIME REALITY   executor.ts must still not publish. If it ever does, every
                       CONNECTED edge in the estate becomes a LIVE candidate and the
                       reality states must be re-derived, not inherited (R2).
  5  PROSE MATCHES     every count AEIT_11_ESTATE_AUDIT.md states in prose must equal
                       the measurement. Written after that audit claimed Presence held
                       5 of the 11 unassigned producers; it held 6. A number inside a
                       sentence is a claim like any other and needs its test (R1).
  6  NO NEW RE-ENTRY   no agent may emit an event it also subscribes to unless the edge
                       is already recorded in the register. The bus is a bare node
                       EventEmitter - no cycle detection, no depth limit, no dedupe -
                       so a pure loop (sole emitter == sole subscriber == same agent)
                       does not terminate once executor.ts starts publishing.
"""
import io, os, re, sys, glob, json, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REG  = os.path.join(os.path.dirname(__file__), "estate-event-register.json")
DOC  = os.path.join(os.path.dirname(__file__), "AEIT_11_ESTATE_AUDIT.md")
BASELINE = {"agents": 115, "emit_declarations": 201, "emit_distinct": 195,
            "subscriptions": 184, "sub_distinct": 145, "union_distinct": 269,
            "both_ends": 71, "emit_no_sub": 124, "sub_no_emit": 74}


def parse():
    emit, sub, dept, zero = collections.defaultdict(list), collections.defaultdict(list), {}, []
    for a in sorted(glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md"))):
        n = os.path.basename(a)[:-3]
        s = io.open(a, encoding="utf-8").read()
        fm = s.split("---")[1] if s.startswith("---") else s
        m = re.search(r"^department:\s*\"?([0-9]+)\"?", fm, re.M)
        dept[n] = m.group(1) if m else "??"
        got = 0
        mb = re.search(r"^emits:\s*\n((?:\s+-\s+\S+\n)+)", fm, re.M)
        if mb:
            for e in re.findall(r"-\s+([A-Za-z_][A-Za-z0-9_]*)", mb.group(1)):
                emit[e].append(n); got += 1
        mi = re.search(r"^emits:\s*\[([^\]]*)\]", fm, re.M)
        if mi:
            for e in [x.strip() for x in mi.group(1).split(",") if x.strip()]:
                emit[e].append(n); got += 1
        if got == 0:
            zero.append(n)
        for e in re.findall(r"^\s+on:\s*([A-Za-z_][A-Za-z0-9_]*)", fm, re.M):
            sub[e].append(n)
    return emit, sub, dept, zero


def check_audit_prose(measured, entries, fail):
    """Check 5 - the audit states counts in prose, and prose does not recompute."""
    if not os.path.exists(DOC):
        fail.append("AEIT_11_ESTATE_AUDIT.md not found - the prose check did not run.")
        return
    t = io.open(DOC, encoding="utf-8").read()
    cls = collections.Counter(v["classification"] for v in entries.values())
    nu = cls["producer_unassigned"]
    by21 = len([v for v in entries.values()
                if v["classification"] == "producer_unassigned"
                and "21" in v["waiting_departments"]])
    B = r"\*\*"
    claims = [
        (r"\| `emits` declarations \| " + B + r"(\d+)" + B,        measured["emit_declarations"], "emits declarations"),
        (r"\(" + B + r"(\d+)" + B + r" distinct event names",      measured["emit_distinct"],     "distinct emitted names"),
        (r"\| Event subscriptions \| " + B + r"(\d+)" + B,         measured["subscriptions"],     "subscriptions"),
        (r"\| Distinct events in the estate \| " + B + r"(\d+)" + B, measured["union_distinct"],  "distinct events"),
        (B + r"Both ends named" + B + r" \| " + B + r"(\d+)" + B,  measured["both_ends"],         "both-ends edges"),
        (B + r"Emitter, no subscriber" + B + r" \| " + B + r"(\d+)" + B, measured["emit_no_sub"], "emitter-only edges"),
        (B + r"Subscriber, no emitter" + B + r" \| " + B + r"(\d+)" + B, measured["sub_no_emit"], "subscriber-only edges"),
        (r"`external_entry_point` \| " + B + r"(\d+)" + B,         cls["external_entry_point"],   "external entry points"),
        (r"`manual_entry_point` \| " + B + r"(\d+)" + B,           cls["manual_entry_point"],     "manual entry points"),
        (r"`producer_unassigned` \| " + B + r"(\d+)" + B,          nu,                            "unassigned producers"),
        (r"### 3\.1 The (\d+) real holes",                          nu,                            "section 3.1 heading"),
        (r"0 of (\d+) subscriptions has ever fired",                measured["subscriptions"],     "subscriptions never fired"),
        (B + r"Presence \(21\) holds (\d+) of the (\d+)" + B,      (by21, nu),                    "Presence share"),
    ]
    for pat, want, label in claims:
        m = re.search(pat, t)
        if m is None:
            fail.append("PROSE CLAIM MISSING: the audit no longer states %s in the expected form." % label)
            continue
        got = tuple(int(g) for g in m.groups()) if len(m.groups()) > 1 else int(m.group(1))
        if got != want:
            fail.append("PROSE DRIFT: the audit states %s = %s; measured %s." % (label, got, want))

    rows = re.search(r"### 3\.1 The \d+ real holes\s*\n\s*\n\|[^\n]*\n\|[-| ]+\|\n((?:\|[^\n]*\n)+)", t)
    if rows is None:
        fail.append("PROSE CLAIM MISSING: section 3.1's table of holes did not parse.")
    else:
        listed = [l for l in rows.group(1).splitlines() if l.strip().startswith("|")]
        if len(listed) != nu:
            fail.append("PROSE DRIFT: section 3.1 lists %d holes; the register holds %d." % (len(listed), nu))


def check_reentrancy(emit, sub, reg, fail):
    """Check 6 - an agent that emits what it subscribes to re-enters itself.

    The bus (arika-runtime/src/triggers/event-bus.ts) is a bare node EventEmitter:
    publish() calls emitter.emit() synchronously with no cycle detection, no depth
    limit and no dedupe. A PURE loop - sole emitter == sole subscriber == same agent -
    therefore does not terminate. Three exist today, all in Finance (09).

    They are recorded rather than fixed: they belong to their departments. This check
    fails on any edge NOT already recorded, so the set cannot grow silently.
    """
    known = reg.get("known_reentrant_edges", {})
    allowed = set(known.get("pure_nonterminating", [])) | set(known.get("shared_topic", []))
    for e in sorted(set(emit) & set(sub)):
        if set(emit[e]) & set(sub[e]) and e not in allowed:
            who = sorted(set(emit[e]) & set(sub[e]))
            pure = len(emit[e]) == 1 and len(sub[e]) == 1
            fail.append("NEW RE-ENTRANT EDGE: %s is emitted and subscribed by %s%s. "
                        "The bus has no cycle detection - record it in "
                        "known_reentrant_edges or break the loop."
                        % (e, ", ".join(who),
                           " and NOTHING ELSE TOUCHES IT, so it would not terminate" if pure else ""))
    for e in sorted(allowed):
        if not (set(emit.get(e, [])) & set(sub.get(e, []))):
            fail.append("STALE RE-ENTRANCY RECORD: %s is listed as re-entrant and is no longer. "
                        "Remove it." % e)

def main():
    fail, warn = [], []
    emit, sub, dept, zero = parse()
    n_agents = len(glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md")))

    if zero:
        fail.append("PARSER INTEGRITY: %d agent(s) yielded no parseable `emits` - %s"
                    % (len(zero), ", ".join(zero[:6])))

    both   = set(emit) & set(sub)
    no_sub = set(emit) - set(sub)
    no_em  = set(sub) - set(emit)
    measured = {"agents": n_agents,
                "emit_declarations": sum(len(v) for v in emit.values()),
                "emit_distinct": len(emit),
                "subscriptions": sum(len(v) for v in sub.values()),
                "sub_distinct": len(sub),
                "union_distinct": len(set(emit) | set(sub)),
                "both_ends": len(both), "emit_no_sub": len(no_sub), "sub_no_emit": len(no_em)}

    reg = json.load(io.open(REG, encoding="utf-8"))
    entries = {e["event"]: e for e in reg["entries"]}

    for e in sorted(no_em - set(entries)):
        fail.append("UNREGISTERED ORPHAN: %s - waited on by %s (dept %s) and emitted by nobody. "
                    "AEIT_11 R7 requires a classification."
                    % (e, ", ".join(sorted(sub[e])), ",".join(sorted({dept[x] for x in sub[e]}))))
    for e in sorted(set(entries) - no_em):
        fail.append("STALE REGISTER ENTRY: %s is registered as having no emitter, but %s"
                    % (e, ("%s now emits it" % ", ".join(emit[e])) if e in emit
                       else "no agent subscribes to it any more"))
    for e, v in sorted(entries.items()):
        if "UNCLASSIFIED" in v.get("evidence", ""):
            fail.append("UNRULED HOLE: %s is parked as producer_unassigned with no ruling." % e)

    ex = os.path.join(ROOT, "arika-runtime", "src", "executor.ts")
    if os.path.exists(ex):
        src = io.open(ex, encoding="utf-8").read()
        if "publish(" in src or "event-bus" in src:
            fail.append("RUNTIME REALITY CHANGED: executor.ts now references the event bus. "
                        "Every CONNECTED edge must be re-tested before any LIVE claim (AEIT_11 R2).")
    else:
        warn.append("executor.ts not found - the runtime-reality check did not run.")

    check_reentrancy(emit, sub, reg, fail)
    check_audit_prose(measured, entries, fail)

    for k, v in sorted(BASELINE.items()):
        if measured[k] != v:
            warn.append("count drift: %-18s baseline %-4d measured %-4d" % (k, v, measured[k]))

    c = collections.Counter(v["classification"] for v in entries.values())
    print("AEIT_11 ESTATE EVENT GATE")
    print("=" * 66)
    print("agents %d | emits declared %d (%d distinct) | subscriptions %d (%d distinct)"
          % (measured["agents"], measured["emit_declarations"], measured["emit_distinct"],
             measured["subscriptions"], measured["sub_distinct"]))
    print("CONNECTED (both ends) %d | DESIGNED, no subscriber %d | no emitter %d"
          % (measured["both_ends"], measured["emit_no_sub"], measured["sub_no_emit"]))
    print("  register: external %d | manual %d | PRODUCER UNASSIGNED %d"
          % (c["external_entry_point"], c["manual_entry_point"], c["producer_unassigned"]))
    kr = reg.get("known_reentrant_edges", {})
    print("  re-entrant edges: %d recorded, of which %d would NOT terminate"
          % (len(kr.get("pure_nonterminating", [])) + len(kr.get("shared_topic", [])),
             len(kr.get("pure_nonterminating", []))))
    print()
    for w in warn:
        print("  WARN  " + w)
    if fail:
        print()
        for f in fail:
            print("  FAIL  " + f)
        print("\nGATE FAILED (%d)" % len(fail))
        return 1
    print("GATE PASSED - every orphaned wait is classified, the audit's prose matches the "
          "measurement, and the runtime still does not publish.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
