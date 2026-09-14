# -*- coding: utf-8 -*-
"""
Client intake gate  -  00_Agency_Governance/CLIENT_INTAKE_PROFILE.md.

The question bank lives in markdown (the source of truth). This gate reads it
directly, so there is no sidecar to drift.

Modes
  (default)                 Lint the question bank: core + overlay.
                            Unique IDs, valid Stage / Req / Label codes, every `C` row
                            states its condition, every overlay adjustment names a core ID.
  --template OVERLAY --out  Write a blank answers file (every question NOT_ASKED).
                            Write it into the client folder, never into this repository.
  --answers FILE            Validate a filled answers file: every question has a declared
                            state; ANSWERED carries a value and label; non-answers carry a
                            note; no `R` row at or below `stage_reached` is left NOT_ASKED.
  --scan FILE --key KEY     Check a repo-bound file (e.g. a seed brief) before `arika run`:
                            no email, phone number, secret, money amount, or any string
                            listed in the client-folder key (real names, domains).

Usage
  python 00_Agency_Governance/intake/intake_gate.py [--overlay PATH]
  python 00_Agency_Governance/intake/intake_gate.py --template PATH --out <CLIENT>/intake_answers.json
  python 00_Agency_Governance/intake/intake_gate.py --answers <CLIENT>/intake_answers.json [--overlay PATH]
  python 00_Agency_Governance/intake/intake_gate.py --scan <CLIENT>/R4_seed_brief.json --key <CLIENT>/pilot_key.json

Exit 0 = pass. Exit 1 = a blocking defect. Exit 2 = usage error.
"""
import argparse, io, json, os, re, sys

CORE = "00_Agency_Governance/CLIENT_INTAKE_PROFILE.md"
DEFAULT_OVERLAY = "02_Offer/Hospitality Revenue Content OS - Pilot Intake Overlay.md"

STAGES = ["S0", "S1", "S2", "S3", "S4", "S5"]
REQS = {"R", "O", "C"}
LABELS = {"PUBLIC", "PUBLIC-OTA", "OWNER-SUPPLIED", "CLIENT-SUPPLIED", "CLIENT-SYSTEM"}
STATES = {"ANSWERED", "UNKNOWN", "WITHHELD", "NOT_APPLICABLE", "NOT_ASKED", "BLOCKED"}
NEEDS_NOTE = {"UNKNOWN", "WITHHELD", "NOT_APPLICABLE", "BLOCKED"}

ROW = re.compile(r"^\|\s*((?:U|H)-[A-Z]\d{2})\s*\|")

# --scan patterns: kept deliberately narrow so constraint words like "non-pricing" pass.
SCAN = [
    ("email address", re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")),
    ("phone number", re.compile(r"\+\d{1,3}[\s-]?\d{2,4}[\s-]?\d{3}[\s-]?\d{3,4}\b|\b0[17]\d{2}[\s-]?\d{3}[\s-]?\d{3}\b")),
    ("money amount", re.compile(r"(?i)(?:\b(?:USD|KES|KSH|EUR|GBP)\b|[$€£])\s?\d|\d[\d,.]*\s?(?:\b(?:USD|KES|KSH|EUR|GBP)\b|/\s?(?:month|night|mo)\b|per (?:month|night)\b)")),
    ("secret", re.compile(r"(?i)sk-ant-[\w-]+|\bapi[_-]?key\b\s*[:=]|\bpassword\b\s*[:=]")),
]


def rel(path):
    return path if os.path.isabs(path) else os.path.join(os.getcwd(), path)


def parse(path):
    """Return (questions, adjustments). A question row has exactly 7 cells;
    a 2-cell row starting with a core ID is an overlay adjustment."""
    questions, adjustments = [], []
    for n, line in enumerate(io.open(rel(path), encoding="utf-8"), 1):
        if not ROW.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7:
            qid, question, stage, req, label, feeds, missing = cells
            questions.append(dict(id=qid, question=question, stage=stage, req=req,
                                  label=label, feeds=feeds, missing=missing, file=path, line=n))
        elif len(cells) == 2:
            adjustments.append(dict(id=cells[0], text=cells[1], file=path, line=n))
        else:
            questions.append(dict(id=cells[0], bad_cells=len(cells), file=path, line=n))
    return questions, adjustments


def bank(overlay):
    q, adj = parse(CORE)
    if overlay:
        oq, oadj = parse(overlay)
        q += oq
        adj += oadj
    return q, adj


def lint(overlay):
    q, adj = bank(overlay)
    defects = []
    seen = {}
    for r in q:
        where = "%s:%d %s" % (os.path.basename(r["file"]), r["line"], r["id"])
        if "bad_cells" in r:
            defects.append("%s has %d cells, expected 7" % (where, r["bad_cells"]))
            continue
        if r["id"] in seen:
            defects.append("%s duplicates the ID at line %d" % (where, seen[r["id"]]))
        seen[r["id"]] = r["line"]
        if r["stage"] not in STAGES[1:]:
            defects.append("%s stage '%s' not in S1-S5" % (where, r["stage"]))
        if r["req"] not in REQS:
            defects.append("%s req '%s' not in R/O/C" % (where, r["req"]))
        if r["label"] not in LABELS:
            defects.append("%s label '%s' unknown" % (where, r["label"]))
        if r["req"] == "C" and "condition" not in (r["question"] + r["feeds"]).lower():
            defects.append("%s is conditional but states no condition" % where)
        if not r["missing"]:
            defects.append("%s has no if-missing rule" % where)
    core_ids = {r["id"] for r in q if r["id"].startswith("U-")}
    for a in adj:
        if a["id"] not in core_ids:
            defects.append("%s:%d adjustment names unknown core row %s"
                           % (os.path.basename(a["file"]), a["line"], a["id"]))
    return q, adj, defects


def report_bank(q, adj):
    good = [r for r in q if "bad_cells" not in r]
    print("questions: %d  (core %d, overlay %d)   overlay adjustments: %d"
          % (len(good), sum(r["id"].startswith("U-") for r in good),
             sum(r["id"].startswith("H-") for r in good), len(adj)))
    print("  stage   R    O    C")
    for s in STAGES[1:]:
        row = [sum(1 for r in good if r["stage"] == s and r["req"] == k) for k in "ROC"]
        print("  %s   %3d  %3d  %3d" % (s, row[0], row[1], row[2]))
    fast = sum(1 for r in good if r["stage"] in ("S1", "S2") and r["req"] == "R")
    print("fast set (S1+S2 required): %d" % fast)


def template(overlay, out):
    q, _, defects = lint(overlay)
    if defects:
        print("bank has defects - run the lint first")
        return 1
    if os.path.abspath(out).startswith(os.path.abspath(os.getcwd()) + os.sep) and os.path.isdir(".git"):
        print("REFUSED - %s is inside this git repository. Answers belong in the client folder." % out)
        return 1
    doc = {"pilot_id": "PILOT-H-001", "stage_reached": "S0", "answers": {}}
    for r in q:
        doc["answers"][r["id"]] = {"question": r["question"], "stage": r["stage"], "req": r["req"],
                                   "state": "NOT_ASKED", "value": None, "label": None, "note": None}
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(json.dumps(doc, ensure_ascii=False, indent=2))
    print("wrote %d blank answers to %s" % (len(q), out))
    return 0


def answers(path, overlay):
    q, _, defects = lint(overlay)
    if defects:
        print("bank has defects - run the lint first")
        return 1
    doc = json.load(io.open(path, encoding="utf-8"))
    reached = doc.get("stage_reached", "S0")
    if reached not in STAGES:
        print("FAIL - stage_reached '%s' not in %s" % (reached, STAGES))
        return 1
    level = STAGES.index(reached)
    got = doc.get("answers", {})
    fails, tally = [], {}
    for r in q:
        a = got.get(r["id"])
        if a is None:
            fails.append("%s missing from answers file" % r["id"])
            continue
        st = a.get("state")
        if st not in STATES:
            fails.append("%s state '%s' is not a declared state" % (r["id"], st))
            continue
        tally.setdefault(r["stage"], {}).setdefault(st, 0)
        tally[r["stage"]][st] += 1
        if st == "ANSWERED":
            if a.get("value") in (None, "", []):
                fails.append("%s ANSWERED with no value" % r["id"])
            label = (a.get("label") or "").strip("[] ").split(" ")[0]
            if label not in LABELS and label not in ("SECTOR", "INFERENCE"):
                fails.append("%s ANSWERED with no valid label" % r["id"])
        if st in NEEDS_NOTE and not a.get("note"):
            fails.append("%s is %s with no note (who asked / why / which gate)" % (r["id"], st))
        if st == "NOT_ASKED" and r["req"] == "R" and STAGES.index(r["stage"]) <= level:
            fails.append("%s is required at %s but NOT_ASKED (stage_reached %s)" % (r["id"], r["stage"], reached))
    extra = set(got) - {r["id"] for r in q}
    for e in sorted(extra):
        fails.append("%s is not in the question bank" % e)
    print("answers %s  stage_reached %s" % (doc.get("pilot_id"), reached))
    for s in STAGES[1:]:
        if s in tally:
            print("  %s  %s" % (s, "  ".join("%s=%d" % kv for kv in sorted(tally[s].items()))))
    for f in fails:
        print("FAIL - " + f)
    print("PASS" if not fails else "%d blocking defect(s)" % len(fails))
    return 0 if not fails else 1


def scan(path, key):
    text = io.open(path, encoding="utf-8").read()
    hits = []
    for name, pat in SCAN:
        for m in pat.finditer(text):
            hits.append("%s: '%s'" % (name, m.group(0)))
    if key:
        k = json.load(io.open(key, encoding="utf-8"))
        for s in list(k.get("real_names", [])) + list(k.get("domains", [])):
            if s and s.lower() in text.lower():
                hits.append("identifying string from the key file (not printed)")
    else:
        print("WARNING - no --key given; real names and domains were not checked")
    print("scan %s" % path)
    for h in hits:
        print("FAIL - " + h)
    print("PASS - nothing identifying, personal, secret or priced found" if not hits
          else "%d finding(s) - do not pass this file to arika run" % len(hits))
    return 0 if not hits else 1


def main():
    p = argparse.ArgumentParser(description="Client intake gate")
    p.add_argument("--overlay", default=DEFAULT_OVERLAY)
    p.add_argument("--template", metavar="OVERLAY")
    p.add_argument("--out")
    p.add_argument("--answers")
    p.add_argument("--scan")
    p.add_argument("--key")
    a = p.parse_args()
    if a.template:
        if not a.out:
            print("--template needs --out <CLIENT>/intake_answers.json")
            return 2
        return template(a.template, a.out)
    if a.answers:
        return answers(a.answers, a.overlay)
    if a.scan:
        return scan(a.scan, a.key)
    q, adj, defects = lint(a.overlay)
    print("Client intake gate  -  %s + %s\n" % (CORE, a.overlay))
    report_bank(q, adj)
    for d in defects:
        print("FAIL - " + d)
    print("\nPASS" if not defects else "\n%d blocking defect(s)" % len(defects))
    return 0 if not defects else 1


if __name__ == "__main__":
    sys.exit(main())
