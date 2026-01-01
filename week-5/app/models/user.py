from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.enums.user_role import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"<User id={self.id} "
            f"email={self.email} "
            f"role={self.role}>"
        )

    def is_doctor(self) -> bool:
        return self.role == UserRole.DOCTOR

    def is_patient(self) -> bool:
        return self.role == UserRole.PATIENT

    def is_admin(self) -> bool:
        return self.role == UserRole.ADMIN

    def __str__(self) -> str:
        return f"User(id={self.id}, email={self.email}, role={self.role}, name={self.name})"
