from openai import OpenAI

from app.opportunity_models import OpportunityProfile
from app.utils.prompts import load_prompt

client = OpenAI()

PROMPT = load_prompt(
    "opportunity_intelligence.md"
)


def profile_opportunity(
    evidence: str,
) -> OpportunityProfile:

    response = client.responses.parse(
        model="gpt-5.5",
        instructions=PROMPT,
        input=evidence,
        text_format=OpportunityProfile,
    )

    return response.output_parsed