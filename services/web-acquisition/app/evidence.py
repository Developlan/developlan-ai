from app.models import OpportunityPackage


def build_evidence_corpus(
    package: OpportunityPackage,
) -> str:

    sections = []

    if package.webpage_text:

        sections.append(
            "# Opportunity Web Page\n\n"
            + package.webpage_text
        )

    for document in package.documents:

        if not document.extracted_text:
            continue

        sections.append(

            f"# Document: {document.filename}\n\n"

            + document.extracted_text

        )

    return "\n\n".join(sections)