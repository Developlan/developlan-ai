from app.opportunity_models import (
    OpportunityBrief,
    OpportunityBriefSection,
    OpportunityIntelligence,
    OpportunityIntelligenceSection,
    OpportunityStatement,
)


BRIEF_SECTIONS = [
    ("opportunity_snapshot", "Opportunity Snapshot"),
    ("client", "Client"),
    ("services_scope", "Services / Scope"),
    ("key_dates", "Key Dates"),
    ("geography", "Geography"),
    ("submission_requirements", "Submission Requirements"),
    ("required_qualifications", "Required Qualifications"),
    ("required_experience", "Required Experience"),
    ("supporting_documents", "Supporting Documents"),
    ("investigation_confidence", "Investigation Confidence"),
]


INTELLIGENCE_SECTIONS = [
    ("executive_summary", "Executive Summary"),
    ("investigation_summary", "Investigation Summary"),
    ("evidence_summary", "Evidence Summary"),
    ("opportunity_characteristics", "Opportunity Characteristics"),
    ("risks_unknowns", "Risks & Unknowns"),
    ("supporting_evidence_inventory", "Supporting Evidence Inventory"),
    ("investigation_metadata", "Investigation Metadata"),
]


def render_opportunity_brief_markdown(
    brief: OpportunityBrief,
) -> str:

    sections = ["# Opportunity Brief"]

    for field_name, title in BRIEF_SECTIONS:
        sections.append(
            _render_brief_section(
                title,
                getattr(brief, field_name),
            )
        )

    return "\n\n".join(sections)


def render_opportunity_intelligence_markdown(
    intelligence: OpportunityIntelligence,
) -> str:

    sections = ["# Opportunity Intelligence Package"]

    for field_name, title in INTELLIGENCE_SECTIONS:
        sections.append(
            _render_intelligence_section(
                title,
                getattr(intelligence, field_name),
            )
        )

    return "\n\n".join(sections)


def _render_brief_section(
    title: str,
    section: OpportunityBriefSection,
) -> str:

    lines = [f"## {title}"]

    if section.facts:
        lines.extend(
            _format_statement(statement)
            for statement in section.facts
        )

    if section.unknowns:
        lines.append("")
        lines.append("Unknowns:")
        lines.extend(
            f"- {unknown}"
            for unknown in section.unknowns
        )

    if len(lines) == 1:
        lines.append("- Unknown")

    return "\n".join(lines)


def _render_intelligence_section(
    title: str,
    section: OpportunityIntelligenceSection,
) -> str:

    lines = [f"## {title}"]

    if section.factual_findings:
        lines.append("Factual Findings:")
        lines.extend(
            _format_statement(statement)
            for statement in section.factual_findings
        )

    if section.inferred_analysis:
        if len(lines) > 1:
            lines.append("")
        lines.append("Inferred Analysis:")
        lines.extend(
            _format_statement(statement)
            for statement in section.inferred_analysis
        )

    if section.unknowns:
        if len(lines) > 1:
            lines.append("")
        lines.append("Unknowns:")
        lines.extend(
            f"- {unknown}"
            for unknown in section.unknowns
        )

    if len(lines) == 1:
        lines.append("- Unknown")

    return "\n".join(lines)


def _format_statement(
    statement: OpportunityStatement,
) -> str:

    source = ""

    if statement.source:
        source = f" Source: {statement.source}"

    return f"- [{statement.basis}] {statement.text}{source}"
