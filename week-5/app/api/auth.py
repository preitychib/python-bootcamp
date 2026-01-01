from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.auth import (ForgotPasswordRequest, ForgotPasswordResponse,
                              Token, UserCreate, UserInDB)
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

@router.post("/forgot-password", response_model=ForgotPasswordResponse)
async def forgot_password(
    request: ForgotPasswordRequest,
    db: AsyncSession = Depends(get_db)
):
    auth_service = AuthService(db)
    reset_token = await auth_service.forgot_password(request.email)
    return ForgotPasswordResponse(reset_token=reset_token)
