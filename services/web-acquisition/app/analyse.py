from app.download import download_documents
from app.extract import extract_documents
from app.evidence import build_evidence_corpus
from app.investigation_orchestrator import InvestigationOrchestrator
from app.opportunity_intelligence import generate_opportunity_outputs
from app.opportunity_renderers import (
    render_opportunity_brief_markdown,
    render_opportunity_intelligence_markdown,
)


def analyse_opportunity(url: str):

    #
    # Stage 1
    #

    investigation = InvestigationOrchestrator().run(url)
    package = investigation.latest_opportunity_package()

    if package is None:

        return investigation

    #
    # Stage 2
    #

    package = download_documents(package)

    #
    # Stage 3
    #

    package = extract_documents(package)

    #
    # Stage 4
    #

    evidence = build_evidence_corpus(package)

    #
    # Stage 5
    #

    outputs = generate_opportunity_outputs(
        investigation,
        evidence,
    )

    return {
        "investigation": investigation,
        "opportunity_brief": outputs.opportunity_brief,
        "opportunity_intelligence": outputs.opportunity_intelligence,
        "opportunity_package": package,
        "evidence_corpus": evidence,
        "opportunity_brief_markdown": render_opportunity_brief_markdown(
            outputs.opportunity_brief
        ),
        "opportunity_intelligence_markdown": render_opportunity_intelligence_markdown(
            outputs.opportunity_intelligence
        ),
    }
