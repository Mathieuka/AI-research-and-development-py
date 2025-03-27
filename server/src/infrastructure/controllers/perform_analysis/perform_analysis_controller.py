from fastapi import APIRouter
from typing import Protocol
from server.src.infrastructure.agent.client import Agent
from pydantic import BaseModel

class Resume(BaseModel):
    resume: str

class IAnalysisUseCase(Protocol):
    async def perform_analysis(self, resume: Resume, agent: Agent) -> str: ...


class PerformAnalysisController:

    def __init__(self, perform_analysis_use_case: IAnalysisUseCase, agent: Agent):
        self.perform_analysis_use_case = perform_analysis_use_case
        self.router = APIRouter(tags=["Agent"])
        self.agent = agent

        # Add routes
        self.router.add_api_route("/hello", self.hello, methods=["GET"])
        self.router.add_api_route(
            "/perform-analysis", self.perform_analysis, methods=["POST"]
        )


    async def hello(self):
        return "Hello World"

    async def perform_analysis(self, resume: Resume | None) -> str:
        if resume is None:
            resume = Resume(resume="Default CV")

        return await self.perform_analysis_use_case.perform_analysis(resume, self.agent)

    def get_router(self) -> APIRouter:
        return self.router
