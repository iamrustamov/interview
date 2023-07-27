from fastapi import APIRouter
from app.v1.endpoints.deposit import router as deposit_router

router = APIRouter()

router.include_router(deposit_router, prefix="/deposit")
