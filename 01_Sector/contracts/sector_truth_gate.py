# -*- coding: utf-8 -*-
"""
Sector documentation-truth gate.

    python 01_Sector/contracts/sector_truth_gate.py

AEIT_11 exists because a claim about the system's state kept getting filed where a
statement about operation belonged. On 2026-09-13 that defect was found SIXTEEN more
times inside Sector itself - the department that produced AEIT_11:

  * SECTOR_WRITE_CONTRACT.md, the file every skill opens with, still said
    "Gate 1 - contract only. No skill authored, nothing written to Notion."
    Ten skills existed and had written to Notion fourteen times.
  * SECTOR_OS.md said two SKILL.md files exist. Ten did.
  * SECTOR_EVENT_CATALOG.md still used `DEAD`, a value AEIT_11 4 retires - while
    its own JSON twin had already been migrated to the five reality states.
  * SECTOR_OS_ARCHITECTURE.md had two different changelog entries both numbered v0.2.
  * sector-databases.json claimed DB 8 held 87 rows. It holds 139.

Every one of those was found by a person reading carefully. That does not scale and
it did not hold. AEIT_11 5: "Make the test runnable wherever it can be. A described
gate decays; a gate with an exit code does not."

Checks:
  1  SKILL INVENTORY   SECTOR_OS.md 6 agrees with what is on disk, both directions
  2  RETIRED VOCAB     no event described as live/dead outside a changelog (AEIT_11 4)
  3  VERSION UNIQUE    no version string appears twice in one changelog
  4  HEADER/CHANGELOG  a doc's **Version:** equals the newest entry in its changelog
  5  ROW-COUNT DATES   no verified_date in the future; warn on any older than 90 days
  6  DESTINATIONS      Hospitality plugin P5 DB 16 states agree between the markdown and
                       plugin.config.json, match DB16's verified row count, and every
                       validation destination in P4 is profiled
"""
import io, os, re, sys, glob, json, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SECTOR = os.path.join(ROOT, "01_Sector")
DBJSON = os.path.join(os.path.dirname(__file__), "sector-databases.json")
PLUGIN_MD = os.path.join(SECTOR, "sector_plugins", "hospitality", "HOSPITALITY_PLUGIN.md")
PLUGIN_CFG = os.path.join(SECTOR, "sector_plugins", "hospitality", "plugin.config.json")

# The OS-layer docs. Deliberately NOT the raw `Draft N.md` archive - those are
# unedited brainstorm exports and were never claims about the system's state.
DOCS = [
    "SECTOR_OS.md", "SECTOR_OS_ARCHITECTURE.md", "SECTOR_WRITE_CONTRACT.md",
    "SECTOR_SKILL_MATRIX.md", "SECTOR_EVENT_CATALOG.md", "SECTOR_ACTIVATION_PROTOCOL.md",
    "SECTOR_ACTIVATION_CONTRACT.md", "SECTOR_DISCOVERY_INVENTORY.md",
    "SECTOR_NOTION_SCHEMA.md", "SECTOR_CALENDAR_REFRESH_SPEC.md",
    "CALENDAR_INTELLIGENCE.md", "FIELD_POPULATION_PLAN.md", "SECTOR_CADENCE.md",
]

EVENTS = ["SECTOR_MAPPED", "ICP_CLASSIFIED", "PROSPECT_SCORED", "SECTOR_READINESS_SET",
          "CALENDAR_UPDATED", "REGULATORY_CHANGE", "DEMAND_SHIFT", "COMPRESSION_EVENT",
          "COMPETITOR_MOVE"]
STATES = ["INTENDED", "DESIGNED", "BUILT", "CONNECTED", "LIVE"]
STALE_DAYS = 90

# Proper nouns that contain a reality word without making a reality claim.
# Kept as an explicit, auditable list rather than a clever regex - a heuristic that
# silently swallows a real claim would be worse than the defect this gate catches.
EXEMPT_PHRASES = ["Live Sector Event Intelligence", "LSEI"]


def read(path):
    return io.open(path, encoding="utf-8").read() if os.path.exists(path) else None


HISTORY_HEADING = re.compile(r"^##+\s*\d*\.?\s*(Changelog|Decision Log|Risk / Incident Log)",
                             re.I)


def live_prose_lines(text):
    """Yield (lineno, line) for prose that makes a CURRENT claim.

    Changelogs and decision logs are dated historical records - they are SUPPOSED to
    contain what was once claimed, including claims later corrected. Checking them
    would fail the very entry that records a correction, which would teach people to
    stop writing corrections down. Only current prose is checked."""
    in_history = False
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            in_history = bool(HISTORY_HEADING.match(line))
        if not in_history:
            yield i, line


def changelog_versions(text):
    """Version tokens from changelog bullets, newest first (these files are
    reverse-chronological)."""
    m = re.search(r"^##+\s*\d*\.?\s*Changelog", text, re.M | re.I)
    if not m:
        return []
    return re.findall(r"^[-*]\s*\**\s*(v\d+\.\d+(?:\.\d+)?)", text[m.end():], re.M)


def main():
    fail, warn, notes = [], [], []

    # ---- 1  SKILL INVENTORY -------------------------------------------------
    disk = {}
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "skills", "sector-*", "SKILL.md"))):
        m = re.search(r"Skill\s+(S\d{2})\s+of\s+Sector", read(p) or "")
        if m:
            disk[m.group(1)] = os.path.basename(os.path.dirname(p))

    os_md = read(os.path.join(SECTOR, "SECTOR_OS.md"))
    claimed = {}
    if os_md:
        for line in os_md.splitlines():
            m = re.match(r"^\|\s*(S\d{2})\s*\|(.+)\|\s*$", line)
            if m:
                # "not built" / "unbuilt" are denials, not claims. Strip them before
                # asking whether the row says built, or a correct denial reads as a claim.
                cell = re.sub(r"not\s+\**built|\bunbuilt\b", "", m.group(2).lower())
                claimed[m.group(1)] = "built" in cell
    for sid, name in sorted(disk.items()):
        if sid not in claimed:
            fail.append("CHECK 1  %s (%s) has a SKILL.md on disk and no row in "
                        "SECTOR_OS.md 6." % (sid, name))
        elif not claimed[sid]:
            fail.append("CHECK 1  %s (%s) IS built on disk, and SECTOR_OS.md 6 does not "
                        "say so. A built thing filed as unbuilt sends the reader to do "
                        "work that is already done." % (sid, name))
    for sid, is_built in sorted(claimed.items()):
        if is_built and sid not in disk:
            fail.append("CHECK 1  %s is marked built in SECTOR_OS.md 6 and has NO "
                        "SKILL.md on disk. AEIT_11 R1: the state needs its test." % sid)
    notes.append("skills on disk %d (%s) | rows in SECTOR_OS.md 6 %d"
                 % (len(disk), ", ".join(sorted(disk)), len(claimed)))

    # ---- 2  RETIRED VOCABULARY ---------------------------------------------
    for doc in DOCS:
        text = read(os.path.join(SECTOR, doc))
        if text is None:
            continue
        for i, raw in live_prose_lines(text):
            if not any(e in raw for e in EVENTS):
                continue
            line = raw
            for phrase in EXEMPT_PHRASES:
                line = line.replace(phrase, "")
            if re.search(r"\b(dead|live)\b", line, re.I) and not any(s in line for s in STATES):
                fail.append("CHECK 2  %s:%d describes an event as live/dead. `DEAD` is "
                            "RETIRED (AEIT_11 4) - it conflated 'specified and "
                            "unsubscribed' with 'broken'. Use one of: %s."
                            % (doc, i, " / ".join(STATES)))

    # ---- 3 + 4  VERSIONS ----------------------------------------------------
    for doc in DOCS:
        text = read(os.path.join(SECTOR, doc))
        if text is None:
            continue
        vs = changelog_versions(text)
        seen = set()
        for v in vs:
            if v in seen:
                fail.append("CHECK 3  %s has TWO changelog entries numbered %s. Two "
                            "different states cannot share one version - the second is "
                            "invisible to anyone reading by version." % (doc, v))
            seen.add(v)
        hm = re.search(r"\*\*Version:\*\*\s*(v\d+\.\d+(?:\.\d+)?)", text[:2000])
        if hm and vs and hm.group(1) != vs[0]:
            fail.append("CHECK 4  %s header says %s; its newest changelog entry is %s. "
                        "The body moved and the header did not."
                        % (doc, hm.group(1), vs[0]))

    # ---- 5  ROW-COUNT DATES -------------------------------------------------
    today = datetime.date.today()
    try:
        dbs = json.load(io.open(DBJSON, encoding="utf-8"))["databases"]
    except Exception as e:
        fail.append("CHECK 5  cannot read sector-databases.json: %s" % e)
        dbs = []
    for db in dbs:
        d, name = db.get("verified_date"), db.get("name", "?")
        if not d:
            continue
        try:
            when = datetime.datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            fail.append("CHECK 5  %s: verified_date %r is not YYYY-MM-DD." % (name, d))
            continue
        if when > today:
            fail.append("CHECK 5  %s: verified_date %s is in the FUTURE (today %s). "
                        "A date is a claim (AEIT_11 5)." % (name, d, today))
        elif (today - when).days > STALE_DAYS:
            warn.append("%s: row count last verified %s (%d days ago)."
                        % (name, d, (today - when).days))

    # ---- 6  DESTINATION PROFILES (Hospitality plugin) -------------------------
    # Found 2026-09-15: plugin P5 and its sidecar still marked Diani as unauthored and
    # named Mombasa a validation destination, 18 days after DB 16 profiled Nairobi,
    # Maasai Mara and Diani. The plugin is not in DOCS, so no check saw it.
    # Truth = DB16 in sector-databases.json; the markdown wins over the sidecar.
    db16 = next((d for d in dbs if d.get("db_id") == "DB16"), None)
    md, cfg_text = read(PLUGIN_MD), read(PLUGIN_CFG)
    if db16 is None or md is None or cfg_text is None:
        fail.append("CHECK 6  cannot read DB16 in sector-databases.json, "
                    "HOSPITALITY_PLUGIN.md or plugin.config.json.")
    else:
        try:
            assign = json.loads(cfg_text)["P5"]["proposed_assignments"]
        except Exception as e:
            assign = {}
            fail.append("CHECK 6  plugin.config.json P5 proposed_assignments unreadable: %s" % e)
        cfg_state = {k: v.get("db16") for k, v in assign.items() if not k.startswith("_")}

        p5 = re.search(r"^## P5\b.*?(?=^## )", md, re.M | re.S)
        md_state = {}
        for place, cells in re.findall(r"^\|\s*\*\*(.+?)\*\*\s*\|(.*)\|\s*$",
                                       p5.group(0) if p5 else "", re.M):
            last = cells.split("|")[-1].lower()
            md_state[place] = ("not_profiled" if "not profiled" in last
                               else "profiled" if "profiled" in last else None)

        for place in sorted(set(cfg_state) | set(md_state)):
            c, m = cfg_state.get(place), md_state.get(place)
            if c not in ("profiled", "not_profiled"):
                fail.append("CHECK 6  plugin.config.json P5 %s has no db16 state "
                            "(profiled / not_profiled)." % place)
            elif c != m:
                fail.append("CHECK 6  %s: HOSPITALITY_PLUGIN.md P5 says %s, "
                            "plugin.config.json says %s. The markdown wins; regenerate "
                            "the sidecar." % (place, m, c))
            if c == "profiled" and place not in db16.get("row_count_note", ""):
                fail.append("CHECK 6  %s is marked profiled in plugin P5, but DB16's "
                            "row_count_note in sector-databases.json does not name it."
                            % place)

        profiled = sorted(p for p, s in cfg_state.items() if s == "profiled")
        verified = db16.get("row_count_verified")
        if isinstance(verified, int) and len(profiled) != verified:
            fail.append("CHECK 6  plugin P5 marks %d destination(s) profiled (%s); DB16 "
                        "row_count_verified is %d. One moved and the other did not."
                        % (len(profiled), ", ".join(profiled), verified))

        vm = re.search(r"\*\*Validation destinations[^*]*\*\*\s*(.+?)\s+—", md)
        if not vm:
            fail.append("CHECK 6  HOSPITALITY_PLUGIN.md P4 has no 'Validation destinations' line.")
        else:
            for place in (p.strip() for p in vm.group(1).split("·")):
                if cfg_state.get(place) != "profiled":
                    fail.append("CHECK 6  %s is a P4 validation destination but has no "
                                "DB 16 profile. Destination Fit (31h) would block it." % place)
        notes.append("destinations: DB16 verified %s | plugin P5 profiled %d (%s)"
                     % (verified, len(profiled), ", ".join(profiled)))

    print("SECTOR DOCUMENTATION-TRUTH GATE")
    print("=" * 66)
    for n in notes:
        print("  " + n)
    print("  docs scanned %d | events %d | today %s"
          % (sum(1 for d in DOCS if read(os.path.join(SECTOR, d))), len(EVENTS), today))
    print()
    for w in warn:
        print("  WARN  " + w)
    if fail:
        print()
        for f in fail:
            print("  FAIL  " + f)
        print("\nGATE FAILED (%d)" % len(fail))
        return 1
    print("GATE PASSED - the prose agrees with the disk, the contracts and AEIT_11.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
