from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import verify_password
from app.enums.user_role import UserRole
from app.models.availability import Availability
from app.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        await self.db.flush()
        await self.db.refresh(user)
        return user

    async def get_by_id(self, user_id: UUID) -> User | None:
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def authenticate(self, email: str, password: str) -> User | None:
        user = await self.get_by_email(email)
        if not user:
            return None

        if not verify_password(password, user.password_hash):
            return None

        return user


    async def update_role(self, user: User, role: UserRole) -> User:
        user.role = role
        await self.db.flush()
        await self.db.refresh(user)
        return user
    
    async def get_all_doctors(self) -> List[User]:
        result = await self.db.execute(
            select(User).where(User.role == UserRole.DOCTOR)
        )
        return list(result.scalars().all())
    
    async def get_doctor_availability(self, doctor_id: int) -> List[Availability]:
        result = await self.db.execute(
            select(Availability).where(Availability.doctor_id == doctor_id)
        )
        return list(result.scalars())
