from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Availability(Base):
    __tablename__ = "availability"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    doctor_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        index=True,
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime] = mapped_column(nullable=False)

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    __table_args__ = (
        CheckConstraint("start_time < end_time", name="check_availability_time"),
    )
    
    def __str__(self) -> str:
        return f"Availability(id={self.id}, doctor_id={self.doctor_id}, start_time={self.start_time}, end_time={self.end_time})"

    def __repr__(self) -> str:
        return self.__str__()