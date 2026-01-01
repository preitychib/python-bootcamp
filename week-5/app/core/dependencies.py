from typing import Any, Callable

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums.user_role import UserRole
from app.models.user import User
from app.repositories.user_repo import UserRepository

from .config import settings
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        email: str | None = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    
    user_repo = UserRepository(db)
    user = await user_repo.get_by_email(email)
    if not user:
        raise HTTPException(status_code=401)

    return user

def get_current_active_user(current_user = Depends(get_current_user)):
    return current_user


def require_role(*allowed_roles: UserRole):
    def decorator(func: Callable[..., Any]):
        from functools import wraps
        @wraps(func)
        async def wrapper(
            *args,
            user=Depends(get_current_user),
            **kwargs,
        ):
            if user.role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissions",
                )

            return await func(*args, user=user, **kwargs)

        return wrapper

    return decorator
