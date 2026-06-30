import json
from datetime import datetime, timezone
from typing import Literal
from urllib.parse import urldefrag
from uuid import uuid4

from pydantic import BaseModel, Field

from app.acquire import acquire_opportunity
from app.investigate_page import (
    extract_candidate_links,
    investigate_page,
)
from app.models import OpportunityPackage


InvestigationPriority = Literal[
    "high",
    "medium",
    "low",
]

InvestigationStatus = Literal[
    "pending",
    "running",
    "evidence_complete",
    "max_pages_reached",
    "max_depth_reached",
    "no_candidate_actions",
]

HypothesisStatus = Literal[
    "active",
    "confirmed",
    "rejected",
]


class QueuedInvestigationAction(BaseModel):
    link_text: str
    url: str
    priority: InvestigationPriority
    reasoning: str
    source_url: str | None = None
    depth: int = 0


class CompletedInvestigationAction(QueuedInvestigationAction):
    page_type: str
    confidence: float = Field(ge=0.0, le=1.0)
    evidence_complete: bool


class InvestigationEvidence(BaseModel):
    url: str
    page_type: str
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)
    evidence_complete: bool
    package: OpportunityPackage


class InvestigationReasoning(BaseModel):
    url: str
    reasoning: str


class Observation(BaseModel):
    source_url: str
    page_type: str
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Hypothesis(BaseModel):
    statement: str
    confidence: float = Field(ge=0.0, le=1.0)
    status: HypothesisStatus = "active"


class Investigation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    start_url: str
    status: InvestigationStatus = "pending"
    visited_urls: list[str] = Field(default_factory=list)
    candidate_actions: list[QueuedInvestigationAction] = Field(default_factory=list)
    completed_actions: list[CompletedInvestigationAction] = Field(default_factory=list)
    evidence: list[InvestigationEvidence] = Field(default_factory=list)
    observations: list[Observation] = Field(default_factory=list)
    hypotheses: list[Hypothesis] = Field(default_factory=list)
    rejected_hypotheses: list[Hypothesis] = Field(default_factory=list)
    reasoning_history: list[InvestigationReasoning] = Field(default_factory=list)
    confidence: float = Field(default=0.0, ge=0.0, le=1.0)
    evidence_complete: bool = False

    def latest_opportunity_package(self) -> OpportunityPackage | None:

        for evidence in reversed(self.evidence):

            if evidence.page_type == "opportunity":
                return evidence.package

        return None

    def latest_package(self) -> OpportunityPackage | None:

        if not self.evidence:
            return None

        return self.evidence[-1].package

    def memory_summary(
        self,
        max_items: int = 5,
    ) -> str:

        active_hypotheses = [
            hypothesis
            for hypothesis in self.hypotheses
            if hypothesis.status == "active"
        ]

        memory = {
            "observations": [
                {
                    "source_url": observation.source_url,
                    "page_type": observation.page_type,
                    "summary": self._clip(observation.summary),
                    "confidence": observation.confidence,
                    "timestamp": observation.timestamp.isoformat(),
                }
                for observation in self.observations[-max_items:]
            ],
            "active_hypotheses": [
                {
                    "statement": self._clip(hypothesis.statement),
                    "confidence": hypothesis.confidence,
                    "status": hypothesis.status,
                }
                for hypothesis in active_hypotheses[-max_items:]
            ],
            "reasoning_history": [
                {
                    "url": reasoning.url,
                    "reasoning": self._clip(reasoning.reasoning),
                }
                for reasoning in self.reasoning_history[-max_items:]
            ],
        }

        if not any(memory.values()):
            return "No prior investigation memory."

        return json.dumps(
            memory,
            indent=2,
        )

    def _clip(
        self,
        value: str,
        max_chars: int = 700,
    ) -> str:

        if len(value) <= max_chars:
            return value

        return value[:max_chars].rstrip() + "..."


class InvestigationOrchestrator:
    def __init__(
        self,
        max_pages: int = 10,
        max_depth: int = 3,
    ):
        self.max_pages = max_pages
        self.max_depth = max_depth

    def run(
        self,
        start_url: str,
    ) -> Investigation:

        investigation = Investigation(
            start_url=start_url,
            status="running",
            candidate_actions=[
                QueuedInvestigationAction(
                    link_text="Start URL",
                    url=start_url,
                    priority="high",
                    reasoning="Initial investigation URL.",
                    depth=0,
                )
            ],
        )

        max_depth_reached = False

        while investigation.candidate_actions:

            if len(investigation.visited_urls) >= self.max_pages:
                investigation.status = "max_pages_reached"
                return investigation

            action = self._pop_next_action(investigation)
            url = self._normalise_url(action.url)

            if url in investigation.visited_urls:
                continue

            if action.depth > self.max_depth:
                max_depth_reached = True
                continue

            package = acquire_opportunity(url)
            page_url = self._normalise_url(package.url)

            if page_url in investigation.visited_urls:
                continue

            page_investigation = investigate_page(
                package.webpage_text or "",
                package.url,
                extract_candidate_links(
                    package.url,
                    package.webpage_html,
                ),
                investigation.memory_summary(),
            )

            investigation.visited_urls.append(page_url)
            investigation.confidence = page_investigation.confidence
            investigation.evidence_complete = page_investigation.evidence_complete

            self._record_memory(
                investigation,
                package.url,
                page_investigation,
            )

            investigation.evidence.append(
                InvestigationEvidence(
                    url=package.url,
                    page_type=page_investigation.page_type,
                    summary=page_investigation.summary,
                    confidence=page_investigation.confidence,
                    evidence_complete=page_investigation.evidence_complete,
                    package=package,
                )
            )

            investigation.completed_actions.append(
                CompletedInvestigationAction(
                    link_text=action.link_text,
                    url=action.url,
                    priority=action.priority,
                    reasoning=action.reasoning,
                    source_url=action.source_url,
                    depth=action.depth,
                    page_type=page_investigation.page_type,
                    confidence=page_investigation.confidence,
                    evidence_complete=page_investigation.evidence_complete,
                )
            )

            if page_investigation.evidence_complete:
                investigation.status = "evidence_complete"
                return investigation

            if len(investigation.visited_urls) >= self.max_pages:
                investigation.status = "max_pages_reached"
                return investigation

            next_depth = action.depth + 1

            if next_depth > self.max_depth:
                if page_investigation.next_actions:
                    max_depth_reached = True
                continue

            self._queue_actions(
                investigation,
                source_url=package.url,
                depth=next_depth,
                visited_urls=set(investigation.visited_urls),
                existing_urls=self._candidate_urls(investigation),
                actions=page_investigation.next_actions,
            )

        if max_depth_reached:
            investigation.status = "max_depth_reached"
        else:
            investigation.status = "no_candidate_actions"

        return investigation

    def _queue_actions(
        self,
        investigation: Investigation,
        source_url: str,
        depth: int,
        visited_urls: set[str],
        existing_urls: set[str],
        actions,
    ) -> None:

        for action in actions:

            if not action.url:
                continue

            url = self._normalise_url(action.url)

            if url in visited_urls or url in existing_urls:
                continue

            investigation.candidate_actions.append(
                QueuedInvestigationAction(
                    link_text=action.link_text,
                    url=url,
                    priority=action.priority,
                    reasoning=action.reasoning,
                    source_url=source_url,
                    depth=depth,
                )
            )

            existing_urls.add(url)

    def _record_memory(
        self,
        investigation: Investigation,
        source_url: str,
        page_investigation,
    ) -> None:

        investigation.observations.append(
            Observation(
                source_url=source_url,
                page_type=page_investigation.page_type,
                summary=page_investigation.summary,
                confidence=page_investigation.confidence,
            )
        )

        investigation.reasoning_history.append(
            InvestigationReasoning(
                url=source_url,
                reasoning=page_investigation.reasoning,
            )
        )

        if (
            page_investigation.evidence_complete
            and page_investigation.page_type == "opportunity"
        ):
            investigation.hypotheses.append(
                Hypothesis(
                    statement=f"{source_url} contains sufficient opportunity evidence.",
                    confidence=page_investigation.confidence,
                    status="confirmed",
                )
            )
            return

        if page_investigation.evidence_complete:
            investigation.rejected_hypotheses.append(
                Hypothesis(
                    statement=f"{source_url} does not provide a viable opportunity path.",
                    confidence=page_investigation.confidence,
                    status="rejected",
                )
            )
            return

        if page_investigation.next_actions:
            investigation.hypotheses.append(
                Hypothesis(
                    statement=f"{source_url} may lead to useful opportunity evidence.",
                    confidence=page_investigation.confidence,
                    status="active",
                )
            )
            return

        investigation.rejected_hypotheses.append(
            Hypothesis(
                statement=f"{source_url} produced no actionable investigation links.",
                confidence=page_investigation.confidence,
                status="rejected",
            )
        )

    def _pop_next_action(
        self,
        investigation: Investigation,
    ) -> QueuedInvestigationAction:

        priorities = {
            "high": 0,
            "medium": 1,
            "low": 2,
        }

        best_index = min(
            range(len(investigation.candidate_actions)),
            key=lambda index: (
                priorities[investigation.candidate_actions[index].priority],
                investigation.candidate_actions[index].depth,
                index,
            ),
        )

        return investigation.candidate_actions.pop(best_index)

    def _candidate_urls(
        self,
        investigation: Investigation,
    ) -> set[str]:

        return {
            self._normalise_url(action.url)
            for action in investigation.candidate_actions
        }

    def _normalise_url(
        self,
        url: str,
    ) -> str:

        return urldefrag(url).url
