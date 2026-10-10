# -*- coding: utf-8 -*-
"""
Content (04) write gate.

    python 04_Content/contracts/content_write_gate.py                     # contract integrity
    python 04_Content/contracts/content_write_gate.py readiness FILE.json   # design path: G1 + readiness before Ready for Design
    python 04_Content/contracts/content_write_gate.py submission FILE.json  # either path: G2 submission (C06) on a snapshot
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
     C10 the six approval-evidence DB7 fields exist with their writers (G1
         fields human-only; the G2 manifest and fingerprint written by C06),
         and G1 / G2 approvers are recorded (owner only, initially)

2. PROPOSAL REFUSALS. validate_write(), validate_design_readiness(),
   validate_generation_start(), validate_g2_submission(),
   validate_publication(), validate_publish_route() and
   validate_schema_change() return a Verdict. A skill runs them, or reasons
   through the same rules, BEFORE any apply. The rules are the refusal list
   in CONTENT_WRITE_CONTRACT.md s5.

   Stage evidence (G1, storyboard, spend approval, claim review, asset
   provenance, a G2 submission) binds to ONE brief ID and ONE Version. A
   record for another brief, another revision, or with no identity at all
   is refused, even when every other value matches (R12, R20, R24, R25).

What it cannot see. The gate validates proposals and snapshots handed to it.
It does not read Notion. A person editing a brief directly in Notion bypasses
it entirely: a copy change made there without a Version bump is invisible to
this file (CONTENT_WRITE_CONTRACT.md s0.2). It narrows the defect for writes
that go through a skill; it does not close it.

Approval evidence (storage unit, 2026-10-10). build_evidence() computes the
G2 Packet Manifest and the G2 Submitted Fingerprint from a FRESH read-back
(the brief, its one linked translation and every linked offer, read in one
session, inside FRESH_WINDOW_SECONDS). compare_evidence() checks stored
evidence against a fresh computation. A failed, partial, stale or foreign read
is R27 and computes nothing: stored evidence is never reused in its place. A
difference is R26. Neither these checks nor the Notion Approval Integrity
formula prevent an edit or authenticate a reviewer: a typed reviewer name is
taken at its word, and a check only runs when someone runs it.
"""
import hashlib
import json
import os
import re
import sys
import unicodedata
from datetime import datetime
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
# Until Design (19)'s Asset Registry defines its ID format, an asset ID is a
# 3-128 character token of letters, digits and . _ : -. That excludes URLs
# (a temporary vendor link is never an asset's reference, contract s9.3),
# whitespace and empty values. Provisional, not Design's ratified format.
ASSET_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{2,127}$")
# A page ID (brief, write target, read-back) is the same kind of token: a Notion
# page ID in either form, or a synthetic test ID. Never blank, padded or spaced.
# Comparison is exact: a dashed and an undashed form of one page do NOT match.
PAGE_ID = ASSET_ID
PRODUCTION_PATHS = ("design", "text_only")

# Approval evidence (storage unit, 2026-10-10).
NOTION_HEX = re.compile(r"^[0-9a-f]{32}$")
NOTION_DASHED = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
FINGERPRINT = re.compile(r"^sha256:[0-9a-f]{64}$")
MANIFEST_FORMAT = "content-g2-manifest/1"
FRESH_WINDOW_SECONDS = 1800          # every part read within 30 minutes before the check
EVIDENCE_TEXT_FIELDS = ("Script", "Caption", "Visual Direction", "Canva Instructions",
                        "Engagement Follow-up", "Evidence")
EVIDENCE_MULTI_FIELDS = ("Platform",)
EVIDENCE_RELATION_FIELDS = ("Translation", "Offer")
TRANSLATION_CONTEXT = ("Surface", "Audience Role", "Format", "Platform")
STORAGE_FIELDS = {"G1 Decision": "human_only", "G1 Reviewer": "human_only", "G1 Decided At": "human_only",
                  "G1 Revision": "human_only", "G2 Packet Manifest": "C06", "G2 Submitted Fingerprint": "C06"}
EVIDENCE_CHANGE_REASONS = ("context_change", "asset_change")


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
    for name in ("surface", "audience_role", "format", "g1_decision", "offer_status"):
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

    for name, writer in STORAGE_FIELDS.items():
        if db7.get(name, {}).get("writer") != writer:
            errors.append("C10 DB7 %s must exist with writer %s" % (name, writer))
    approvers = contract.get("approvers", {})
    for gate_name in ("g1", "g2"):
        names = approvers.get(gate_name)
        if not (isinstance(names, list) and names and all(isinstance(n, str) and n.strip() == n and n for n in names)):
            errors.append("C10 approvers.%s must list at least one exact reviewer name" % gate_name)
    for o in vocabs_options(contract, "g1_decision"):
        if o.get("decision") not in ("passed", "returned") or (o["decision"] == "passed") != (o.get("path") in PRODUCTION_PATHS):
            errors.append("C10 g1_decision option %r needs decision passed/returned and a path when passed" % o.get("notion"))
    return errors


def vocabs_options(contract, vocabulary):
    return (contract.get("vocabularies", {}).get(vocabulary) or {}).get("options", [])


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
    elif proposal.get("reason") in EVIDENCE_CHANGE_REASONS:
        # A context-only or asset-only change: nothing in DB7's copy moved, so no copy
        # edit is invented. The change itself must be evidenced against the stored
        # manifest (or, for context before any submission, a declared baseline).
        if mode != "VERSION":
            v.refuse("R21_REVISION_INCREMENT", "an evidenced %s is a VERSION, not an %s" % (proposal["reason"], mode))
        if _evidenced_change(v, proposal, state, contract, prior_rev) and new != prior_rev + 1:
            v.refuse("R21_REVISION_INCREMENT", "%s: Version must be %d (prior %d + 1), got %d"
                     % (proposal["reason"], prior_rev + 1, prior_rev, new))
    else:
        if new != prior_rev:
            v.refuse("R21_REVISION_INCREMENT",
                     "Version moves %d -> %d with no publication-affecting change" % (prior_rev, new))
        if mode == "VERSION":
            v.refuse("R21_REVISION_INCREMENT", "VERSION with no publication-affecting change; this is a NO_OP")


def _evidenced_change(v, proposal, state, contract, prior_rev):
    """True only when the declared context or asset change is visible in the evidence."""
    prior = (state or {}).get("prior") or {}
    stored = parse_manifest(v, prior["G2 Packet Manifest"]) if prior.get("G2 Packet Manifest") else None
    if prior.get("G2 Packet Manifest") and stored is None:
        return False
    if proposal["reason"] == "context_change":
        ctx_v, ctx = read_context((state or {}).get("fresh"), contract)
        v.extend(ctx_v)
        if ctx is None:
            return False
        if ctx["revision"] != prior_rev:
            v.refuse("R12_REVISION_MISMATCH", "the fresh read shows Version %r; the brief on record is at %d"
                     % (ctx["revision"], prior_rev))
            return False
        baseline = stored["resolved"] if stored is not None else proposal.get("context_before")
        if not isinstance(baseline, dict):
            v.refuse("R21_REVISION_INCREMENT", "a context-only VERSION needs a baseline: the stored G2 Packet "
                     "Manifest, or a declared context_before when nothing was submitted yet")
            return False
        if baseline == ctx["resolved"]:
            v.refuse("R21_REVISION_INCREMENT", "the resolved context has not changed against its baseline; nothing to version")
            return False
        return True
    if stored is None:
        v.refuse("R21_REVISION_INCREMENT", "an asset-only VERSION needs the stored G2 Packet Manifest to compare against")
        return False
    new_assets = proposal.get("assets")
    if not isinstance(new_assets, list):
        v.refuse("R25_ASSET_INVALID", "an asset-only VERSION must name the new asset set")
        return False
    _check_assets(v, new_assets, None, None, "new", provenance=False)
    if _artifact_set(new_assets) == _artifact_set(stored["assets"]):
        v.refuse("R21_REVISION_INCREMENT", "the asset set has not changed against the stored manifest; nothing to version")
        return False
    return v.ok


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
    prior = (state or {}).get("prior")
    target = proposal.get("target")
    if isinstance(prior, dict) and prior.get("id") and target and prior["id"] != target:
        v.refuse("R24_EVIDENCE_IDENTITY", "the prior record %r is not the write target %r" % (prior["id"], target))
    if proposal.get("db") == "DB7" and proposal.get("fields", {}).get("G2 Decision") == "Submitted for review":
        _check_submission_target(v, proposal, state, contract)
    return v


def valid_page_id(x):
    return isinstance(x, str) and bool(PAGE_ID.match(x))


def _check_submission_target(v, proposal, state, contract):
    """The G2 packet must describe the page being written, at its current Version.

    Three IDs must each be a valid page ID and be exactly equal: proposal.target
    (the page written), state.prior.id (the page read back) and
    g2_submission.brief.id (the page the packet describes). Exact string
    equality: no trimming, no case-folding, no dash normalisation."""
    sub = proposal.get("g2_submission")
    if not sub:
        v.refuse("R22_STAGE_ORDER", "Submitted for review needs the submission context: brief, revision, G1, "
                 "claim review, and the finished artifact or the final copy")
        return
    prior = (state or {}).get("prior")
    ids = [("proposal.target", proposal.get("target")),
           ("state.prior.id", prior.get("id") if isinstance(prior, dict) else None),
           ("g2_submission.brief.id", (sub.get("brief") or {}).get("id"))]
    unusable = False
    if not isinstance(prior, dict):
        v.refuse("R24_EVIDENCE_IDENTITY", "the target brief was not read back (state.prior), so its ID and Version are unknown")
        unusable = True
    for name, value in ids:
        if name == "state.prior.id" and not isinstance(prior, dict):
            continue
        if not valid_page_id(value):
            v.refuse("R24_EVIDENCE_IDENTITY", "%s is missing or not a valid page ID (%r)" % (name, value))
            unusable = True
    if not unusable and len({value for _, value in ids}) != 1:
        v.refuse("R24_EVIDENCE_IDENTITY", "the IDs disagree: target %r, read-back %r, packet %r"
                 % tuple(value for _, value in ids))
    if isinstance(prior, dict):
        on_record = revision_value(prior.get("Version"))
        described = revision_value((sub.get("brief") or {}).get("version"))
        if on_record is None:
            v.refuse("R20_REVISION_INVALID", "the target brief has no valid Version (%r)" % prior.get("Version"))
        elif described != on_record:
            v.refuse("R12_REVISION_MISMATCH", "the submission describes Version %r; the target is at %d" % (described, on_record))
    _check_submission_evidence(v, proposal, state, contract, sub)
    v.extend(validate_g2_submission(sub, contract))


def _check_submission_evidence(v, proposal, state, contract, sub):
    """Storage unit (2026-10-10). The G2 Packet Manifest and G2 Submitted Fingerprint
    are computed by the gate from a FRESH read-back of the exact write target. They
    are never typed, and never reused from an earlier submission."""
    fields = proposal.get("fields", {})
    for name in ("G2 Packet Manifest", "G2 Submitted Fingerprint"):
        if not fields.get(name):
            v.refuse("R22_STAGE_ORDER", "Submitted for review must also write %s" % name)
    fresh = (state or {}).get("fresh")
    ev_v, ev = build_evidence(fresh, sub.get("artifacts") or [], contract)
    v.extend(ev_v)
    if ev is None:
        return
    read_id = (fresh.get("brief") or {}).get("page_id")
    if read_id != proposal.get("target"):
        v.refuse("R24_EVIDENCE_IDENTITY", "the fresh read is of page %r, not the write target %r"
                 % (read_id, proposal.get("target")))
    described = revision_value((sub.get("brief") or {}).get("version"))
    if ev["context"]["revision"] != described:
        v.refuse("R12_REVISION_MISMATCH", "the fresh read shows Version %r; the packet describes %r"
                 % (ev["context"]["revision"], described))
    copy = sub.get("brief") or {}
    read = ev["context"]["fields"]
    for key, name in (("caption", "Caption"), ("script", "Script"),
                      ("visual_direction", "Visual Direction"), ("canva_instructions", "Canva Instructions")):
        if _norm_text(copy.get(key) or "") != read.get(name):
            v.refuse("R26_FINGERPRINT_MISMATCH", "the packet's %s differs from the fresh read of the page" % name)
    resolved = ev["context"]["resolved"]
    tr = sub.get("translation") or {}
    surface = resolve_surface(contract, tr.get("surface"))
    if (surface or {}).get("notion") != resolved.get("surface") or tr.get("format") != resolved.get("format"):
        v.refuse("R26_FINGERPRINT_MISMATCH", "the packet's translation context (%r, %r) differs from the fresh read (%r, %r)"
                 % (tr.get("surface"), tr.get("format"), resolved.get("surface"), resolved.get("format")))
    for name, key in (("G2 Packet Manifest", "manifest_text"), ("G2 Submitted Fingerprint", "fingerprint")):
        if fields.get(name) and fields[name] != ev[key]:
            v.refuse("R26_FINGERPRINT_MISMATCH", "the %s written differs from the one computed from the fresh read-back" % name)
    prior = (state or {}).get("prior") or {}
    if prior.get("G2 Submitted Fingerprint") and prior.get("G2 Packet Manifest"):
        earlier = parse_manifest(Verdict(), prior["G2 Packet Manifest"])
        if (earlier is not None and earlier.get("revision") == ev["context"]["revision"]
                and prior["G2 Submitted Fingerprint"] != ev["fingerprint"]):
            v.refuse("R21_REVISION_INCREMENT", "since the last submission at Version %d, %s changed without a Version "
                     "bump; record a VERSION first" % (ev["context"]["revision"],
                                                     "; ".join(evidence_diff(earlier, ev["manifest"])) or "publishable copy"))


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


def _brief_identity(v, b, stage):
    """The brief under check must carry its own ID, or no evidence can be bound to it."""
    bid = (b or {}).get("id")
    if not valid_page_id(bid):
        v.refuse("R24_EVIDENCE_IDENTITY", "the brief has no valid ID (%r), so %s evidence cannot be bound to it"
                 % (bid, stage))
        return None
    return bid


def _bind(v, ev, brief_id, rev, what, rev_key="revision"):
    """Stage evidence must name this exact brief and its current Version. A record
    for another brief, another revision, or with no identity is refused, even when
    every other value in it matches."""
    ev = ev if isinstance(ev, dict) else {}
    named = ev.get("brief_id")
    if not isinstance(named, str) or not named.strip():
        v.refuse("R24_EVIDENCE_IDENTITY", "%s names no brief" % what)
    elif brief_id is not None and named != brief_id:
        v.refuse("R24_EVIDENCE_IDENTITY", "%s belongs to brief %r, not %r" % (what, named, brief_id))
    got = revision_value(ev.get(rev_key))
    if got is None:
        v.refuse("R20_REVISION_INVALID", "%s names no valid revision (%r)" % (what, ev.get(rev_key)))
    elif rev is not None and got != rev:
        v.refuse("R12_REVISION_MISMATCH", "%s is for revision %d; the brief is at %d" % (what, got, rev))


def _human_record(v, rec, brief_id, rev, what):
    """A gate record (G1, spend approval): a named human, a date, this brief, this Version."""
    rec = rec if isinstance(rec, dict) else {}
    if not (_is_human(rec.get("by")) and rec.get("at")):
        v.refuse("R22_STAGE_ORDER", "%s is not recorded by a named human with a date" % what)
    _bind(v, rec, brief_id, rev, what)


def _authorised(v, contract, gate_name, reviewer, what):
    """Owner-only, initially (owner authorisation 2026-10-10). This compares a typed
    name with the recorded approver list. It does not authenticate anyone."""
    allowed = (contract or load_contract()).get("approvers", {}).get(gate_name, [])
    if reviewer not in allowed:
        v.refuse("R28_REVIEWER_NOT_AUTHORISED", "%s was recorded by %r; only %s may decide it" % (what, reviewer, allowed))


def g1_from_properties(props, brief_id, contract=None):
    """The G1 record as stored on the brief (G1 Decision / Reviewer / Decided At /
    Revision), shaped for _check_g1. The page it was read from IS the binding, so
    brief_id is the ID of that page. None when no G1 has been recorded."""
    contract = contract or load_contract()
    decision = props.get("G1 Decision")
    if decision is None or decision == "":
        return None
    opt = next((o for o in vocabs_options(contract, "g1_decision") if o["notion"] == decision), None)
    reviewer = props.get("G1 Reviewer")
    return {"decision": opt["decision"] if opt else "unrecognised option %r" % decision,
            "path": opt.get("path") if opt else None,
            "by": "human:%s" % reviewer if isinstance(reviewer, str) and reviewer else None,
            "at": props.get("G1 Decided At"), "brief_id": brief_id, "revision": props.get("G1 Revision")}


def _check_g1(v, g1, brief_id, rev, path, contract=None):
    """G1 is required on BOTH paths, design and text-only. The human records the
    production path at G1; the brief as it stands must still be that path."""
    g1 = g1 if isinstance(g1, dict) else {}
    if g1.get("decision") != "passed":
        v.refuse("R22_STAGE_ORDER", "G1 concept review has not passed this brief (decision %r)" % g1.get("decision"))
        return
    _human_record(v, g1, brief_id, rev, "G1 concept review")
    if _is_human(g1.get("by")):
        _authorised(v, contract, "g1", g1["by"][len("human:"):], "G1")
    if g1.get("path") not in PRODUCTION_PATHS:
        v.refuse("R22_STAGE_ORDER", "G1 does not record the production path (design or text_only): %r" % g1.get("path"))
    elif path is not None and g1["path"] != path:
        v.refuse("R22_STAGE_ORDER", "G1 decided the %s path; the brief as it stands is %s work" % (g1["path"], path))


def valid_asset_id(x):
    return isinstance(x, str) and bool(ASSET_ID.match(x))


def _check_assets(v, arts, brief_id, rev, what, provenance=True):
    """Each asset: a valid ID, a whole-number version >= 1, listed once; and, on the
    authoritative lists, production provenance naming this brief and revision."""
    if not isinstance(arts, list):
        v.refuse("R25_ASSET_INVALID", "the %s asset list is not a list" % what)
        return
    seen = set()
    for a in arts:
        a = a if isinstance(a, dict) else {}
        aid = a.get("asset_id")
        label = "%s asset %r" % (what, aid)
        if not valid_asset_id(aid):
            v.refuse("R25_ASSET_INVALID", "%s: not a valid asset ID (a registry token; never a URL or blank)" % label)
        elif aid in seen:
            v.refuse("R25_ASSET_INVALID", "%s is listed twice" % label)
        else:
            seen.add(aid)
        if revision_value(a.get("version")) is None:
            v.refuse("R25_ASSET_INVALID", "%s has no whole-number version >= 1 (%r)" % (label, a.get("version")))
        if provenance:
            _bind(v, a.get("provenance"), brief_id, rev, "production provenance of %s" % label, rev_key="brief_revision")


def validate_design_readiness(ctx, contract=None):
    """Design path: G1 concept review + readiness, checked BEFORE a human sets Ready for Design.

    ctx = {"brief": {"id", "version", "visual_direction", "canva_instructions", "caption", "script"},
           "links": {"opportunity", "translation", "narrative_position_ids"},
           "opportunity": {"strategic_dragon"},
           "translation": {"editorial_dragon", "surface", "format", "family_id"},
           "g1": {"decision": "passed", "path": "design", "by": "human:...", "at", "brief_id", "revision"}}"""
    contract = contract or load_contract()
    v = Verdict()
    b, links, tr = ctx.get("brief") or {}, ctx.get("links") or {}, ctx.get("translation") or {}
    bid = _brief_identity(v, b, "readiness")
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
        v.refuse("R22_STAGE_ORDER", "text-only content does not go to Design; its G1 is checked at G2 submission")
    elif not all((b.get(k) or "").strip() for k in ("visual_direction", "canva_instructions")):
        v.refuse("R22_STAGE_ORDER", "Visual Direction and Canva Instructions are needed before Design")
    _check_g1(v, ctx.get("g1"), bid, rev, "design", contract)
    return v


def validate_generation_start(ctx, contract=None):
    """Human spend approval, checked BEFORE any generation or credit spend.

    ctx = {"brief": {"id", "version", "publishing_status"},
           "storyboard": {"brief_id", "revision"},     # read from the routine's COMPLETED marker
           "spend_approval": {"by": "human:...", "at", "brief_id", "revision", "scope"}}"""
    v = Verdict()
    b = ctx.get("brief") or {}
    bid = _brief_identity(v, b, "generation")
    rev = revision_value(b.get("version"))
    if rev is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % b.get("version"))
    if b.get("publishing_status") != "Ready for Design":
        v.refuse("R22_STAGE_ORDER", "generation before the brief reached Design (status %r)" % b.get("publishing_status"))
    if not ctx.get("storyboard"):
        v.refuse("R22_STAGE_ORDER", "no storyboard on record for this brief")
    else:
        _bind(v, ctx["storyboard"], bid, rev, "storyboard")
    sa = ctx.get("spend_approval")
    if not sa:
        v.refuse("R22_STAGE_ORDER", "no human spend approval; nothing may be generated or spent")
        return v
    _human_record(v, sa, bid, rev, "spend approval")
    if not sa.get("scope"):
        v.refuse("R22_STAGE_ORDER", "spend approval names no scope (what may be generated)")
    return v


def validate_g2_submission(ctx, contract=None):
    """G2 is on the exact finished artifact, and G1 is required on both paths.

    ctx = {"brief": {"id", "version", "caption", "script", "visual_direction", "canva_instructions"},
           "revision": N,                                     # what is being submitted
           "opportunity": {"strategic_dragon"},
           "translation": {"editorial_dragon", "surface", "format"},
           "g1": {"decision": "passed", "path", "by", "at", "brief_id", "revision"},
           "claim_review": {"verdict": "pass", "brief_id", "revision"},
           "artifacts": [{"asset_id", "version", "rights",
                          "provenance": {"brief_id", "brief_revision"}}]}   # design work only"""
    contract = contract or load_contract()
    v = Verdict()
    b, tr = ctx.get("brief") or {}, ctx.get("translation") or {}
    bid = _brief_identity(v, b, "G2 submission")
    cur, sub = revision_value(b.get("version")), revision_value(ctx.get("revision"))
    if cur is None:
        v.refuse("R20_REVISION_INVALID", "brief Version %r is not a whole number >= 1" % b.get("version"))
    if sub is None:
        v.refuse("R20_REVISION_INVALID", "submitted revision %r is not a whole number >= 1" % ctx.get("revision"))
    if cur and sub and cur != sub:
        v.refuse("R12_REVISION_MISMATCH", "submitting revision %d; the brief is at %d" % (sub, cur))
    _dragon_and_surface(v, ctx, contract, "G2 submission")
    cr = ctx.get("claim_review")
    if not isinstance(cr, dict) or cr.get("verdict") != "pass":
        v.refuse("R22_STAGE_ORDER", "claim review (C05) has not passed (verdict %r)" % (cr or {}).get("verdict"))
    _bind(v, cr, bid, cur, "claim review (C05)")
    prod = production_class(contract, tr.get("format"), b)
    _check_g1(v, ctx.get("g1"), bid, cur, prod, contract)
    arts = ctx.get("artifacts") or []
    if prod is None:
        v.refuse("R23_UNKNOWN_OPTION", "format %r is unknown; cannot tell design work from text-only" % tr.get("format"))
    elif prod == "text_only":
        if not any((b.get(k) or "").strip() for k in ("caption", "script")):
            v.refuse("R22_STAGE_ORDER", "text-only content reaches G2 once its final copy exists; Caption and Script are empty")
        if arts:
            v.refuse("R22_STAGE_ORDER", "a text-only brief lists design artifacts; it is not asset-free, so route it through Design")
    else:
        if not arts:
            v.refuse("R22_STAGE_ORDER", "G2 judges the finished artifact; Design has delivered none for revision %r" % cur)
        else:
            _check_assets(v, arts, bid, cur, "submitted", provenance=True)
            for a in arts:
                if (a or {}).get("rights") in (None, "", "unknown"):
                    v.refuse("R22_STAGE_ORDER", "submitted asset %r has unknown rights" % (a or {}).get("asset_id"))
    return v


# --------------------------------------------------------------------------- approval evidence

def canonical_page_id(x):
    """One canonical form for evidence: 32 lowercase hex, no dashes. A dashed
    lowercase UUID converts. Anything else (upper case, padded, a fixture token,
    a non-string) is not a Notion page ID here and yields None."""
    if isinstance(x, str):
        if NOTION_HEX.match(x):
            return x
        if NOTION_DASHED.match(x):
            return x.replace("-", "")
    return None


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _norm_text(s):
    return unicodedata.normalize("NFC", s.replace("\r\n", "\n"))


def _parse_time(s):
    if not isinstance(s, str):
        return None
    try:
        t = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return t if t.tzinfo is not None else None


def _fresh_part(v, part, name, session, checked_at):
    """A part of the read-back counts only when it was read completely, in this
    session, with a timezone-aware read time inside the freshness window."""
    if not isinstance(part, dict) or part.get("status") != "complete":
        status = part.get("status") if isinstance(part, dict) else None
        v.refuse("R27_CONTEXT_UNREADABLE", "%s was not read completely (status %r)" % (name, status))
        return False
    ok = True
    if part.get("session") != session:
        v.refuse("R27_CONTEXT_UNREADABLE", "%s was read in another session (%r)" % (name, part.get("session")))
        ok = False
    t = _parse_time(part.get("read_at"))
    if t is None:
        v.refuse("R27_CONTEXT_UNREADABLE", "%s has no timezone-aware read time (%r)" % (name, part.get("read_at")))
        ok = False
    elif checked_at is not None and (t > checked_at or (checked_at - t).total_seconds() > FRESH_WINDOW_SECONDS):
        v.refuse("R27_CONTEXT_UNREADABLE", "%s was read at %s, outside the %d-minute window before the check"
                 % (name, part.get("read_at"), FRESH_WINDOW_SECONDS // 60))
        ok = False
    if not isinstance(part.get("properties"), dict):
        v.refuse("R27_CONTEXT_UNREADABLE", "%s carries no properties" % name)
        ok = False
    return ok


def _page_ids(v, values, what):
    values = [] if values is None else values
    if not isinstance(values, list):
        v.refuse("R27_CONTEXT_UNREADABLE", "%s is not a list of page IDs (%r)" % (what, values))
        return None
    out = []
    for x in values:
        c = canonical_page_id(x)
        if c is None:
            v.refuse("R27_CONTEXT_UNREADABLE", "%s holds %r, which is not a Notion page ID" % (what, x))
            return None
        out.append(c)
    if len(set(out)) != len(out):
        v.refuse("R27_CONTEXT_UNREADABLE", "%s lists a page twice" % what)
        return None
    return sorted(out)


def _known_option(v, contract, vocabulary, value, what, code):
    """Exact Notion option name or None (read, and empty). Anything else is refused."""
    if value is None:
        return None
    if not isinstance(value, str) or value not in {o["notion"] for o in vocabs_options(contract, vocabulary)}:
        v.refuse(code, "%s = %r is not a recorded Notion option" % (what, value))
    return value


def read_context(fresh, contract=None):
    """Normalise a FRESH read-back into {brief_id, revision, fields, resolved}.

    fresh = {"session": str, "checked_at": ISO-8601 with zone,
             "brief":       {"status": "complete", "session", "read_at", "page_id", "properties": {...DB7}},
             "translation": {"status", "session", "read_at", "page_id",
                             "properties": {"Surface", "Audience Role", "Format", "Platform": [ids]}},
             "offers":      [{"status", "session", "read_at", "page_id", "properties": {"Offer Status"}}]}

    Returns (verdict, None) when anything is unreadable, partial, stale, from
    another session, foreign or unknown. Stored evidence is never substituted."""
    contract = contract or load_contract()
    v = Verdict()
    if not isinstance(fresh, dict):
        v.refuse("R27_CONTEXT_UNREADABLE", "no fresh read-back was supplied; stored evidence is not reused in its place")
        return v, None
    session = fresh.get("session")
    if not (isinstance(session, str) and session and session.strip() == session):
        v.refuse("R27_CONTEXT_UNREADABLE", "the read-back names no session")
    checked_at = _parse_time(fresh.get("checked_at"))
    if checked_at is None:
        v.refuse("R27_CONTEXT_UNREADABLE", "the read-back has no timezone-aware check time")
    brief_ok = _fresh_part(v, fresh.get("brief"), "the brief", session, checked_at)
    translation_ok = _fresh_part(v, fresh.get("translation"), "the linked translation", session, checked_at)
    if not brief_ok:
        return v, None
    bp = fresh["brief"]["properties"]
    bid = canonical_page_id(fresh["brief"].get("page_id"))
    if bid is None:
        v.refuse("R27_CONTEXT_UNREADABLE", "the brief page ID %r is not a Notion page ID" % fresh["brief"].get("page_id"))
    needed = EVIDENCE_TEXT_FIELDS + EVIDENCE_MULTI_FIELDS + EVIDENCE_RELATION_FIELDS + ("Version",)
    missing = [k for k in needed if k not in bp]
    if missing:
        v.refuse("R27_CONTEXT_UNREADABLE", "the brief read is partial: %s missing" % ", ".join(missing))
        return v, None
    rev = revision_value(bp["Version"])
    if rev is None:
        v.refuse("R20_REVISION_INVALID", "the brief's Version %r is not a whole number >= 1" % bp["Version"])
    fields = {}
    for k in EVIDENCE_TEXT_FIELDS:
        val = "" if bp[k] is None else bp[k]
        if not isinstance(val, str):
            v.refuse("R27_CONTEXT_UNREADABLE", "the brief's %s is not text (%r)" % (k, val))
            continue
        fields[k] = _norm_text(val)
    platforms = [] if bp["Platform"] is None else bp["Platform"]
    if not (isinstance(platforms, list) and all(isinstance(p, str) for p in platforms)):
        v.refuse("R27_CONTEXT_UNREADABLE", "the brief's Platform is not a list of names (%r)" % (platforms,))
    else:
        fields["Platform"] = sorted(_norm_text(p) for p in platforms)
    for k in EVIDENCE_RELATION_FIELDS:
        ids = _page_ids(v, bp[k], "the brief's %s relation" % k)
        if ids is not None:
            fields[k] = ids
    resolved = {}
    linked_translation = fields.get("Translation")
    if linked_translation is not None and len(linked_translation) != 1:
        v.refuse("R27_CONTEXT_UNREADABLE", "the brief links %d translations; exactly one is required"
                 % len(linked_translation))
    elif linked_translation is not None and translation_ok:
        tp = fresh["translation"]["properties"]
        read_id = canonical_page_id(fresh["translation"].get("page_id"))
        if read_id != linked_translation[0]:
            v.refuse("R24_EVIDENCE_IDENTITY", "the translation read (%r) is not the page the brief links (%r)"
                     % (fresh["translation"].get("page_id"), linked_translation[0]))
        missing = [k for k in TRANSLATION_CONTEXT if k not in tp]
        if missing:
            v.refuse("R27_CONTEXT_UNREADABLE", "the translation read is partial: %s missing" % ", ".join(missing))
        else:
            resolved["translation_id"] = linked_translation[0]
            resolved["surface"] = _known_option(v, contract, "surface", tp["Surface"], "Surface", "R09_SURFACE_UNKNOWN")
            resolved["audience_role"] = _known_option(v, contract, "audience_role", tp["Audience Role"],
                                                      "Audience Role", "R23_UNKNOWN_OPTION")
            resolved["format"] = _known_option(v, contract, "format", tp["Format"], "Format", "R23_UNKNOWN_OPTION")
            platform_ids = _page_ids(v, tp["Platform"], "the translation's Platform relation")
            if platform_ids is not None:
                resolved["platform_ids"] = platform_ids
    parts = fresh.get("offers", [])
    if not isinstance(parts, list):
        v.refuse("R27_CONTEXT_UNREADABLE", "the offer reads are not a list")
        parts = []
    by_id = {}
    for part in parts:
        pid = canonical_page_id(part.get("page_id")) if isinstance(part, dict) else None
        if pid is None:
            v.refuse("R27_CONTEXT_UNREADABLE", "an offer read has no Notion page ID")
        elif pid in by_id:
            v.refuse("R27_CONTEXT_UNREADABLE", "offer %s was read twice" % pid)
        else:
            by_id[pid] = part
    linked_offers = fields.get("Offer")
    if linked_offers is not None:
        offers = []
        for oid in linked_offers:
            part = by_id.get(oid)
            if part is None:
                v.refuse("R27_CONTEXT_UNREADABLE", "linked offer %s was not read" % oid)
                continue
            if not _fresh_part(v, part, "linked offer %s" % oid, session, checked_at):
                continue
            if "Offer Status" not in part["properties"]:
                v.refuse("R27_CONTEXT_UNREADABLE", "the read of offer %s is partial: Offer Status missing" % oid)
                continue
            offers.append({"offer_id": oid,
                           "offer_status": _known_option(v, contract, "offer_status", part["properties"]["Offer Status"],
                                                         "Offer Status of %s" % oid, "R23_UNKNOWN_OPTION")})
        for pid in by_id:
            if pid not in linked_offers:
                v.refuse("R24_EVIDENCE_IDENTITY", "offer %s was read but is not linked to the brief" % pid)
        resolved["offers"] = sorted(offers, key=lambda o: o["offer_id"])
    if not v.ok:
        return v, None
    return v, {"brief_id": bid, "revision": rev, "fields": fields, "resolved": resolved}


def build_evidence(fresh, assets, contract=None, provenance=True):
    """Compute the G2 Packet Manifest and G2 Submitted Fingerprint from a fresh read.

    Fingerprint = "sha256:" + SHA-256 of canonical JSON (keys sorted, separators
    "," and ":", UTF-8, NFC text, CRLF -> LF, nothing trimmed) of
    {brief_id, revision, fields: every publication-affecting DB7 field,
     assets: [[asset_id, version], ...] sorted, resolved: {translation_id, surface,
     audience_role, format, platform_ids, offers: [{offer_id, offer_status}]}}.
    `provenance=False` is for the publication recompute, where the published
    assets carry no provenance (the stored manifest holds it)."""
    contract = contract or load_contract()
    v, ctx = read_context(fresh, contract)
    if ctx is None:
        return v, None
    if not isinstance(assets, list):
        v.refuse("R25_ASSET_INVALID", "the asset set is not a list")
        return v, None
    norm = []
    for a in assets:
        a = a if isinstance(a, dict) else {}
        prov = a.get("provenance") if isinstance(a.get("provenance"), dict) else {}
        named = prov.get("brief_id")
        norm.append({"asset_id": a.get("asset_id"), "version": a.get("version"),
                     "provenance": {"brief_id": canonical_page_id(named) or named,
                                    "brief_revision": prov.get("brief_revision")}})
    _check_assets(v, norm, ctx["brief_id"], ctx["revision"], "packet", provenance=provenance)
    if not v.ok:
        return v, None
    manifest_assets = []
    for a in sorted(norm, key=lambda a: a["asset_id"]):
        entry = {"asset_id": a["asset_id"], "version": revision_value(a["version"])}
        if provenance:
            entry["provenance"] = {"brief_id": a["provenance"]["brief_id"],
                                   "brief_revision": revision_value(a["provenance"]["brief_revision"])}
        manifest_assets.append(entry)
    manifest = {"format": MANIFEST_FORMAT, "brief_id": ctx["brief_id"], "revision": ctx["revision"],
                "assets": manifest_assets, "resolved": ctx["resolved"]}
    payload = {"brief_id": ctx["brief_id"], "revision": ctx["revision"], "fields": ctx["fields"],
               "assets": [[a["asset_id"], a["version"]] for a in manifest_assets], "resolved": ctx["resolved"]}
    digest = hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()
    return v, {"fingerprint": "sha256:" + digest, "manifest": manifest,
               "manifest_text": canonical_json(manifest), "context": ctx}


def parse_manifest(v, text, what="the stored G2 Packet Manifest"):
    """The stored manifest, or None with an R26. A manifest that is not in canonical
    form was edited by hand and is not trusted."""
    if not isinstance(text, str) or not text:
        v.refuse("R26_FINGERPRINT_MISMATCH", "%s is empty" % what)
        return None
    try:
        m = json.loads(text)
    except ValueError:
        v.refuse("R26_FINGERPRINT_MISMATCH", "%s is not JSON" % what)
        return None
    if (not isinstance(m, dict) or m.get("format") != MANIFEST_FORMAT
            or not isinstance(m.get("assets"), list) or not isinstance(m.get("resolved"), dict)):
        v.refuse("R26_FINGERPRINT_MISMATCH", "%s is not a %s manifest" % (what, MANIFEST_FORMAT))
        return None
    if canonical_json(m) != text:
        v.refuse("R26_FINGERPRINT_MISMATCH", "%s is not in canonical form, so it was edited outside the gate" % what)
        return None
    return m


def evidence_diff(old, new):
    """Names of the manifest components that differ (copy is not in the manifest)."""
    if not isinstance(old, dict) or not isinstance(new, dict):
        return []
    moved = [k for k in ("brief_id", "revision") if old.get(k) != new.get(k)]
    if _artifact_set(old.get("assets")) != _artifact_set(new.get("assets")):
        moved.append("assets")
    o, n = old.get("resolved") or {}, new.get("resolved") or {}
    for k in sorted(set(o) | set(n)):
        if o.get(k) != n.get(k):
            moved.append("resolved.%s: %r -> %r" % (k, o.get(k), n.get(k)))
    return moved


def compare_evidence(v, stored_fingerprint, stored_manifest, fresh_ev):
    """R26 when stored evidence and a fresh computation differ, naming what moved."""
    if not (isinstance(stored_fingerprint, str) and FINGERPRINT.match(stored_fingerprint)):
        v.refuse("R26_FINGERPRINT_MISMATCH", "no valid G2 Submitted Fingerprint on record (%r)" % (stored_fingerprint,))
        return
    if fresh_ev is None:
        return  # the read failed: R27 is already recorded, and nothing stored is inherited
    if stored_fingerprint != fresh_ev["fingerprint"]:
        moved = evidence_diff(stored_manifest, fresh_ev["manifest"])
        v.refuse("R26_FINGERPRINT_MISMATCH", "the approved evidence no longer matches a fresh read: %s"
                 % ("; ".join(moved) or "publishable copy or a DB7 relation changed (copy is not stored in the manifest)"))


# --------------------------------------------------------------------------- publication

def _artifact_set(arts):
    return sorted((str(a.get("asset_id")), revision_value(a.get("version")) or 0)
                  for a in (arts or []) if isinstance(a, dict))


def validate_publication(record, brief, contract=None, fresh=None):
    """A manual publication record linking a live post back to the exact approved artifact.

    brief = {"id", "version", "g2_decision", "g2_reviewer", "g2_decided_at", "g2_approved_revision",
             "g2_packet_manifest", "g2_submitted_fingerprint"}    # as stored on DB7
    record = {"brief_id", "revision", "surface", "native_post_url", "published_at", "publisher",
              "artifacts": [{"asset_id", "version"}]}
    fresh  = a fresh read-back (read_context). The approved surface, format and asset set come
             from the stored manifest; the stored fingerprint must equal a recomputation from
             the fresh read plus the assets actually published."""
    contract = contract or load_contract()
    v = Verdict()
    bid = _brief_identity(v, brief, "publication")
    if not _is_human(record.get("publisher")):
        v.refuse("R11_APPROVAL_MISSING", "agents never publish; publisher must be a named human")
    if brief.get("g2_decision") != "Approved":
        v.refuse("R11_APPROVAL_MISSING", "G2 decision is %r, not Approved" % brief.get("g2_decision"))
    if not (brief.get("g2_reviewer") and brief.get("g2_decided_at")):
        v.refuse("R11_APPROVAL_MISSING", "G2 approval has no reviewer or date on record")
    elif brief.get("g2_decision") == "Approved":
        _authorised(v, contract, "g2", brief.get("g2_reviewer"), "G2")
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
    if record.get("brief_id") and record.get("brief_id") != bid:
        v.refuse("R14_LINKBACK", "record points at brief %r, not %r" % (record.get("brief_id"), bid))
    canonical_bid = canonical_page_id(bid) if bid else None
    if bid and canonical_bid is None:
        v.refuse("R24_EVIDENCE_IDENTITY", "brief ID %r is not a Notion page ID, so stored evidence cannot be bound" % bid)
    stored = parse_manifest(v, brief.get("g2_packet_manifest"))
    if stored is not None:
        if stored.get("brief_id") != canonical_bid:
            v.refuse("R24_EVIDENCE_IDENTITY", "the stored manifest is for brief %r, not %r" % (stored.get("brief_id"), canonical_bid))
        if approved is not None and stored.get("revision") != approved:
            v.refuse("R12_REVISION_MISMATCH", "the stored manifest is for revision %r; the approval is for %r"
                     % (stored.get("revision"), approved))
    approved_context = (stored or {}).get("resolved") or {}
    rs = resolve_surface(contract, record.get("surface")) if record.get("surface") else None
    bs = resolve_surface(contract, approved_context.get("surface")) if stored is not None else None
    if record.get("surface") and rs is None:
        v.refuse("R14_LINKBACK", "published surface %r is not in the recorded vocabulary" % record.get("surface"))
    if stored is not None and bs is None:
        v.refuse("R14_LINKBACK", "the approved surface %r is not in the recorded vocabulary" % approved_context.get("surface"))
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
    published_arts = record.get("artifacts") or []
    ev_v, ev = build_evidence(fresh, published_arts, contract, provenance=False)
    v.extend(ev_v)
    if ev is not None:
        if canonical_bid and ev["context"]["brief_id"] != canonical_bid:
            v.refuse("R24_EVIDENCE_IDENTITY", "the fresh read is of brief %r, not %r" % (ev["context"]["brief_id"], canonical_bid))
        if cur is not None and ev["context"]["revision"] != cur:
            v.refuse("R12_REVISION_MISMATCH", "the fresh read shows Version %r; the record says %d" % (ev["context"]["revision"], cur))
    compare_evidence(v, brief.get("g2_submitted_fingerprint"), stored, ev)
    if stored is None:
        return v
    if stored["assets"]:
        _check_assets(v, stored["assets"], canonical_bid, approved, "approved", provenance=True)
    if _artifact_set(published_arts) != _artifact_set(stored["assets"]):
        v.refuse("R12_REVISION_MISMATCH", "published artifacts %r differ from the approved set %r"
                 % (_artifact_set(published_arts), _artifact_set(stored["assets"])))
    if ev is None:
        return v
    fields = ev["context"]["fields"]
    prod = production_class(contract, approved_context.get("format"),
                            {"visual_direction": fields.get("Visual Direction"),
                             "canva_instructions": fields.get("Canva Instructions")})
    if prod is None:
        v.refuse("R23_UNKNOWN_OPTION", "format %r is unknown; cannot tell which artifact was approved" % approved_context.get("format"))
    elif prod == "design" and not stored["assets"]:
        v.refuse("R11_APPROVAL_MISSING", "G2 approved no finished artifact for this design brief")
    elif prod == "text_only" and (published_arts or stored["assets"]):
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
    commands = {"readiness": ("READINESS (design path: G1, before Ready for Design)", validate_design_readiness),
                "submission": ("G2 SUBMISSION (either path: G1, claim review, final copy or finished artifact)",
                               validate_g2_submission)}
    if argv[:1] and argv[0] in commands and len(argv) == 2:
        label, check = commands[argv[0]]
        try:
            # utf-8-sig: Windows PowerShell 5.1 writes a BOM; a snapshot written there must still load.
            with open(argv[1], encoding="utf-8-sig") as fh:
                ctx = json.load(fh)
        except (OSError, ValueError) as exc:
            print("%s: NOT RUN - snapshot unreadable (%s). Not a pass." % (argv[0].upper(), exc))
            return 2
        if not isinstance(ctx, dict):
            print("%s: NOT RUN - snapshot is not a JSON object. Not a pass." % argv[0].upper())
            return 2
        return _print_verdict(label, check(ctx, contract))
    if argv:
        print("usage: content_write_gate.py [readiness|submission SNAPSHOT.json]")
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
