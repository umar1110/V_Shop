from fastapi import APIRouter

from app.api.v1.routes import test, order_routes

api_router = APIRouter()

api_router.include_router(test.router, prefix="/test", tags=["Test"])
api_router.include_router(order_routes.router, prefix="/orders", tags=["Orders"])