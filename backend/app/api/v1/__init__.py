from fastapi import APIRouter
from .auth import router as auth_router
from .food import router as food_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(food_router)

__all__ = ["router"]
