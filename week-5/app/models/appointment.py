from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    doctor_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"), 
        index=True,
        nullable=False
    )

    patient_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        index=True,
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime] = mapped_column(nullable=False)

    status: Mapped[str] = mapped_column(
        String(20),
        default="BOOKED",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    __table_args__ = (
        CheckConstraint("start_time < end_time", name="check_time_order"),
    )

    def __str__(self) -> str:
        return f"Appointment(id={self.id}, doctor_id={self.doctor_id}, patient_id={self.patient_id}, start_time={self.start_time}, status={self.status})"

    def __repr__(self) -> str:
        return self.__str__()
