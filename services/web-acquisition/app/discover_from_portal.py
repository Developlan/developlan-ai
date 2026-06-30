from bs4 import BeautifulSoup

from app.discovery_models import (
    OpportunityCandidate,
    DiscoveryResult,
)


def discover_from_portal(
    url: str,
    html: str,
) -> DiscoveryResult:

    soup = BeautifulSoup(
        html,
        "lxml",
    )

    candidates = []

    for link in soup.find_all("a", href=True):

        href = link["href"]
        text = link.get_text(" ", strip=True)

        if len(text) < 5:
            continue

        if href.startswith("/"):
            href = url.rstrip("/") + href

        candidates.append(

            OpportunityCandidate(
                title=text,
                url=href,
                source="portal",
            )

        )

    return DiscoveryResult(
        page_type="portal",
        opportunities=candidates,
    )