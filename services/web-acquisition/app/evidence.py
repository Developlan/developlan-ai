from app.models import OpportunityPackage


def build_evidence_corpus(
    package: OpportunityPackage,
) -> str:

    sections = []

    sections.append(
        "# Opportunity Web Page\n\n"
        + (package.webpage_text or "No webpage text was captured.")
    )

    for document in package.documents:

        if not document.extracted_text:
            continue

        sections.append(

            f"# Document: {document.filename}\n\n"

            + document.extracted_text

        )

    document_metadata = []

    for document in package.documents:

        if document.extracted_text:
            continue

        status = document.extraction_status

        if not status and not document.downloaded:
            status = "not downloaded"

        if not status:
            continue

        metadata = [
            f"filename: {document.filename}",
            f"url: {document.url}",
            f"file_type: {document.file_type}",
            f"status: {status}",
        ]

        if document.extraction_note:
            metadata.append(f"note: {document.extraction_note}")

        document_metadata.append("- " + "; ".join(metadata))

    if document_metadata:

        sections.append(
            "# Document Acquisition Metadata\n\n"
            + "\n".join(document_metadata)
        )

    return "\n\n".join(sections)
