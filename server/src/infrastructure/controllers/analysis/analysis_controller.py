from fastapi import APIRouter
from typing import Protocol
from pydantic import BaseModel


class Resume(BaseModel):
    resume: str


class AnalysisUseCase(Protocol):
    def perform_analysis(self, resume: str) -> str: ...


class AnalysisController:

    def __init__(self, analysis_use_case: AnalysisUseCase):
        self.analysis_use_case = analysis_use_case
        self.router = APIRouter(tags=["Agent"])

        # Add routes
        self.router.add_api_route("/hello", self.hello, methods=["GET"])
        self.router.add_api_route(
            "/perform-analysis", self.perform_analysis, methods=["POST"]
        )

    async def hello(self):
        return "Hello World"

    async def perform_analysis(self, payload: Resume) -> str:
        return self.analysis_use_case.perform_analysis(payload.resume)

    def get_router(self) -> APIRouter:
        return self.router
