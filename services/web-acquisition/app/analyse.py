from app.download import download_documents
from app.extract import extract_documents
from app.evidence import build_evidence_corpus
from app.investigation_orchestrator import InvestigationOrchestrator
from app.opportunity_intelligence import profile_opportunity


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

    profile = profile_opportunity(
        evidence
    )

    return {
        "package": package,
        "investigation": investigation,
        "profile": profile,
    }
