from app.acquire import acquire_opportunity
from app.download import download_documents
from app.extract import extract_documents
from app.evidence import build_evidence_corpus
from app.opportunity_intelligence import profile_opportunity
from app.investigate_page import (
    extract_candidate_links,
    investigate_page,
)


def analyse_opportunity(url: str):

    #
    # Stage 1
    #

    package = acquire_opportunity(url)

    investigation = investigate_page(
        package.webpage_text or "",
        package.url,
        extract_candidate_links(
            package.url,
            package.webpage_html,
        ),
    )

    if investigation.page_type != "opportunity":

        return {
            "status": investigation.page_type,
            "package": package,
            "investigation": investigation,
        }

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
