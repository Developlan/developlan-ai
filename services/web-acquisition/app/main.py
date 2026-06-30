from fastapi import FastAPI

from app.schemas import (
    SearchPlan,
    SearchPlanRequest,
)

from app.search_executor import execute_search_plan
from app.schemas import OpportunitySearchResult

from app.planner import create_search_plan

from pydantic import BaseModel

from app.acquire import acquire_opportunity
from app.models import OpportunityPackage

from app.download import download_documents

from app.analyse import analyse_opportunity

app = FastAPI(
    title="Developlan Web Acquisition",
    version="0.1",
)

class AcquireRequest(BaseModel):
    url: str

class AnalyseRequest(BaseModel):
    url: str

@app.post("/plan", response_model=SearchPlan)
def plan(
    request: SearchPlanRequest,
):

    return create_search_plan(request)

@app.post("/acquire", response_model=OpportunityPackage)
def acquire(request: AcquireRequest):

    return acquire_opportunity(request.url)

@app.post("/download", response_model=OpportunityPackage)
def download(request: AcquireRequest):

    package = acquire_opportunity(request.url)

    return download_documents(package)

@app.post("/discover", response_model=OpportunitySearchResult)
def discover(
    request: SearchPlanRequest,
):

    plan = create_search_plan(request)

    return execute_search_plan(plan)

@app.post("/analyse")
def analyse(request: AnalyseRequest):

    return analyse_opportunity(
        request.url
    )