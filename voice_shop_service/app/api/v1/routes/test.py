from fastapi import APIRouter
from app.config.settings import settings
router = APIRouter()

@router.get("/")
def read_test():
    
    return {
        "message": "This is a test endpoint", 
        "app_name": settings.APP_NAME,
        "environment": settings.ENV
    }