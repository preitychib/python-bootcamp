from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.appointment import Appointment
from app.models.availability import Availability
from app.repositories.user_repo import UserRepository
from app.schemas.appointment import (AppointmentResponse,
                                     CreateAppointmentRequest)


class AppointmentService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)

    async def create_appointment(
        self,
        patient_id,
        data: CreateAppointmentRequest
    ) -> AppointmentResponse:

        start_dt = datetime.strptime(
            f"{data.date} {data.start_time}",
            "%d-%m-%Y %H:%M"
        )
        end_dt = datetime.strptime(
            f"{data.date} {data.end_time}",
            "%d-%m-%Y %H:%M"
        )

        if end_dt <= start_dt:
            raise ValueError("end_time must be after start_time")

        if start_dt < datetime.now():
            raise ValueError("Cannot book appointment in the past")

        doctor = await self.user_repo.get_by_id(data.doctor_id)

        if not doctor or not doctor.is_doctor():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid doctor_id"
            )

        # pessimistic lock
        availability_query = (
            select(Availability)
            .where(
                Availability.doctor_id == data.doctor_id,
                Availability.is_active.is_(True),
                Availability.start_time <= start_dt,
                Availability.end_time >= end_dt
            )
            .with_for_update()
        )

        availability_result = await self.db.execute(availability_query)
        availability = availability_result.scalars().first()

        if not availability:
            raise ValueError(
                "Doctor is not available for the selected date and time"
            )

        appointment_query = (
            select(Appointment)
            .where(
                Appointment.doctor_id == data.doctor_id,
                Appointment.start_time < end_dt,
                Appointment.end_time > start_dt
            )
            .with_for_update()
        )

        result = await self.db.execute(appointment_query)
        overlapping = result.scalars().first()

        if overlapping:
            raise ValueError("This time slot is already booked")

        new_appointment = Appointment(
            id=uuid4(),
            doctor_id=data.doctor_id,
            patient_id=patient_id,
            start_time=start_dt,
            end_time=end_dt
        )

        self.db.add(new_appointment)

        try:
            await self.db.commit()
        except IntegrityError:
            await self.db.rollback()
            raise ValueError("Failed to book appointment, please try again")

        await self.db.refresh(new_appointment)

        return AppointmentResponse(
            id=new_appointment.id,
            doctor_id=new_appointment.doctor_id,
            patient_id=new_appointment.patient_id,
            date=data.date,
            start_time=data.start_time,
            end_time=data.end_time
        )
