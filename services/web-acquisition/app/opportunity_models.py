from typing import Literal

from pydantic import BaseModel, Field


InformationBasis = Literal[
    "factual",
    "inferred",
    "unknown",
]


class OpportunityStatement(BaseModel):
    text: str
    basis: InformationBasis
    source: str | None = None


class OpportunityBriefSection(BaseModel):
    facts: list[OpportunityStatement] = Field(default_factory=list)
    unknowns: list[str] = Field(default_factory=list)


class OpportunityBrief(BaseModel):
    opportunity_snapshot: OpportunityBriefSection
    client: OpportunityBriefSection
    services_scope: OpportunityBriefSection
    key_dates: OpportunityBriefSection
    geography: OpportunityBriefSection
    submission_requirements: OpportunityBriefSection
    required_qualifications: OpportunityBriefSection
    required_experience: OpportunityBriefSection
    supporting_documents: OpportunityBriefSection
    investigation_confidence: OpportunityBriefSection


class OpportunityIntelligenceSection(BaseModel):
    factual_findings: list[OpportunityStatement] = Field(default_factory=list)
    inferred_analysis: list[OpportunityStatement] = Field(default_factory=list)
    unknowns: list[str] = Field(default_factory=list)


class OpportunityIntelligence(BaseModel):
    executive_summary: OpportunityIntelligenceSection
    investigation_summary: OpportunityIntelligenceSection
    evidence_summary: OpportunityIntelligenceSection
    opportunity_characteristics: OpportunityIntelligenceSection
    risks_unknowns: OpportunityIntelligenceSection
    supporting_evidence_inventory: OpportunityIntelligenceSection
    investigation_metadata: OpportunityIntelligenceSection


class OpportunityIntelligenceResult(BaseModel):
    opportunity_brief: OpportunityBrief
    opportunity_intelligence: OpportunityIntelligence


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
