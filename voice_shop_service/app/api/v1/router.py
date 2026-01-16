from fastapi import APIRouter

from app.api.v1.routes import test

api_router = APIRouter()

api_router.include_router(test.router, prefix="/test", tags=["Test"])