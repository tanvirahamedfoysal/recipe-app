from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core import get_db
from app.schema.v1.auth import UserLogin

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])


DbSession = Annotated[AsyncSession, Depends(get_db)]

@router.post("/login")
async def login(
    payload: Annotated[UserLogin, Depends()],
    db: DbSession,
):
    pass