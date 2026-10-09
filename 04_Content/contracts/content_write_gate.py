# -*- coding: utf-8 -*-
"""
Content (04) write gate.

    python 04_Content/contracts/content_write_gate.py
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

2. WRITE-PROPOSAL REFUSALS. validate_write(), validate_publication(),
   validate_publish_route() and validate_schema_change() return a Verdict.
   A skill runs them, or reasons through the same rules, BEFORE any apply.
   The rules are the refusal list in CONTENT_WRITE_CONTRACT.md s5.

Why it exists: Sector's contract says plainly that "this contract is not
enforced by a validator". Content's write layer is new, so it starts with one.
It still validates proposals, not Notion itself: the apply step remains a
human-invoked session, and read-after-write verification remains a step the
skill performs.
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

LINKEDIN_SURFACES = {"LinkedIn - Founder profile", "LinkedIn - Company Page"}
UNASSIGNED = "Not yet assigned"
FIRST_PERSON = re.compile(r"\b(I|I'm|I've|I'd|I'll|me|my|mine|myself)\b")
QUOTABLE_OFFER_STATUS = {"Active"}


class Verdict:
    """ok is True only when no refusal was raised. Refusals are records, not silence."""

    def __init__(self):
        self.refusals = []

    def refuse(self, code, detail):
        self.refusals.append({"code": code, "detail": detail})

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
    return errors


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


def _check_surface(v, proposal):
    db, links, fields = proposal["db"], proposal.get("links", {}), proposal.get("fields", {})
    if db == "DB6":
        platform = links.get("platform")
        surface = fields.get("Surface")
        if platform == "LinkedIn" and surface and surface not in LINKEDIN_SURFACES | {UNASSIGNED}:
            v.refuse("R09_SURFACE", "LinkedIn translation cannot use surface %r" % surface)
        if proposal.get("mode") == "CREATE" and not surface:
            v.refuse("R09_SURFACE", "translation CREATE must declare a Surface (use Not yet assigned)")
    if db == "DB7":
        tr = links.get("translation") or {}
        surface = tr.get("surface")
        if proposal.get("recommend_ready_for_design"):
            if tr.get("platform") == "LinkedIn" and surface in (None, UNASSIGNED):
                v.refuse("R09_SURFACE", "a LinkedIn brief cannot be recommended Ready for Design without a surface")
            if (links.get("opportunity") or {}).get("strategic_dragon") not in DRAGON_DONE:
                v.refuse("R08_DRAGON_ORDER", "Strategic pass not run; brief cannot be recommended ready")
            if tr.get("editorial_dragon") not in DRAGON_DONE:
                v.refuse("R08_DRAGON_ORDER", "Editorial pass not run; brief cannot be recommended ready")
        if surface == "LinkedIn - Company Page":
            for name in ("Caption", "Script"):
                text = fields.get(name) or ""
                hit = FIRST_PERSON.search(text)
                if hit:
                    v.refuse("R15_PAGE_VOICE",
                             "Company Page copy in %s uses first person (%r); the Page speaks institutionally" % (name, hit.group(0)))


def _check_duplicate(v, proposal, contract, state):
    if proposal.get("mode") != "CREATE":
        return
    db = next(d for d in contract["databases"] if d["db_id"] == proposal["db"])
    key_fields = db.get("natural_key", [])
    values = dict(proposal.get("key_values", {}))
    for k in key_fields:
        if k not in values and k in proposal.get("fields", {}):
            values[k] = proposal["fields"][k]
    if not key_fields or any(values.get(k) in (None, "") for k in key_fields):
        v.refuse("R10_NO_NATURAL_KEY", "CREATE on %s must supply its natural key %s" % (db["db_id"], key_fields))
        return
    for rec in (state or {}).get("existing", {}).get(db["db_id"], []):
        if all(rec.get(k) == values.get(k) for k in key_fields):
            v.refuse("R10_DUPLICATE",
                     "%s already holds %s; use UPDATE, VERSION or SUPERSEDE" %
                     (db["db_id"], {k: values[k] for k in key_fields}))
            return


def validate_write(proposal, contract=None, state=None):
    contract = contract or load_contract()
    v = Verdict()
    idx = field_index(contract)
    if proposal.get("db") not in idx:
        v.refuse("R00_UNKNOWN_DB", "unknown database %r" % proposal.get("db"))
        return v
    if proposal.get("mode") not in ("CREATE", "UPDATE", "VERSION", "SUPERSEDE"):
        v.refuse("R00_MODE", "mode must be explicit: CREATE / UPDATE / VERSION / SUPERSEDE")
    _check_writers(v, proposal, idx[proposal["db"]])
    _check_claims(v, proposal)
    _check_dragon(v, proposal)
    _check_upstream_and_family(v, proposal)
    _check_surface(v, proposal)
    _check_duplicate(v, proposal, contract, state)
    return v


# --------------------------------------------------------------------------- publication

def validate_publication(record, brief):
    """A manual publication record linking a live post back to the exact approved brief revision."""
    v = Verdict()
    if not _is_human(record.get("publisher")):
        v.refuse("R11_APPROVAL_MISSING", "agents never publish; publisher must be a named human")
    if brief.get("g2_decision") != "Approved":
        v.refuse("R11_APPROVAL_MISSING", "G2 decision is %r, not Approved" % brief.get("g2_decision"))
    if not (brief.get("g2_reviewer") and brief.get("g2_decided_at")):
        v.refuse("R11_APPROVAL_MISSING", "G2 approval has no reviewer or date on record")
    if brief.get("g2_approved_revision") != brief.get("version"):
        v.refuse("R12_REVISION_MISMATCH", "approval is for revision %r, brief is at %r" %
                 (brief.get("g2_approved_revision"), brief.get("version")))
    if record.get("revision") != brief.get("g2_approved_revision"):
        v.refuse("R12_REVISION_MISMATCH", "published revision %r was not the approved one" % record.get("revision"))
    for k in ("brief_id", "surface", "native_post_url", "published_at"):
        if not record.get(k):
            v.refuse("R14_LINKBACK", "publication record has no %s" % k)
    if record.get("brief_id") and record.get("brief_id") != brief.get("id"):
        v.refuse("R14_LINKBACK", "record points at a different brief")
    if record.get("surface") and record.get("surface") != brief.get("surface"):
        v.refuse("R14_LINKBACK", "published surface %r differs from the approved surface %r" %
                 (record.get("surface"), brief.get("surface")))
    url = record.get("native_post_url") or ""
    if url and record.get("surface") in LINKEDIN_SURFACES:
        host = urlparse(url).netloc.lower()
        if not (host == "linkedin.com" or host.endswith(".linkedin.com")) or urlparse(url).scheme != "https":
            v.refuse("R14_LINKBACK", "native post URL %r is not an https linkedin.com URL" % url)
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


def main():
    contract = load_contract()
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
