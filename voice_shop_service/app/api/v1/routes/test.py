from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def read_test():
    return {"message": "This is a test endpoint"}