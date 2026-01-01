from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.auth import Token, UserCreate, UserInDB
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=UserInDB)
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    return await AuthService(db).register(user)


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    return await AuthService(db).login(
        email=form_data.username,
        password=form_data.password,
    )
