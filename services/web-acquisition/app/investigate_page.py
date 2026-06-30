import json
from typing import Literal
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from openai import OpenAI
from pydantic import BaseModel, Field

from app.utils.prompts import load_prompt


client = OpenAI()

PROMPT = load_prompt(
    "page_investigation.md"
)


class CandidateLink(BaseModel):
    link_text: str
    url: str


class InvestigationAction(BaseModel):
    link_text: str
    url: str | None
    priority: Literal["high", "medium", "low"]
    reasoning: str


class IgnoredLink(BaseModel):
    link_text: str
    url: str | None
    reason: str


class PageInvestigation(BaseModel):
    page_type: Literal[
        "portal",
        "listing",
        "opportunity",
        "login",
        "informational",
        "error",
        "unknown",
    ]
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str
    reasoning: str
    next_actions: list[InvestigationAction]
    ignored_links: list[IgnoredLink]
    evidence_complete: bool


def extract_candidate_links(
    page_url: str,
    page_html: str | None,
) -> list[CandidateLink]:

    soup = BeautifulSoup(
        page_html or "",
        "lxml",
    )

    links = []
    seen = set()

    for anchor in soup.find_all("a", href=True):

        link_text = anchor.get_text(
            " ",
            strip=True,
        )

        if not link_text:
            continue

        url = urljoin(
            page_url,
            anchor["href"],
        )

        key = (
            link_text,
            url,
        )

        if key in seen:
            continue

        seen.add(key)

        links.append(
            CandidateLink(
                link_text=link_text,
                url=url,
            )
        )

    return links


def investigate_page(
    rendered_page_text: str,
    page_url: str,
    candidate_links: list[CandidateLink] | None = None,
) -> PageInvestigation:

    links = [
        link.model_dump()
        for link in candidate_links or []
    ]

    response = client.responses.parse(
        model="gpt-5.5",
        instructions=PROMPT,
        input=f"""
Page URL:
{page_url}

Candidate links:
{json.dumps(links, indent=2)}

Rendered page text:
{rendered_page_text}
""",
        text_format=PageInvestigation,
    )

    return response.output_parsed
