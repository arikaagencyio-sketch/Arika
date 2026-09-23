# -*- coding: utf-8 -*-
"""Create the CRM custom fields the repository already defines, by direct ClickUp REST call.

    python 00_Agency_Governance/crm_provisioning/provision_clickup_fields.py --validate
    python 00_Agency_Governance/crm_provisioning/provision_clickup_fields.py --check  --auth CRM-PROV-1
    python 00_Agency_Governance/crm_provisioning/provision_clickup_fields.py --apply  --auth CRM-PROV-1

WHY THIS EXISTS. The ClickUp MCP connector reads field definitions and sets values on existing
fields, but exposes no field-creation operation at all (verified 2026-09-22/23). The 2026-07-01
build created every custom field by direct REST call with an owner-supplied personal token. This
makes that path repeatable and governed rather than ad hoc.

WHAT IT WILL NOT DO, by construction:
  - It never renames, deletes, reorders or hides a field, and never writes a field VALUE.
  - It never reads a task, contact, member, comment or activity.
  - It only touches a target named in clickup-field-spec.json, and only after confirming the live
    list's name matches the spec.
  - It creates a field only when no field of that exact name already exists (idempotent).
  - It stops at the first failure and never retries. A failed create is reported, not repeated.
  - It refuses to apply without an `approved` authorisation, and spends that authorisation on use.

THE TOKEN is read from the CLICKUP_TOKEN environment variable. It is never read from this
repository, never printed, and never written to the audit record. Any accidental echo is redacted.

Risk Class 3 (Constitution section 5): hard to reverse, because ClickUp's API refuses custom-field
rename and delete under both token types. Owner sign-off is required per authorisation.
"""
import argparse, datetime, io, json, os, re, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SPEC = os.path.join(HERE, "clickup-field-spec.json")
AUTHS = os.path.join(HERE, "provisioning-authorisations.json")
AUDIT = os.path.join(HERE, "_audit")
API = "https://api.clickup.com/api/v2"
TOKEN_ENV = "CLICKUP_TOKEN"
LEGAL_TYPES = {"short_text", "text", "drop_down", "number", "email", "url", "date", "checkbox"}


def read_json(path):
    with io.open(path, encoding="utf-8") as fh:
        return json.load(fh)


def redact(s, token):
    return s.replace(token, "<CLICKUP_TOKEN redacted>") if token else s


def resolve_list_id(target):
    """The id lives in its recorded home, not in the spec - one source of truth."""
    src = target["list_id_from"]
    with io.open(os.path.join(ROOT, src["file"]), encoding="utf-8") as fh:
        m = re.search(src["pattern"], fh.read())
    if not m:
        raise SystemExit("STOP: could not resolve the list id from %s" % src["file"])
    return m.group(1)


def api(method, path, token, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode("utf-8") if body is not None else None)
    req.add_header("Authorization", token)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {"error": redact(e.read().decode("utf-8", "replace"), token)}
    except Exception as e:  # network/DNS/TLS - report, never retry
        return 0, {"error": redact(str(e), token)}


def load_auth(auth_id, needed):
    reg = read_json(AUTHS)
    a = next((x for x in reg["authorisations"] if x["id"] == auth_id), None)
    if a is None:
        raise SystemExit("STOP: no authorisation %r in the registry." % auth_id)
    if needed and a["status"] != "approved":
        raise SystemExit("STOP: authorisation %s is %r, not 'approved'. Nothing was created."
                         % (auth_id, a["status"]))
    return reg, a


def spend(reg, a, note):
    a["status"], a["spent"] = "spent", note
    with io.open(AUTHS, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(reg, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def validate(spec, auth_id):
    """Offline: the spec, the registry and the recorded list id, with no network and no token."""
    ok = True
    reg, a = load_auth(auth_id, needed=False) if auth_id else (None, None)
    for t in spec["targets"]:
        lid = resolve_list_id(t)
        print("  ok  target %-10s resolves to a recorded list id (%d digits), expects name %r"
              % (t["ref"], len(lid), t["list_name_expected"]))
        for f in t["fields"]:
            bad = []
            if f["type"] not in LEGAL_TYPES:
                bad.append("unknown type %r" % f["type"])
            if f.get("required"):
                bad.append("required=True is not permitted; blank must stay legitimate")
            if f["type"] == "drop_down" and not f.get("type_config", {}).get("options"):
                bad.append("a dropdown with no options")
            if f["type"] != "drop_down" and f.get("type_config"):
                bad.append("type_config on a non-dropdown")
            print("  %s  %-12s %-10s %s" % ("ok " if not bad else "FAIL", f["name"], f["type"],
                                            "; ".join(bad) or "spec clean"))
            ok &= not bad
    if a:
        print("  --  authorisation %s: status %r, max_creates %d, fields %s"
              % (a["id"], a["status"], a["max_creates"], ", ".join(a["fields"])))
        named = {f["name"] for t in spec["targets"] if t["ref"] == a["target"] for f in t["fields"]}
        if set(a["fields"]) != named:
            print("  FAIL authorisation names %s; the spec target names %s" % (sorted(a["fields"]), sorted(named)))
            ok = False
    print("\nVALIDATE %s (offline; no token used, no call made)" % ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


def token_or_stop():
    tok = os.environ.get(TOKEN_ENV, "").strip()
    if not tok:
        raise SystemExit(
            "STOP: %s is not set in this environment, so nothing was attempted.\n"
            "      Set it where THIS process can see it, then re-run. The value is never printed,\n"
            "      never stored in the repository and never written to the audit record." % TOKEN_ENV)
    return tok


def live_fields(list_id, token):
    st, body = api("GET", "/list/%s/field" % list_id, token)
    if st != 200:
        raise SystemExit("STOP: could not read the list's fields (HTTP %s): %s" % (st, body.get("error")))
    return {f["name"]: f for f in body.get("fields", [])}


def confirm_target(t, list_id, token):
    st, body = api("GET", "/list/%s" % list_id, token)
    if st != 200:
        raise SystemExit("STOP: could not read the target list (HTTP %s): %s" % (st, body.get("error")))
    if body.get("name") != t["list_name_expected"]:
        raise SystemExit("STOP: the recorded id resolves to a list named %r, but the spec expects %r. "
                         "Nothing was created." % (body.get("name"), t["list_name_expected"]))
    print("  ok  target list confirmed by name (%r), space %r" % (body.get("name"), body.get("space", {}).get("name")))


def run(spec, auth_id, apply_it):
    tok = token_or_stop()
    reg, a = load_auth(auth_id, needed=apply_it)
    t = next(x for x in spec["targets"] if x["ref"] == a["target"])
    list_id = resolve_list_id(t)
    confirm_target(t, list_id, tok)
    existing = live_fields(list_id, tok)
    print("  --  the list currently carries %d custom field(s)" % len(existing))

    wanted = [f for f in t["fields"] if f["name"] in a["fields"]]
    missing = [f for f in wanted if f["name"] not in existing]
    for f in wanted:
        print("  %-12s %s" % (f["name"], "already present - skip" if f["name"] in existing else "MISSING"))
    if not apply_it:
        print("\nCHECK complete: %d missing. Nothing was created (--check is read-only)." % len(missing))
        return 0
    if len(missing) > a["max_creates"]:
        raise SystemExit("STOP: %d creates needed, over %s's limit of %d."
                         % (len(missing), a["id"], a["max_creates"]))

    created, failed = [], None
    try:
        for f in missing:
            body = {"name": f["name"], "type": f["type"]}
            if f.get("type_config"):
                body["type_config"] = f["type_config"]
            st, resp = api("POST", "/list/%s/field" % list_id, tok, body)
            if st not in (200, 201):
                failed = {"field": f["name"], "http": st, "error": resp.get("error")}
                print("  FAIL create %s -> HTTP %s: %s" % (f["name"], st, resp.get("error")))
                break  # first failure stops the run; no retry
            created.append(f["name"])
            print("  ok  created %s (%s)" % (f["name"], f["type"]))
    finally:
        after = {}
        try:
            after = live_fields(list_id, tok)
        except SystemExit as e:
            print("  WARN could not re-read fields after the run: %s" % e)
        verified = {n: (after[n]["type"],
                        [o["name"] for o in after[n].get("type_config", {}).get("options", [])])
                    for n in a["fields"] if n in after}
        os.makedirs(AUDIT, exist_ok=True)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
        record = {"authorisation": a["id"], "target": a["target"], "list_name": t["list_name_expected"],
                  "utc": stamp, "created": created, "skipped_already_present":
                      [f["name"] for f in wanted if f["name"] in existing],
                  "failed": failed, "verified_after": verified,
                  "limitation": "Field existence only. No value was written and no hand-off was "
                                "delivered; the CRM route stays HANDOFF_FAILURE until a round-trip "
                                "test passes."}
        path = os.path.join(AUDIT, "%s-%s.json" % (stamp, a["id"]))
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(record, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        spend(reg, a, "%s - created %s%s" % (stamp, created or "nothing",
                                             "; FAILED on %s" % failed["field"] if failed else ""))
        print("  --  audit record written; %s is now spent" % a["id"])
    return 1 if failed else 0


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--validate", action="store_true", help="offline: check the spec and registry, no token, no call")
    g.add_argument("--check", action="store_true", help="read-only: report which fields are missing")
    g.add_argument("--apply", action="store_true", help="create the missing fields under an approved authorisation")
    p.add_argument("--auth", help="authorisation id, e.g. CRM-PROV-1")
    args = p.parse_args()
    spec = read_json(SPEC)
    if args.validate:
        return validate(spec, args.auth)
    if not args.auth:
        raise SystemExit("STOP: --auth is required for --check and --apply.")
    return run(spec, args.auth, apply_it=args.apply)


if __name__ == "__main__":
    sys.exit(main())
