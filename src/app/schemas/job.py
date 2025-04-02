from datetime import datetime

from pydantic import BaseModel

from app.schemas.base import TimestampMixin


class JobCreate(BaseModel):
    title: str
    description: str
    company: str
    required_skills: str


class JobResponse(BaseModel, TimestampMixin):
    id: int
    title: str
    description: str
    company: str
    required_skills: str
    posted_at: datetime

    class Config:
        from_attributes = True
