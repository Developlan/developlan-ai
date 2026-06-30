from pydantic import BaseModel


class SearchPlanRequest(BaseModel):
    organisation: str
    capability_profile: str
    search_scope: str = "global"


class SearchPlan(BaseModel):
    objective: str
    sources: list[str]
    geographies: list[str]
    sectors: list[str]
    queries: list[str]


class Opportunity(BaseModel):
    title: str
    url: str
    source: str
    snippet: str


class OpportunitySearchResult(BaseModel):
    opportunities: list[Opportunity]