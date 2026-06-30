from openai import OpenAI
from tavily import TavilyClient

from app.settings import settings

openai_client = OpenAI(
    api_key=settings.openai_api_key
)

tavily_client = TavilyClient(
    api_key=settings.tavily_api_key
)