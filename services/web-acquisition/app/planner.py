from pathlib import Path

from openai import OpenAI

from app.schemas import (
    SearchPlan,
    SearchPlanRequest,
)

client = OpenAI()

from app.utils.prompts import load_prompt

PROMPT = load_prompt(
    "search_planner.md"
)


def create_search_plan(request: SearchPlanRequest):

    response = client.responses.parse(
        model="gpt-5.5",
        instructions=PROMPT,
        input=f"""
Organisation:
{request.organisation}

Capability Profile:
{request.capability_profile}

Search Scope:
{request.search_scope}
""",
        text_format=SearchPlan,
    )

    return response.output_parsed