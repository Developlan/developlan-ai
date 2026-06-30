from urllib.parse import urljoin

from bs4 import BeautifulSoup

from app.models import OpportunityDocument, OpportunityPackage

from app.session_manager import get_page

DOCUMENT_HINTS = [
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    "tor",
    "terms",
    "guidelines",
    "annex",
    "rfp",
    "itt",
    "eoi",
]


def acquire_opportunity(url: str) -> OpportunityPackage:

    page = get_page("unpartner")

    page.goto(
        url,
        wait_until="networkidle",
        timeout=60000,
    )

    html = page.content()

    soup = BeautifulSoup(html, "lxml")

    package = OpportunityPackage(
        url=url,
        title=soup.title.string.strip() if soup.title and soup.title.string else None,
        webpage_html=html,
        webpage_text=soup.get_text(" ", strip=True),
    )

    for link in soup.find_all("a", href=True):

        href = urljoin(url, link["href"])

        lower = href.lower()

        if any(hint in lower for hint in DOCUMENT_HINTS):

            filename = href.split("/")[-1]

            if "." in filename:
                filetype = filename.rsplit(".", 1)[1]
            else:
                filetype = "html"

            package.documents.append(
                OpportunityDocument(
                    filename=filename,
                    url=href,
                    file_type=filetype,
                )
            )

    return package