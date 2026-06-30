from bs4 import BeautifulSoup

from app.discovery_models import (
    DiscoveryResult,
    OpportunityCandidate,
)


def discover_from_listing(
    url: str,
    html: str,
) -> DiscoveryResult:

    soup = BeautifulSoup(
        html,
        "lxml",
    )

    opportunities = []

    for link in soup.find_all("a", href=True):

        text = link.get_text(" ", strip=True)

        if len(text) < 10:
            continue

        href = link.get("href")

        opportunities.append(

            OpportunityCandidate(
                title=text,
                url=href,
                source="listing",
            )

        )

    return DiscoveryResult(
        page_type="listing",
        opportunities=opportunities,
    )