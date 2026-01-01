from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_active_user, require_role
from app.enums.user_role import UserRole
from app.schemas.doctor import (CreateAvailabilityRequest, DoctorAvailability,
                                DoctorBase)
from app.services.doctor_service import DoctorService

router = APIRouter()


@router.get("/", response_model=List[DoctorBase])
async def list_doctors(
    db: AsyncSession = Depends(get_db), 
    current_user = Depends(get_current_active_user)
):
    service = DoctorService(db)
    return await service.list_doctors()


@router.get("/{doctor_id}/availability", response_model=List[DoctorAvailability])
async def doctor_availability(
    doctor_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    service = DoctorService(db)
    availability = await service.get_availability(doctor_id)

    if not availability:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No availability found for this doctor",
        )

    return availability


@require_role(UserRole.DOCTOR)
@router.post("/availability", response_model=DoctorAvailability)
async def add_availability(
    slot: CreateAvailabilityRequest,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):

    service = DoctorService(db)
    try:
        return await service.add_availability(current_user.id, slot)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )