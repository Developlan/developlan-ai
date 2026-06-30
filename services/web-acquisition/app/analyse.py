from app.acquire import acquire_opportunity
from app.download import download_documents
from app.extract import extract_documents
from app.evidence import build_evidence_corpus
from app.opportunity_intelligence import profile_opportunity
from app.opportunity_detector import detect_page_type


def analyse_opportunity(url: str):

    #
    # Stage 1
    #

    package = acquire_opportunity(url)

    page_type = detect_page_type(
        package.webpage_text or ""
    )

    if page_type == "portal":

        from app.discover_from_portal import discover_from_portal
        from app.navigation_intelligence import rank_navigation

        discovery = discover_from_portal(
            package.url,
            package.webpage_html or "",
        )

        discovery.opportunities = rank_navigation(
            discovery.opportunities
        )

        return discovery

    if page_type != "opportunity":

        return {
            "status": page_type,
            "package": package,
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
        "profile": profile,
    }