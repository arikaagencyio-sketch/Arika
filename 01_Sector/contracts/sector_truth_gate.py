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
  7  DB9 PROVENANCE    DB 9's recorded 21-field structure, its seven provenance field names,
                       types and option sets, agreement across sector-databases.json,
                       intelligence-object.schema.json, SECTOR_NOTION_SCHEMA.md and S10's
                       fail-closed rules, and the explicit row-level UNRESOLVED status
                       (DB9-PROV-1, 2026-10-02)
  7b DB6/DB10 PROV     DB 6's recorded 18-field and DB 10's 15-field structures, the six
                       provenance field names, types and option sets in each, `Evidence`
                       recorded ABSENT from both, the superseded MISSING_FIELD claims with the
                       date each stopped being true, row-level status and backfill_authorised
                       false, divergence F14 recorded as propagated, open decisions OD1-OD5 all
                       still OPEN, DB 6's unsupported-Confidence conflict recorded without
                       legislating rule V3, the Q2/Q3/Q4 mappings, and S10 Step 4 naming every
                       contributing element rather than DB 9 alone
                       (DB6-DB10-PROV-1 Step 1, 2026-10-02)

Checks 7 and 7b are REPOSITORY-INTERNAL BY DESIGN. This gate NEVER CALLS NOTION, so that offline
validation stays deterministic - which means IT CANNOT DETECT LATER LIVE NOTION DRIFT in DB 6,
DB 9 or DB 10. The 21-, 18- and 15-field structures it enforces are SNAPSHOTS from two bounded
live audits (DB9-PROV-AUDIT-1 and DB6-DB10-PROV-AUDIT-1, both 2026-10-02); re-verifying any live
schema requires another separately authorised audit. A passing gate means the REPOSITORY IS
SELF-CONSISTENT, not that it still matches Notion.

Check 7b exists because of a specific, repeated failure mode: owner item 31e added provenance
fields to DB 6/9/10 on 2026-09-13 and recorded it in `_divergences` F14, but never carried it
into the three per-database entries - so one file contradicted itself for nineteen days and no
gate noticed. What 7b really enforces is PROPAGATION: that a divergence closed in one place
reached every per-database entry it touches.
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

    # ---------------------------------------------------------------- 7  DB 9 PROVENANCE
    # Added by DB9-PROV-1 (2026-10-02). REPOSITORY-INTERNAL ONLY, and deliberately so: this gate
    # must stay offline and deterministic, so it never calls Notion. It therefore cannot detect
    # LIVE DRIFT - the 21-field snapshot it enforces came from one bounded live audit
    # (DB9-PROV-AUDIT-1), and re-verifying the live schema needs another authorised audit.
    DB9_PROV = {
        "Confidence":    ("select", ["High", "Medium", "Low"]),
        "Source":        ("text",   None),
        "Source Tier":   ("select", ["T1 Primary", "T2 Institutional", "T3 Commercial-intel",
                                     "T4 Secondary"]),
        "Source URL":    ("url",    None),
        "Evidence":      ("text",   None),
        "Last Verified": ("date",   None),
        "Next Review":   ("date",   None),
    }
    dbjson = read(DBJSON)
    if not dbjson:
        fail.append("CHECK 7  sector-databases.json is missing.")
    else:
        rows = json.loads(dbjson)["databases"]
        d9 = next((r for r in rows if r.get("db_id") == "DB9"), None)
        if d9 is None:
            fail.append("CHECK 7  sector-databases.json records no DB9 entry.")
        else:
            names = [f["name"] for f in d9.get("fields", [])]
            if len(names) != 21:
                fail.append("CHECK 7  DB9 must record 21 fields (the audited live schema); "
                            "found %d." % len(names))
            if len(names) != len(set(names)):
                dupes = sorted({n for n in names if names.count(n) > 1})
                fail.append("CHECK 7  DB9 has duplicate field names: %s" % ", ".join(dupes))
            if d9.get("field_count_verified") != 21:
                fail.append("CHECK 7  DB9 field_count_verified must be 21; found %r."
                            % d9.get("field_count_verified"))
            by = {f["name"]: f for f in d9.get("fields", [])}
            for pname, (ptype, opts) in DB9_PROV.items():
                f = by.get(pname)
                if f is None:
                    fail.append("CHECK 7  DB9 does not record provenance field %r." % pname)
                    continue
                if f.get("notion_type") != ptype:
                    fail.append("CHECK 7  DB9 %s must be %s; recorded as %r."
                                % (pname, ptype, f.get("notion_type")))
                if f.get("required") is not False:
                    fail.append("CHECK 7  DB9 %s must be recorded nullable "
                                "(required: false)." % pname)
                if opts is not None and f.get("allowed_values") != opts:
                    fail.append("CHECK 7  DB9 %s option set must be %s; recorded as %r."
                                % (pname, opts, f.get("allowed_values")))
            # the superseded false claim must stay superseded, and the row-level gap must stay named
            mf = d9.get("MISSING_FIELD") or {}
            note = mf.get("note", "")
            if "NO Confidence, Source, Evidence or Last Verified field at all" in note \
                    and "FACTUALLY WRONG" not in note:
                fail.append("CHECK 7  DB9's MISSING_FIELD repeats the superseded claim without "
                            "marking it corrected.")
            rl = mf.get("row_level_status") or {}
            if rl.get("non_null_cells") != 0:
                fail.append("CHECK 7  DB9 row-level provenance must be recorded as 0 non-null "
                            "cells until a backfill is authorised; found %r."
                            % rl.get("non_null_cells"))
            if rl.get("backfill_authorised") is not False:
                fail.append("CHECK 7  DB9 must record that no row-value backfill is authorised.")
            # Q2/Q3/Q4 mapping
            iojson = read(os.path.join(os.path.dirname(DBJSON), "intelligence-object.schema.json"))
            if not iojson:
                fail.append("CHECK 7  intelligence-object.schema.json is missing.")
            else:
                props = json.loads(iojson).get("properties", {})
                for q in ("source", "when_observed", "reliability"):
                    nf = (props.get(q) or {}).get("notion_field") or {}
                    if "DB9" not in nf:
                        fail.append("CHECK 7  intelligence-object.schema.json does not map DB9 "
                                    "for %s." % q)
                mapped = (props.get("when_observed") or {}).get("notion_field", {}).get("DB9", "")
                if "Next Verification" in mapped:
                    fail.append("CHECK 7  DB9 maps `Next Verification`; the live field name is "
                                "`Next Review`.")
            # the human-readable schema doc must agree
            ns = read(os.path.join(SECTOR, "SECTOR_NOTION_SCHEMA.md")) or ""
            if "### DB 9 — Audience Roles" in ns:
                seg = ns.split("### DB 9 — Audience Roles", 1)[1].split("### DB 10", 1)[0]
                for pname in DB9_PROV:
                    if pname not in seg:
                        fail.append("CHECK 7  SECTOR_NOTION_SCHEMA.md DB 9 omits %r." % pname)
                if "21 properties" not in seg:
                    fail.append("CHECK 7  SECTOR_NOTION_SCHEMA.md DB 9 does not state 21 "
                                "properties.")
                if "UNRESOLVED" not in seg:
                    fail.append("CHECK 7  SECTOR_NOTION_SCHEMA.md DB 9 does not state that "
                                "row-level provenance is UNRESOLVED.")
            # S10 must carry the fail-closed floors
            s10 = read(os.path.join(ROOT, ".claude", "skills", "sector-handoff-packet",
                                    "SKILL.md")) or ""
            for needle, what in [
                    ("null is weaker than", "that null is weaker than Low"),
                    ("UNRESOLVED", "the UNRESOLVED outcome"),
                    ("Low < Medium < High", "the confidence ordering"),
                    ("Next Review", "the live field name Next Review"),
                    ("assembly date", "the ban on substituting the assembly date")]:
                if needle not in s10:
                    fail.append("CHECK 7  S10 SKILL.md does not state %s." % what)
            notes.append("DB9 provenance: 21 fields recorded | 7 provenance fields | "
                         "row-level 0/%d populated | snapshot from a bounded live audit, "
                         "drift undetectable offline" % (rl.get("cells") or 28))

    # ---------------------------------------------------------------- 7b  DB 6 / DB 10 PROVENANCE
    # Added by DB6-DB10-PROV-1 Step 1 (2026-10-02). SAME BOUNDARY AS CHECK 7 ABOVE: offline,
    # deterministic, repository-internal. It CANNOT DETECT LIVE NOTION DRIFT. The 18- and 15-field
    # snapshots come from one bounded live audit (DB6-DB10-PROV-AUDIT-1); re-verifying the live
    # schema needs another separately authorised audit.
    #
    # This check exists because of a specific failure: owner item 31e added provenance fields to
    # DB6/DB9/DB10 on 2026-09-13 and recorded it in _divergences F14, but never propagated it to
    # the per-database entries. One file then contradicted itself for nineteen days and nothing
    # noticed. What is enforced here is PROPAGATION - that a closed divergence reached every
    # per-database entry it touches.
    SIX = {
        "Confidence":    ("select", ["High", "Medium", "Low"]),
        "Source":        ("text",   None),
        "Source Tier":   ("select", ["T1 Primary", "T2 Institutional", "T3 Commercial-intel",
                                     "T4 Secondary"]),
        "Source URL":    ("url",    None),
        "Last Verified": ("date",   None),
        "Next Review":   ("date",   None),
    }
    COUNTS = {"DB6": 18, "DB10": 15}
    AUDIT = "DB6-DB10-PROV-AUDIT-1"
    if dbjson:
        dbj7b = json.loads(dbjson)          # read() returns raw text, as check 7 above assumes
        rows7b = dbj7b.get("databases") or []
        ns7b = read(os.path.join(SECTOR, "SECTOR_NOTION_SCHEMA.md")) or ""
        flat7b = re.sub(r"\s+", " ", ns7b)
        for db_id, want_n in sorted(COUNTS.items()):
            row = next((r for r in rows7b if r.get("db_id") == db_id), None)
            if not row:
                fail.append("CHECK 7b %s has no entry in sector-databases.json." % db_id)
                continue
            flds = row.get("fields") or []
            names = [f.get("name") for f in flds]

            # exact recorded field count, and the mechanical count key
            if len(flds) != want_n:
                fail.append("CHECK 7b %s must record %d fields (the audited live schema); "
                            "found %d." % (db_id, want_n, len(flds)))
            if row.get("field_count_verified") != want_n:
                fail.append("CHECK 7b %s field_count_verified must be %d; found %r."
                            % (db_id, want_n, row.get("field_count_verified")))
            dupes = sorted({n for n in names if names.count(n) > 1})
            if dupes:
                fail.append("CHECK 7b %s has duplicate field names: %s"
                            % (db_id, ", ".join(dupes)))

            # provenance field names and types
            by = {f.get("name"): f for f in flds}
            for pname, (ptype, opts) in sorted(SIX.items()):
                f = by.get(pname)
                if not f:
                    fail.append("CHECK 7b %s does not record provenance field %r."
                                % (db_id, pname))
                    continue
                if f.get("notion_type") != ptype:
                    fail.append("CHECK 7b %s %s must be %s; recorded as %r."
                                % (db_id, pname, ptype, f.get("notion_type")))
                if opts and sorted(f.get("allowed_values") or []) != sorted(opts):
                    fail.append("CHECK 7b %s %s option set must be %s; recorded as %r."
                                % (db_id, pname, opts, f.get("allowed_values")))

            # Evidence recorded ABSENT - not silently added, and not silently forgotten
            if "Evidence" in names:
                fail.append("CHECK 7b %s must NOT record an Evidence field: it is absent from the "
                            "live schema and no live write is authorised (open decision OD3)."
                            % db_id)
            if "Evidence" not in re.sub(r"\s+", " ", json.dumps(row)):
                fail.append("CHECK 7b %s must state that Evidence is absent, not merely omit it."
                            % db_id)

            # snapshot attribution + the drift warning
            if AUDIT not in (row.get("field_count_note") or ""):
                fail.append("CHECK 7b %s field_count_note must attribute the snapshot to %s."
                            % (db_id, AUDIT))
            mf = row.get("MISSING_FIELD") or {}
            if not re.search(r"(?i)drift", re.sub(r"\s+", " ", json.dumps(row))):
                fail.append("CHECK 7b %s must warn that live drift is undetectable offline."
                            % db_id)

            # the superseded claim must be preserved, dated, and not re-asserted
            sc = mf.get("superseded_claim") or {}
            if not sc.get("text"):
                fail.append("CHECK 7b %s MISSING_FIELD must preserve the claim it supersedes "
                            "under `superseded_claim`." % db_id)
            if "2026-09-13" not in (sc.get("became_false_on") or ""):
                fail.append("CHECK 7b %s must record 2026-09-13 as the date its prior claim "
                            "stopped being true (owner item 31e)." % db_id)
            if "SUPERSEDES" not in (mf.get("note") or ""):
                fail.append("CHECK 7b %s MISSING_FIELD must say it SUPERSEDES the prior claim."
                            % db_id)
            if "flagged, not fixed" in (mf.get("severity") or ""):
                fail.append("CHECK 7b %s severity still repeats the superseded framing."
                            % db_id)

            # row-level status must be present and must not claim completeness
            rl7b = mf.get("row_level_status") or {}
            for key in ("rows", "cells", "non_null_cells"):
                if not isinstance(rl7b.get(key), int):
                    fail.append("CHECK 7b %s row_level_status must record an integer %r."
                                % (db_id, key))
            if rl7b.get("backfill_authorised") is not False:
                fail.append("CHECK 7b %s must record backfill_authorised false." % db_id)
            for m in re.finditer(r"provenance-complete", re.sub(r"\s+", " ", json.dumps(row))):
                window = re.sub(r"\s+", " ", json.dumps(row))[max(0, m.start() - 45):m.start()]
                if "NOT" not in window:
                    fail.append("CHECK 7b %s describes itself as provenance-complete." % db_id)

            # the human-readable schema doc must agree
            nxt = {"DB6": "### DB 7", "DB10": "### DB 11"}[db_id]
            hdr = {"DB6": "### DB 6", "DB10": "### DB 10"}[db_id]
            if hdr in ns7b:
                seg = re.sub(r"\s+", " ", ns7b.split(hdr, 1)[1].split(nxt, 1)[0])
                for pname in SIX:
                    if pname not in seg:
                        fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md %s omits %r."
                                    % (db_id, pname))
                if "%d properties" % want_n not in seg:
                    fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md %s does not state %d "
                                "properties." % (db_id, want_n))
                if "Evidence` is absent" not in seg:
                    fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md %s does not state that "
                                "Evidence is absent." % db_id)
            else:
                fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md has no %s section." % hdr)

        # the phantom DB6 field must stay recorded as absent, not quietly re-listed as real
        if "`Decision-language patterns` does NOT exist in the live schema" not in flat7b:
            fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md must record that DB 6's "
                        "`Decision-language patterns` field does not exist live.")
        if "DB 11 Sector Linguistics" in flat7b:
            fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md still mis-numbers Sector Linguistics "
                        "as DB 11; it is DB 6 and DB 11 is Geography.")

        # F14's closure must be recorded as propagated, not just closed
        f14 = next((e for e in (dbj7b.get("_divergences") or [])
                    if e.get("id") == "F14"), None)
        if not f14:
            fail.append("CHECK 7b divergence F14 is missing.")
        else:
            if "resolution_update_2026_09_13" not in f14:
                fail.append("CHECK 7b F14 must keep its original 2026-09-13 closure.")
            if "resolution_update_2026_10_02" not in f14:
                fail.append("CHECK 7b F14 must record that its 2026-09-13 closure was never "
                            "propagated to the per-database entries.")

        # the five open decisions must be recorded and must all still be OPEN
        od = dbj7b.get("_open_decisions") or {}
        for k in ("OD1", "OD2", "OD3", "OD4", "OD5"):
            if k not in od:
                fail.append("CHECK 7b open decision %s is not recorded." % k)
            elif "OPEN" not in (od[k].get("status") or ""):
                fail.append("CHECK 7b open decision %s must remain OPEN; found %r."
                            % (k, od[k].get("status")))
        # DB6's unsupported-Confidence conflict must stay recorded and must not be legislated
        c6 = next((f for f in ((next((r for r in rows7b if r.get("db_id") == "DB6"), {})
                                .get("fields")) or []) if f.get("name") == "Confidence"), None)
        if c6 is None:
            fail.append("CHECK 7b DB6 records no Confidence field.")
        else:
            if "OD1" not in (c6.get("open_decision_2026_10_02") or ""):
                fail.append("CHECK 7b DB6's Confidence must carry the OD1 open conflict "
                            "(populated value, empty Source).")
            if "validation" in c6:
                fail.append("CHECK 7b DB6's Confidence must NOT carry a V3-style validation: "
                            "rule V3 is deliberately not extended to DB6 (OD1 is open).")

        # intelligence mappings
        _io_raw = read(os.path.join(os.path.dirname(DBJSON),
                                   "intelligence-object.schema.json"))
        iprops = (json.loads(_io_raw).get("properties") or {}) if _io_raw else {}
        for q, needs in (("source", ["Source", "Source Tier", "Source URL"]),
                         ("when_observed", ["Last Verified", "Next Review"]),
                         ("reliability", ["Confidence"])):
            nf = ((iprops.get(q) or {}).get("notion_field") or {})
            for db_id in ("DB6", "DB10"):
                if db_id not in nf:
                    fail.append("CHECK 7b intelligence-object.schema.json does not map %s "
                                "under %s." % (db_id, q))
                    continue
                for need in needs:
                    if need not in nf[db_id]:
                        fail.append("CHECK 7b %s %s mapping omits %r." % (db_id, q, need))
                if q == "source" and "Evidence" in nf[db_id]:
                    fail.append("CHECK 7b %s must NOT map Evidence under source: the field does "
                                "not exist live." % db_id)
                if q == "when_observed" and "Next Verification" in nf[db_id]:
                    fail.append("CHECK 7b %s uses `Next Review`, not `Next Verification`."
                                % db_id)

        # S10 Step 4 must name every contributing element, not DB9 alone
        s10b = re.sub(r"\s+", " ", read(os.path.join(
            ROOT, ".claude", "skills", "sector-handoff-packet", "SKILL.md")) or "")
        for needle, what in [
                ("DB 6", "DB 6 as a contributing element"),
                ("DB 10", "DB 10 as a contributing element"),
                ("populated `Confidence` with an EMPTY `Source`",
                 "DB 6's populated-but-unsupported Confidence"),
                ("rule V3 is deliberately NOT extended to DB 6",
                 "that rule V3 is not extended to DB 6"),
                ("`Evidence` does not exist in DB 6's or DB 10's live schema",
                 "that Evidence is absent from both"),
                ("Null and unsupported both fail closed",
                 "that null AND unsupported both fail closed"),
                ("OD2", "the undefined multi-source tier mapping")]:
            if needle not in s10b:
                fail.append("CHECK 7b S10 SKILL.md Step 4 does not state %s." % what)

        n6 = next((r for r in rows7b if r.get("db_id") == "DB6"), {})
        n10 = next((r for r in rows7b if r.get("db_id") == "DB10"), {})
        r6 = ((n6.get("MISSING_FIELD") or {}).get("row_level_status") or {})
        r10 = ((n10.get("MISSING_FIELD") or {}).get("row_level_status") or {})
        notes.append("DB6/DB10 provenance: %s/%s fields recorded | 6 provenance fields each | "
                     "Evidence absent from both | row-level %s/%s and %s/%s populated | "
                     "OD1-OD5 open | snapshot from a bounded live audit, drift undetectable "
                     "offline"
                     % (n6.get("field_count_verified"), n10.get("field_count_verified"),
                        r6.get("non_null_cells"), r6.get("cells"),
                        r10.get("non_null_cells"), r10.get("cells")))

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
