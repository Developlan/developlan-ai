from pathlib import Path
from urllib.parse import urlparse

import httpx

from app.models import OpportunityPackage


DOWNLOAD_ROOT = Path("/tmp/opportunities")


def download_documents(package: OpportunityPackage) -> OpportunityPackage:

    opportunity_dir = DOWNLOAD_ROOT / safe_folder_name(package.title or "opportunity")
    opportunity_dir.mkdir(parents=True, exist_ok=True)

    for document in package.documents:

        try:

            response = httpx.get(
                document.url,
                timeout=120,
                follow_redirects=True,
            )

            response.raise_for_status()

            filename = document.filename

            if not filename:
                filename = Path(urlparse(document.url).path).name

            local_file = opportunity_dir / filename

            local_file.write_bytes(response.content)

            document.downloaded = True
            document.local_path = str(local_file)

        except Exception:
            document.downloaded = False

    package.acquisition_complete = True

    return package


def safe_folder_name(name: str) -> str:

    return "".join(
        c if c.isalnum() or c in "-_ " else "_"
        for c in name
    ).strip()