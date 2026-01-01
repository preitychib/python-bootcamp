from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.enums.user_role import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: UserRole = UserRole.PATIENT


class UserInDB(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    role: UserRole

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ForgotPasswordResponse(BaseModel):
    reset_token: str
    message: str = "Mock reset token generated (no email sent)"