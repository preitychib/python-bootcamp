import re
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, validator


class DoctorBase(BaseModel):
    id: UUID
    name: str
    email: str
    role: str

class DoctorAvailability(BaseModel):
    date: str
    start_time: str
    end_time: str

class CreateAvailabilityRequest(BaseModel):
    date: str
    start_time: str
    end_time: str

    @validator("date")
    def validate_date(cls, v):
        if not re.match(r"\d{2}-\d{2}-\d{4}$", v):
            raise ValueError("Date must be in dd-mm-yyyy format")
        return v

    @validator("start_time", "end_time")
    def validate_time(cls, v):
        if not re.match(r"([01]\d|2[0-3]):[0-5]\d$", v):
            raise ValueError("Time must be in HH:MM 24-hour format")
        return v
