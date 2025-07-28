from fastapi import APIRouter
from src.models.upload import Upload

router = APIRouter(prefix="/uploads", tags=["Uploads"])

@router.get("/count")
async def upload_count():
    count = await Upload.all().count()
    return {"count": count}