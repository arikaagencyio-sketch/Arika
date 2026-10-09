# -*- coding: utf-8 -*-
"""
Content (04) write gate.

    python 04_Content/contracts/content_write_gate.py                    # contract integrity
    python 04_Content/contracts/content_write_gate.py readiness FILE.json  # G1 readiness on a brief snapshot
    python -m unittest discover -s 04_Content/contracts -p "test_*.py"

Two jobs, both pure (no network, no Notion, no file writes):

1. CONTRACT INTEGRITY over content-databases.json. Exit code 1 on any failure.
     C1  every field has exactly one writer, of a known kind
     C2  every skill writer is a declared skill whose SKILL.md exists on disk
     C3  every reverse writer names a forward relation that exists and is writable
     C4  the six trigger-read DB7 properties exist with their exact types, and
         Ready for Design is a human-only value of Publishing Status
     C5  field names are unique per database
     C6  a skill writes only in the databases it declares, and owns >= 1 field
         in each of them
     C7  every vocabulary has unique Notion names, option IDs and agent enums;
         every field that names a vocabulary is the field that vocabulary
         describes; the Publishing Status option IDs are recorded
     C8  DB7 Version is the revision field, and the four copy fields that
         reach the public are publication-affecting
     C9  every natural-key field exists, and DB6's key carries Audience Role

2. PROPOSAL REFUSALS. validate_write(), validate_design_readiness(),
   validate_generation_start(), validate_g2_submission(),
   validate_publication(), validate_publish_route() and
   validate_schema_change() return a Verdict. A skill runs them, or reasons
   through the same rules, BEFORE any apply. The rules are the refusal list
   in CONTENT_WRITE_CONTRACT.md s5.

What it cannot see. The gate validates proposals and snapshots handed to it.
It does not read Notion. A person editing a brief directly in Notion bypasses
it entirely: a copy change made there without a Version bump is invisible to
this file (CONTENT_WRITE_CONTRACT.md s0.2). It narrows the defect for writes
that go through a skill; it does not close it.
"""
import json
import os
import re
import sys
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CONTRACT_PATH = os.path.join(HERE, "content-databases.json")
SKILLS_DIR = os.path.join(REPO, ".claude", "skills")

FIXED_WRITERS = {"computed:formula", "computed:rollup", "human_only"}
PREFIXED_WRITERS = ("reverse:", "external:", "reserved:")

DRAGON_DONE = {"Complete", "Partial", "Not applicable"}
DRAGON_ALL = DRAGON_DONE | {"Not yet run"}
NEEDS_REASON = {"Partial", "Not applicable"}

EVIDENCE_KINDS = {"fact", "statistic"}          # need a dated, tiered source
OUTCOME_KINDS = {"outcome"}                      # client results, performance, case studies
COMMERCIAL_KINDS = {"pricing", "offer_term"}     # need a quotable Offer (02) row
SAFE_KINDS = {"opinion", "hypothesis", "framework", "question"}
ALL_CLAIM_KINDS = EVIDENCE_KINDS | OUTCOME_KINDS | COMMERCIAL_KINDS | SAFE_KINDS

FIRST_PERSON = re.compile(r"\b(I|I'm|I've|I'd|I'll|me|my|mine|myself)\b")
QUOTABLE_OFFER_STATUS = {"Active"}
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
COPY_FIELDS_THAT_PUBLISH = ("Script", "Caption", "Visual Direction", "Canva Instructions")
LOOKUP_OK = "complete"


class Verdict:
    """ok is True only when no refusal was raised. Refusals are records, not silence."""

    def __init__(self):
        self.refusals = []

    def refuse(self, code, detail):
        self.refusals.append({"code": code, "detail": detail})

    def extend(self, other):
        self.refusals.extend(other.refusals)

    @property
    def ok(self):
        return not self.refusals

    @property
    def codes(self):
        return [r["code"] for r in self.refusals]

    def __repr__(self):
        return "Verdict(ok=%s, refusals=%r)" % (self.ok, self.refusals)


# --------------------------------------------------------------------------- contract

def load_contract(path=CONTRACT_PATH):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def field_index(contract):
    return {db["db_id"]: {f["name"]: f for f in db["fields"]} for db in contract["databases"]}


def _writer_kind(writer):
    if writer in FIXED_WRITERS:
        return writer
    for p in PREFIXED_WRITERS:
        if writer.startswith(p):
            return p.rstrip(":")
    return "skill"


def _check_vocabularies(contract, idx, errors):
    vocabs = contract.get("vocabularies", {})
    for name in ("surface", "audience_role", "format"):
        voc = vocabs.get(name)
        if not voc:
            errors.append("C7 vocabulary %r is missing" % name)
            continue
        opts = voc.get("options", [])
        for key in ("notion", "option_id", "agent_enum"):
            vals = [o.get(key) for o in opts if o.get(key) is not None]
            if len(vals) != len(set(vals)):
                errors.append("C7 vocabulary %r has duplicate %s values" % (name, key))
        for o in opts:
            if not UUID.match(o.get("option_id") or ""):
                errors.append("C7 vocabulary %r option %r has no recorded option ID" % (name, o.get("notion")))
        f = idx.get(voc.get("db_id"), {}).get(voc.get("field"))
        if f is None or f.get("vocabulary") != name:
            errors.append("C7 vocabulary %r describes %s.%s, which does not point back to it" %
                          (name, voc.get("db_id"), voc.get("field")))
        if name == "surface":
            enums = {o["agent_enum"] for o in opts}
            for a in voc.get("agent_only", []):
                if a.get("agent_enum") in enums:
                    errors.append("C7 surface agent-only value %r collides with a Notion option" % a["agent_enum"])
    for dbid, fields in idx.items():
        for f in fields.values():
            vname = f.get("vocabulary")
            if vname and vname not in vocabs:
                errors.append("C7 %s.%s names unknown vocabulary %r" % (dbid, f["name"], vname))
    ds = vocabs.get("dragon_status", {})
    if set(ds.get("done", [])) != DRAGON_DONE or set(ds.get("done", [])) | set(ds.get("not_done", [])) != DRAGON_ALL:
        errors.append("C7 dragon_status vocabulary differs from the gate's DRAGON constants")
    tc = contract.get("trigger_contract", {})
    ids = tc.get("publishing_status_option_ids", {})
    if list(ids) != tc.get("publishing_status_options") or not all(UUID.match(i or "") for i in ids.values()):
        errors.append("C7 Publishing Status option IDs are not recorded for every option, in order")


def check_contract(contract, skills_dir=SKILLS_DIR):
    errors = []
    skills = contract.get("skills", {})
    idx = field_index(contract)

    for db in contract["databases"]:
        dbid = db["db_id"]
        names = [f["name"] for f in db["fields"]]
        dupes = {n for n in names if names.count(n) > 1}
        if dupes:
            errors.append("C5 %s: duplicate field names %s" % (dbid, sorted(dupes)))
        for k in db.get("natural_key", []):
            if k not in names:
                errors.append("C9 %s: natural-key field %r does not exist" % (dbid, k))
        for f in db["fields"]:
            w = f.get("writer")
            if not w:
                errors.append("C1 %s.%s: no writer" % (dbid, f["name"]))
                continue
            kind = _writer_kind(w)
            if kind == "skill":
                if w not in skills:
                    errors.append("C2 %s.%s: writer %s is not a declared skill" % (dbid, f["name"], w))
                elif dbid not in skills[w].get("writes", []):
                    errors.append("C6 %s.%s: %s writes it but does not declare %s" % (dbid, f["name"], w, dbid))
            elif kind == "reverse":
                target = w[len("reverse:"):]
                tdb, _, tfield = target.partition(".")
                fwd = idx.get(tdb, {}).get(tfield)
                if fwd is None:
                    errors.append("C3 %s.%s: reverse target %s does not exist" % (dbid, f["name"], target))
                elif fwd.get("type") != "relation":
                    errors.append("C3 %s.%s: reverse target %s is not a relation" % (dbid, f["name"], target))
                elif _writer_kind(fwd["writer"]) not in ("skill", "external"):
                    errors.append("C3 %s.%s: forward side %s has no writer that can set it" % (dbid, f["name"], target))

    for sid, s in skills.items():
        path = os.path.join(skills_dir, s["name"], "SKILL.md")
        if not os.path.isfile(path):
            errors.append("C2 skill %s (%s): no SKILL.md at %s" % (sid, s["name"], path))
        for dbid in s.get("writes", []):
            owned = [f for f in idx.get(dbid, {}).values() if f.get("writer") == sid]
            if not owned:
                errors.append("C6 skill %s declares %s but owns no field there" % (sid, dbid))

    tc = contract.get("trigger_contract", {})
    db7 = idx.get(tc.get("db_id", "DB7"), {})
    for name, typ in tc.get("properties", {}).items():
        f = db7.get(name)
        if f is None:
            errors.append("C4 trigger property %r missing from DB7" % name)
        elif f.get("type") != typ:
            errors.append("C4 trigger property %r is %s, must be %s" % (name, f.get("type"), typ))
        elif not f.get("trigger_sensitive"):
            errors.append("C4 trigger property %r is not marked trigger_sensitive" % name)
    ps = db7.get("Publishing Status", {})
    if "Ready for Design" not in ps.get("human_only_values", []):
        errors.append("C4 Ready for Design must be a human-only value of Publishing Status")
    if tc.get("publishing_status_options") != ["Not started", "In progress", "Ready for Design", "Done"]:
        errors.append("C4 Publishing Status options changed: %r" % tc.get("publishing_status_options"))

    _check_vocabularies(contract, idx, errors)

    ver = db7.get("Version", {})
    if ver.get("type") != "number" or not ver.get("revision"):
        errors.append("C8 DB7 Version must be a number marked as the revision field")
    for name in COPY_FIELDS_THAT_PUBLISH:
        if not db7.get(name, {}).get("publication_affecting"):
            errors.append("C8 DB7 %s must be publication_affecting" % name)

    db6 = next((d for d in contract["databases"] if d["db_id"] == "DB6"), {})
    if "Audience Role" not in db6.get("natural_key", []):
        errors.append("C9 DB6 natural key must include Audience Role (one Narrative x Platform x Audience expression)")
    return errors


# --------------------------------------------------------------------------- vocabularies

def resolve_option(contract, vocabulary, value):
    """Exact match on a Notion option name or a mapped agent enum. None means unknown.

    No case-folding and no dash normalisation: 'Company Page' and
    'LinkedIn — Company Page' are unknown, which is the point."""
    if not isinstance(value, str):
        return None
    for o in contract["vocabularies"][vocabulary]["options"]:
        if value == o["notion"] or (o.get("agent_enum") and value == o["agent_enum"]):
            return o
    return None


def resolve_surface(contract, value):
    """Agent-only values (not_applicable, unknown) resolve to None: they never pass."""
    return resolve_option(contract, "surface", value)


def production_class(contract, fmt, brief):
    """'design', 'text_only', or None when the format is unknown (fail closed)."""
    o = resolve_option(contract, "format", fmt)
    if o is None:
        return None
    if o["production"] == "design":
        return "design"
    direction = [(brief.get(k) or "").strip() for k in ("visual_direction", "canva_instructions")]
    if all(d == "" or d.lower() == "text-only" for d in direction):
        return "text_only"
    return "design"


# --------------------------------------------------------------------------- revisions

def revision_value(x):
    """A revision is a whole number >= 1. Notion returns numbers as floats (1.0).
    Anything else (None, 0, negatives, 1.5, True, "1") is not a revision."""
    if isinstance(x, bool) or x is None:
        return None
    if isinstance(x, int):
        return x if x >= 1 else None
    if isinstance(x, float) and x == x and x.is_integer() and x >= 1:
        return int(x)
    return None


def publication_affecting(contract):
    db7 = field_index(contract)["DB7"]
    return {n for n, f in db7.items() if f.get("publication_affecting")}


def _same(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return sorted(map(str, a)) == sorted(map(str, b))
    return a == b


def _check_revision(v, proposal, contract, state):
    if proposal["db"] != "DB7":
        return
    fields, mode = proposal.get("fields", {}), proposal.get("mode")
    touched = [f for f in fields if f in publication_affecting(contract)]
    if mode == "CREATE":
        rev = revision_value(fields.get("Version"))
        if rev is None:
            v.refuse("R20_REVISION_INVALID", "a new brief needs Version = 1; got %r" % fields.get("Version"))
        elif rev != 1:
            v.refuse("R21_REVISION_INCREMENT", "a new brief starts at Version 1, not %d" % rev)
        return
    if mode == "SUPERSEDE":
        if revision_value(fields.get("Version")) is None:
            v.refuse("R20_REVISION_INVALID", "the superseding brief needs a valid Version; got %r" % fields.get("Version"))
        return
    if not touched and "Version" not in fields:
        return
    prior = (state or {}).get("prior")
    if not isinstance(prior, dict):
        v.refuse("R21_REVISION_INCREMENT",
                 "the prior brief was not supplied, so the change to %s cannot be checked against it"
                 % (", ".join(touched) or "Version"))
        return
    prior_rev = revision_value(prior.get("Version"))
    if prior_rev is None:
        v.refuse("R20_REVISION_INVALID",
                 "the brief on record has no valid Version (%r); a human repairs it before any copy change"
                 % prior.get("Version"))
        return
    new = prior_rev
    if "Version" in fields:
        new = revision_value(fields["Version"])
        if new is None:
            v.refuse("R20_REVISION_INVALID", "Version %r is not a whole number >= 1" % fields["Version"])
            return
    changed = [f for f in touched if not _same(fields[f], prior.get(f))]
    if changed:
        if mode != "VERSION":
            v.refuse("R21_REVISION_INCREMENT", "a change to %s is a VERSION, not an %s" % (", ".join(changed), mode))
        if new != prior_rev + 1:
            v.refuse("R21_REVISION_INCREMENT", "%s changed: Version must be %d (prior %d + 1), got %d"
                     % (", ".join(changed), prior_rev + 1, prior_rev, new))
    else:
        if new != prior_rev:
            v.refuse("R21_REVISION_INCREMENT",
                     "Version moves %d -> %d with no publication-affecting change" % (prior_rev, new))
        if mode == "VERSION":
            v.refuse("R21_REVISION_INCREMENT", "VERSION with no publication-affecting change; this is a NO_OP")


# --------------------------------------------------------------------------- write proposals

def _is_human(actor):
    return isinstance(actor, str) and actor.startswith("human")


def _check_writers(v, proposal, dbfields):
    actor = proposal.get("actor", "")
    for name, value in proposal.get("fields", {}).items():
        f = dbfields.get(name)
        if f is None:
            v.refuse("R00_UNKNOWN_FIELD", "%s has no field %r" % (proposal["db"], name))
            continue
        kind = _writer_kind(f["writer"])
        if kind in ("computed:formula", "computed:rollup", "reverse"):
            v.refuse("R02_NOT_WRITABLE", "%r is %s and is never written directly" % (name, f["writer"]))
            continue
        if kind in ("external", "reserved"):
            v.refuse("R18_FOREIGN_FIELD", "%r belongs to %s" % (name, f["writer"]))
            continue
        if kind == "human_only":
            if not _is_human(actor):
                v.refuse("R01_HUMAN_ONLY", "%r is human-only; %s may not write it" % (name, actor))
            continue
        # skill-written field
        if _is_human(actor):
            continue  # a human may perform any skill's write by hand; the rules below still apply
        if f["writer"] != actor:
            v.refuse("R01_WRONG_WRITER", "%r is written by %s, not %s" % (name, f["writer"], actor))
            continue
        hov = f.get("human_only_values", [])
        if value in hov:
            v.refuse("R01_HUMAN_ONLY", "%r = %r may only be set by a human" % (name, value))
        odv = f.get("owner_decision_values", [])
        if odv and ("*" in odv or value in odv):
            dec = proposal.get("owner_decision") or {}
            if not (dec.get("quote") and dec.get("date")):
                v.refuse("R19_OWNER_DECISION",
                         "%r = %r needs a recorded owner decision (quote + date)" % (name, value))


def _check_options(v, proposal, dbfields, contract):
    """A Notion write carries the exact Notion option name. An agent enum would
    make Notion create a new option silently, so it is refused like any unknown."""
    for name, value in proposal.get("fields", {}).items():
        vname = (dbfields.get(name) or {}).get("vocabulary")
        if not vname or value is None:
            continue
        names = {o["notion"] for o in contract["vocabularies"][vname]["options"]}
        if value not in names:
            code = "R09_SURFACE_UNKNOWN" if vname == "surface" else "R23_UNKNOWN_OPTION"
            v.refuse(code, "%s.%s = %r is not a recorded Notion option %s" %
                     (proposal["db"], name, value, sorted(names)))


def _check_claims(v, proposal):
    offer = proposal.get("offer")
    for c in proposal.get("claims", []):
        kind = c.get("kind")
        text = c.get("text", "")[:80]
        if kind not in ALL_CLAIM_KINDS:
            v.refuse("R04_UNCLASSIFIED_CLAIM", "claim %r has no recognised kind" % text)
            continue
        sources = [s for s in c.get("sources", []) if s.get("id") and s.get("verified_at")]
        if kind in EVIDENCE_KINDS:
            if not sources:
                v.refuse("R04_UNEVIDENCED", "fact %r has no dated source" % text)
            elif all(s.get("tier") == "T4 Secondary" for s in sources):
                v.refuse("R05_T4_SOURCE", "fact %r rests only on T4 sources" % text)
        elif kind in OUTCOME_KINDS:
            if c.get("proof_status") != "Proof exists" or not sources:
                v.refuse("R04_UNPROVEN_OUTCOME", "outcome %r has no proof on record" % text)
        elif kind in COMMERCIAL_KINDS:
            if not offer or offer.get("status") not in QUOTABLE_OFFER_STATUS:
                v.refuse("R16_NO_QUOTABLE_OFFER",
                         "%s claim %r needs an Active Offer (02) row; none linked" % (kind, text))


def _check_dragon(v, proposal):
    db, fields, links = proposal["db"], proposal.get("fields", {}), proposal.get("links", {})
    pairs = {"DB5": ("Strategic DRAGON", "Strategic DRAGON Notes"),
             "DB6": ("Editorial DRAGON", "Editorial DRAGON Notes")}
    if db not in pairs:
        return
    status_f, notes_f = pairs[db]
    status = fields.get(status_f)
    if proposal.get("mode") == "CREATE" and not status:
        v.refuse("R07_DRAGON_STATUS", "%s CREATE must declare %s (use Not yet run, never blank)" % (db, status_f))
    if status is not None:
        if status not in DRAGON_ALL:
            v.refuse("R07_DRAGON_STATUS", "%s = %r is not a valid pass status" % (status_f, status))
        elif status in NEEDS_REASON and not (fields.get(notes_f) or "").strip():
            v.refuse("R07_DRAGON_STATUS", "%s = %s needs a reason in %s" % (status_f, status, notes_f))
    if db == "DB6" and status in DRAGON_DONE:
        strategic = (links.get("opportunity") or {}).get("strategic_dragon")
        if strategic not in DRAGON_DONE:
            v.refuse("R08_DRAGON_ORDER",
                     "Editorial pass recorded while the Opportunity's Strategic pass is %r" % strategic)


def _check_upstream_and_family(v, proposal):
    db, links, fields = proposal["db"], proposal.get("links", {}), proposal.get("fields", {})
    mode = proposal.get("mode")
    if db == "DB7" and (mode in ("CREATE", "VERSION", "SUPERSEDE") or proposal.get("recommend_ready_for_design")):
        missing = [k for k in ("opportunity", "translation") if not links.get(k)]
        if not links.get("narrative_position_ids"):
            missing.append("narrative_position")
        if missing:
            v.refuse("R03_UPSTREAM_MISSING", "brief has no %s" % ", ".join(missing))
        tr = links.get("translation") or {}
        fam = tr.get("family_id")
        if fam and links.get("narrative_position_ids") and fam not in links["narrative_position_ids"]:
            v.refuse("R06_FAMILY_MISMATCH",
                     "translation family %r is not among the brief's narrative positions" % fam)
    if db == "DB6" and mode == "CREATE":
        missing = [k for k in ("opportunity", "platform") if not links.get(k)]
        if not (links.get("source_truth") or links.get("source_intelligence")):
            missing.append("source_truth or source_intelligence")
        if missing:
            v.refuse("R03_UPSTREAM_MISSING", "translation has no %s" % ", ".join(missing))
    if db == "DB6" and links.get("source_truth"):
        fam = fields.get("Translation Family ID")
        pid = links["source_truth"].get("position_id")
        if fam is not None and fam != pid:
            v.refuse("R06_FAMILY_MISMATCH", "Translation Family ID %r != Source Truth Position ID %r" % (fam, pid))
    if db == "DB5" and mode == "CREATE":
        if not (fields.get("Source") or "").strip():
            v.refuse("R03_UPSTREAM_MISSING", "opportunity has no Source")
        if not (links.get("source_intelligence") or links.get("narrative_position_ids")):
            v.refuse("R03_UPSTREAM_MISSING", "opportunity cites neither a Sector finding nor a narrative position")


def _first_person(v, entry, texts):
    if not entry or entry.get("voice") != "institutional":
        return
    for name, text in texts:
        hit = FIRST_PERSON.search(text or "")
        if hit:
            v.refuse("R15_PAGE_VOICE",
                     "%s copy in %s uses first person (%r); the Page speaks institutionally"
                     % (entry["notion"], name, hit.group(0)))


def _check_surface(v, proposal, contract):
    db, links, fields = proposal["db"], proposal.get("links", {}), proposal.get("fields", {})
    mode = proposal.get("mode")
    if db == "DB6":
        if "Surface" in fields:
            entry = resolve_surface(contract, fields["Surface"])
            platform = links.get("platform")
            if entry and entry["notion"] == fields["Surface"]:
                if entry["linkedin"] is True and platform != "LinkedIn":
                    v.refuse("R09_SURFACE", "%r is a LinkedIn surface; this translation's platform is %r"
                             % (entry["notion"], platform))
                if entry["linkedin"] is False and platform == "LinkedIn":
                    v.refuse("R09_SURFACE", "a LinkedIn translation cannot use surface %r" % entry["notion"])
        elif mode == "CREATE":
            v.refuse("R09_SURFACE", "translation CREATE must declare a Surface (use Not yet assigned)")
    if db == "DB7":
        writes_copy = (mode in ("CREATE", "VERSION", "SUPERSEDE") or proposal.get("recommend_ready_for_design")
                       or any(f in fields for f in publication_affecting(contract)))
        if not writes_copy:
            return
        raw = (links.get("translation") or {}).get("surface")
        entry = resolve_surface(contract, raw)
        if entry is None:
            v.refuse("R09_SURFACE_UNKNOWN", "translation surface %r is not in the recorded vocabulary; "
                     "the voice and route rules cannot be checked" % raw)
            return
        if proposal.get("recommend_ready_for_design"):
            if not entry["assigned"]:
                v.refuse("R09_SURFACE", "a brief cannot be recommended Ready for Design while its surface is %r"
                         % entry["notion"])
            if (links.get("opportunity") or {}).get("strategic_dragon") not in DRAGON_DONE:
                v.refuse("R08_DRAGON_ORDER", "Strategic pass not run; brief cannot be recommended ready")
            if (links.get("translation") or {}).get("editorial_dragon") not in DRAGON_DONE:
                v.refuse("R08_DRAGON_ORDER", "Editorial pass not run; brief cannot be recommended ready")
        _first_person(v, entry, [(n, fields.get(n)) for n in ("Caption", "Script")])


def _lookup_records(state, dbid):
    """The verified result of the natural-key lookup, or None. Only a lookup that
    actually completed counts: missing, failed, partial or unknown is not 'empty'."""
    lk = ((state or {}).get("lookups") or {}).get(dbid)
    if not isinstance(lk, dict) or lk.get("status") != LOOKUP_OK:
        return None
    if not lk.get("checked_at") or not isinstance(lk.get("records"), list):
        return None
    return lk["records"]


def _check_duplicate(v, proposal, contract, state):
    if proposal.get("mode") != "CREATE":
        return
    db = next(d for d in contract["databases"] if d["db_id"] == proposal["db"])
    key_fields = db.get("natural_key", [])
    values = dict(proposal.get("key_values", {}))
    for k in key_fields:
        if k not in values and k in proposal.get("fields", {}):
            values[k] = proposal["fields"][k]
    if not key_fields or any(values.get(k) in (None, "", []) for k in key_fields):
        v.refuse("R10_NO_NATURAL_KEY", "CREATE on %s must supply its natural key %s" % (db["db_id"], key_fields))
        return
    records = _lookup_records(state, db["db_id"])
    if records is None:
        lk = ((state or {}).get("lookups") or {}).get(db["db_id"])
        status = lk.get("status") if isinstance(lk, dict) else "not supplied"
        v.refuse("R10_LOOKUP_UNVERIFIED",
                 "duplicate lookup on %s is %r; a missing, failed or partial lookup is never an empty database"
                 % (db["db_id"], status))
        return
    for rec in records:
        if all(_same(rec.get(k), values.get(k)) for k in key_fields):
            v.refuse("R10_DUPLICATE",
                     "%s already holds %s; use UPDATE, VERSION or SUPERSEDE" %
                     (db["db_id"], {k: values[k] for k in key_fields}))
            return


def validate_write(proposal, contract=None, state=None):
    """state = {"lookups": {DB: {"status": "complete", "checked_at": ..., "records": [...]}},
                "prior": {<the DB7 brief on record, Notion field names>}}"""
    contract = contract or load_contract()
    v = Verdict()
    idx = field_index(contract)
    if proposal.get("db") not in idx:
        v.refuse("R00_UNKNOWN_DB", "unknown database %r" % proposal.get("db"))
        return v
    if proposal.get("mode") not in ("CREATE", "UPDATE", "VERSION", "SUPERSEDE"):
        v.refuse("R00_MODE", "mode must be explicit: CREATE / UPDATE / VERSION / SUPERSEDE")
    _check_writers(v, proposal, idx[proposal["db"]])
    _check_options(v, proposal, idx[proposal["db"]], contract)
    _check_claims(v, proposal)
    _check_dragon(v, proposal)
    _check_upstream_and_family(v, proposal)
    _check_surface(v, proposal, contract)
    _check_revision(v, proposal, contract, state)
    _check_duplicate(v, proposal, contract, state)
    if proposal.get("db") == "DB7" and proposal.get("fields", {}).get("G2 Decision") == "Submitted for review":
        sub = proposal.get("g2_submission")
        if not sub:
            v.refuse("R22_STAGE_ORDER", "Submitted for review needs the submission context: brief, revision, "
                     "claim review, and the finished artifact or the final copy")
        else:
            v.extend(validate_g2_submission(sub, contract))
    return v


# --------------------------------------------------------------------------- workflow stages

def _dragon_and_surface(v, ctx, contract, stage):
    if (ctx.get("opportunity") or {}).get("strategic_dragon") not in DRAGON_DONE:
        v.refuse("R08_DRAGON_ORDER", "Strategic pass not run; %s refused" % stage)
    tr = ctx.get("translation") or {}
    if tr.get("editorial_dragon") not in DRAGON_DONE:
        v.refuse("R08_DRAGON_ORDER", "Editorial pass not run; %s refused" % stage)
    entry = resolve_surface(contract, tr.get("surface"))
    if entry is None:
        v.refuse("R09_SURFACE_UNKNOWN", "surface %r is not in the recorded vocabulary; %s refused"
                 % (tr.get("surface"), stage))
    elif not entry["assigned"]:
        v.refuse("R09_SURFACE", "surface is %r; %s needs an assigned publishing identity" % (entry["notion"], stage))
    return entry


def _human_record(v, rec, rev, what):
    """A gate record (G1, spend approval) made by a named human, dated, for revision `rev`."""
    rec = rec or {}
    if not (_is_human(rec.get("by")) and rec.get("at")):
        v.refuse("R22_STAGE_ORDER", "%s is not recorded by a named human with a date" % what)
        return
    got = revision_value(rec.get("revision"))
    if got is None:
        v.refuse("R20_REVISION_INVALID", "%s names no valid revision (%r)" % (what, rec.get("revision")))
    elif rev is not None and got != rev:
        v.refuse("R12_REVISION_MISMATCH", "%s was given for revision %d; the brief is at %d" % (what, got, rev))


def validate_design_readiness(ctx, contract=None):
    """G1 concept review + readiness, checked BEFORE a human sets Ready for Design.

    ctx = {"brief": {"id", "version", "visual_direction", "canva_instructions", "caption", "script"},
           "links": {"opportunity", "translation", "narrative_position_ids"},
           "opportunity": {"strategic_dragon"},
           "translation": {"editorial_dragon", "surface", "format", "family_id"},
           "g1": {"decision": "passed", "by": "human:...", "at", "revision"}}"""
    contract = contract or load_contract()
    v = Verdict()
    b, links, tr = ctx.get("brief") or {}, ctx.get("links") or {}, ctx.get("translation") or {}
    rev = revision_value(b.get("version"))
    if rev is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % b.get("version"))
    missing = [k for k in ("opportunity", "translation") if not links.get(k)]
    if not links.get("narrative_position_ids"):
        missing.append("narrative_position")
    if missing:
        v.refuse("R03_UPSTREAM_MISSING", "brief has no %s" % ", ".join(missing))
    if tr.get("family_id") and links.get("narrative_position_ids") and tr["family_id"] not in links["narrative_position_ids"]:
        v.refuse("R06_FAMILY_MISMATCH", "translation family %r is not among the brief's positions" % tr["family_id"])
    _dragon_and_surface(v, ctx, contract, "Ready for Design")
    prod = production_class(contract, tr.get("format"), b)
    if prod is None:
        v.refuse("R23_UNKNOWN_OPTION", "format %r is unknown; cannot tell design work from text-only" % tr.get("format"))
    elif prod == "text_only":
        v.refuse("R22_STAGE_ORDER", "text-only content does not go to Design; it reaches G2 once its final copy exists")
    elif not all((b.get(k) or "").strip() for k in ("visual_direction", "canva_instructions")):
        v.refuse("R22_STAGE_ORDER", "Visual Direction and Canva Instructions are needed before Design")
    g1 = ctx.get("g1") or {}
    if g1.get("decision") != "passed":
        v.refuse("R22_STAGE_ORDER", "G1 concept review has not passed this brief (decision %r)" % g1.get("decision"))
    else:
        _human_record(v, g1, rev, "G1 concept review")
    return v


def validate_generation_start(ctx, contract=None):
    """Human spend approval, checked BEFORE any generation or credit spend.

    ctx = {"brief": {"id", "version", "publishing_status"},
           "storyboard": {"revision"},             # the routine's completed comment
           "spend_approval": {"by": "human:...", "at", "revision", "scope"}}"""
    v = Verdict()
    b = ctx.get("brief") or {}
    rev = revision_value(b.get("version"))
    if rev is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % b.get("version"))
    if b.get("publishing_status") != "Ready for Design":
        v.refuse("R22_STAGE_ORDER", "generation before the brief reached Design (status %r)" % b.get("publishing_status"))
    sb = revision_value((ctx.get("storyboard") or {}).get("revision"))
    if sb is None:
        v.refuse("R22_STAGE_ORDER", "no storyboard on record for this brief")
    elif rev is not None and sb != rev:
        v.refuse("R12_REVISION_MISMATCH", "storyboard is for revision %d; the brief is at %d" % (sb, rev))
    sa = ctx.get("spend_approval")
    if not sa:
        v.refuse("R22_STAGE_ORDER", "no human spend approval; nothing may be generated or spent")
        return v
    _human_record(v, sa, rev, "spend approval")
    if not sa.get("scope"):
        v.refuse("R22_STAGE_ORDER", "spend approval names no scope (what may be generated)")
    return v


def validate_g2_submission(ctx, contract=None):
    """G2 is on the exact finished artifact. C06 may submit only when it exists.

    ctx = {"brief": {"id", "version", "caption", "script", "visual_direction", "canva_instructions"},
           "revision": N,                                   # what is being submitted
           "opportunity": {"strategic_dragon"},
           "translation": {"editorial_dragon", "surface", "format"},
           "claim_review": {"verdict": "pass", "revision": N},
           "artifacts": [{"asset_id", "version", "brief_revision", "rights"}]}   # design work only"""
    contract = contract or load_contract()
    v = Verdict()
    b, tr = ctx.get("brief") or {}, ctx.get("translation") or {}
    cur, sub = revision_value(b.get("version")), revision_value(ctx.get("revision"))
    if cur is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % b.get("version"))
    if sub is None:
        v.refuse("R20_REVISION_INVALID", "submitted revision %r is not a whole number >= 1" % ctx.get("revision"))
    if cur and sub and cur != sub:
        v.refuse("R12_REVISION_MISMATCH", "submitting revision %d; the brief is at %d" % (sub, cur))
    _dragon_and_surface(v, ctx, contract, "G2 submission")
    cr = ctx.get("claim_review") or {}
    if cr.get("verdict") != "pass" or revision_value(cr.get("revision")) != cur:
        v.refuse("R22_STAGE_ORDER", "claim review (C05) has not passed revision %r" % cur)
    prod = production_class(contract, tr.get("format"), b)
    arts = ctx.get("artifacts") or []
    if prod is None:
        v.refuse("R23_UNKNOWN_OPTION", "format %r is unknown; cannot tell design work from text-only" % tr.get("format"))
    elif prod == "text_only":
        if not any((b.get(k) or "").strip() for k in ("caption", "script")):
            v.refuse("R22_STAGE_ORDER", "text-only content reaches G2 once its final copy exists; Caption and Script are empty")
        if arts:
            v.refuse("R22_STAGE_ORDER", "a text-only brief lists design artifacts; re-classify it or route it through Design")
    else:
        if not arts:
            v.refuse("R22_STAGE_ORDER", "G2 judges the finished artifact; Design has delivered none for revision %r" % cur)
        for a in arts:
            if not a.get("asset_id") or revision_value(a.get("version")) is None:
                v.refuse("R22_STAGE_ORDER", "artifact %r has no asset ID or valid version" % a.get("asset_id"))
            made_for = revision_value(a.get("brief_revision"))
            if made_for is None or (cur and made_for != cur):
                v.refuse("R12_REVISION_MISMATCH", "artifact %r was produced for revision %r; the brief is at %r"
                         % (a.get("asset_id"), a.get("brief_revision"), cur))
            if a.get("rights") in (None, "", "unknown"):
                v.refuse("R22_STAGE_ORDER", "artifact %r has unknown rights" % a.get("asset_id"))
    return v


# --------------------------------------------------------------------------- publication

def _artifact_set(arts):
    return sorted((a.get("asset_id"), revision_value(a.get("version"))) for a in (arts or []))


def validate_publication(record, brief, contract=None):
    """A manual publication record linking a live post back to the exact approved artifact.

    brief = {"id", "version", "surface", "format", "visual_direction", "canva_instructions",
             "g2_decision", "g2_reviewer", "g2_decided_at", "g2_approved_revision",
             "g2_approved_artifacts": [{"asset_id", "version"}]}   # design work only"""
    contract = contract or load_contract()
    v = Verdict()
    if not _is_human(record.get("publisher")):
        v.refuse("R11_APPROVAL_MISSING", "agents never publish; publisher must be a named human")
    if brief.get("g2_decision") != "Approved":
        v.refuse("R11_APPROVAL_MISSING", "G2 decision is %r, not Approved" % brief.get("g2_decision"))
    if not (brief.get("g2_reviewer") and brief.get("g2_decided_at")):
        v.refuse("R11_APPROVAL_MISSING", "G2 approval has no reviewer or date on record")
    cur = revision_value(brief.get("version"))
    approved = revision_value(brief.get("g2_approved_revision"))
    published = revision_value(record.get("revision"))
    if cur is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % brief.get("version"))
    if approved is None:
        v.refuse("R20_REVISION_INVALID", "the approval names no valid revision (%r)" % brief.get("g2_approved_revision"))
    if published is None:
        v.refuse("R20_REVISION_INVALID", "the publication record names no valid revision (%r)" % record.get("revision"))
    if cur and approved and approved != cur:
        v.refuse("R12_REVISION_MISMATCH", "approval is for revision %d, brief is at %d (stale)" % (approved, cur))
    if published and approved and published != approved:
        v.refuse("R12_REVISION_MISMATCH", "published revision %d was not the approved one (%d)" % (published, approved))
    for k in ("brief_id", "surface", "native_post_url", "published_at"):
        if not record.get(k):
            v.refuse("R14_LINKBACK", "publication record has no %s" % k)
    if record.get("brief_id") and record.get("brief_id") != brief.get("id"):
        v.refuse("R14_LINKBACK", "record points at a different brief")
    rs = resolve_surface(contract, record.get("surface")) if record.get("surface") else None
    bs = resolve_surface(contract, brief.get("surface"))
    if record.get("surface") and rs is None:
        v.refuse("R14_LINKBACK", "published surface %r is not in the recorded vocabulary" % record.get("surface"))
    if bs is None:
        v.refuse("R14_LINKBACK", "the approved surface %r is not in the recorded vocabulary" % brief.get("surface"))
    if rs and not rs["assigned"]:
        v.refuse("R14_LINKBACK", "a post cannot be published to %r" % rs["notion"])
    if rs and bs and rs["notion"] != bs["notion"]:
        v.refuse("R14_LINKBACK", "published surface %r differs from the approved surface %r" % (rs["notion"], bs["notion"]))
    url = record.get("native_post_url") or ""
    if url:
        parsed = urlparse(url)
        if parsed.scheme != "https":
            v.refuse("R14_LINKBACK", "native post URL %r is not https" % url)
        hosts = (rs or {}).get("url_hosts")
        host = parsed.netloc.lower()
        if hosts and not any(host == h or host.endswith("." + h) for h in hosts):
            v.refuse("R14_LINKBACK", "native post URL %r is not on %s for surface %r" % (url, hosts, rs["notion"]))
    prod = production_class(contract, brief.get("format"), brief)
    if prod is None:
        v.refuse("R23_UNKNOWN_OPTION", "format %r is unknown; cannot tell which artifact was approved" % brief.get("format"))
    elif prod == "design":
        approved_set = _artifact_set(brief.get("g2_approved_artifacts"))
        if not approved_set:
            v.refuse("R11_APPROVAL_MISSING", "G2 approved no finished artifact for this design brief")
        elif _artifact_set(record.get("artifacts")) != approved_set:
            v.refuse("R12_REVISION_MISMATCH", "published artifacts %r differ from the approved set %r"
                     % (_artifact_set(record.get("artifacts")), approved_set))
    elif record.get("artifacts"):
        v.refuse("R12_REVISION_MISMATCH", "a text-only approval covers no design artifact")
    return v


def validate_publish_route(route, platform_state):
    """Postiz is a later gated transition; the manual route is the only one open during warm-up."""
    v = Verdict()
    if route == "manual":
        if not _is_human(platform_state.get("publisher")):
            v.refuse("R13_ROUTE_UNAVAILABLE", "manual publishing needs a named human publisher")
        return v
    if route == "postiz":
        for need, msg in (("warmup_cleared", "manual warm-up has not cleared"),
                          ("channel_connected", "the Postiz channel is not connected"),
                          ("approval_matrix_row", "no AUTOMATION_APPROVAL_MATRIX.md row exists")):
            if not platform_state.get(need):
                v.refuse("R13_ROUTE_UNAVAILABLE", "%s; use the manual route" % msg)
        return v
    v.refuse("R13_ROUTE_UNAVAILABLE", "unknown route %r" % route)
    return v


def validate_schema_change(op, contract=None):
    """op = {"action": "rename|retype|drop|reorder_options|add", "db": "DB7", "property": "Script"}"""
    contract = contract or load_contract()
    v = Verdict()
    tc = contract["trigger_contract"]
    if op.get("db") == tc["db_id"] and op.get("property") in tc["properties"] and op.get("action") != "add":
        v.refuse("R17_TRIGGER_PROPERTY",
                 "%s on trigger-read property %r would break routine %s" %
                 (op.get("action"), op.get("property"), tc["routine"]))
    return v


def _print_verdict(label, v):
    if v.ok:
        print("%s: PASS" % label)
        return 0
    print("%s: REFUSED (%d)" % (label, len(v.refusals)))
    for r in v.refusals:
        print("  - %s: %s" % (r["code"], r["detail"]))
    return 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    contract = load_contract()
    if argv[:1] == ["readiness"] and len(argv) == 2:
        try:
            # utf-8-sig: Windows PowerShell 5.1 writes a BOM; a snapshot written there must still load.
            with open(argv[1], encoding="utf-8-sig") as fh:
                ctx = json.load(fh)
        except (OSError, ValueError) as exc:
            print("READINESS: NOT RUN - snapshot unreadable (%s). Not a pass." % exc)
            return 2
        if not isinstance(ctx, dict):
            print("READINESS: NOT RUN - snapshot is not a JSON object. Not a pass.")
            return 2
        return _print_verdict("READINESS (G1, before Ready for Design)", validate_design_readiness(ctx, contract))
    if argv:
        print("usage: content_write_gate.py [readiness SNAPSHOT.json]")
        return 2
    errors = check_contract(contract)
    counts = {db["db_id"]: len(db["fields"]) for db in contract["databases"]}
    if errors:
        print("CONTENT WRITE GATE: FAIL (%d)" % len(errors))
        for e in errors:
            print("  - " + e)
        return 1
    print("CONTENT WRITE GATE: PASS - %d databases, %d fields, one writer each. %s" %
          (len(counts), sum(counts.values()), counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
