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
  7b DB6/DB10 PROV     DB 6's recorded 19-field and DB 10's 16-field structures, the SEVEN
                       provenance field names, types and option sets in each, `Evidence` recorded
                       PRESENT as nullable text with NULL row values, the superseded
                       MISSING_FIELD claims with the date each stopped being true, row-level
                       status (rows x 7 cells) and backfill_authorised false, divergence F14
                       recorded as propagated and schema-closed, OD3 CLOSED while OD1/OD2/OD4/OD5
                       stay OPEN, the shared seven-field shape recorded as OBSERVED and NOT
                       ratified, DB 6's unsupported-Confidence conflict recorded without
                       legislating rule V3, the Q2/Q3/Q4 mappings, and S10 Step 4 naming every
                       contributing element rather than DB 9 alone
                       (DB6-DB10-PROV-1 Step 1 + Step 2, 2026-10-02)
  7b DB6 OD1/OD2       the 13-cell DB6 backfill (17 of 28 populated), Confidence untouched and
                       still required with no V3 validator, Source Tier and Source URL null by
                       the DB6-LOCAL multi-source convention, the ONE named Buyer exception
                       (scope, expiry 2026-11-24, no auto-renewal, not a class of rows), OD1
                       closed-with-exception, OD2 closed LOCALLY only, OD4/OD5/OD6 open, the DB3
                       finding recorded unmutated, and S10's freshness floor failing closed on
                       EITHER a null Last Verified or a null Next Review
                       (DB6-OD1-OD2-1, 2026-10-02)
  7c DB3 PROVENANCE    DB 3's recorded 17-field count with the superseded 15 preserved,
                       `Source` as a four-value PROCESS-KIND select, `Evidence` required and
                       recorded populated 217/217, `Last Verified` and `Next Review` recorded
                       PRESENT-BUT-NULL 0/217 with `Next Verification` still absent and
                       `Source Tier`/`Source URL` still STRUCTURALLY ABSENT, `Freshness` recorded
                       NON-GOVERNING and not derived, OD6 superseded-and-re-scoped with its
                       disproven claim preserved, OD10 CLOSED BY DISSOLUTION with its original
                       question preserved, OD7-OD9/OD11-OD13 open, OD12's three High rows
                       classified, no seven-field-shape ratification, the intelligence-object Q2
                       mapping left as `Evidence + Source`, and S10 Step 4 naming ALL FOUR
                       contributing elements with DB 3's freshness failing closed EMPTILY
                       (DB3-PROV-1 Step A + DB3-OD10-OD12-1, 2026-10-02)

Checks 7, 7b and 7c are REPOSITORY-INTERNAL BY DESIGN. This gate NEVER CALLS NOTION, so that offline
validation stays deterministic - which means IT CANNOT DETECT LATER LIVE NOTION DRIFT in DB 6,
DB 9 or DB 10. The 21-, 19- and 16-field structures it enforces are SNAPSHOTS from two bounded
live audits (DB9-PROV-AUDIT-1 and DB6-DB10-PROV-AUDIT-1, both 2026-10-02) plus the verified
post-write reads of DB6-DB10-PROV-1 Step 2; re-verifying any live schema requires another
separately authorised audit. A passing gate means the REPOSITORY IS SELF-CONSISTENT, not that it
still matches Notion.

A further limit worth stating because Step 2 invites the mistake: `Evidence` EXISTS in DB 6, DB 9
and DB 10. A column is a place to put evidence, not evidence. This gate checks that the repository
records that distinction; it cannot check that anyone honours it.

CHECK 7c ADDS A SHARPER LIMIT, AND ITS SUBJECT CHANGED ON 2026-10-02. It used to read:
"DB 3 has NO `Last Verified`, NO `Next Review` and NO `Source Tier` FIELD AT ALL - an ABSENT
FIELD, not an empty cell." THAT WAS TRUE WHEN WRITTEN AND IS NOW TRUE OF `Source Tier` AND
`Source URL` ONLY. DB3-OD10-OD12-1 added `Last Verified` and `Next Review` as nullable live date
properties under OD10 Option D, so DB 3's temporal fields moved from ABSENT to PRESENT-BUT-NULL.

THREE STATES MUST BE DISTINGUISHED, NOT TWO: absent, present-but-null, and present-and-populated.
Absent and present-but-null BOTH fail closed, but only the second can ever be filled, so a reader
must be told which one they are looking at. This gate enforces that the repository states the
difference - and it enforces that the OLD claim is PRESERVED AND SUPERSEDED rather than silently
corrected, because a dated claim that stops being true is the exact failure class check 7b exists
for.

The limits are otherwise unchanged. This gate CANNOT verify DB 3's live schema: the 17-field count
and the two null date columns are a SNAPSHOT from the verified post-write reads of
DB3-OD10-OD12-1, and DB 3's 217 rows are recorded from ONE bounded audit (DB3-PROV-AUDIT-1), of
which 211 were never body-read. The three High-confidence rows WERE body-read under separate owner
authorisation and are now classified; the gate enforces that those classifications are recorded
as read-and-blank, and must never be read as confirming anything about the other 211.

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
        "Evidence":      ("text",   None),   # added live 2026-10-02 by Step 2
    }
    COUNTS = {"DB6": 19, "DB10": 16}
    AUDIT = "DB6-DB10-PROV-AUDIT-1"
    STEP2 = "DB6-DB10-PROV-1 Step 2"
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

            # Evidence recorded PRESENT, nullable text, with NULL row values.
            # INVERTED 2026-10-02 by Step 2, which added the field under its own owner approval.
            ev = by.get("Evidence")
            if not ev:
                fail.append("CHECK 7b %s must record the Evidence field added live by Step 2."
                            % db_id)
            else:
                if ev.get("notion_type") != "text":
                    fail.append("CHECK 7b %s Evidence must be text; recorded as %r."
                                % (db_id, ev.get("notion_type")))
                if ev.get("required", False):
                    fail.append("CHECK 7b %s Evidence must be recorded nullable." % db_id)
                if "NULL" not in (ev.get("row_values") or ""):
                    fail.append("CHECK 7b %s Evidence row values must be recorded NULL: adding a "
                                "column is not adding evidence." % db_id)
                if STEP2 not in (ev.get("provenance_of_record") or ""):
                    fail.append("CHECK 7b %s Evidence must be attributed to Step 2, not to the "
                                "2026-09-13 item 31e additions." % db_id)
            # attribution of the six vs the one must stay distinct
            for pname in ("Source", "Source Tier", "Source URL", "Last Verified", "Next Review"):
                f = by.get(pname) or {}
                if "31e" not in (f.get("schema_history") or ""):
                    fail.append("CHECK 7b %s %s must stay attributed to owner item 31e."
                                % (db_id, pname))

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
            # "SUPERSED" covers Step 1's "SUPERSEDES" and Step 2's "SUPERSEDED IN PART" - both
            # supersede rather than silently replace, which is the invariant that matters.
            if "SUPERSED" not in (mf.get("note") or ""):
                fail.append("CHECK 7b %s MISSING_FIELD must say it supersedes the prior claim, "
                            "not silently replace it." % db_id)
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
            if rl7b.get("provenance_fields_live") != 7:
                fail.append("CHECK 7b %s must record 7 live provenance fields; found %r."
                            % (db_id, rl7b.get("provenance_fields_live")))
            if isinstance(rl7b.get("rows"), int) and isinstance(rl7b.get("cells"), int):
                if rl7b["rows"] * 7 != rl7b["cells"]:
                    fail.append("CHECK 7b %s cells (%d) must equal rows (%d) x 7."
                                % (db_id, rl7b["cells"], rl7b["rows"]))
            if "NULL" not in (rl7b.get("evidence_row_values") or ""):
                fail.append("CHECK 7b %s must record that Evidence is NULL on every row."
                            % db_id)
            # the schema/row distinction must be stated, never blurred into one claim
            _mfb = (mf.get("status") or "") + (mf.get("note") or "")
            if "SCHEMA GAP" not in _mfb or "ROW-LEVEL PROVENANCE" not in _mfb:
                fail.append("CHECK 7b %s must state the schema gap and row-level provenance "
                            "SEPARATELY - closing one closes nothing about the other." % db_id)
            if not re.search(r"(?i)field existence|column exists",
                             re.sub(r"\s+", " ", json.dumps(row))):
                fail.append("CHECK 7b %s must warn that field existence is not evidence."
                            % db_id)
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
                if "Evidence` now EXISTS" not in seg:
                    fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md %s does not state that "
                                "Evidence now exists live." % db_id)
                if not re.search(r"(?i)column existing is not evidence", seg):
                    fail.append("CHECK 7b SECTOR_NOTION_SCHEMA.md %s does not warn that a column "
                                "existing is not evidence." % db_id)
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
        # OD3 was CLOSED by Step 2. The other four must still be OPEN - closing the schema gap
        # resolves nothing about rows, conventions or standardisation.
        if od.get("OD3") is not None:
            if "CLOSED" not in (od["OD3"].get("status") or ""):
                fail.append("CHECK 7b OD3 must be recorded CLOSED by Step 2; found %r."
                            % od["OD3"].get("status"))
            if STEP2 not in (od["OD3"].get("closed_by") or ""):
                fail.append("CHECK 7b OD3 must name Step 2 as what closed it.")
            if "remain OPEN" not in (od["OD3"].get("what_it_did_not_close") or ""):
                fail.append("CHECK 7b OD3 must record what closing it did NOT close.")
        # OD1 and OD2 were CLOSED 2026-10-02 by DB6-OD1-OD2-1 - OD1 with ONE named exception,
        # OD2 LOCALLY for DB6 only. OD4, OD5 and the new OD6 must stay OPEN.
        if od.get("OD1") is not None:
            st1 = od["OD1"].get("status") or ""
            if "CLOSED" not in st1:
                fail.append("CHECK 7b OD1 must be recorded CLOSED by DB6-OD1-OD2-1; found %r."
                            % st1)
            if "EXCEPTION" not in st1.upper():
                fail.append("CHECK 7b OD1's closure must name its exception.")
            if "what_it_did_not_close" not in od["OD1"]:
                fail.append("CHECK 7b OD1 must record what closing it did NOT close.")
        if od.get("OD2") is not None:
            st2 = od["OD2"].get("status") or ""
            if "CLOSED LOCALLY" not in st2:
                fail.append("CHECK 7b OD2 must be recorded CLOSED LOCALLY for DB6; found %r."
                            % st2)
            if "NOT A SECTOR-WIDE RATIFICATION" not in st2:
                fail.append("CHECK 7b OD2's local closure must deny Sector-wide ratification.")
            if "V4" not in (od["OD2"].get("scope_warning") or ""):
                fail.append("CHECK 7b OD2 must warn that DB9's rule V4 is unchanged.")
        for k in ("OD4", "OD5", "OD6"):
            if k in od:
                st_k = od[k].get("status") or ""
                if "OPEN" not in st_k:
                    fail.append("CHECK 7b open decision %s must remain OPEN; found %r."
                                % (k, st_k))
                if "CLOSED" in st_k:
                    fail.append("CHECK 7b open decision %s must not be closed." % k)
            else:
                fail.append("CHECK 7b open decision %s is not recorded." % k)
        # OD6 - the DB3 finding - must stay recorded and must have caused no DB3 mutation
        od6 = od.get("OD6") or {}
        if od6.get("db") != "DB3":
            fail.append("CHECK 7b OD6 must record the DB3 unsupported-provenance finding.")
        # Requires the CURRENT statement by key. Searching the whole record is not enough: OD6's
        # `superseded_claim` preserves the original facts, one of which also says "NOT mutated",
        # so a loose search passed even after the live statement was deleted. Mutation testing
        # found that; the lesson is that a check over preserved history is not a check over
        # current state.
        if "NOT mutated" not in (od6.get("db3_not_mutated") or ""):
            fail.append("CHECK 7b OD6 must record, in `db3_not_mutated`, that DB3 was NOT "
                        "mutated. A statement inside the preserved `superseded_claim` does not "
                        "satisfy this - that is history, not current state.")
        d3row = next((r for r in rows7b if r.get("db_id") == "DB3"), None)
        if d3row is not None and "od1_exception" in d3row:
            fail.append("CHECK 7b DB3 must carry no OD1 exception - it was not in scope.")

        # ---- the 13-cell backfill and the DB6-local convention
        d6b = next((r for r in rows7b if r.get("db_id") == "DB6"), None)
        if d6b is not None:
            mf6 = d6b.get("MISSING_FIELD") or {}
            rl6 = mf6.get("row_level_status") or {}
            by6 = {f.get("name"): f for f in (d6b.get("fields") or [])}
            if rl6.get("non_null_cells") != 17:
                fail.append("CHECK 7b DB6 must record 17 populated provenance cells "
                            "(4 Confidence + 13 backfilled); found %r."
                            % rl6.get("non_null_cells"))
            if (isinstance(rl6.get("non_null_cells"), int)
                    and isinstance(rl6.get("null_cells"), int)
                    and rl6["non_null_cells"] + rl6["null_cells"] != rl6.get("cells")):
                fail.append("CHECK 7b DB6 populated + null must equal %r cells."
                            % rl6.get("cells"))
            bp = rl6.get("backfill_performed") or {}
            if bp.get("cells_written") != 13:
                fail.append("CHECK 7b DB6 must record 13 cells written; found %r."
                            % bp.get("cells_written"))
            if rl6.get("backfill_authorised") is not False:
                fail.append("CHECK 7b DB6 backfill_authorised must stay false - the fail-closed "
                            "default must survive its own exercise.")
            for must in ("Confidence", "Source Tier", "Source URL", "Buyer"):
                if must not in (bp.get("not_written") or ""):
                    fail.append("CHECK 7b DB6 backfill record must state %s was NOT written."
                                % must)
            # Confidence untouched and still required
            c6b = by6.get("Confidence") or {}
            if c6b.get("required") is not True:
                fail.append("CHECK 7b DB6 Confidence must remain required: true.")
            if "validation" in c6b:
                fail.append("CHECK 7b DB6 Confidence must NOT carry a V3 validator: V3 is a "
                            "documented expectation, not an enforced rule.")
            if "NOT WRITTEN" not in (c6b.get("row_values") or ""):
                fail.append("CHECK 7b DB6 Confidence must be recorded as never written by the "
                            "backfill.")
            # tier/URL null by convention, and the convention is local
            for p in ("Source Tier", "Source URL"):
                rv = (by6.get(p) or {}).get("row_values") or ""
                if "NULL on all four rows" not in rv:
                    fail.append("CHECK 7b DB6 %s must be recorded null on all four rows." % p)
                if "LOCAL TO DB6" not in rv or "MUST NOT be applied to DB9" not in rv:
                    fail.append("CHECK 7b DB6 %s must record the convention as LOCAL to DB6 and "
                                "barred from DB9." % p)
            # the exception: singular, named, expiring, non-renewing
            ex = d6b.get("od1_exception") or {}
            if not ex:
                fail.append("CHECK 7b DB6 must carry the od1_exception record.")
            else:
                if ex.get("row_alias") != "Buyer":
                    fail.append("CHECK 7b the OD1 exception must name the Buyer row; found %r."
                                % ex.get("row_alias"))
                if ex.get("scope") != "this row only":
                    fail.append("CHECK 7b the OD1 exception scope must be 'this row only'.")
                if ex.get("expiry") != "2026-11-24":
                    fail.append("CHECK 7b the OD1 exception expiry must be 2026-11-24; found %r."
                                % ex.get("expiry"))
                if ex.get("automatic_waiver_renewal") is not False:
                    fail.append("CHECK 7b the OD1 exception must not auto-renew.")
                if "Nothing happens by itself" not in (ex.get("no_automatic_action_on_expiry")
                                                       or ""):
                    fail.append("CHECK 7b the OD1 exception must record that no automatic action "
                                "occurs on expiry.")
                dna = ex.get("does_not_apply_to") or ""
                if "future" not in dna or "historical rows generally" not in dna:
                    fail.append("CHECK 7b the OD1 exception must exclude future rows and must "
                                "NOT be phrased as applying to historical rows generally.")
            for other in ("DB9", "DB10"):
                orow = next((r for r in rows7b if r.get("db_id") == other), None)
                if orow is not None and "od1_exception" in orow:
                    fail.append("CHECK 7b %s must carry no OD1 exception." % other)
        # the shared shape is OBSERVED, never ratified
        od4 = od.get("OD4") or {}
        if "NOT ratified" not in (od4.get("status") or ""):
            fail.append("CHECK 7b OD4 must record that no Sector-wide standard is ratified.")
        if not any("OBSERVED convergence" in f for f in (od4.get("facts") or [])):
            fail.append("CHECK 7b OD4 must record the shared seven-field shape as an OBSERVED "
                        "convergence, not a ratified standard.")
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
                ("`Evidence` exists structurally in DB 6, DB 9 and DB 10",
                 "that Evidence now exists in all three"),
                ("populated on three DB 6 rows and null everywhere else",
                 "which Evidence cells are populated and which are not"),
                ("null Last Verified", "the Last Verified half of the freshness floor"),
                ("null Next Review", "the Next Review half of the freshness floor"),
                ("Both dates are required from every contributing record",
                 "that BOTH dates are required before either floor is computed"),
                ("may NEVER be filled from another row's",
                 "the ban on inheriting another row's Next Review"),
                ("no current date and no global decay threshold",
                 "the ban on substitute dates"),
                ("OD2 closed LOCALLY FOR DB 6 ONLY",
                 "that OD2 closed locally only"),
                ("NOT ratified for DB 9, DB 10 or Sector-wide",
                 "that the convention is not ratified beyond DB 6"),
                ("Rule V3 is a DOCUMENTED EXPECTATION for DB 6, not an enforced validator",
                 "that V3 is documented, not enforced, on DB 6"),
                ("A sourced row and an excepted row must never be reported the same way",
                 "that an excepted row is not a sourced row"),
                ("null `Evidence` continues to force an UNRESOLVED provenance floor",
                 "that a null Evidence still forces an UNRESOLVED floor"),
                ("No confidence or freshness value may be inferred from the fact that a field "
                 "exists", "that nothing may be inferred from field existence"),
                ("Null and unsupported both fail closed",
                 "that null AND unsupported both fail closed"),
                ("OD2", "the undefined multi-source tier mapping")]:
            if needle not in s10b:
                fail.append("CHECK 7b S10 SKILL.md Step 4 does not state %s." % what)

        n6 = next((r for r in rows7b if r.get("db_id") == "DB6"), {})
        n10 = next((r for r in rows7b if r.get("db_id") == "DB10"), {})
        r6 = ((n6.get("MISSING_FIELD") or {}).get("row_level_status") or {})
        r10 = ((n10.get("MISSING_FIELD") or {}).get("row_level_status") or {})
        notes.append("DB6/DB10 provenance: %s/%s fields recorded | 7 provenance fields each | "
                     "row-level %s/%s and %s/%s populated | DB6 backfill 13 cells, 1 named "
                     "exception (Buyer, expires 2026-11-24) | OD1 closed-with-exception, OD2 "
                     "closed LOCALLY, OD3 closed | OD4/OD5/OD6 open | shape OBSERVED not "
                     "ratified | drift undetectable offline"
                     % (n6.get("field_count_verified"), n10.get("field_count_verified"),
                        r6.get("non_null_cells"), r6.get("cells"),
                        r10.get("non_null_cells"), r10.get("cells")))

    # ---------------------------------------------------------------- 7c  DB 3 PROVENANCE
    # Added by DB3-PROV-1 Step A (2026-10-02); extended by DB3-OD10-OD12-1 the same day,
    # which added two nullable date properties to live DB3 under OD10 Option D. SAME BOUNDARY as
    # checks 7 and 7b: offline, deterministic, repository-internal, and BLIND TO LIVE DRIFT.
    #
    # DB 3 is the reason this check exists at all. It does NOT use the seven-field shape - it
    # answers all three provenance questions with its own four-field model - so a gate written
    # around the other shape would have reported it as broken. What is enforced here is that the
    # repository describes DB 3 AS IT IS: a database whose row-level provenance is complete and
    # whose SCHEMA cannot express a tier or a verification date.
    DB3_SOURCE_OPTS = ["xlsx", "chat", "agent run", "research"]
    # REWRITTEN 2026-10-02, not loosened. This list used to be
    #   ["Source Tier", "Source URL", "Last Verified", "Next Review", "Next Verification"]
    # and it banned every one of them from DB3's recorded `fields`. DB3-OD10-OD12-1 added two of
    # them live, so the ban would now fire on a TRUE record. The ban is kept for the three that
    # are still absent and REPLACED BY A POSITIVE REQUIREMENT for the two that now exist - which
    # is strictly stronger than deleting the rule, because an undated schema regression would
    # still fail.
    DB3_STILL_ABSENT = ["Source Tier", "Source URL", "Next Verification"]
    DB3_NOW_PRESENT = ["Last Verified", "Next Review"]
    if dbjson:
        d3 = next((r for r in rows7b if r.get("db_id") == "DB3"), None)
        if d3 is None:
            fail.append("CHECK 7c sector-databases.json records no DB3 entry.")
        else:
            f3 = d3.get("fields") or []
            by3 = {f.get("name"): f for f in f3}
            blob3 = re.sub(r"\s+", " ", json.dumps(d3))

            # 15 -> 17 on 2026-10-02 (DB3-OD10-OD12-1). The prior count is not deleted:
            # it must survive in `field_count_superseded`, or this file would be rewriting its
            # own dated history.
            if len(f3) != 17:
                fail.append("CHECK 7c DB3 must record 17 fields (15 audited + the two dates "
                            "added live by DB3-OD10-OD12-1); found %d." % len(f3))
            if d3.get("field_count_verified") != 17:
                fail.append("CHECK 7c DB3 field_count_verified must be 17; found %r."
                            % d3.get("field_count_verified"))
            fcs = d3.get("field_count_superseded") or {}
            if fcs.get("was") != 15:
                fail.append("CHECK 7c DB3 must PRESERVE the superseded 15-field count in "
                            "`field_count_superseded`, not silently replace it.")
            elif not all(k in fcs for k in ("was_true_when_written", "became_false_on")):
                fail.append("CHECK 7c DB3's superseded field count must record BOTH when it was "
                            "true and when it became false.")
            elif fcs.get("preserved_not_rewritten") is not True:
                fail.append("CHECK 7c DB3's superseded field count must be marked preserved, "
                            "not rewritten.")
            names3 = [f.get("name") for f in f3]
            dup3 = sorted({n for n in names3 if names3.count(n) > 1})
            if dup3:
                fail.append("CHECK 7c DB3 has duplicate field names: %s" % ", ".join(dup3))

            # Source: a four-value PROCESS-KIND select, never an authority
            src3 = by3.get("Source") or {}
            if src3.get("notion_type") != "select":
                fail.append("CHECK 7c DB3 Source must be a select; recorded as %r."
                            % src3.get("notion_type"))
            if (src3.get("allowed_values") or []) != DB3_SOURCE_OPTS:
                fail.append("CHECK 7c DB3 Source options must be exactly %s; recorded as %r."
                            % (DB3_SOURCE_OPTS, src3.get("allowed_values")))
            sem3 = src3.get("semantics") or ""
            if "PROCESS KIND" not in sem3 or "Evidence" not in sem3:
                fail.append("CHECK 7c DB3 Source must be recorded as a PROCESS KIND whose "
                            "locator belongs in Evidence - it is not an authority.")

            # Evidence: required, and recorded populated on every row
            ev3 = by3.get("Evidence") or {}
            if ev3.get("required") is not True:
                fail.append("CHECK 7c DB3 Evidence must be recorded required.")
            rl3 = d3.get("row_level_provenance") or {}
            if rl3.get("rows") != 217:
                fail.append("CHECK 7c DB3 must record 217 rows; found %r." % rl3.get("rows"))
            for fld in ("Evidence", "Confidence", "Source", "Freshness"):
                cell = rl3.get(fld) or {}
                if cell.get("non_null") != 217 or cell.get("of") != 217:
                    fail.append("CHECK 7c DB3 %s must be recorded populated 217/217; found %r."
                                % (fld, cell))
            if rl3.get("rows_with_confidence_and_no_evidence") != 0:
                fail.append("CHECK 7c DB3 must record ZERO rows with a Confidence and no "
                            "Evidence - this is the fact that disproved the original OD6 "
                            "framing.")
            if rl3.get("backfill_authorised") is not False:
                fail.append("CHECK 7c DB3 must record backfill_authorised false.")
            # added 2026-10-02: present-but-null is a CLAIM about row state and needs a gate of
            # its own, or "we added the fields" could silently become "we filled them".
            for fld in DB3_NOW_PRESENT:
                cell = rl3.get(fld) or {}
                if not cell:
                    fail.append("CHECK 7c DB3 must record row-level state for %s." % fld)
                    continue
                if cell.get("non_null") != 0 or cell.get("of") != 217:
                    fail.append("CHECK 7c DB3 %s must be recorded null on 0 of 217 rows; found "
                                "%r. No backfill was authorised." % (fld, cell))
                if "PRESENT BUT NULL" not in str(cell.get("state", "")).upper():
                    fail.append("CHECK 7c DB3 %s must be recorded PRESENT BUT NULL, which is "
                                "not the same fact as absent." % fld)
                if cell.get("backfill_authorised") is not False:
                    fail.append("CHECK 7c DB3 %s must record backfill_authorised false." % fld)
            zp = rl3.get("zero_row_writes_proof") or {}
            if zp.get("row_value_writes") != 0 or zp.get("schema_writes") != 2:
                fail.append("CHECK 7c DB3 must record exactly 2 schema writes and 0 row-value "
                            "writes for DB3-OD10-OD12-1; found %r." % zp)
            if "identical" not in str(zp.get("method", "")):
                fail.append("CHECK 7c DB3's zero-write proof must record the before/after "
                            "method, not just the conclusion.")

            # temporal and tier fields: recorded STRUCTURALLY ABSENT, not merely omitted
            pm3 = d3.get("provenance_model") or {}
            absent3 = pm3.get("fields_absent") or {}
            for a in DB3_STILL_ABSENT:
                if a in by3:
                    fail.append("CHECK 7c DB3 must NOT record a %r field: it is structurally "
                                "absent from the live schema. `Next Verification` in particular "
                                "was NOT created - DB3 uses `Next Review`." % a)
            # the positive half: both dates must now be recorded, as NULLABLE dates, and must be
            # recorded PRESENT-BUT-NULL rather than populated. A gate that only banned fields
            # could not catch a false claim that they had been backfilled.
            for a in DB3_NOW_PRESENT:
                fd = by3.get(a)
                if not fd:
                    fail.append("CHECK 7c DB3 must record a %r field: DB3-OD10-OD12-1 added it "
                                "live on 2026-10-02." % a)
                    continue
                if fd.get("notion_type") != "date":
                    fail.append("CHECK 7c DB3 %s must be recorded as a date; found %r."
                                % (a, fd.get("notion_type")))
                if fd.get("required") is not False:
                    fail.append("CHECK 7c DB3 %s must be recorded NULLABLE (required false): "
                                "the authorisation added it nullable and forbade any "
                                "backfill." % a)
                if "GOVERN" not in (fd.get("semantics") or "").upper():
                    fail.append("CHECK 7c DB3 %s must be recorded as a GOVERNING temporal "
                                "field - that is what OD10 Option D decided." % a)
                if not re.search(r"(?i)null on all 217|present but null",
                                 str(fd.get("semantics")) + str(fd.get("validation"))):
                    fail.append("CHECK 7c DB3 %s must be recorded null on all 217 rows." % a)
                if not re.search(r"(?i)fails? closed", str(fd.get("validation"))):
                    fail.append("CHECK 7c DB3 %s must record that a null FAILS CLOSED." % a)
            nr3 = by3.get("Next Review") or {}
            if "Next Verification" not in (nr3.get("semantics") or ""):
                fail.append("CHECK 7c DB3 Next Review must record that it is NOT "
                            "`Next Verification` - the owner was explicit about the name.")
            if not re.search(r"(?i)past a NON-NULL `Next Review` is STALE|non-null .{0,20}stale",
                             str(nr3.get("validation"))):
                fail.append("CHECK 7c DB3 Next Review must record the governed stale rule: a row "
                            "past a NON-NULL Next Review is stale.")
            if not absent3:
                fail.append("CHECK 7c DB3 must STATE which provenance fields are absent, not "
                            "merely omit them.")
            # REWRITTEN 2026-10-02. This used to require "Last Verified" and a next-review
            # key inside `fields_absent`; both are now PRESENT, so requiring them there would
            # force a false record. The requirement MOVES rather than disappears: the two keys
            # must now appear in `fields_formerly_absent_now_present` WITH their original wording
            # preserved verbatim.
            for a in ("Source Tier", "Source URL"):
                if a not in absent3:
                    fail.append("CHECK 7c DB3 must state that %s is absent - the tier half of "
                                "the limitation is NOT closed." % a)
            if "Last Verified" in absent3 or any("Next Review" in k for k in absent3):
                fail.append("CHECK 7c DB3 must NOT still list its date fields as absent: "
                            "DB3-OD10-OD12-1 added both on 2026-10-02.")
            for k3, v3 in absent3.items():
                if "ABSENT" not in str(v3).upper():
                    fail.append("CHECK 7c DB3 %s must be described as absent." % k3)
            fmr = pm3.get("fields_formerly_absent_now_present") or {}
            if not fmr:
                fail.append("CHECK 7c DB3 must record `fields_formerly_absent_now_present`: the "
                            "two dates were recorded STRUCTURALLY ABSENT until 2026-10-02 and "
                            "that dated claim must be superseded, not erased.")
            else:
                verb = fmr.get("superseded_claims_verbatim") or {}
                if len(verb) != 2:
                    fail.append("CHECK 7c DB3 must preserve BOTH superseded absence claims "
                                "verbatim; found %d." % len(verb))
                if not any("ABSENT" in str(v).upper() for v in verb.values()):
                    fail.append("CHECK 7c DB3's preserved absence claims must still read as "
                                "absence claims - preserved means verbatim, not paraphrased.")
                if fmr.get("preserved_not_rewritten") is not True:
                    fail.append("CHECK 7c DB3's formerly-absent record must be marked "
                                "preserved, not rewritten.")
                for k3 in DB3_NOW_PRESENT:
                    if "NULL" not in str(fmr.get(k3, "")).upper():
                        fail.append("CHECK 7c DB3's %s must be recorded PRESENT BUT NULL." % k3)
                if not re.search(r"(?i)different fact",
                                 str(fmr.get("why_this_distinction_matters", ""))):
                    fail.append("CHECK 7c DB3 must record WHY absent and present-but-null are "
                                "different facts.")

            # Freshness: a declaration, with no defined threshold
            fr3 = by3.get("Freshness") or {}
            frsem = fr3.get("semantics") or ""
            if "DECLARED" not in frsem.upper():
                fail.append("CHECK 7c DB3 Freshness must be recorded as a DECLARED state, not a "
                            "computed measurement.")
            if "threshold" not in frsem.lower():
                fail.append("CHECK 7c DB3 Freshness must record that no threshold is defined.")
            if not re.search(r"(?i)never substitute", frsem):
                fail.append("CHECK 7c DB3 Freshness must forbid substituting it for a "
                            "verification date.")
            # added 2026-10-02: the OD10 Option D decisions must be recorded, not just implied
            frd = (pm3.get("freshness_is_a_declaration_not_a_measurement") or {})
            sd = frd.get("superseding_decision") or {}
            if not sd:
                fail.append("CHECK 7c DB3's Freshness record must carry the OD10 Option D "
                            "superseding decision.")
            else:
                if sd.get("freshness_is_non_governing") is not True:
                    fail.append("CHECK 7c DB3 Freshness must be recorded NON-GOVERNING - that "
                                "is decision 2 of OD10 Option D.")
                if "DISSOLVED" not in str(sd.get("no_threshold_is_defined_or_needed", "")).upper():
                    fail.append("CHECK 7c DB3 must record that OD10 was DISSOLVED, not answered, "
                                "and that no threshold is needed.")
                if "notAvailableInQuerySql" not in str(sd.get("do_not_derive", "")):
                    fail.append("CHECK 7c DB3 must record WHY Freshness is not derived - the "
                                "DB5 `Total Score` formula precedent, not a bare prohibition.")
                if "not being called" not in str(
                        sd.get("historical_values_are_non_governing_not_false", "")):
                    fail.append("CHECK 7c DB3 must record that the 217 historical `Fresh` values "
                                "are NON-GOVERNING, not false.")
            odr = pm3.get("od10_decision_record") or {}
            if len(odr.get("decisions") or []) != 9:
                fail.append("CHECK 7c DB3 must record all NINE OD10 Option D decisions; found "
                            "%d." % len(odr.get("decisions") or []))
            if "UNIMPLEMENTABLE" not in str((odr.get("options_rejected") or {}).get(
                    "A - define a threshold", "")).upper():
                fail.append("CHECK 7c DB3 must record that Option A was UNIMPLEMENTABLE - no "
                            "date to measure from - not merely unattractive.")
            if "EXCLUDED BY CONTRACT" not in str((odr.get("options_rejected") or {}).get(
                    "C - retire `Freshness`", "")).upper():
                fail.append("CHECK 7c DB3 must record that Option C was EXCLUDED BY CONTRACT: "
                            "`freshness` is a REQUIRED property of the Intelligence Object.")
            thr = odr.get("thresholds_examined_and_rejected_as_not_reusable") or {}
            # The record says "NEITHER IS REUSABLE"; an exact "NOT REUSABLE" needle was my
            # own paraphrase of it. Accept either phrasing of the same verdict.
            if not re.search(r"(?i)neither is reusable|not reusable", str(thr.get("verdict", ""))):
                fail.append("CHECK 7c DB3 must record that the 30- and 90-day horizons were "
                            "examined and are NOT REUSABLE.")
            if "never run" not in str(odr.get("stale_rule_now_has_a_trigger", "")):
                fail.append("CHECK 7c DB3 must record that the `Stale` rule was a consequence "
                            "with no trigger, and that the M4 stale sweep has never run.")
            cnc = odr.get("contract_non_compliances_this_addresses") or {}
            if "SECTOR_ACTIVATION_CONTRACT.md" not in cnc:
                fail.append("CHECK 7c DB3 must record the two GOVERNED CONTRACT "
                            "non-compliances that motivated Option D.")
            if "never the reason" not in str(cnc.get("why_this_matters", "")):
                fail.append("CHECK 7c DB3 must record that S10 computability was a CONSEQUENCE "
                            "and never the reason - defining a threshold to make S10 computable "
                            "was expressly forbidden.")
            if "DOES NOT MAKE THE FRESHNESS FLOOR COMPUTABLE TODAY" not in str(
                    odr.get("what_this_does_NOT_do", "")).upper():
                fail.append("CHECK 7c DB3 must state that Option D does NOT make the freshness "
                            "floor computable today.")

            # the limitation must be named as expressiveness, not missing provenance
            lim3 = (pm3.get("the_actual_limitation") or "").upper()
            if "SCHEMA EXPRESSIVENESS" not in lim3:
                fail.append("CHECK 7c DB3's limitation must be recorded as SCHEMA "
                            "EXPRESSIVENESS for tier and temporal verification.")
            if "NOT MISSING PROVENANCE" not in lim3:
                fail.append("CHECK 7c DB3 must NOT be described as missing provenance generally.")
            # Added 2026-10-02 after mutation testing: the two checks above both survived a
            # mutation that declared the limitation CLOSED, because the mutation kept their
            # phrases. Only the TEMPORAL half closed; the tier half is untouched.
            if "HALF CLOSED" not in lim3:
                fail.append("CHECK 7c DB3's limitation must be recorded HALF CLOSED - "
                            "DB3-OD10-OD12-1 closed the temporal half only.")
            if "SOURCE TIER REMAINS STRUCTURALLY INEXPRESSIBLE" not in lim3:
                fail.append("CHECK 7c DB3 must record that SOURCE TIER REMAINS STRUCTURALLY "
                            "INEXPRESSIBLE - closing the temporal half must never read as "
                            "closing the tier half.")
            if "EXPRESSIBLE but UNPOPULATED" not in (pm3.get("the_actual_limitation") or ""):
                fail.append("CHECK 7c DB3's temporal half must be recorded EXPRESSIBLE but "
                            "UNPOPULATED, not solved.")
            if not re.search(r"(?i)cannot detect later live|no offline gate can detect", blob3):
                fail.append("CHECK 7c DB3 must warn that live drift is undetectable offline.")

            # no claim about the three unaudited High-confidence rows
            hc3 = rl3.get("high_confidence_rows") or {}
            if hc3.get("count") != 3 or hc3.get("in_target_set") != 0:
                fail.append("CHECK 7c DB3 must record 3 High-confidence rows, none in the "
                            "Target set.")
            # REWRITTEN 2026-10-02, not loosened. This used to require
            # no_claim_is_made_about_them is True. The bodies were then read under explicit owner
            # authorisation and all three are blank, so the refusal would now be a FALSE record.
            # The old flag must survive inside `superseded_claim`, and the replacement is
            # STRICTER: three specific classifications are now required by name.
            if hc3.get("no_claim_is_made_about_them") is not False:
                fail.append("CHECK 7c DB3's three High-confidence rows were body-read under "
                            "authorisation on 2026-10-02 and are now CLASSIFIED; the "
                            "no-claim flag must be False.")
            sc3 = hc3.get("superseded_claim") or {}
            if sc3.get("prior_no_claim_flag") is not True:
                fail.append("CHECK 7c DB3 must PRESERVE the earlier no-claim position in "
                            "`superseded_claim` - it was correct while the bodies were unread.")
            elif "NOT WRONG" not in str(sc3.get("verdict", "")).upper():
                fail.append("CHECK 7c DB3's earlier no-claim position must be marked superseded "
                            "but NOT WRONG.")
            if hc3.get("all_three_bodies_blank") is not True or hc3.get("bodies_read") != 3:
                fail.append("CHECK 7c DB3 must record that all THREE High-confidence bodies "
                            "were read and all three are BLANK.")
            cls = hc3.get("classifications") or {}
            want = {"HIGH_OVERSTATED": 1, "HIGH_UNRESOLVED": 2}
            got = {}
            for k3, v3 in cls.items():
                if isinstance(v3, dict) and v3.get("verdict"):
                    got[v3["verdict"]] = got.get(v3["verdict"], 0) + 1
            if got != want:
                fail.append("CHECK 7c DB3 must classify the three High rows as exactly one "
                            "HIGH_OVERSTATED and two HIGH_UNRESOLVED; found %r." % got)
            h1 = next((v3 for k3, v3 in cls.items()
                       if isinstance(v3, dict) and v3.get("verdict") == "HIGH_OVERSTATED"), {})
            if h1.get("correction_required") is not True:
                fail.append("CHECK 7c DB3's HIGH_OVERSTATED row must be recorded as REQUIRING a "
                            "correction.")
            if "NOT AUTHORISED" not in str(h1.get("correction_is_a_separate_decision", "")).upper():
                fail.append("CHECK 7c DB3's HIGH_OVERSTATED correction must be recorded as a "
                            "SEPARATE, unauthorised decision - DB3-OD10-OD12-1 did not make it.")
            if not re.search(r"(?i)draft 15", str(h1.get("why", ""))):
                fail.append("CHECK 7c DB3's HIGH_OVERSTATED row must record the actual basis: "
                            "its Evidence cites Arika's own internal draft.")
            for k3, v3 in cls.items():
                if isinstance(v3, dict) and v3.get("verdict") == "HIGH_UNRESOLVED":
                    if v3.get("correction_required") is not False:
                        fail.append("CHECK 7c DB3's HIGH_UNRESOLVED rows must NOT be recorded as "
                                    "requiring a correction - they need RE-SOURCING.")
                    if "RE-SOURCING" not in str(v3.get("needs", "")).upper():
                        fail.append("CHECK 7c DB3's HIGH_UNRESOLVED rows must record that they "
                                    "need re-sourcing, not re-rating.")
            if "NO Confidence value was written" not in str(
                    cls.get("_confidence_values_unchanged", "")):
                fail.append("CHECK 7c DB3 must record that NO Confidence value was changed.")
            nt3 = rl3.get("non_target_rows") or {}
            if nt3.get("count") != 211:
                fail.append("CHECK 7c DB3 must record 211 non-Target rows.")
            if "NOT READ" not in (nt3.get("bodies") or ""):
                fail.append("CHECK 7c DB3 must record that the 211 non-Target bodies were not "
                            "read.")

        # OD6 superseded and re-scoped, with the disproven claim preserved
        od6b = od.get("OD6") or {}
        if "RE-SCOPED" not in (od6b.get("status") or ""):
            fail.append("CHECK 7c OD6 must be recorded RE-SCOPED by DB3-PROV-1 Step A.")
        if "OPEN" not in (od6b.get("status") or ""):
            fail.append("CHECK 7c OD6 must remain OPEN.")
        sc6 = od6b.get("superseded_claim") or {}
        if not sc6:
            fail.append("CHECK 7c OD6 must PRESERVE its disproven original claim.")
        else:
            if "DISPROVEN" not in (sc6.get("verdict") or ""):
                fail.append("CHECK 7c OD6's prior claim must be marked DISPROVEN.")
            if sc6.get("preserved_not_rewritten") is not True:
                fail.append("CHECK 7c OD6's prior claim must be preserved, not rewritten.")
            if "ZERO of 217" not in (sc6.get("why_it_was_wrong") or ""):
                fail.append("CHECK 7c OD6 must record the zero-of-217 fact that disproved it.")
        if len(od6b.get("rescoped_to") or []) != 4:
            fail.append("CHECK 7c OD6 must be re-scoped to exactly its four specific items.")
        # OD10 LEFT THIS LOOP on 2026-10-02 - it is the only one of the twelve that closed.
        # It is not simply dropped: it gets its own stricter block below, which requires the
        # dissolution verdict AND the preserved original question. OD13 joins the loop.
        for k3 in ("OD7", "OD8", "OD9", "OD11", "OD12", "OD13"):
            if k3 not in od:
                fail.append("CHECK 7c open item %s is not recorded." % k3)
            elif "OPEN" not in (od[k3].get("status") or ""):
                fail.append("CHECK 7c open item %s must remain OPEN." % k3)

        od10 = od.get("OD10") or {}
        if "CLOSED BY DISSOLUTION" not in (od10.get("status") or ""):
            fail.append("CHECK 7c OD10 must be recorded CLOSED BY DISSOLUTION by "
                        "DB3-OD10-OD12-1 - not 'resolved', and not still open.")
        sq10 = od10.get("superseded_question") or {}
        if not sq10.get("verbatim"):
            fail.append("CHECK 7c OD10 must PRESERVE its original question verbatim.")
        elif "threshold" not in sq10["verbatim"].lower():
            fail.append("CHECK 7c OD10's preserved question must be the original "
                        "threshold-definition question, verbatim.")
        if "DISSOLVED, NOT ANSWERED" not in str(sq10.get("verdict", "")).upper():
            fail.append("CHECK 7c OD10 must record that it was DISSOLVED, NOT ANSWERED - the "
                        "question presupposed a threshold that turned out to be "
                        "unimplementable.")
        if sq10.get("preserved_not_rewritten") is not True:
            fail.append("CHECK 7c OD10's original question must be marked preserved, not "
                        "rewritten.")
        if "not authorised" not in str(od10.get("what_remains_open", "")).lower() and \
                "NOT authorised" not in str(od10.get("what_remains_open", "")):
            fail.append("CHECK 7c OD10 must record that both columns are null and backfill is "
                        "NOT authorised - closing OD10 did not make anything computable.")

        od12 = od.get("OD12") or {}
        if "HIGH_OVERSTATED" not in (od12.get("status") or ""):
            fail.append("CHECK 7c OD12 must record the H1 HIGH_OVERSTATED classification in "
                        "its status.")
        if "SEPARATE DECISION" not in (od12.get("status") or "").upper():
            fail.append("CHECK 7c OD12 must record that H1's correction is a SEPARATE decision, "
                        "not authorised by DB3-OD10-OD12-1.")
        if not (od12.get("superseded_question") or {}).get("preserved_not_rewritten"):
            fail.append("CHECK 7c OD12 must preserve its original question.")

        od13 = od.get("OD13") or {}
        if "UNMEASURED" not in (od13.get("status") or "").upper():
            fail.append("CHECK 7c OD13 must record the estate-wide Sub-Sector null count as "
                        "UNMEASURED.")
        if od13.get("bounded_measurement_requires_its_own_authorisation") is not True:
            fail.append("CHECK 7c OD13 must record that a bounded measurement needs its own "
                        "authorisation.")
        if "gap" not in str(od13.get("disclosed_gap_in_the_prior_audit", "")).lower():
            fail.append("CHECK 7c OD13 must disclose that DB3-PROV-AUDIT-1 did not check "
                        "Sub-Sector population - the gap is in my own prior audit's scope.")

        # intelligence-object: the Q2 mapping must still be LEFT ALONE - it was already
        # correct and every authorisation since has said so. The Q3 mapping is a different
        # matter: it read `Freshness` ALONE, which could not satisfy this block's own `required`
        # list of [last_verified, freshness]. That was one of the two governed non-compliances
        # that motivated Option D, so after 2026-10-02 it must name the two dates.
        if _io_raw:
            _iop = (json.loads(_io_raw).get("properties") or {})
            m3 = ((_iop.get("source") or {}).get("notion_field") or {}).get("DB3")
            if m3 != "Evidence + Source":
                fail.append("CHECK 7c DB3's Q2 mapping must stay 'Evidence + Source'; found %r."
                            % m3)
            _wo = (_iop.get("when_observed") or {})
            w3 = (_wo.get("notion_field") or {}).get("DB3")
            if w3 != "Last Verified + Next Review":
                fail.append("CHECK 7c DB3's Q3 mapping must be 'Last Verified + Next Review' "
                            "now that both exist; found %r." % w3)
            if sorted(_wo.get("required") or []) != ["freshness", "last_verified"]:
                fail.append("CHECK 7c when_observed.required must still be BOTH last_verified "
                            "and freshness - DB3-OD10-OD12-1 did not relax the canonical "
                            "object, it made DB3 able to satisfy it.")
            if "NON-GOVERNING" not in (_wo.get("notion_field_notes") or ""):
                fail.append("CHECK 7c the when_observed notes must record that DB3's "
                            "`Freshness` is NON-GOVERNING and is not the Q3 answer.")

        # S10 must name all four contributing elements and state DB3's behaviour
        for needle, what in [
                ("| **DB 3** findings |", "DB 3 as the fourth contributing element"),
                # REWRITTEN 2026-10-02. These two needles were "FIELD DOES NOT EXIST", once bare
                # and once as the paired table cells. Both fields now EXIST and are null, so the
                # old needles would force S10 to state something false. The replacements are the
                # same shape - paired cells, so one is not enough - with the new truth.
                ("| **PRESENT, null on all 217** | **PRESENT, null on all 217** |",
                 "that BOTH of DB 3's date fields are present-but-null - one is not enough"),
                ("now *emptily*, no longer *structurally*",
                 "that DB 3's freshness floor now fails EMPTILY rather than STRUCTURALLY"),
                ("Three states, not two",
                 "the three-state distinction: absent, present-but-null, present-and-populated"),
                ("present and populated", "the third state by name"),
                ("`Freshness` is NON-GOVERNING and MUST NOT be read as a temporal signal",
                 "that DB 3's Freshness is non-governing as of OD10 Option D"),
                ("A row past a **non-null** `Next Review` is **stale**",
                 "the governed stale rule that `Next Review` finally gives a trigger"),
                ("No backfill is authorised, so nothing in DB 3 can supply a freshness floor "
                 "today",
                 "that adding the fields did NOT make the floor computable"),
                ("HIGH_OVERSTATED", "H1's classification"),
                ("HIGH_UNRESOLVED", "H2 and H3's classification"),
                ("There are **four** contributing elements",
                 "the explicit four-element count (the looser phrase also occurs in the prose "
                 "describing the omission, so it cannot be the test)"),
                ("An absent field is a different fact from a present-but-null cell",
                 "the absent-field versus null-cell distinction"),
                ("`Source` is a process-kind dimension, not an authority",
                 "that DB 3's Source is not an authority"),
                ("may substitute", "the ban on substituting a date or a Freshness label"),
                ("Restrictions recorded only in page bodies can be lost",
                 "that body-only restrictions can be lost"),
                # REWRITTEN 2026-10-02: the bodies were read under authorisation and all
                # three are blank, so "make no claim about them" is no longer the honest
                # statement. What must now be stated is that the earlier refusal is SUPERSEDED
                # rather than quietly dropped.
                ("*Superseded: this bullet previously said to make no claim about them",
                 "that the earlier no-claim position is superseded, not silently deleted"),
                ("all three bodies are blank",
                 "that all three High-confidence bodies were read and are blank"),
                # Added 2026-10-02 after mutation testing: reinstating the unfixable claim as
                # CURRENT passed the gate, because no needle covered that sentence at all.
                ("DB 3 was the harder case until 2026-10-02",
                 "the unfixable-case claim in the PAST tense - it is superseded, and "
                 "reinstating it as current must fail"),
                ("DB 3 is now an ordinary empty-cell case",
                 "that DB 3 is now an ordinary empty-cell element like DB 9 and DB 10")]:
            if needle not in s10b:
                fail.append("CHECK 7c S10 SKILL.md Step 4 does not state %s." % what)

        # the human-readable schema doc must agree about DB3, too. There was no such check until
        # mutation testing reverted the markdown's Source type and the gate stayed green.
        if "### DB 3" in ns7b:
            seg3 = re.sub(r"\s+", " ", ns7b.split("### DB 3", 1)[1].split("### DB 4", 1)[0])
            if "| **Source** | **Select** |" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must type `Source` as a "
                            "Select only - not 'Select/Text'.")
            # Matches the OPTION-LIST form ("xlsx sheet · chat"), not the bare phrase: the
            # correction note itself legitimately contains the words "not 'xlsx sheet'", and a
            # blanket ban flagged that sentence. Same false-positive class as a prohibition
            # sentence tripping a scan for the thing it prohibits.
            if "xlsx sheet ·" in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 still lists the first Source "
                            "option as 'xlsx sheet'; live and the JSON contract both say 'xlsx'.")
            if "PROCESS LABELS" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must state that all four "
                            "Source options are process labels, not authorities.")
            # 15 -> 17 on 2026-10-02. The superseded sentence must remain quoted in the
            # doc, so the old phrase is still required - as PRESERVED HISTORY, not as the
            # current count.
            if "17 properties, verified live" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must state 17 properties.")
            if "15 properties, verified live" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must still quote the "
                            "superseded 15-property sentence - dated history is superseded, "
                            "not deleted.")
            if "SUPERSEDED, NOT REWRITTEN" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must mark the property-count "
                            "change as superseded rather than rewritten.")
            if "NON-GOVERNING" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must record `Freshness` as "
                            "NON-GOVERNING as of OD10 Option D.")
            if "HALF CLOSED" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must record the "
                            "cannot-hold limitation as HALF CLOSED - tier still absent, "
                            "temporal now expressible.")
            if "not reusable" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must record that the 30- and "
                            "90-day horizons are not reusable.")
            if "STRUCTURALLY ABSENT" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must record the tier and "
                            "temporal fields as structurally absent.")
            if "SCHEMA EXPRESSIVENESS" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must name the limitation as "
                            "schema expressiveness, not missing provenance.")
            if "DECLARATION, not a computed measurement" not in seg3:
                fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md DB 3 must record Freshness as a "
                            "declaration rather than a measurement.")
        else:
            fail.append("CHECK 7c SECTOR_NOTION_SCHEMA.md has no DB 3 section.")

        d3n = next((r for r in rows7b if r.get("db_id") == "DB3"), {}) or {}
        rl3n = d3n.get("row_level_provenance") or {}
        notes.append("DB3 provenance: %s fields recorded (was 15, +2 dates 2026-10-02) | own "
                     "4-field model + 2 governing dates, NOT the 7-field shape | Evidence "
                     "required %s/%s | 0 rows with Confidence and no Evidence | "
                     "tier STRUCTURALLY ABSENT, dates PRESENT BUT NULL 0/217 | Freshness "
                     "NON-GOVERNING, no threshold defined or needed | OD6 re-scoped, OD10 CLOSED "
                     "BY DISSOLUTION, OD7-OD9/OD11-OD13 open | 211 bodies unread; 3 High rows "
                     "read and blank: 1 HIGH_OVERSTATED, 2 HIGH_UNRESOLVED | no backfill "
                     "authorised | drift undetectable offline"
                     % (d3n.get("field_count_verified"),
                        (rl3n.get("Evidence") or {}).get("non_null"),
                        (rl3n.get("Evidence") or {}).get("of")))

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
