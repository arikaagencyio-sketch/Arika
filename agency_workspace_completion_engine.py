from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path.cwd()
RUN_DATE = "2026-06-03"
BASELINE_DIR = ROOT / "Agency_Master_Intelligence_Extraction_2026-05-28"
BASELINE_REGISTER = BASELINE_DIR / "Agency_Document_Intelligence_Register.csv"
CENTRAL_DIR = ROOT / "00_Agency_Workspace_Intelligence"


WORKSPACES = {
    "The Agency Drafts Root": {
        "domain": "Agency",
        "slug": "AGENCY",
        "folder": "",
        "owner": "Agency Operating Council / Founder",
        "intent": "Own the full agency operating constitution, source-of-truth model, cross-domain governance, dependency map, executive cadence, and completion doctrine.",
        "role": "Master workspace operating system and enterprise control layer.",
        "upstream": "All domain workspaces, market reality, client outcomes, financial controls",
        "downstream": "All domain operating systems, governance, orchestration, dashboards, memory, automation",
        "critical_outputs": "Agency constitution, global source registry, RACI, KPI dictionary, CRM schema, dashboard spine, risk register, roadmap, version log",
    },
    "Sales Drafts": {
        "domain": "Sales",
        "slug": "SALES",
        "folder": "Sales Drafts",
        "owner": "Sales OS Owner / Revenue Conversion Lead",
        "intent": "Turn qualified demand, offer context, buyer psychology, and CRM intelligence into governed revenue conversion and downstream client handoff.",
        "role": "Revenue conversion, pipeline intelligence, objection learning, forecast signal, and client promise handoff.",
        "upstream": "Sector, Offer, Marketing, Branding, ClientPartner Acquisition, Legal",
        "downstream": "Client, Finance, Management, Offer refinement, delivery promise memory",
        "critical_outputs": "Sales source registry, CRM stage rules, discovery protocol, objection memory, proposal governance, handoff packet, win/loss log",
    },
    "Marketing Drafts": {
        "domain": "Marketing",
        "slug": "MARKETING",
        "folder": "Marketing Drafts",
        "owner": "Marketing OS Owner / Demand Generation Lead",
        "intent": "Translate sector, offer, brand, and audience intelligence into demand generation, channel execution, attribution, lifecycle growth, and sales-ready context.",
        "role": "Demand system, content/funnel/channel architecture, attribution intelligence, and sales enablement layer.",
        "upstream": "Sector, Offer, Branding, Finance, Management",
        "downstream": "Sales, ClientPartner Acquisition, CRM, Revenue forecasting, Brand feedback",
        "critical_outputs": "Campaign registry, content doctrine, attribution schema, funnel workflow, agent cards, channel governance, experiment memory",
    },
    "The Sector Drafts": {
        "domain": "Sector",
        "slug": "SECTOR",
        "folder": "The Sector Drafts",
        "owner": "Sector Intelligence Owner / Market Strategy Lead",
        "intent": "Define market arenas, sector constraints, language systems, audience maps, risk patterns, opportunity theses, and sector-specific execution intelligence.",
        "role": "Upstream market intelligence and context separation layer.",
        "upstream": "Market data, client context, competitive research, management priorities",
        "downstream": "Offer, Marketing, Sales, Client, Branding, Automation",
        "critical_outputs": "Sector registry, ontology, research protocol, signal confidence model, opportunity map, sector handoff packet",
    },
    "The ClientPartner Draft": {
        "domain": "ClientPartner Acquisition",
        "slug": "CLIENTPARTNER",
        "folder": "The ClientPartner Draft",
        "owner": "ClientPartner Acquisition Owner / Partnership Growth Lead",
        "intent": "Convert partner, relationship, referral, and acquisition channel intelligence into governed pipeline leverage and CRM-backed relationship systems.",
        "role": "Partnership, acquisition channel, relationship CRM, and distribution leverage layer.",
        "upstream": "Sector, Offer, Branding, Marketing, Sales",
        "downstream": "Sales, Partnerships, Distribution, Revenue channels, Client acquisition memory",
        "critical_outputs": "Partner registry, acquisition channel map, CRM protocol, partnership governance, referral memory, relationship health dashboard",
    },
    "Offer Drafts": {
        "domain": "Offer",
        "slug": "OFFER",
        "folder": "Offer Drafts",
        "owner": "Offer OS Owner / Value Architecture Lead",
        "intent": "Convert sector truth, client pain, delivery capability, brand promise, sales feedback, and financial constraints into priced, packaged, validated offers.",
        "role": "Value architecture, pricing, packaging, promise control, risk reduction, and revenue model layer.",
        "upstream": "Sector, Client, Finance, Sales, Branding, Management",
        "downstream": "Marketing, Sales, Client Delivery, Finance, ClientPartner Acquisition",
        "critical_outputs": "Offer registry, value stack, pricing model, proof registry, promise governance, delivery feasibility gate, offer-market fit score",
    },
    "Branding Drafts": {
        "domain": "Branding",
        "slug": "BRANDING",
        "folder": "Branding Drafts",
        "owner": "Brand OS Owner / Trust and Narrative Lead",
        "intent": "Turn identity, sector codes, audience psychology, trust signals, narrative, and visual systems into a governable brand intelligence operating system.",
        "role": "Trust architecture, narrative system, identity logic, brand memory, presentation/retrieval layer.",
        "upstream": "Sector, Client, Offer, Culture, Management",
        "downstream": "Marketing, Sales, Client experience, Authority building, Agency positioning",
        "critical_outputs": "Brand ontology, scoring system, brand context schema, validation gates, governance system, retrieval rules, monitoring",
    },
    "Financial Drafts": {
        "domain": "Finance",
        "slug": "FINANCE",
        "folder": "Financial Drafts",
        "owner": "Finance OS Owner / Financial Control Lead",
        "intent": "Turn revenue, cost, delivery, tax, runway, allocation, and risk intelligence into governed financial control and agency survivability.",
        "role": "Cash, profitability, risk, ledger, allocation, reporting, and financial observability layer.",
        "upstream": "Sales revenue, Client delivery economics, Operations spend, Legal/tax, Management priorities",
        "downstream": "Management decisions, Offer pricing, Operations capacity, Hiring, Risk controls",
        "critical_outputs": "FinOS architecture, revenue event contracts, cash controls, dashboard thresholds, security policy, observability, automation catalog",
    },
    "Legal Drafts": {
        "domain": "Legal",
        "slug": "LEGAL",
        "folder": "Legal Drafts",
        "owner": "Legal OS Owner / Governance and Risk Control Lead",
        "intent": "Convert claims, contracts, privacy concerns, payment terms, compliance duties, IP boundaries, partner terms, and risk decisions into governed legal controls for every agency domain.",
        "role": "Enterprise legal governance, contract control, compliance, claims approval, privacy, payment terms, IP protection, and risk acceptance layer.",
        "upstream": "Management intent, Sales terms, Client obligations, Finance compliance, Offer promises, Marketing and Branding claims, Partner channels",
        "downstream": "Sales, Client, Finance, Offer, Marketing, Branding, ClientPartner Acquisition, Management, Operations, Automation",
        "critical_outputs": "Legal source registry, contract template pack, MSA/SOW/DPA clauses, claims approval policy, privacy controls, partner terms, risk register, approval gates, legal handoff packet",
    },
    "The Agency Client. Drafts": {
        "domain": "Client",
        "slug": "CLIENT",
        "folder": "The Agency Client. Drafts",
        "owner": "Client OS Owner / Client Success Lead",
        "intent": "Transform sales promises, client context, onboarding, success criteria, delivery state, retention signals, and expansion opportunities into governed client value realization.",
        "role": "Client lifecycle, onboarding, delivery handoff, health, retention, expansion, and proof capture layer.",
        "upstream": "Sales, Offer, Legal, Finance, Branding, Operations",
        "downstream": "Operations, Finance, Management, Retention, Expansion, Referrals, Case studies",
        "critical_outputs": "Client registry, onboarding control pack, success criteria, SLA model, health score, expansion/referral triggers, client memory",
    },
    "The Agency Draft 1.2": {
        "domain": "Management",
        "slug": "MANAGEMENT",
        "folder": "The Agency Draft 1.2",
        "owner": "Management OS Owner / Agency Strategy Lead",
        "intent": "Hold the agency vision, 360 dependency map, operating model, cross-domain execution architecture, decision authority, and executive roadmap.",
        "role": "Agency management, strategic command, cross-domain dependency, resource allocation, and operating model layer.",
        "upstream": "All domain intelligence, finance, market reality, client outcomes, founder direction",
        "downstream": "All domains, governance, resource allocation, cadence, roadmap, risk management",
        "critical_outputs": "Agency constitution, dependency map, RACI, decision log, initiative portfolio, executive dashboard, change control",
    },
}


CONCERNS = {
    "Intent": ["mission", "vision", "objective", "intent", "purpose", "values", "why"],
    "Strategy": ["strategy", "strategic", "roadmap", "prioritization", "initiative", "growth", "positioning"],
    "Constitution": ["constitution", "charter", "amendment", "policy", "governing", "operating principles"],
    "Governance": ["governance", "approval", "risk", "escalation", "policy", "legal", "compliance", "decision rights"],
    "Orchestration": ["orchestration", "routing", "handoff", "coordination", "dependency", "trigger", "command"],
    "Workspace Intelligence": ["workspace", "source", "registry", "index", "inventory", "knowledge graph", "document"],
    "Separation Intelligence": ["separation", "domain", "layer", "boundary", "handoff", "authoritative source"],
    "Domain Intelligence": ["ontology", "domain", "actor", "capability", "constraint", "knowledge", "intelligence"],
    "Registries": ["registry", "catalog", "index", "matrix", "source id", "source", "master"],
    "Architecture": ["architecture", "architure", "blueprint", "framework", "system map", "operating system"],
    "State Management": ["state", "status", "health", "lifecycle", "stage", "current", "dashboard"],
    "Execution": ["execution", "runbook", "action plan", "daily", "playbook", "implementation"],
    "Workflows": ["workflow", "process", "cadence", "sop", "pipeline", "cycle"],
    "Agents": ["agent", "agentic", "role card", "runtime", "ai operations"],
    "Tools": ["tool", "connector", "api", "mcp", "plugin", "integration"],
    "Schemas": ["schema", "data contract", "object", "template", "field"],
    "Events": ["event", "trigger", "log", "stream", "runtime"],
    "Artifacts": ["artifact", "template", "packet", "playbook", "document", "asset"],
    "Ownership": ["owner", "raci", "responsible", "accountable", "role", "operator"],
    "Validation": ["validation", "qa", "quality", "gate", "checklist", "score"],
    "Observability": ["observability", "monitoring", "dashboard", "metric", "kpi", "alert", "tracking"],
    "Information Storage": ["storage", "persistence", "database", "archive", "repository", "source", "record", "registry"],
    "Historical Memory": ["history", "historical", "archive", "past", "timeline"],
    "Operational Memory": ["operational memory", "memory log", "learning loop", "cadence", "operations log"],
    "Decision Memory": ["decision log", "decision", "approval", "assumption", "why"],
    "Execution Memory": ["execution log", "runtime example", "run", "incident", "delivery log"],
    "Learning Systems": ["learning", "retrospective", "lesson", "feedback", "optimization"],
    "Enterprise Controls": ["control", "risk", "audit", "security", "compliance", "approval"],
    "Automation": ["automation", "agent", "ai", "trigger", "runtime", "workflow automation"],
    "Security": ["security", "access", "privacy", "permission", "secret", "credential"],
    "Resources": ["resource", "capacity", "hiring", "budget", "team", "allocation"],
    "Knowledge": ["knowledge", "graph", "retrieval", "rag", "memory", "taxonomy"],
    "Change Management": ["change", "amendment", "migration", "release", "revision"],
    "Versioning": ["version", "draft", "release", "changelog", "active", "superseded"],
    "Recovery": ["recovery", "fallback", "rollback", "incident", "manual fallback"],
    "Strategic Planning": ["plan", "roadmap", "initiative", "quarterly", "annual", "prioritization"],
    "Evolution": ["evolution", "improvement", "learning", "iteration", "optimization", "upgrade"],
    "Completion": ["completion", "done", "closure", "acceptance", "gate", "criteria"],
}


CRITICAL_CONCERNS = {
    "Intent",
    "Strategy",
    "Constitution",
    "Governance",
    "Orchestration",
    "Workspace Intelligence",
    "Registries",
    "Ownership",
    "Validation",
    "Observability",
    "Completion",
}

HIGH_CONCERNS = {
    "Separation Intelligence",
    "Domain Intelligence",
    "Architecture",
    "State Management",
    "Execution",
    "Workflows",
    "Decision Memory",
    "Enterprise Controls",
    "Automation",
    "Change Management",
    "Versioning",
    "Evolution",
}


ARTIFACT_PLANS = {
    "Intent": "00_Foundation/{slug}_MISSION_VISION_OBJECTIVES.md",
    "Strategy": "00_Foundation/{slug}_STRATEGIC_ROADMAP.md",
    "Constitution": "00_Governance/{slug}_OPERATING_CONSTITUTION.md",
    "Governance": "00_Governance/{slug}_GOVERNANCE_CHARTER_AND_RACI.md",
    "Orchestration": "01_Orchestration/{slug}_ORCHESTRATION_ENGINE.md",
    "Workspace Intelligence": "00_Workspace_Intelligence_Inventory/{slug}_SOURCE_INTELLIGENCE_REGISTER.md",
    "Separation Intelligence": "00_Workspace_Intelligence_Inventory/{slug}_SEPARATION_DELIVERY_MAP.md",
    "Domain Intelligence": "02_Domain_Intelligence/{slug}_ONTOLOGY_AND_DOMAIN_REGISTRY.md",
    "Registries": "03_Registries/{slug}_MASTER_REGISTRY.md",
    "Architecture": "01_Architecture/{slug}_OPERATING_ARCHITECTURE.md",
    "State Management": "04_State/{slug}_STATE_MODEL_AND_STATUS_BOARD.md",
    "Execution": "05_Execution/{slug}_EXECUTION_PLAYBOOK.md",
    "Workflows": "05_Execution/{slug}_WORKFLOW_CATALOG.md",
    "Agents": "06_Automation/{slug}_AGENT_REGISTRY.md",
    "Tools": "06_Automation/{slug}_TOOL_AND_CONNECTOR_REGISTRY.md",
    "Schemas": "07_Schemas/{slug}_DATA_CONTRACTS_AND_SCHEMAS.md",
    "Events": "07_Schemas/{slug}_EVENT_CATALOG.md",
    "Artifacts": "08_Artifacts/{slug}_ARTIFACT_CATALOG.md",
    "Ownership": "00_Governance/{slug}_OWNERSHIP_RACI.md",
    "Validation": "09_Validation/{slug}_VALIDATION_GATES.md",
    "Observability": "10_Observability/{slug}_OBSERVABILITY_DASHBOARD_SPEC.md",
    "Information Storage": "10_Observability/{slug}_INFORMATION_STORAGE_AND_PERSISTENCE_MAP.md",
    "Historical Memory": "11_Memory/{slug}_HISTORICAL_MEMORY_LOG.md",
    "Operational Memory": "11_Memory/{slug}_OPERATIONAL_MEMORY_LOG.md",
    "Decision Memory": "11_Memory/{slug}_DECISION_LOG.md",
    "Execution Memory": "11_Memory/{slug}_EXECUTION_LOG.md",
    "Learning Systems": "12_Learning/{slug}_LEARNING_LOOP_PROTOCOL.md",
    "Enterprise Controls": "00_Governance/{slug}_ENTERPRISE_CONTROLS.md",
    "Automation": "06_Automation/{slug}_AUTOMATION_REGISTRY_AND_APPROVAL_MATRIX.md",
    "Security": "00_Governance/{slug}_SECURITY_AND_ACCESS_POLICY.md",
    "Resources": "13_Resources/{slug}_RESOURCE_AND_CAPACITY_MODEL.md",
    "Knowledge": "14_Knowledge/{slug}_KNOWLEDGE_GRAPH_INDEX.md",
    "Change Management": "15_Change/{slug}_CHANGE_CONTROL_PROTOCOL.md",
    "Versioning": "15_Change/{slug}_VERSIONING_AND_RELEASE_LOG.md",
    "Recovery": "16_Recovery/{slug}_RECOVERY_AND_FALLBACK_PLAN.md",
    "Strategic Planning": "00_Foundation/{slug}_INITIATIVE_PORTFOLIO.md",
    "Evolution": "17_Evolution/{slug}_EVOLUTION_ROADMAP.md",
    "Completion": "18_Completion/{slug}_COMPLETION_CRITERIA.md",
}


def md_escape(value: object) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def table(headers: list[str], rows: list[list[object]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(md_escape(cell) for cell in row) + " |")
    return "\n".join(out)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def read_register() -> list[dict[str, str]]:
    if not BASELINE_REGISTER.exists():
        raise FileNotFoundError(f"Baseline register not found: {BASELINE_REGISTER}")
    with BASELINE_REGISTER.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def workspace_from_path(relative_path: str) -> str:
    return relative_path.replace("/", "\\").split("\\")[0]


def text_blob(row: dict[str, str]) -> str:
    keys = [
        "Document Name",
        "Relative Path",
        "Purpose",
        "Strategic Function",
        "Business Function",
        "Layer Assignment",
        "Dependencies",
        "Inputs",
        "Outputs",
        "Workflows Supported",
        "KPIs Influenced",
        "Headings / Signals",
        "Related Systems",
    ]
    return " ".join(row.get(key, "") for key in keys).lower()


def extension_weight(row: dict[str, str]) -> int:
    ext = row.get("Extension", "").lower()
    if ext in {".md", ".csv", ".json", ".jsonl", ".yaml", ".yml"}:
        return 3
    if ext in {".py", ".ts", ".mjs", ".sql", ".ps1"}:
        return 2
    if ext == ".docx":
        return 1
    return 1


def evidence_for(rows: list[dict[str, str]], concern: str) -> tuple[int, list[str], bool]:
    keywords = CONCERNS[concern]
    score = 0
    hits: list[str] = []
    has_authoritative = False
    for row in rows:
        blob = text_blob(row)
        matched = [word for word in keywords if word in blob]
        if not matched:
            continue
        score += extension_weight(row)
        rel = row.get("Relative Path", "")
        hits.append(rel)
        if row.get("Extension", "").lower() in {".md", ".csv", ".json", ".jsonl", ".yaml", ".yml"}:
            has_authoritative = True
    return score, hits[:6], has_authoritative


def root_status(concern: str) -> tuple[str, str]:
    present = {"Workspace Intelligence", "Architecture", "Domain Intelligence", "Knowledge", "Registries"}
    partial = {
        "Intent",
        "Strategy",
        "Governance",
        "Orchestration",
        "Separation Intelligence",
        "State Management",
        "Execution",
        "Workflows",
        "Artifacts",
        "Validation",
        "Observability",
        "Historical Memory",
        "Decision Memory",
        "Enterprise Controls",
        "Automation",
        "Strategic Planning",
        "Evolution",
        "Completion",
        "Change Management",
        "Versioning",
    }
    if concern in present:
        return "Present", "Baseline extraction pack provides central blueprint/register/relationship graph evidence."
    if concern in partial:
        return "Partially Present", "Baseline architecture exists, but the concern is not yet promoted into a governed agency-wide operating artifact with owner, cadence, and closure gate."
    return "Missing", "No authoritative agency-wide artifact was found for this concern in the root operating layer."


def concern_status(workspace: str, rows: list[dict[str, str]], concern: str) -> tuple[str, str]:
    if workspace in WORKSPACES:
        canonical_path = ROOT / required_artifact(WORKSPACES[workspace], concern)
        if canonical_path.exists():
            return "Present", str(canonical_path.relative_to(ROOT))
    if workspace == "The Agency Drafts Root":
        return root_status(concern)
    if not rows:
        return "Missing", "No source documents were found for this workspace folder in the current baseline register."
    score, hits, has_authoritative = evidence_for(rows, concern)
    if score >= 5 and has_authoritative:
        return "Present", "; ".join(hits)
    if score > 0:
        return "Partially Present", "; ".join(hits)
    return "Missing", "No direct source evidence detected for this concern."


def severity_for(status: str, concern: str, rows: list[dict[str, str]]) -> str:
    if status == "Present":
        return "None"
    if not rows and concern in CRITICAL_CONCERNS:
        return "Critical"
    if concern in CRITICAL_CONCERNS and status == "Missing":
        return "Critical"
    if concern in CRITICAL_CONCERNS:
        return "High"
    if concern in HIGH_CONCERNS and status == "Missing":
        return "High"
    if concern in HIGH_CONCERNS:
        return "Medium-High"
    if status == "Missing":
        return "Medium-High"
    return "Medium"


def required_artifact(config: dict[str, str], concern: str) -> str:
    template = ARTIFACT_PLANS[concern]
    rel = template.format(slug=config["slug"])
    folder = config["folder"]
    return str(Path(folder) / rel) if folder else str(Path("00_Agency_Workspace_Intelligence") / rel)


def root_cause(workspace: str, status: str, rows: list[dict[str, str]]) -> str:
    if workspace == "The Agency Drafts Root":
        if status == "Missing":
            return "The workspace has a powerful extraction pack, but no root-level canonical operating artifact yet owns this concern."
        return "The concern exists as central intelligence, but it is not fully converted into governed execution, ownership, cadence, and validation."
    if not rows:
        return "The named workspace is absent from the current folder map, so its knowledge cannot be discovered, governed, or learned from."
    md_count = sum(1 for row in rows if row.get("Extension", "").lower() == ".md")
    if md_count == 0:
        return "Domain knowledge exists mainly as DOCX drafts, so it lacks controlled markdown registries, protocols, owners, validation gates, and runtime memory."
    return "Conceptual or runtime evidence exists, but the concern is fragmented across drafts and has not been made a single authoritative source with lifecycle status."


def gap_impact(config: dict[str, str], concern: str) -> str:
    domain = config["domain"]
    return (
        f"{domain} operators cannot reliably answer who owns {concern.lower()}, what is current, "
        "what must happen next, which evidence is authoritative, or how completion is proven."
    )


def solution(config: dict[str, str], concern: str) -> str:
    return (
        f"Promote {concern.lower()} into the authoritative {config['domain']} OS layer with source IDs, owner, "
        "governance rule, dependency links, validation gate, dashboard signal, memory update, and version path."
    )


def protocol_for(config: dict[str, str], concern: str) -> str:
    domain = config["domain"]
    return (
        f"{domain} {concern} protocol: trigger -> source evidence -> owner review -> approval/risk check -> "
        "execution or handoff -> validation -> memory/version update."
    )


def completion_criteria(config: dict[str, str], concern: str) -> str:
    return (
        f"{config['domain']} {concern} is complete when the markdown exists at the recommended placement, "
        "has an owner and cadence, references source IDs, is registered in the local and agency registry, "
        "defines validation and observability, and has a version/evolution log entry."
    )


def sequence_for(concern: str) -> str:
    return (
        "1. Confirm source inventory; 2. create canonical markdown; 3. assign owner/RACI; "
        "4. register dependencies and handoffs; 5. define validation and dashboard signals; "
        "6. approve, version, and schedule evolution review."
    )


def build_gap_rows(workspace: str, rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    config = WORKSPACES[workspace]
    gap_rows: list[dict[str, str]] = []
    status_rows: list[dict[str, str]] = []
    for concern in CONCERNS:
        status, evidence = concern_status(workspace, rows, concern)
        severity = severity_for(status, concern, rows)
        artifact = required_artifact(config, concern)
        status_rows.append(
            {
                "Workspace": workspace,
                "Domain": config["domain"],
                "Concern": concern,
                "Status": status,
                "Severity": severity,
                "Evidence": evidence,
                "Recommended Addition": artifact,
                "Completion Criteria": completion_criteria(config, concern),
            }
        )
        if status == "Present":
            continue
        gap_rows.append(
            {
                "Gap ID": f"{config['slug']}-{concern.upper().replace(' ', '-')}",
                "Workspace": workspace,
                "Domain": config["domain"],
                "Gap Name": f"{config['domain']} {concern} Control Gap",
                "Gap Category": concern,
                "Gap Layer": config["role"],
                "Status": status,
                "Severity": severity,
                "Gap Impact": gap_impact(config, concern),
                "Root Cause": root_cause(workspace, status, rows),
                "Required Solution": solution(config, concern),
                "Required Markdowns": artifact,
                "Required Protocols": protocol_for(config, concern),
                "Required Registries": f"{config['slug']}_MASTER_REGISTRY plus Agency Global Source Registry.",
                "Required Governance": f"{config['owner']} approves ownership, risk class, cadence, and escalation route.",
                "Required Ownership": config["owner"],
                "Required Orchestration": f"Route through {config['domain']} orchestration and the agency dependency graph: upstream {config['upstream']}; downstream {config['downstream']}.",
                "Required Validation": "Entry criteria, source evidence check, owner sign-off, handoff acceptance, and completion gate.",
                "Required Observability": "Dashboard status, freshness date, owner review cadence, risk indicator, and gap closure metric.",
                "Required Evolution": "Decision log entry, version log entry, quarterly review, and source registry state update.",
                "Required Dependencies": f"Upstream: {config['upstream']}. Downstream: {config['downstream']}.",
                "Required Placement": artifact,
                "Required Sequencing": sequence_for(concern),
                "Completion Criteria": completion_criteria(config, concern),
            }
        )
    return gap_rows, status_rows


def artifact_register_rows(workspace: str, rows: list[dict[str, str]]) -> list[dict[str, object]]:
    config = WORKSPACES[workspace]
    output: list[dict[str, object]] = []
    for row in rows:
        output.append(
            {
                "Workspace": workspace,
                "Domain": config["domain"],
                "Document Name": row.get("Document Name", ""),
                "Relative Path": row.get("Relative Path", ""),
                "Extension": row.get("Extension", ""),
                "Word Count": row.get("Word Count", ""),
                "Layer Assignment": row.get("Layer Assignment", ""),
                "Purpose": row.get("Purpose", ""),
                "Strategic Function": row.get("Strategic Function", ""),
                "Automation Potential": row.get("Automation Potential", ""),
                "Risk Factors": row.get("Risk Factors", ""),
            }
        )
    return output


def summarize_workspace_rows(rows: list[dict[str, str]]) -> dict[str, object]:
    extensions = Counter(row.get("Extension", "").lower() for row in rows)
    words = sum(int(row.get("Word Count", "0") or 0) for row in rows if str(row.get("Word Count", "")).isdigit())
    layers = Counter(row.get("Layer Assignment", "") for row in rows)
    runtime = sum(extensions[ext] for ext in [".py", ".ts", ".mjs", ".sql", ".ps1", ".yaml", ".yml"])
    return {
        "Files": len(rows),
        "DOCX": extensions[".docx"],
        "Markdown": extensions[".md"],
        "CSV": extensions[".csv"],
        "JSON": extensions[".json"] + extensions[".jsonl"],
        "Runtime": runtime,
        "Words": words,
        "Top Layers": "; ".join(f"{name} ({count})" for name, count in layers.most_common(4) if name),
    }


def recommendation_rows(gaps: list[dict[str, str]]) -> list[dict[str, str]]:
    recs: list[dict[str, str]] = []
    seen: set[str] = set()
    for gap in gaps:
        artifact = gap["Required Markdowns"]
        if artifact in seen:
            continue
        seen.add(artifact)
        recs.append(
            {
                "Workspace": gap["Workspace"],
                "Domain": gap["Domain"],
                "Recommended Markdown": artifact,
                "Purpose": gap["Required Solution"],
                "Owner": gap["Required Ownership"],
                "Priority": gap["Severity"],
                "Dependencies": gap["Required Dependencies"],
                "Completion Criteria": gap["Completion Criteria"],
            }
        )
    return recs


def phase_plan(config: dict[str, str]) -> list[list[str]]:
    domain = config["domain"]
    return [
        [
            "Phase 1 - Source Truth and Ownership",
            f"Create/confirm {domain} source register, inventory all current artifacts, assign owner/RACI, and mark active/superseded/archive states.",
            "Existing source drafts and baseline extraction register.",
            "All documents have source IDs, owner, lifecycle status, and registry entry.",
        ],
        [
            "Phase 2 - Canonical Operating Layer",
            f"Promote core {domain} doctrine into canonical markdowns for intent, architecture, governance, orchestration, and execution.",
            "Phase 1 registry and source state.",
            "Canonical markdowns exist in recommended locations and replace scattered draft usage.",
        ],
        [
            "Phase 3 - Handoffs, Schemas, and Dashboards",
            f"Define {domain} handoff packets, data contracts, event triggers, KPIs, validation gates, and dashboard signals.",
            "Canonical operating layer and upstream/downstream dependency acceptance.",
            "Every workflow has trigger, input, output, owner, KPI, and acceptance gate.",
        ],
        [
            "Phase 4 - Automation and Memory",
            f"Register safe {domain} automations, agent roles, logs, operational memory, decision memory, and fallback paths.",
            "Governed workflows, schemas, and approval classes.",
            "Low-risk automation is observable, reversible, and memory-writing.",
        ],
        [
            "Phase 5 - Evolution and Completeness Proof",
            f"Run governance review, close remaining gaps, publish version log, and schedule recurring {domain} evolution cadence.",
            "Validation evidence, dashboards, memory logs, and owner sign-off.",
            "Completion criteria are met and the workspace can prove current operating readiness.",
        ],
    ]


def is_legal_reference(row: dict[str, str]) -> bool:
    name = row.get("Document Name", "").lower()
    layer = row.get("Layer Assignment", "").lower()
    return "legal" in name or "legal" in layer


def source_evidence_rows(rows: list[dict[str, str]]) -> list[list[object]]:
    evidence = []
    for row in rows[:12]:
        evidence.append(
            [
                row.get("Relative Path", ""),
                row.get("Layer Assignment", ""),
                row.get("Purpose", ""),
                row.get("Risk Factors", ""),
            ]
        )
    if evidence:
        return evidence
    return [
        [
            str(BASELINE_REGISTER.relative_to(ROOT)),
            "Agency baseline",
            "No local source documents were detected; this artifact is initialized from the agency operating model, layer dependency map, and workspace completion doctrine.",
            "High risk until domain owner validates and adds source evidence.",
        ]
    ]


def canonical_artifact_markdown(workspace: str, concern: str, rows: list[dict[str, str]]) -> str:
    config = WORKSPACES[workspace]
    artifact = required_artifact(config, concern)
    traceability_id = f"{config['slug']}-{concern.upper().replace(' ', '-')}-CANONICAL-001"
    source_rows = source_evidence_rows(rows)
    source_count = len(rows)
    return f"""
# {config['domain']} {concern} Canonical Operating Artifact

Generated: {RUN_DATE}

## Traceability

| Field | Value |
|---|---|
| Traceability ID | {traceability_id} |
| Workspace | {workspace} |
| Domain | {config['domain']} |
| Canonical Concern | {concern} |
| Canonical Placement | {artifact} |
| Source Baseline | {BASELINE_REGISTER.relative_to(ROOT)} |
| Source Evidence Rows | {source_count} |
| Owner | {config['owner']} |
| Lifecycle State | Active canonical foundation |

## Source Evidence

{table(['Source', 'Layer Assignment', 'Purpose', 'Risk Factors'], source_rows)}

## Workspace Intent

| Field | Specification |
|---|---|
| Domain Intent | {config['intent']} |
| Operating Role | {config['role']} |
| Upstream Dependencies | {config['upstream']} |
| Downstream Dependencies | {config['downstream']} |
| Critical Outputs | {config['critical_outputs']} |

## Operating Doctrine

This artifact makes {concern.lower()} governable for the {config['domain']} operating system. It exists so the agency can preserve domain separation, prove source lineage, control dependencies, validate execution, observe state, update memory, and evolve without losing operational truth.

The authoritative rule is simple: {config['domain']} {concern.lower()} is not considered operational until it has source evidence, an accountable owner, dependency links, validation criteria, observability signals, a memory update path, and a version history.

## Control Model

| Control | Rule |
|---|---|
| Source Authority | Every claim must map to a source ID, baseline source, or owner-approved new source record. |
| Ownership | {config['owner']} is accountable for approval, cadence, escalation, and retirement. |
| Dependency Enforcement | Upstream evidence must be accepted before downstream execution is released. |
| Validation | Entry criteria, source check, output check, handoff acceptance, and completion gate are required. |
| Observability | Dashboard state must show owner, freshness, risk class, status, blocker, next action, and review date. |
| Memory | Material decisions update decision memory; workflow activity updates operational and execution memory; lessons update learning memory. |
| Versioning | Any material change creates a dated version entry and active/superseded/archive state update. |
| Recovery | Failure triggers root-cause review, rollback or fallback path, owner sign-off, and learning-loop update. |

## Execution Protocol

1. Confirm the source evidence and current lifecycle state.
2. Check upstream dependencies: {config['upstream']}.
3. Apply the {config['domain']} rule set for {concern.lower()}.
4. Produce the downstream packet for: {config['downstream']}.
5. Validate the output against the gates below.
6. Register the result, update memory, and schedule the next review.

## Registry Requirements

| Registry Field | Required Value |
|---|---|
| Source ID | Stable ID for each source document or generated operating artifact. |
| Owner | Named accountable role and backup role. |
| Status | Active, draft, superseded, archived, blocked, or approved exception. |
| Dependencies | Upstream sources, downstream consumers, and required handoff packets. |
| Risk Class | Low, medium, high, critical, or legal/financial controlled. |
| Validation Evidence | Link or note proving source check, owner review, and output acceptance. |
| Observability Signal | Dashboard metric, review date, freshness date, and blocker state. |
| Memory Link | Decision, operational, execution, and learning log references. |
| Version | Current version, previous version, change reason, and next review date. |

## Handoff Contract

| Direction | Contract |
|---|---|
| Upstream Intake | Receive source evidence, assumptions, current state, owner, risk class, and required decision. |
| Local Transformation | Apply {config['domain']} {concern.lower()} rules, resolve conflicts, and record decisions. |
| Downstream Release | Send accepted output, validation evidence, unresolved risks, owner, and next action. |
| Rejection Path | If evidence, owner, validation, or risk approval is missing, return to upstream owner with blocker reason. |

## Validation Gates

| Gate | Pass Standard |
|---|---|
| Source Gate | Source evidence is present or the owner approves an explicit source gap with remediation date. |
| Ownership Gate | Accountable owner and review cadence are present. |
| Dependency Gate | Upstream and downstream dependencies are named and accepted. |
| Risk Gate | Legal, financial, client, brand, and operational risks are classified and escalated when required. |
| Output Gate | Artifact, workflow, schema, packet, or decision is usable by the downstream domain. |
| Memory Gate | Decision and execution notes are recorded before completion is claimed. |
| Completion Gate | The registry, dashboard, validation evidence, and version log all point to the same current state. |

## Observability Signals

- Status: draft, active, blocked, under review, approved exception, or archived.
- Freshness: last reviewed date and next review date.
- Risk: current risk class, escalation owner, and unresolved blockers.
- Flow: upstream source ready, local work in progress, downstream accepted, or rejected.
- Quality: validation pass rate, rework count, decision latency, and stale artifact count.

## Memory And Evolution

- Historical memory preserves source lineage and retired drafts.
- Operational memory records cadence, owners, blockers, and handoff results.
- Decision memory records approvals, exceptions, rejected paths, and rationale.
- Execution memory records completed runs, incidents, and recovery actions.
- Learning memory records repeated failure patterns and improvement actions.

## Completion Criteria

{completion_criteria(config, concern)}

This artifact remains active until superseded by a later version in the local registry and the agency global source registry.
"""


def materialize_required_artifacts(records_by_workspace: dict[str, list[dict[str, str]]]) -> list[dict[str, object]]:
    register_rows: list[dict[str, object]] = []
    for workspace, config in WORKSPACES.items():
        rows = records_by_workspace.get(workspace, [])
        for concern in CONCERNS:
            rel = required_artifact(config, concern)
            path = ROOT / rel
            action = "Existing"
            if not path.exists():
                write_text(path, canonical_artifact_markdown(workspace, concern, rows))
                action = "Created"
            register_rows.append(
                {
                    "Workspace": workspace,
                    "Domain": config["domain"],
                    "Concern": concern,
                    "Artifact Path": rel,
                    "State": action,
                    "Owner": config["owner"],
                    "Source Evidence Rows": len(rows),
                    "Generated On": RUN_DATE,
                }
            )
    return register_rows


def canonical_artifact_register_rows(workspace: str) -> list[dict[str, object]]:
    config = WORKSPACES[workspace]
    rows: list[dict[str, object]] = []
    for concern in CONCERNS:
        rel = required_artifact(config, concern)
        path = ROOT / rel
        if not path.exists():
            continue
        try:
            word_count = len(path.read_text(encoding="utf-8").split())
        except OSError:
            word_count = 0
        rows.append(
            {
                "Document Name": path.name,
                "Relative Path": rel,
                "Extension": ".md",
                "Word Count": str(word_count),
                "Purpose": f"Canonical {config['domain']} {concern} operating artifact with source mapping, ownership, validation, observability, memory, and version controls.",
                "Strategic Function": f"{concern} control; Governance / risk control; Architecture / system map; Execution workflow.",
                "Business Function": f"Supports {config['domain']} operating performance and downstream handoffs into {config['downstream']}.",
                "Layer Assignment": f"{config['domain']} + Management, Governance, Automation",
                "Dependencies": config["upstream"],
                "Inputs": "source evidence, owner review, upstream handoff, risk class, current state",
                "Outputs": "canonical rule, registry entry, validation gate, dashboard signal, memory update",
                "Workflows Supported": "source promotion, handoff acceptance, validation, monitoring, recovery, evolution",
                "KPIs Influenced": "source freshness, validation pass rate, decision latency, risk closure, completion readiness",
                "Revenue Impact": "Protects revenue quality by reducing operating ambiguity, handoff failure, compliance drift, and unmanaged risk.",
                "Automation Potential": "High",
                "Decision Value": "High",
                "Scalability Value": "High",
                "Risk Factors": "stale source evidence, owner ambiguity, unvalidated handoffs, dashboard drift",
                "Related Documents": str(BASELINE_REGISTER.relative_to(ROOT)),
                "Related Systems": "Agency OS; Domain OS; Registry Backbone; Dashboard Spine; Memory System",
                "Related Departments": f"{config['domain']}; Management; Legal; Finance; Automation",
                "Lifecycle Position": "All governed lifecycle stages",
                "Headings / Signals": f"{concern}; Traceability; Source Evidence; Control Model; Validation Gates; Observability Signals; Memory And Evolution",
            }
        )
    return rows


def add_canonical_rows(records_by_workspace: dict[str, list[dict[str, str]]]) -> None:
    for workspace in WORKSPACES:
        existing_paths = {row.get("Relative Path", "") for row in records_by_workspace.get(workspace, [])}
        for row in canonical_artifact_register_rows(workspace):
            if str(row.get("Relative Path", "")) not in existing_paths:
                records_by_workspace[workspace].append({key: str(value) for key, value in row.items()})


def workspace_markdown(workspace: str, rows: list[dict[str, str]], gaps: list[dict[str, str]], statuses: list[dict[str, str]]) -> str:
    config = WORKSPACES[workspace]
    summary = summarize_workspace_rows(rows)
    present = sum(1 for row in statuses if row["Status"] == "Present")
    partial = sum(1 for row in statuses if row["Status"] == "Partially Present")
    missing = sum(1 for row in statuses if row["Status"] == "Missing")
    critical = sum(1 for row in gaps if row["Severity"] == "Critical")
    high = sum(1 for row in gaps if row["Severity"] in {"High", "Medium-High"})
    inventory_rows = [
        [
            row.get("Relative Path", ""),
            row.get("Extension", ""),
            row.get("Word Count", ""),
            row.get("Layer Assignment", ""),
            row.get("Purpose", ""),
            row.get("Automation Potential", ""),
        ]
        for row in rows
    ]
    if not inventory_rows:
        inventory_rows = [["No source documents found in this workspace.", "", "", "", "Create the workspace source registry before operational use.", ""]]
    gap_table_rows = [
        [
            row["Gap Category"],
            row["Status"],
            row["Severity"],
            row["Root Cause"],
            row["Required Markdowns"],
            row["Completion Criteria"],
        ]
        for row in gaps
    ]
    if not gap_table_rows:
        gap_table_rows = [["No unresolved concern gaps detected by this pass.", "Present", "None", "N/A", "N/A", "Maintain cadence and version governance."]]
    status_table_rows = [
        [row["Concern"], row["Status"], row["Severity"], row["Evidence"], row["Recommended Addition"]]
        for row in statuses
    ]
    return f"""
# {workspace} - Workspace Architectural Completion Inventory

Generated: {RUN_DATE}

Source baseline: `{BASELINE_REGISTER.relative_to(ROOT)}`

## Workspace Intent

| Field | Specification |
|---|---|
| Domain | {config['domain']} |
| Owner | {config['owner']} |
| Intent | {config['intent']} |
| Operating Role | {config['role']} |
| Upstream Dependencies | {config['upstream']} |
| Downstream Dependencies | {config['downstream']} |
| Critical Outputs | {config['critical_outputs']} |

## Existing Architecture Inventory

| Metric | Value |
|---|---:|
| Files in baseline register | {summary['Files']} |
| DOCX source drafts | {summary['DOCX']} |
| Markdown control artifacts | {summary['Markdown']} |
| CSV registries/indexes | {summary['CSV']} |
| JSON/JSONL assets | {summary['JSON']} |
| Runtime/code/config assets | {summary['Runtime']} |
| Extracted words | {summary['Words']} |

Top layer signals: {summary['Top Layers'] or 'No layer evidence detected.'}

Completeness signal: {present} present, {partial} partially present, {missing} missing concerns. Gap pressure: {critical} critical, {high} high or medium-high.

## Complete Existing Artifact Register

{table(['Relative Path', 'Ext', 'Words', 'Layer Assignment', 'Purpose', 'Automation Potential'], inventory_rows)}

## Completeness Verification by Concern

{table(['Concern', 'Status', 'Severity', 'Evidence', 'Recommended Addition'], status_table_rows)}

## Gap Inventory and Resolution Plan

{table(['Gap Category', 'Status', 'Severity', 'Root Cause', 'Required Markdown', 'Completion Criteria'], gap_table_rows)}

## Required Solution Architecture

Every non-present concern above must be closed through a local authoritative markdown, local registry update, agency registry reference, owner assignment, dependency map, validation gate, observability signal, and version/evolution entry.

## Required Registries

- Local source registry for {config['domain']} source IDs, active/superseded/archive state, owner, cadence, dependencies, and related domains.
- Local master registry for workflows, artifacts, schemas, events, automations, decisions, metrics, and memory logs.
- Agency Global Source Registry reference so this workspace can be routed without duplicating intelligence.

## Required Protocols

- Source promotion protocol: draft source -> canonical markdown -> registry entry -> owner approval -> version log.
- Handoff protocol: upstream evidence -> {config['domain']} transformation -> downstream acceptance packet -> memory update.
- Governance protocol: risk class -> approval path -> execution boundary -> audit/memory entry.
- Validation protocol: entry criteria -> evidence check -> output check -> completion gate.
- Evolution protocol: decision log -> learning loop -> version update -> quarterly operating review.

## Workspace Placement and Separation Delivery

This workspace owns only {config['domain']} intelligence and operating controls. Cross-domain concerns must be referenced through registries and handoff packets rather than duplicated. Authoritative local artifacts should live inside `{config['folder'] or '00_Agency_Workspace_Intelligence'}` and connect upward to the agency root registry.

## Dependency Resolution

| Direction | Dependency |
|---|---|
| Upstream | {config['upstream']} |
| Downstream | {config['downstream']} |
| Required routing | Source registry -> domain orchestration -> handoff contract -> validation gate -> dashboard/memory update |

## Prompt OS Completion Roadmap

{table(['Phase', 'Objectives', 'Dependencies', 'Completion Gate'], phase_plan(config))}

## Local Output Files

- `00_Workspace_Intelligence_Inventory/WORKSPACE_ARCHITECTURAL_COMPLETION_INVENTORY.md`
- `00_Workspace_Intelligence_Inventory/WORKSPACE_EXISTING_ARTIFACT_REGISTER.csv`
- `00_Workspace_Intelligence_Inventory/WORKSPACE_GAP_RESOLUTION_BACKLOG.csv`
- `00_Workspace_Intelligence_Inventory/RECOMMENDED_MARKDOWN_ADDITIONS.csv`
"""


def central_index(
    records_by_workspace: dict[str, list[dict[str, str]]],
    all_gaps: list[dict[str, str]],
    all_statuses: list[dict[str, str]],
    all_recs: list[dict[str, str]],
) -> str:
    workspace_rows = []
    for workspace in WORKSPACES:
        config = WORKSPACES[workspace]
        rows = records_by_workspace.get(workspace, [])
        summary = summarize_workspace_rows(rows)
        statuses = [row for row in all_statuses if row["Workspace"] == workspace]
        present = sum(1 for row in statuses if row["Status"] == "Present")
        partial = sum(1 for row in statuses if row["Status"] == "Partially Present")
        missing = sum(1 for row in statuses if row["Status"] == "Missing")
        gaps = [row for row in all_gaps if row["Workspace"] == workspace]
        workspace_rows.append(
            [
                workspace,
                config["domain"],
                summary["Files"],
                summary["DOCX"],
                summary["Markdown"],
                summary["CSV"],
                summary["JSON"],
                present,
                partial,
                missing,
                len(gaps),
            ]
        )
    critical_rows = [
        [
            gap["Gap ID"],
            gap["Workspace"],
            gap["Gap Category"],
            gap["Severity"],
            gap["Required Markdowns"],
        ]
        for gap in all_gaps
        if gap["Severity"] == "Critical"
    ][:80]
    if not critical_rows:
        critical_rows = [["None", "All Workspaces", "Critical gaps", "None", "All required canonical artifacts are present."]]
    output_rows = []
    for workspace, config in WORKSPACES.items():
        if workspace == "The Agency Drafts Root":
            path = CENTRAL_DIR / "00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md"
        else:
            path = ROOT / config["folder"] / "00_Workspace_Intelligence_Inventory" / "WORKSPACE_ARCHITECTURAL_COMPLETION_INVENTORY.md"
        output_rows.append([workspace, str(path.relative_to(ROOT))])
    score_rows = final_score_rows(all_statuses)
    return f"""
# Agency Workspace Architectural Completion Index

Generated: {RUN_DATE}

This pass operationalizes the pasted Prompt OS directive across the agency root and each named workspace. It preserves domain separation by placing local inventories inside each workspace and placing cross-domain governance, gap, integration, roadmap, and verification artifacts in `00_Agency_Workspace_Intelligence`.

## Source Baseline

- Prior extraction pack: `{BASELINE_DIR.relative_to(ROOT)}`
- Baseline register: `{BASELINE_REGISTER.relative_to(ROOT)}`
- Workspace evidence rows represented after materialization: {sum(len(rows) for rows in records_by_workspace.values())}
- Unique relative paths represented: {len({row.get('Relative Path', '') for rows in records_by_workspace.values() for row in rows if row.get('Relative Path', '')})}

## Existing Architecture by Workspace

{table(['Workspace', 'Domain', 'Files', 'DOCX', 'MD', 'CSV', 'JSON', 'Present', 'Partial', 'Missing', 'Gap Rows'], workspace_rows)}

## Critical Gap Inventory Snapshot

{table(['Gap ID', 'Workspace', 'Category', 'Severity', 'Required Markdown'], critical_rows)}

## Output Placement

{table(['Workspace', 'Inventory Path'], output_rows)}

## Cross-Workspace Operating Flow

Primary flow: Sector -> Offer -> Marketing -> Sales -> Client -> Operations -> Finance -> Management.

Support layers: Branding supports Marketing, Sales, Client, and Management; ClientPartner Acquisition feeds Sales and distribution; Legal Drafts now owns enterprise legal/governance controls; Automation, Memory, Observability, and Security govern all layers.

## Required Agency-Wide Closure Systems

1. Agency Global Source Registry with source IDs, active/superseded/archive state, owners, cadence, dependencies, and domain placement.
2. Agency Operating Constitution with amendment process, decision rights, risk classes, and governance boundaries.
3. Cross-domain RACI covering Management, Finance, Legal Drafts, Automation, Operations, and every domain owner.
4. CRM schema connecting Marketing -> Sales -> Client -> Finance -> Legal, including source context, promise handoff, revenue events, contract state, and client health.
5. KPI dictionary with formula, source, owner, cadence, threshold, dashboard, and decision consequence.
6. Handoff packet standards for Sector -> Offer, Offer -> Marketing, Marketing -> Sales, Sales -> Client, Client -> Operations, Operations -> Finance, Finance -> Management.
7. Automation approval matrix with trigger, action, risk class, rollback, fallback, log destination, and human gate.
8. Memory protocol for historical, operational, decision, execution, and learning memory after every significant workflow.
9. Dashboard spine covering executive health, revenue, marketing, sales, client, operations, finance, automation, risk, and source freshness.
10. Versioning/change protocol that prevents draft collisions from becoming operating confusion.

## Final Architectural Completeness Score

{table(['Readiness Area', 'Score', 'Interpretation'], score_rows)}

## Files Written

- `00_Agency_Workspace_Intelligence/00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md`
- `00_Agency_Workspace_Intelligence/01_EXISTING_ARCHITECTURE_INVENTORY.csv`
- `00_Agency_Workspace_Intelligence/02_GAP_RESOLUTION_INVENTORY.csv`
- `00_Agency_Workspace_Intelligence/03_RECOMMENDED_MARKDOWN_ADDITIONS.csv`
- `00_Agency_Workspace_Intelligence/04_WORKSPACE_INTEGRATION_PLAN.md`
- `00_Agency_Workspace_Intelligence/05_PROMPT_OS_COMPLETION_ROADMAP.md`
- `00_Agency_Workspace_Intelligence/06_COMPLETENESS_VERIFICATION.md`
- `00_Agency_Workspace_Intelligence/07_WORKSPACE_SEPARATION_DELIVERY_INVENTORY.md`
- `00_Agency_Workspace_Intelligence/09_MATERIALIZED_OPERATING_ARTIFACT_REGISTER.csv`
- Per-workspace inventory packs under each `00_Workspace_Intelligence_Inventory` folder.
- Canonical operating artifacts under every required workspace concern path.
"""


def status_score(statuses: list[dict[str, str]], concerns: list[str]) -> float:
    relevant = [row for row in statuses if row["Concern"] in concerns]
    if not relevant:
        return 0.0
    value = 0.0
    for row in relevant:
        if row["Status"] == "Present":
            value += 1.0
        elif row["Status"] == "Partially Present":
            value += 0.5
    return round((value / len(relevant)) * 100, 1)


def final_score_rows(statuses: list[dict[str, str]]) -> list[list[str]]:
    areas = {
        "Foundation Completeness": ["Intent", "Strategy", "Architecture", "Strategic Planning"],
        "Governance Completeness": ["Constitution", "Governance", "Ownership", "Enterprise Controls", "Security"],
        "Orchestration Completeness": ["Orchestration", "Workflows", "Execution", "Separation Intelligence"],
        "State Completeness": ["State Management", "Information Storage"] if "Information Storage" in CONCERNS else ["State Management", "Registries"],
        "Validation Completeness": ["Validation", "Completion"],
        "Observability Completeness": ["Observability"],
        "Workspace Separation Delivery Completeness": ["Separation Intelligence", "Domain Intelligence", "Registries"],
        "Historical Memory Completeness": ["Historical Memory", "Operational Memory", "Decision Memory", "Execution Memory"],
        "Information Storage Completeness": ["Registries", "Knowledge", "Artifacts", "Schemas"],
        "Automation Completeness": ["Automation", "Agents", "Tools", "Events"],
        "Evolution Completeness": ["Change Management", "Versioning", "Recovery", "Evolution", "Learning Systems"],
        "Prompt OS Completeness": list(CONCERNS.keys()),
        "Enterprise Readiness": ["Governance", "Ownership", "Validation", "Observability", "Security", "Completion"],
        "Self-Governance Readiness": ["Constitution", "Governance", "Decision Memory", "Change Management", "Versioning"],
        "Self-Evolution Readiness": ["Learning Systems", "Evolution", "Historical Memory", "Decision Memory"],
        "Autonomous Operations Readiness": ["Automation", "Agents", "Tools", "Events", "Validation", "Observability", "Recovery"],
        "Knowledge Preservation Readiness": ["Workspace Intelligence", "Knowledge", "Historical Memory", "Decision Memory", "Versioning"],
    }
    rows = []
    for area, concerns in areas.items():
        score = status_score(statuses, concerns)
        if score >= 80:
            interp = "Strong but still requires cadence and owner review."
        elif score >= 55:
            interp = "Partially established; close high-severity registry/governance gaps before scale."
        else:
            interp = "Not yet enterprise-ready; requires canonical markdowns, ownership, validation, and observability."
        rows.append([area, f"{score}%", interp])
    return rows


def integration_plan() -> str:
    placement_rows = []
    for workspace, config in WORKSPACES.items():
        placement_rows.append(
            [
                workspace,
                config["domain"],
                config["folder"] or "00_Agency_Workspace_Intelligence",
                config["owner"],
                config["upstream"],
                config["downstream"],
            ]
        )
    return f"""
# Workspace Integration Plan

Generated: {RUN_DATE}

## Placement Doctrine

Artifacts must live at the closest authoritative layer. Local domain truth lives inside the domain workspace. Cross-domain rules, source IDs, enterprise governance, dashboards, and dependency maps live in the agency root intelligence layer. Repetition is avoided by references: local registries point upward to the agency registry, and the agency registry points back to local owners.

## Authoritative Workspace Placement

{table(['Workspace', 'Domain', 'Authoritative Location', 'Owner', 'Upstream', 'Downstream'], placement_rows)}

## Registry Relationships

- Local Source Registry: owns local document IDs, status, owner, cadence, dependencies, and source evidence.
- Local Master Registry: owns workflows, artifacts, schemas, events, agents, tools, automations, metrics, decisions, and memory.
- Agency Global Source Registry: owns cross-domain source routing, active/superseded/archive state, duplication decisions, and agency-level lineage.
- Agency Dependency Registry: owns cross-workspace dependencies and required handoff packets.
- Agency KPI Registry: owns formulas, thresholds, dashboard locations, and decision consequences.

## Orchestration Rules

1. Source work starts in the local workspace and is registered locally.
2. Any cross-domain output must create or update a handoff packet.
3. Handoffs are accepted only when entry/exit criteria, source evidence, owner, KPI impact, and legal/risk approval state are present where required.
4. Automation can execute only when the action has a risk class, approval route, rollback, fallback, and log destination.
5. Every material decision updates the decision log and version log.
6. Every completed workflow updates operational memory and learning memory.

## Dependency Graph

Sector -> Offer -> Marketing -> Sales -> Client -> Operations -> Finance -> Management.

Branding supports Sector, Offer, Marketing, Sales, Client, and Management.

ClientPartner Acquisition feeds Marketing, Sales, and distribution.

Legal Drafts governs contracts, claims, privacy, payment terms, IP, compliance, partner terms, and risk acceptance across all domains.

Automation, Observability, Memory, Security, and Change Management apply across all domains.
"""


def roadmap() -> str:
    rows = [
        [
            "Phase 1",
            "Source truth, ownership, and governance foundation",
            "Agency Global Source Registry, local source registries, RACI, risk classes, active/superseded/archive status",
            "Existing baseline register and local inventories",
            "Every source has ID, owner, status, cadence, and dependency tags",
            "Agency owner approves governance charter and RACI",
            "No workspace remains without a local inventory and gap backlog",
        ],
        [
            "Phase 2",
            "Canonical domain OS promotion",
            "Intent, architecture, constitution, orchestration, execution, registry, and validation markdowns for each workspace",
            "Phase 1 source truth",
            "Canonical markdowns exist and reference source IDs",
            "Domain owners approve local operating authority",
            "Operators can identify the current authoritative document for every concern",
        ],
        [
            "Phase 3",
            "Cross-domain handoffs, schemas, and dashboards",
            "CRM schema, legal approval state, handoff packets, KPI dictionary, dashboard specs, event catalog, state boards",
            "Phase 2 canonical domain OS",
            "Every upstream/downstream edge has input/output contract and acceptance gate",
            "Management and Legal approve KPI thresholds, risk classes, claims boundaries, and decision consequences",
            "Agency can see what is happening now and what needs attention",
        ],
        [
            "Phase 4",
            "Automation, memory, and observability runtime",
            "Automation registry, approval matrix, agent registries, operational/decision/execution memory logs, monitoring routines",
            "Governed workflows, schemas, and dashboards",
            "Automations are risk-classed, observable, reversible, and memory-writing",
            "Automation owner approves low-risk runtime execution and high-risk escalation paths",
            "Manual fallback exists for every automation",
        ],
        [
            "Phase 5",
            "Enterprise readiness, evolution, and completeness proof",
            "Version log, change protocol, recovery plan, quarterly review cadence, self-audit checklist, completion certificates",
            "Validation evidence and live dashboard signals",
            "All critical/high gaps are closed or approved with dated remediation plan",
            "Agency Operating Council approves readiness score and evolution cadence",
            "The workspace can prove completeness and preserve history, decisions, and learning",
        ],
    ]
    return f"""
# Prompt OS Completion Roadmap

Generated: {RUN_DATE}

{table(['Phase', 'Objectives', 'Deliverables', 'Dependencies', 'Validation Gate', 'Governance Gate', 'Completion Gate'], rows)}

## Phase Priority Logic

Do not automate before source truth, ownership, governance, legal/risk gates, handoff contracts, and validation exist. Do not scale client execution before Client, Offer, Sales, Finance, Legal, and Operations handoffs are accepted. Do not archive or merge drafts before source IDs preserve lineage.
"""


def completeness_verification(statuses: list[dict[str, str]]) -> str:
    rows = [
        [row["Workspace"], row["Domain"], row["Concern"], row["Status"], row["Severity"], row["Recommended Addition"], row["Completion Criteria"]]
        for row in statuses
    ]
    return f"""
# Completeness Verification

Generated: {RUN_DATE}

This file verifies each required architectural concern for each workspace. `Present` means a strong local or root authoritative signal exists. `Partially Present` means the concern exists conceptually or in runtime fragments but still needs canonical ownership, registry, validation, observability, and evolution. `Missing` means the concern cannot be proven from authoritative artifacts.

{table(['Workspace', 'Domain', 'Concern', 'Status', 'Severity', 'Recommended Addition', 'Completion Criteria'], rows)}
"""


def separation_inventory(records_by_workspace: dict[str, list[dict[str, str]]]) -> str:
    rows = []
    for workspace, config in WORKSPACES.items():
        summary = summarize_workspace_rows(records_by_workspace.get(workspace, []))
        rows.append(
            [
                workspace,
                config["domain"],
                config["role"],
                config["folder"] or "00_Agency_Workspace_Intelligence",
                summary["Files"],
                config["upstream"],
                config["downstream"],
                config["critical_outputs"],
            ]
        )
    return f"""
# Workspace Separation Delivery Inventory

Generated: {RUN_DATE}

Each workspace is treated as an authoritative domain, not as a pile of interchangeable documents. Separation is achieved through ownership, local registries, source IDs, handoff packets, and references to agency-level registries.

{table(['Workspace', 'Domain', 'Operating Role', 'Authoritative Location', 'Source Files', 'Upstream', 'Downstream', 'Critical Outputs'], rows)}
"""


def main() -> None:
    source_rows = read_register()
    records_by_workspace: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        records_by_workspace[workspace_from_path(row.get("Relative Path", ""))].append(row)
    for workspace in WORKSPACES:
        records_by_workspace.setdefault(workspace, [])
    legal_seen = {row.get("Relative Path", "") for row in records_by_workspace["Legal Drafts"]}
    for row in source_rows:
        rel = row.get("Relative Path", "")
        if is_legal_reference(row) and rel not in legal_seen:
            records_by_workspace["Legal Drafts"].append(dict(row))
            legal_seen.add(rel)

    materialized_register = materialize_required_artifacts(records_by_workspace)
    add_canonical_rows(records_by_workspace)

    all_existing: list[dict[str, object]] = []
    all_gaps: list[dict[str, str]] = []
    all_statuses: list[dict[str, str]] = []
    all_recs: list[dict[str, str]] = []

    existing_fields = [
        "Workspace",
        "Domain",
        "Document Name",
        "Relative Path",
        "Extension",
        "Word Count",
        "Layer Assignment",
        "Purpose",
        "Strategic Function",
        "Automation Potential",
        "Risk Factors",
    ]
    gap_fields = [
        "Gap ID",
        "Workspace",
        "Domain",
        "Gap Name",
        "Gap Category",
        "Gap Layer",
        "Status",
        "Severity",
        "Gap Impact",
        "Root Cause",
        "Required Solution",
        "Required Markdowns",
        "Required Protocols",
        "Required Registries",
        "Required Governance",
        "Required Ownership",
        "Required Orchestration",
        "Required Validation",
        "Required Observability",
        "Required Evolution",
        "Required Dependencies",
        "Required Placement",
        "Required Sequencing",
        "Completion Criteria",
    ]
    rec_fields = [
        "Workspace",
        "Domain",
        "Recommended Markdown",
        "Purpose",
        "Owner",
        "Priority",
        "Dependencies",
        "Completion Criteria",
    ]
    status_fields = [
        "Workspace",
        "Domain",
        "Concern",
        "Status",
        "Severity",
        "Evidence",
        "Recommended Addition",
        "Completion Criteria",
    ]
    materialized_fields = [
        "Workspace",
        "Domain",
        "Concern",
        "Artifact Path",
        "State",
        "Owner",
        "Source Evidence Rows",
        "Generated On",
    ]

    for workspace, config in WORKSPACES.items():
        rows = records_by_workspace.get(workspace, [])
        gaps, statuses = build_gap_rows(workspace, rows)
        recs = recommendation_rows(gaps)
        existing = artifact_register_rows(workspace, rows)
        all_existing.extend(existing)
        all_gaps.extend(gaps)
        all_statuses.extend(statuses)
        all_recs.extend(recs)

        if workspace != "The Agency Drafts Root":
            inv_dir = ROOT / config["folder"] / "00_Workspace_Intelligence_Inventory"
            write_text(inv_dir / "WORKSPACE_ARCHITECTURAL_COMPLETION_INVENTORY.md", workspace_markdown(workspace, rows, gaps, statuses))
            write_csv(inv_dir / "WORKSPACE_EXISTING_ARTIFACT_REGISTER.csv", existing, existing_fields)
            write_csv(inv_dir / "WORKSPACE_GAP_RESOLUTION_BACKLOG.csv", gaps, gap_fields)
            write_csv(inv_dir / "RECOMMENDED_MARKDOWN_ADDITIONS.csv", recs, rec_fields)

    CENTRAL_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(CENTRAL_DIR / "01_EXISTING_ARCHITECTURE_INVENTORY.csv", all_existing, existing_fields)
    write_csv(CENTRAL_DIR / "02_GAP_RESOLUTION_INVENTORY.csv", all_gaps, gap_fields)
    write_csv(CENTRAL_DIR / "03_RECOMMENDED_MARKDOWN_ADDITIONS.csv", all_recs, rec_fields)
    write_csv(CENTRAL_DIR / "06_COMPLETENESS_VERIFICATION.csv", all_statuses, status_fields)
    write_csv(CENTRAL_DIR / "09_MATERIALIZED_OPERATING_ARTIFACT_REGISTER.csv", materialized_register, materialized_fields)
    write_text(CENTRAL_DIR / "00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md", central_index(records_by_workspace, all_gaps, all_statuses, all_recs))
    write_text(CENTRAL_DIR / "04_WORKSPACE_INTEGRATION_PLAN.md", integration_plan())
    write_text(CENTRAL_DIR / "05_PROMPT_OS_COMPLETION_ROADMAP.md", roadmap())
    write_text(CENTRAL_DIR / "06_COMPLETENESS_VERIFICATION.md", completeness_verification(all_statuses))
    write_text(CENTRAL_DIR / "07_WORKSPACE_SEPARATION_DELIVERY_INVENTORY.md", separation_inventory(records_by_workspace))
    write_text(
        CENTRAL_DIR / "08_EXECUTION_SEQUENCE_AND_GOVERNANCE_GATES.md",
        "# Execution Sequence and Governance Gates\n\n"
        + roadmap().split("\n", 2)[-1]
        + "\n\n## Non-Negotiable Gates\n\n"
        + "- No domain workflow is complete without source ID, owner, input, output, validation, observability, and memory update.\n"
        + "- No cross-domain handoff is accepted without upstream evidence and downstream acceptance criteria.\n"
        + "- No claim, contract, payment term, privacy commitment, partner obligation, or risk exception is released without Legal Drafts approval state.\n"
        + "- No automation runs externally without risk class, approval route, rollback, fallback, and log destination.\n"
        + "- No draft becomes canonical without registry update, version log, and owner approval.\n"
        + "- No workspace can claim completion while critical gaps remain unclosed or unapproved.\n",
    )

    summary = {
        "generated": RUN_DATE,
        "central_dir": str(CENTRAL_DIR),
        "source_records": len(source_rows),
        "workspaces": len(WORKSPACES),
        "existing_rows": len(all_existing),
        "gap_rows": len(all_gaps),
        "recommended_markdowns": len(all_recs),
        "status_rows": len(all_statuses),
        "materialized_artifacts": len(materialized_register),
        "created_artifacts": sum(1 for row in materialized_register if row["State"] == "Created"),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
