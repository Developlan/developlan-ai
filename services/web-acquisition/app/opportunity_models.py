from pydantic import BaseModel


class OpportunityProfile(BaseModel):

    # Overview
    title: str
    donor: str | None = None
    funding_mechanism: str | None = None
    opportunity_type: str | None = None
    geography: list[str] = []
    programme_duration: str | None = None
    estimated_value: str | None = None
    closing_date: str | None = None

    # Strategic understanding
    strategic_context: str
    donor_priorities: list[str] = []

    # Technical understanding
    sectors: list[str] = []
    thematic_areas: list[str] = []
    services_required: list[str] = []
    expected_outputs: list[str] = []
    expected_outcomes: list[str] = []
    methodologies: list[str] = []

    # Delivery
    implementation_model: str | None = None
    consortium_requirements: str | None = None
    localisation_requirements: str | None = None
    staffing_requirements: list[str] = []
    reporting_requirements: list[str] = []
    mel_requirements: list[str] = []
    financial_requirements: list[str] = []

    # Eligibility
    mandatory: list[str] = []
    preferred: list[str] = []
    advantageous: list[str] = []
    unknown: list[str] = []

    # Evaluation
    evaluation_criteria: list[str] = []

    # Risks
    risks: list[str] = []

    # Questions
    unknown_questions: list[str] = []

    # Executive assessment
    executive_summary: str