from pydantic import BaseModel


class OpportunityDocument(BaseModel):
    filename: str
    url: str
    file_type: str

    downloaded: bool = False

    local_path: str | None = None

    extracted_text: str | None = None


class OpportunityPackage(BaseModel):
    url: str

    title: str | None = None

    webpage_html: str | None = None
    
    webpage_text: str | None = None

    documents: list[OpportunityDocument] = []

    acquisition_complete: bool = False