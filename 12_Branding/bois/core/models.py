from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass(slots=True)
class ClientObject:
    client_id: str
    company_name: str
    sector: str = ""
    sub_sector: str = ""
    geography: str = ""
    audience: str = ""
    psychographics: List[str] = field(default_factory=list)
    products: List[str] = field(default_factory=list)
    services: List[str] = field(default_factory=list)
    pricing_model: str = ""
    market_position: str = ""
    competitors: List[str] = field(default_factory=list)
    communication_style: str = ""
    emotional_positioning: str = ""
    visual_preferences: List[str] = field(default_factory=list)
    typography_preferences: List[str] = field(default_factory=list)
    color_preferences: List[str] = field(default_factory=list)
    campaign_history: List[Dict[str, Any]] = field(default_factory=list)
    brand_memory: Dict[str, Any] = field(default_factory=dict)
    visual_memory: Dict[str, Any] = field(default_factory=dict)
    narrative_memory: Dict[str, Any] = field(default_factory=dict)
    governance_rules: Dict[str, Any] = field(default_factory=dict)
    stakeholder_notes: List[str] = field(default_factory=list)
    timelines: List[Dict[str, Any]] = field(default_factory=list)
    deliverables: List[str] = field(default_factory=list)
    active_projects: List[Dict[str, Any]] = field(default_factory=list)
    memory_embeddings: List[str] = field(default_factory=list)
    retrieval_indexes: List[str] = field(default_factory=list)


@dataclass(slots=True)
class ParagraphRecord:
    paragraph_id: str
    document_id: str
    ordinal: int
    text: str
    text_hash: str
    tags: List[str] = field(default_factory=list)
    section_hint: str = ""
    reinforcement_count: int = 1
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class DocumentRecord:
    document_id: str
    path: str
    file_type: str
    checksum: str
    created_at: str
    modified_at: str
    paragraph_count: int
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class IngestionReport:
    root: str
    discovered_files: int
    parsed_documents: int
    parsed_paragraphs: int
    repeated_paragraph_groups: int
    started_at: str
    completed_at: str
    errors: List[str] = field(default_factory=list)


@dataclass(slots=True)
class RetrievalResult:
    paragraph_id: str
    document_id: str
    score: float
    retrieval_mode: str
    evidence: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievalBundle:
    query: str
    required_sources: List[str]
    results_by_source: Dict[str, List[RetrievalResult]]
    missing_sources: List[str] = field(default_factory=list)

    @property
    def is_complete(self) -> bool:
        return not self.missing_sources


@dataclass(slots=True)
class DynamicBrandContext:
    context_id: str
    client_id: str
    task: str
    sector: str
    geography: str
    audience: str
    deliverable: str
    positioning_objective: str = ""
    communication_goal: str = ""
    campaign_objective: str = ""
    activated_agents: List[str] = field(default_factory=list)
    retrieval_bundle: Optional[RetrievalBundle] = None
    memory_updates: List[Dict[str, Any]] = field(default_factory=list)


@dataclass(slots=True)
class AgentTask:
    task_id: str
    agent_id: str
    stage: str
    objective: str
    constraints: List[str] = field(default_factory=list)
    required_inputs: List[str] = field(default_factory=list)
    expected_outputs: List[str] = field(default_factory=list)
    context_filters: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentResult:
    task_id: str
    agent_id: str
    stage: str
    status: str
    confidence: float
    outputs: Dict[str, Any] = field(default_factory=dict)
    validation_notes: List[str] = field(default_factory=list)


@dataclass(slots=True)
class ScoreDimension:
    id: str
    label: str
    weight: float
    threshold: float
    metrics: List[str]


@dataclass(slots=True)
class ScoreResult:
    profile_id: str
    total_score: float
    dimension_scores: Dict[str, float]
    failed_dimensions: List[str]
    recommendations: List[str]
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass(slots=True)
class GovernanceFinding:
    rule_id: str
    severity: str
    passed: bool
    detail: str
    recommendation: Optional[str] = None
