import json

from openai import OpenAI

from app.investigation_orchestrator import Investigation
from app.opportunity_models import (
    OpportunityIntelligenceResult,
    OpportunityProfile,
)
from app.utils.prompts import load_prompt

client = OpenAI()

PROMPT = load_prompt(
    "opportunity_intelligence.md"
)

PROFILE_PROMPT = load_prompt(
    "opportunity_profiler.md"
)


def profile_opportunity(
    evidence: str,
) -> OpportunityProfile:

    response = client.responses.parse(
        model="gpt-5.5",
        instructions=PROFILE_PROMPT,
        input=evidence,
        text_format=OpportunityProfile,
    )

    return response.output_parsed


def generate_opportunity_outputs(
    investigation: Investigation,
    evidence_corpus: str,
) -> OpportunityIntelligenceResult:

    response = client.responses.parse(
        model="gpt-5.5",
        instructions=PROMPT,
        input=_build_generation_input(
            investigation,
            evidence_corpus,
        ),
        text_format=OpportunityIntelligenceResult,
    )

    return response.output_parsed


def _build_generation_input(
    investigation: Investigation,
    evidence_corpus: str,
) -> str:

    context = {
        "investigation": _investigation_context(investigation),
        "evidence_corpus": evidence_corpus,
    }

    return json.dumps(
        context,
        indent=2,
    )


def _investigation_context(
    investigation: Investigation,
) -> dict:

    opportunity_package = investigation.latest_opportunity_package()

    return {
        "id": investigation.id,
        "start_url": investigation.start_url,
        "status": investigation.status,
        "completion_reason": investigation.completion_reason,
        "opportunity_found": investigation.opportunity_found,
        "opportunity_url": investigation.opportunity_url,
        "final_page_type": investigation.final_page_type,
        "final_confidence": investigation.final_confidence,
        "evidence_complete": investigation.evidence_complete,
        "visited_urls": investigation.visited_urls,
        "candidate_actions_remaining": len(investigation.candidate_actions),
        "completed_actions": [
            action.model_dump(mode="json")
            for action in investigation.completed_actions
        ],
        "observations": [
            observation.model_dump(mode="json")
            for observation in investigation.observations
        ],
        "reasoning_history": [
            reasoning.model_dump(mode="json")
            for reasoning in investigation.reasoning_history
        ],
        "evidence": [
            {
                "url": evidence.url,
                "page_type": evidence.page_type,
                "summary": evidence.summary,
                "confidence": evidence.confidence,
                "evidence_complete": evidence.evidence_complete,
            }
            for evidence in investigation.evidence
        ],
        "supporting_documents": _document_inventory(opportunity_package),
    }


def _document_inventory(
    package,
) -> list[dict]:

    if package is None:
        return []

    return [
        {
            "filename": document.filename,
            "url": document.url,
            "file_type": document.file_type,
            "downloaded": document.downloaded,
            "local_path": document.local_path,
            "extraction_status": document.extraction_status,
            "extraction_note": document.extraction_note,
            "included_in_evidence_corpus": bool(document.extracted_text),
        }
        for document in package.documents
    ]
