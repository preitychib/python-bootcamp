from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user, require_role
from app.enums.user_role import UserRole
from app.schemas.appointment import (AppointmentResponse,
                                     CreateAppointmentRequest)
from app.services.appointment import AppointmentService

router = APIRouter()

@require_role(UserRole.PATIENT)
@router.post("/", response_model=AppointmentResponse)
async def create_appointment(
    appointment: CreateAppointmentRequest,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    service = AppointmentService(db)
    try:
        return await service.create_appointment(current_user.id, appointment)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
