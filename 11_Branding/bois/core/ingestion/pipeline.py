from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from ..models import DocumentRecord, IngestionReport, ParagraphRecord
from .docx_reader import read_docx_paragraphs, stable_text_hash


DEFAULT_EXTENSIONS = {".docx", ".md", ".txt", ".csv", ".tsv", ".json"}
DEFAULT_EXCLUDED_DIRS = {"bois", "branding-os", ".git", "__pycache__", "bois_shell_test"}

TAG_RULES = {
    "industry": ("industry", "category", "vertical", "market structure", "sector"),
    "sector": ("sector", "domain", "category", "competitive", "regulatory"),
    "psychology": ("motivation", "belief", "behavior", "emotional", "cognitive"),
    "communication": ("messaging", "story", "narrative", "voice", "script"),
    "visuals": ("visual", "design", "symbol", "color", "typography"),
    "governance": ("governance", "policy", "control", "approval", "audit"),
    "execution": ("workflow", "execution", "deployment", "operational", "runbook"),
    "culture": ("culture", "cultural", "localization", "ritual", "norm"),
    "sales": ("sales", "pipeline", "objection", "conversion", "closing"),
    "marketing": ("marketing", "campaign", "funnel", "acquisition", "content"),
    "legal": ("legal", "ip", "trademark", "compliance", "licensing"),
    "psychographics": ("psychographic", "identity", "values", "aspiration", "status"),
    "symbolic_systems": ("symbolic", "semiotic", "archetype", "code", "signal"),
}


def _read_text_file(path: Path) -> List[str]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    blocks = [block.strip() for block in re.split(r"\n\s*\n", raw) if block.strip()]
    return blocks


def _file_checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _section_hint(text: str) -> str:
    t = text.strip()
    if re.match(r"^(STAGE|PHASE|LAYER|MODE)\b", t, flags=re.IGNORECASE):
        return "structured_heading"
    if t.isupper() and len(t) > 12:
        return "all_caps_heading"
    if ":" in t and len(t) < 120:
        return "key_value_heading"
    return "body"


def _tags_for_text(text: str) -> List[str]:
    lowered = text.lower()
    tags: List[str] = []
    for tag, keywords in TAG_RULES.items():
        if any(keyword in lowered for keyword in keywords):
            tags.append(tag)
    return tags


def _paragraphs_for_file(path: Path) -> List[str]:
    if path.suffix.lower() == ".docx":
        return read_docx_paragraphs(path)
    if path.suffix.lower() in {".md", ".txt", ".csv", ".tsv", ".json"}:
        return _read_text_file(path)
    return []


def scan_files(
    root: Path,
    extensions: Iterable[str] = DEFAULT_EXTENSIONS,
    excluded_dirs: Iterable[str] = DEFAULT_EXCLUDED_DIRS,
) -> List[Path]:
    allowed = {ext.lower() for ext in extensions}
    excluded = {name.lower() for name in excluded_dirs}
    files: List[Path] = []
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in allowed:
            continue
        rel_parts = [part.lower() for part in p.relative_to(root).parts[:-1]]
        if any(part in excluded for part in rel_parts):
            continue
        files.append(p)
    return sorted(files)


def ingest(
    root: Path,
    output_dir: Path,
    extensions: Iterable[str] = DEFAULT_EXTENSIONS,
    excluded_dirs: Iterable[str] = DEFAULT_EXCLUDED_DIRS,
) -> IngestionReport:
    started = datetime.utcnow().isoformat()
    output_dir.mkdir(parents=True, exist_ok=True)
    files = scan_files(root, extensions=extensions, excluded_dirs=excluded_dirs)

    document_records: List[DocumentRecord] = []
    paragraph_records: List[ParagraphRecord] = []
    errors: List[str] = []
    text_hash_counter: Counter[str] = Counter()

    for path in files:
        try:
            paragraphs = _paragraphs_for_file(path)
            file_type = path.suffix.lower().lstrip(".")
            checksum = _file_checksum(path)
            stat = path.stat()
            document_id = hashlib.sha1(str(path.resolve()).encode("utf-8")).hexdigest()[:16]

            doc = DocumentRecord(
                document_id=document_id,
                path=str(path.resolve()),
                file_type=file_type,
                checksum=checksum,
                created_at=datetime.utcfromtimestamp(stat.st_ctime).isoformat(),
                modified_at=datetime.utcfromtimestamp(stat.st_mtime).isoformat(),
                paragraph_count=len(paragraphs),
                metadata={},
            )
            document_records.append(doc)

            for ordinal, text in enumerate(paragraphs, start=1):
                h = stable_text_hash(text)
                text_hash_counter[h] += 1
                paragraph_records.append(
                    ParagraphRecord(
                        paragraph_id=f"{document_id}:P{ordinal:04d}",
                        document_id=document_id,
                        ordinal=ordinal,
                        text=text,
                        text_hash=h,
                        tags=_tags_for_text(text),
                        section_hint=_section_hint(text),
                        metadata={"source_path": str(path.resolve())},
                    )
                )
        except Exception as exc:  # pragma: no cover
            errors.append(f"{path}: {exc}")

    repeated_groups = 0
    for record in paragraph_records:
        count = text_hash_counter[record.text_hash]
        record.reinforcement_count = count
        if count > 1:
            repeated_groups += 1

    taxonomy_index: Dict[str, List[str]] = defaultdict(list)
    for record in paragraph_records:
        for tag in record.tags:
            taxonomy_index[tag].append(record.paragraph_id)

    repetition_map: Dict[str, List[str]] = defaultdict(list)
    for record in paragraph_records:
        repetition_map[record.text_hash].append(record.paragraph_id)

    with (output_dir / "documents.json").open("w", encoding="utf-8") as f:
        json.dump([asdict(d) for d in document_records], f, indent=2, ensure_ascii=False)

    with (output_dir / "paragraphs.jsonl").open("w", encoding="utf-8") as f:
        for p in paragraph_records:
            f.write(json.dumps(asdict(p), ensure_ascii=False) + "\n")

    with (output_dir / "taxonomy_index.json").open("w", encoding="utf-8") as f:
        json.dump(taxonomy_index, f, indent=2, ensure_ascii=False)

    with (output_dir / "repetition_map.json").open("w", encoding="utf-8") as f:
        filtered = {k: v for k, v in repetition_map.items() if len(v) > 1}
        json.dump(filtered, f, indent=2, ensure_ascii=False)

    completed = datetime.utcnow().isoformat()
    return IngestionReport(
        root=str(root.resolve()),
        discovered_files=len(files),
        parsed_documents=len(document_records),
        parsed_paragraphs=len(paragraph_records),
        repeated_paragraph_groups=len([1 for v in repetition_map.values() if len(v) > 1]),
        started_at=started,
        completed_at=completed,
        errors=errors,
    )


def load_paragraphs(paragraph_jsonl: Path) -> List[ParagraphRecord]:
    records: List[ParagraphRecord] = []
    with paragraph_jsonl.open("r", encoding="utf-8") as f:
        for raw in f:
            obj = json.loads(raw)
            records.append(ParagraphRecord(**obj))
    return records


def build_document_theme_index(records: List[ParagraphRecord]) -> Dict[str, Dict[str, int]]:
    by_doc: Dict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        for tag in record.tags:
            by_doc[record.document_id][tag] += 1
    return {doc_id: dict(counter) for doc_id, counter in by_doc.items()}


def collect_stage_signals(records: List[ParagraphRecord]) -> Dict[str, List[Tuple[str, str]]]:
    stage_pattern = re.compile(r"^(STAGE|PHASE|LAYER|MODE)\b", flags=re.IGNORECASE)
    out: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for record in records:
        if stage_pattern.search(record.text):
            out[record.document_id].append((record.paragraph_id, record.text))
    return out
