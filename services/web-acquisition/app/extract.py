from pathlib import Path

import fitz
from docx import Document
from openpyxl import load_workbook

from app.models import OpportunityPackage


def extract_documents(
    package: OpportunityPackage,
) -> OpportunityPackage:

    for document in package.documents:

        if not document.downloaded:
            continue

        path = Path(document.local_path)

        suffix = path.suffix.lower()

        try:

            if suffix == ".pdf":

                document.extracted_text = extract_pdf(path)

            elif suffix == ".docx":

                document.extracted_text = extract_docx(path)

            elif suffix == ".xlsx":

                document.extracted_text = extract_xlsx(path)

            elif suffix in [".txt", ".html", ".htm"]:

                document.extracted_text = path.read_text(
                    errors="ignore"
                )

            else:

                document.extracted_text = None

        except Exception as e:

            document.extracted_text = str(e)

    return package


def extract_pdf(path: Path) -> str:

    doc = fitz.open(path)

    pages = []

    for page in doc:

        pages.append(page.get_text())

    doc.close()

    return "\n".join(pages)


def extract_docx(path: Path) -> str:

    doc = Document(path)

    text = []

    for paragraph in doc.paragraphs:

        if paragraph.text.strip():

            text.append(paragraph.text)

    for table in doc.tables:

        for row in table.rows:

            cells = [
                cell.text.strip()
                for cell in row.cells
            ]

            text.append(" | ".join(cells))

    return "\n".join(text)


def extract_xlsx(path: Path) -> str:

    workbook = load_workbook(
        path,
        data_only=True,
    )

    output = []

    for sheet in workbook.worksheets:

        output.append(f"Worksheet: {sheet.title}")

        for row in sheet.iter_rows(values_only=True):

            values = [
                str(v)
                for v in row
                if v is not None
            ]

            if values:

                output.append(" | ".join(values))

    return "\n".join(output)