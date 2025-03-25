# from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Resume(BaseModel):
    text: str


@router.get("/hello", tags=["Agent"])
async def hello():
    return "Hello World"


@router.post("/analyse", tags=["Agent"])
async def analyse(resume: Resume):
    return {"response": resume.text}
