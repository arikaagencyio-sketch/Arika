"""Validate public account evidence and prepare an ID-only prospecting queue.

Real names, public contact routes, and messages stay outside every Git checkout.
This tool makes no model/API calls and never sends or marks a message sent.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

LEVELS = {"group", "property", "outlet", "shared_service"}


def outside_git(path):
    resolved = Path(path).resolve()
    if any((parent / ".git").exists() for parent in [resolved, *resolved.parents]):
        raise ValueError("Public identity/queue artifacts must be outside every Git checkout")
    return resolved


def validate(batch, today):
    if batch.get("classification") != "PUBLIC_COMPANY_RESEARCH":
        raise ValueError("Only public-company research is supported")
    sources = {}
    for source in batch["sources"]:
        if source["id"] in sources:
            raise ValueError("Duplicate source ID")
        observed = dt.date.fromisoformat(source["observed_on"])
        review = dt.date.fromisoformat(source["review_on"])
        if observed > today or review < today or review < observed:
            raise ValueError("Source outside its review window")
        if not source["url"].startswith("https://") or not source.get("observation"):
            raise ValueError("Source must carry its URL and exact public observation")
        sources[source["id"]] = source
    companies = {}
    for company in batch["companies"]:
        company_id = company["company_id"]
        if not company_id.startswith("ORG-") or company_id in companies:
            raise ValueError("Company IDs must be distinct ORG identities")
        if company["entity_level"] not in LEVELS:
            raise ValueError("Unknown organization level")
        if not company.get("source_ids") or any(s not in sources for s in company["source_ids"]):
            raise ValueError("Every company level needs registered public sources")
        companies[company_id] = company
    for company in companies.values():
        cursor, seen = company, set()
        while cursor.get("parent_company_id"):
            if cursor["company_id"] in seen:
                raise ValueError("Organization tree contains a cycle")
            seen.add(cursor["company_id"])
            parent = cursor["parent_company_id"]
            if parent not in companies:
                raise ValueError("Unknown parent company")
            cursor = companies[parent]
        if cursor["company_id"] != company["root_company_id"]:
            raise ValueError("Root does not match the organization tree")
    routes = set()
    account_ids = set()
    for account in batch["accounts"]:
        target = account["target_company_level_id"]
        if target not in companies or target in account_ids:
            raise ValueError("Unknown or duplicate account target")
        account_ids.add(target)
        route = account.get("contact_route", {})
        if route.get("kind") not in {"published_role_inbox", "published_company_phone"}:
            raise ValueError("Named/private contact data is outside this cycle")
        if route.get("source_id") not in sources:
            raise ValueError("Contact route needs its official source")
        if route["value"].casefold() in routes:
            raise ValueError("Duplicate contact route: keep one coordinated first touch")
        routes.add(route["value"].casefold())
        if not account.get("buyer_roles") or not account.get("discovery_questions"):
            raise ValueError("Buyer level and discovery questions are required")
        if account.get("first_touch"):
            message = account["first_touch"]
            if not message.get("subject") or not message.get("body") or not message.get("observation_source_ids"):
                raise ValueError("Message needs a subject, body and its observation sources")
            if any(s not in sources for s in message["observation_source_ids"]):
                raise ValueError("Message references an unknown source")
            if not message.get("contains_price_or_performance_claim") is False:
                raise ValueError("Price/performance claims require the commercial review path")
            if not message.get("opt_out") or message["opt_out"] not in message["body"]:
                raise ValueError("First touch needs an explicit stop-contact instruction")
    return companies


def qualify(company, companies):
    if company.get("country") != "Kenya":
        return "out_of_geography", "none"
    if not company.get("website_url") or not company.get("booking_url"):
        return "needs_evidence", "needs_routing"
    level = company["entity_level"]
    if level == "group":
        children = [c for c in companies.values() if c.get("parent_company_id") == company["company_id"]]
        return (("qualified_for_discovery", "hospitality_group_discovery") if children
                else ("needs_child_structure", "needs_routing"))
    if level in {"outlet", "shared_service"}:
        return "qualified_for_discovery", "hospitality_outlet_discovery"
    return "qualified_for_discovery", "hospitality_property_discovery"


def prepare(batch, destination, today):
    companies = validate(batch, today)
    destination = outside_git(destination)
    destination.mkdir(parents=True, exist_ok=True)
    queue_path = destination / "queue.json"
    content_hash = hashlib.sha256(json.dumps(batch, sort_keys=True).encode()).hexdigest()
    if queue_path.exists():
        existing = json.loads(queue_path.read_text(encoding="utf-8"))
        if existing["batch_sha256"] != content_hash:
            raise ValueError("Batch changed: use a new cycle folder; preserve prior touch history")
        return existing
    queue = {"cycle_id": batch["cycle_id"], "classification": batch["classification"],
             "prepared_on": today.isoformat(), "batch_sha256": content_hash,
             "crm_delivery": "not_verified", "sent_count": 0, "accounts": []}
    for account in batch["accounts"]:
        company = companies[account["target_company_level_id"]]
        fit, offer_route = qualify(company, companies)
        rooms = company.get("published_room_count")
        mvp = (company["entity_level"] == "property" and isinstance(rooms, int)
               and 30 <= rooms <= 120)
        queue["accounts"].append({**account, "fit": fit, "offer_route": offer_route,
                                  "mvp_size_fit_only": mvp, "commercial_status": "unpriced_discovery_only",
                                  "touch_state": "awaiting_sender_and_review" if account.get("first_touch") else "research_only",
                                  "followups": [], "crm_task_id": None,
                                  "unknowns": ["buyer authority", "budget", "direct booking share", "delivery scope"]})
    queue_path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    lines = ["# Public Prospecting Queue", "", f"Cycle: {queue['cycle_id']}",
             "", "| Account ID | Fit | Route | Touch state |", "|---|---|---|---|"]
    lines += [f"| {a['target_company_level_id']} | {a['fit']} | {a['offer_route']} | {a['touch_state']} |" for a in queue["accounts"]]
    lines += ["", "No touch is recorded as sent. Follow-up dates start from a verified actual send, not preparation.",
              "CRM rows remain unverified until written and read back in ClickUp."]
    (destination / "queue-status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return queue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--date", default=dt.datetime.now(dt.timezone(dt.timedelta(hours=3))).date().isoformat())
    args = parser.parse_args()
    batch_path = outside_git(args.batch)
    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    queue = prepare(batch, args.out, dt.date.fromisoformat(args.date))
    print(json.dumps({"cycle_id": queue["cycle_id"], "accounts_researched": len(queue["accounts"]),
                      "messages_prepared": sum(bool(a.get("first_touch")) for a in queue["accounts"]),
                      "sent": queue["sent_count"], "crm_delivery": queue["crm_delivery"]}))


if __name__ == "__main__":
    main()
