from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AvailabilityBase(BaseModel):
    doctor_id: UUID
    start_time: datetime
    end_time: datetime
    is_active: bool = True

class AvailabilityCreate(BaseModel):
    doctor_id: UUID
    start_time: datetime
    end_time: datetime

class AvailabilityResponse(BaseModel):
    id: UUID
    doctor_id: UUID
    start_time: datetime
    end_time: datetime
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
