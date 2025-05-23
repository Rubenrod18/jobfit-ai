from pydantic import BaseModel, EmailStr

from app.schemas.core import TimestampMixin


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class UserResponse(BaseModel, TimestampMixin):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
