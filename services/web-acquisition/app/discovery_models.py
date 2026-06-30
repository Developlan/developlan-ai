from pydantic import BaseModel


class OpportunityCandidate(BaseModel):
    title: str
    url: str
    source: str | None = None
    donor: str | None = None
    closing_date: str | None = None


class DiscoveryResult(BaseModel):
    page_type: str
    opportunities: list[OpportunityCandidate] = []
