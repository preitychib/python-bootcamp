from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash
from app.repositories.user_repo import UserRepository
from app.schemas.auth import Token, UserCreate, UserInDB


class AuthService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def register(self, user: UserCreate) -> UserInDB:
        if await self.user_repo.get_by_email(user.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        user_data = user.model_dump(exclude={"password"})
        user_data["password_hash"] = get_password_hash(user.password)

        created_user = await self.user_repo.create(user_data)
        return created_user

    async def login(self, email: str, password: str) -> Token:
        user = await self.user_repo.authenticate(email, password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        access_token = create_access_token(
            data={
                "sub": user.email,
                "role": user.role,
            },
            expires_delta=access_token_expires,
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )
