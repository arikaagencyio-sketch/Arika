# -*- coding: utf-8 -*-
"""
P2 coverage gate  -  SECTOR_OS_ARCHITECTURE.md 3.1, Rule 4.

Runs BEFORE Gate F. A falsification test on an unruled archetype cannot falsify
anything: it measures gaps in the plugin, not the structure of the market.

Checks
  1. Every P6 `dominant` or `secondary` Signal Type is ruled (verdict != unruled)
     for every archetype in the vocabulary. `watch` / `low_relevance` may stay unruled.
  2. Every archetype in the live DB16 `Asset / Property Archetypes` option set
     appears in P2.
  3. Reports ruled % per archetype AND per signal type. A signal type at 0% across
     every archetype is the `Travel-Trade` failure - now a visible number, not an absence.

Usage:  python 01_Sector/contracts/p2_coverage_gate.py [path/to/plugin.config.json]
Exit 0 = gate passes for the Tier-1 scope. Exit 1 = a blocking gap.
"""
import io, json, sys, os

DEFAULT = "01_Sector/sector_plugins/hospitality/plugin.config.json"
RULED = {"moves", "moves_weakly", "does_not_move", "not_applicable"}


def load(path):
    return json.load(io.open(path, encoding="utf-8"))


def verdicts_for(cells, archetype):
    """Return {signal_type: verdict} for one archetype, resolving inheritance
    and the legacy two-list format. Anything absent is `unruled` by default."""
    node = cells.get(archetype)
    if node is None:
        return {}
    if "_inherits" in node:
        return verdicts_for(cells, node["_inherits"])
    if node.get("_all_cells") == "unruled":
        return {}
    if node.get("_tier") == 3:
        out = {s: "moves" for s in node.get("moves_demand", [])}
        out.update({s: "does_not_move" for s in node.get("does_not_move", [])})
        return out
    return {k: v["verdict"] for k, v in node.items() if not k.startswith("_")}


def main(path):
    cfg = load(path)
    p2, p6 = cfg["P2"], cfg["P6"]
    vocab = p2["archetype_vocabulary"]
    cells = p2["property_type_rule"].get("tier1_cells", {})
    required = list(p6["dominant"]) + list(p6["secondary"])
    scope = p2["property_type_rule"].get("tier1_scope", {})
    tier1_types = scope.get("signal_types", p6["dominant"])
    tier1_archs = scope.get("archetypes", [])

    print("P2 coverage gate  -  %s" % path)
    print("archetypes in vocabulary: %d   required signal types (dominant+secondary): %d\n"
          % (len(vocab), len(required)))

    # check 2 first: vocabulary presence
    missing_arch = [a for a in vocab if a not in cells]
    if missing_arch:
        print("CHECK 2 FAIL - archetypes in the vocabulary with no P2 entry at all:")
        for a in missing_arch:
            print("    %s" % a)
    else:
        print("CHECK 2 pass - every archetype in the vocabulary appears in P2.")
    print("")

    # check 3: per-archetype coverage
    print("ruled %% per archetype (against the %d required types)" % len(required))
    per_arch = {}
    for a in vocab:
        v = verdicts_for(cells, a)
        got = sum(1 for s in required if v.get(s) in RULED)
        per_arch[a] = got
        flag = "  <-- TIER 1" if a in tier1_archs else ""
        print("    %-26s %3d/%-3d  %3.0f%%%s" % (a, got, len(required), 100.0 * got / len(required), flag))
    print("")

    # check 3: per-signal-type coverage
    print("ruled %% per signal type (across all %d archetypes)" % len(vocab))
    zero = []
    for s in required:
        got = sum(1 for a in vocab if verdicts_for(cells, a).get(s) in RULED)
        if got == 0:
            zero.append(s)
        mark = "  <-- RULED BY NO ARCHETYPE" if got == 0 else ""
        print("    %-24s %3d/%-3d  %3.0f%%%s" % (s, got, len(vocab), 100.0 * got / len(vocab), mark))
    print("")

    # check 1, scoped to Tier 1 - the blocking condition
    blocking = []
    for a in tier1_archs:
        v = verdicts_for(cells, a)
        for s in tier1_types:
            if v.get(s) not in RULED:
                blocking.append((a, s))

    if blocking:
        print("CHECK 1 FAIL - Tier-1 cells unruled. Gate F MUST NOT run against these archetypes:")
        for a, s in blocking:
            print("    %-26s x  %s" % (a, s))
        return 1

    print("CHECK 1 pass - all %d Tier-1 cells ruled (%d archetypes x %d dominant types)."
          % (len(tier1_archs) * len(tier1_types), len(tier1_archs), len(tier1_types)))
    if zero:
        print("\nWARNING (not blocking): %d required signal type(s) ruled by NO archetype: %s"
              % (len(zero), ", ".join(zero)))
    if missing_arch:
        print("\nWARNING (not blocking): %d archetype(s) absent from P2." % len(missing_arch))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT))
