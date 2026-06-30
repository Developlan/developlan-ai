from bs4 import BeautifulSoup


def detect_page_type(html: str) -> str:

    text = BeautifulSoup(
        html,
        "lxml",
    ).get_text(" ", strip=True).lower()

    portal_terms = [
        "partner portal",
        "about us",
        "learning platform",
        "news centre",
        "register",
        "sign in",
    ]

    listing_terms = [
        "partnership opportunities",
        "current opportunities",
        "open opportunities",
        "funding opportunities",
        "browse opportunities",
        "opportunity listings",
    ]

    opportunity_terms = [
        "terms of reference",
        "request for proposal",
        "request for proposals",
        "request for quotation",
        "consultancy",
        "vacancy",
        "procurement",
        "scope of work",
        "submission deadline",
        "closing date",
        "reference number",
        "tor",
    ]

    login_terms = [
        "login",
        "sign in",
        "log in",
        "username",
        "password",
    ]

    login_score = sum(
        term in text
        for term in login_terms
    )

    listing_score = sum(
        term in text
        for term in listing_terms
    )

    opportunity_score = sum(
        term in text
        for term in opportunity_terms
    )

    portal_score = sum(
        term in text
        for term in portal_terms
    )

    #
    # Most specific first
    #

    if opportunity_score >= 2:
        return "opportunity"

    if listing_score >= 1:
        return "listing"

    if login_score >= 3:
        return "login"

    if portal_score >= 2:
        return "portal"

    return "unknown"