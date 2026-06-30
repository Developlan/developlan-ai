from tavily import TavilyClient

from app.schemas import (
    Opportunity,
    OpportunitySearchResult,
    SearchPlan,
)

client = TavilyClient()


def execute_search_plan(
    plan: SearchPlan,
) -> OpportunitySearchResult:

    opportunities = []

    for query in plan.queries[:10]:

        result = client.search(
            query=query,
            max_results=5,
        )

        for item in result.get("results", []):

            opportunities.append(
                Opportunity(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    source=item.get("url", ""),
                    snippet=item.get("content", ""),
                )
            )

    return OpportunitySearchResult(
        opportunities=opportunities
    )