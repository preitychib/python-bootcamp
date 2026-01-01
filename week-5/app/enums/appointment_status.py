from enum import Enum


class AppointmentStatus(str, Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    NO_SHOW = "NO_SHOW"

    def __str__(self) -> str:
        return self.value
    
    @classmethod
    def choices(cls):
        return [(status.value, status.name) for status in cls]
    
    @classmethod
    def from_string(cls, value: str):
        for status in cls:
            if status.value == value:
                return status
        raise ValueError(f"Invalid appointment status: {value}")
    
    @classmethod
    def is_valid_status(cls, value: str) -> bool:
        try:
            cls.from_string(value)
            return True
        except ValueError:
            return False
