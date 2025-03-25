# from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Question(BaseModel):
    text: str


@router.get("/hello", tags=["Agent"])
async def hello():
    return "Hello World"


@router.post("/answer", tags=["Agent"])
async def ask(question: Question):
    return {"response": question.text}


# @router.get("/calculate/{payload}")
# async def read_user(payload: str, q: Union[str, None] = None):
#     return {"payload": payload, "q": q}
