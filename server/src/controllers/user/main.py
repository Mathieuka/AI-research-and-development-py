from typing import Union
from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def read_users():
    return {"Hello": "User"}


@router.get("/users/{user_id}")
async def read_user(user_id: int, q: Union[str, None] = None):
    return {"item_id": user_id, "q": q}
