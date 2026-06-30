from __future__ import annotations

import json
import re
from dataclasses import asdict
from pathlib import Path
from typing import Dict

from .models import ClientObject


CLIENT_SUBDIRS = [
    "memory",
    "campaigns",
    "presentations",
    "visuals",
    "governance",
    "deliverables",
    "timelines",
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "unnamed-client"


def create_client_workspace(branding_os_root: Path, client: ClientObject) -> Dict[str, str]:
    client_slug = slugify(client.company_name or client.client_id)
    client_root = branding_os_root / "clients" / client_slug
    for subdir in CLIENT_SUBDIRS:
        (client_root / subdir).mkdir(parents=True, exist_ok=True)

    client_path = client_root / "memory" / "client.json"
    with client_path.open("w", encoding="utf-8") as f:
        json.dump(asdict(client), f, indent=2, ensure_ascii=False)

    return {
        "client_root": str(client_root.resolve()),
        "client_memory": str(client_path.resolve()),
    }

