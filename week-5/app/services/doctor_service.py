from datetime import datetime
from typing import List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.availability import Availability
from app.repositories.user_repo import UserRepository
from app.schemas.doctor import (CreateAvailabilityRequest, DoctorAvailability,
                                DoctorBase)


class DoctorService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def list_doctors(self) -> List[DoctorBase]:
        doctors = await self.user_repo.get_all_doctors()
        return [DoctorBase(
            id=d.id,
            name=d.name,
            email=d.email,
            role=d.role
        ) for d in doctors]

    async def get_availability(self, doctor_id) -> List[DoctorAvailability]:
        availability = await self.user_repo.get_doctor_availability(doctor_id)

        formatted = []
        for a in availability:
            formatted.append(
                DoctorAvailability(
                    date=a.start_time.strftime("%d-%m-%Y"),
                    start_time=a.start_time.strftime("%H:%M"),
                    end_time=a.end_time.strftime("%H:%M")
                )
            )

        return formatted


    async def add_availability(self, doctor_id: UUID, slot: CreateAvailabilityRequest) -> DoctorAvailability:
   
        start_dt = datetime.strptime(f"{slot.date} {slot.start_time}", "%d-%m-%Y %H:%M")
        end_dt = datetime.strptime(f"{slot.date} {slot.end_time}", "%d-%m-%Y %H:%M")

        if end_dt <= start_dt:
            raise ValueError("end_time must be after start_time")

        new_slot = Availability(
            doctor_id=doctor_id,
            start_time=start_dt,
            end_time=end_dt
        )

        self.user_repo.db.add(new_slot)
        await self.user_repo.db.commit()
        await self.user_repo.db.refresh(new_slot)

        return DoctorAvailability(
            date=slot.date,
            start_time=slot.start_time,
            end_time=slot.end_time
        )