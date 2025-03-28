from typing import Protocol
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from server.src.infrastructure.routes.perform_analysis.dependencies import get_analysis_use_case

router = APIRouter(tags=["Agent"])

class _Resume(BaseModel):
    text: str

class _IAnalysisUseCase(Protocol):
    async def perform_analysis(self, resume: _Resume) -> str: ...

@router.post("/perform-analysis")
async def perform_analysis(
    resume: _Resume,
    use_case: _IAnalysisUseCase = Depends(get_analysis_use_case)
) -> str:
    return await use_case.perform_analysis(resume)