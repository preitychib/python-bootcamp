from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", summary="Health check")
async def health_check():
    return {"status": "ok", "project": settings.PROJECT_NAME}
