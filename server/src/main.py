from fastapi import FastAPI
from server.src.infrastructure.controllers.analysis.analysis_controller import (
    AnalysisController,
)
from server.src.application.usecases.analyse_useCase import AnalysisUseCase

analysis_controller = AnalysisController(AnalysisUseCase())

app = FastAPI(
    title="FastAPI",
    description="This API offers endpoints for interacting with an agent and performing various analysis operations on resumes.",
    version="0.1.0",
    docs_url="/",
)

app.include_router(analysis_controller.get_router())


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
