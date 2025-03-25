from fastapi import FastAPI
from infrastructure.controllers.user.user_controller import router as user_router

app = FastAPI(
    title="FastAPI",
    description="This API provides endpoints for interacting with an agent, "
    "allowing users to perform various operations.",
    version="0.1.0",
    docs_url="/",
)
app.include_router(user_router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
