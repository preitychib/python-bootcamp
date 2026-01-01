from uuid import UUID

from pydantic import BaseModel


class CreateAppointmentRequest(BaseModel):
    doctor_id: UUID
    date: str
    start_time: str
    end_time: str

class AppointmentResponse(BaseModel):
    id: UUID
    doctor_id: UUID
    patient_id: UUID
    date: str
    start_time: str
    end_time: str
