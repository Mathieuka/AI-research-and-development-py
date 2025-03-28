from fastapi import FastAPI
from server.src.infrastructure.routes.perform_analysis.perform_analysis import router

app = FastAPI(
    title="FastAPI",
    description="This API offers endpoints for interacting with an agent and performing various analysis operations on resumes.",
    version="0.1.0",
    docs_url="/",
)

app.include_router(router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
