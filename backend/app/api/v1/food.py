from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
router = APIRouter(prefix="/api/v1/food", tags=["Food"])


GetToken = Annotated[str, Depends(oauth2_scheme)]


@router.get("/")
async def get_all_food(
    token: str = GetToken,
):
    pass

@router.post("/toggle-favourite")
async def toggle_favourite():
    pass