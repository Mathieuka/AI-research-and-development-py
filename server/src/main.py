from fastapi import FastAPI
from controllers.user.main import router as user_router

app = FastAPI()
app.include_router(user_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
