from datetime import datetime, UTC

from sqlalchemy import func
from sqlmodel import Field

from app.models.base import TimestampedModel


class Job(TimestampedModel, table=True):
    __tablename__ = 'jobs'

    title: str
    description: str
    company: str
    required_skills: str
    posted_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC), sa_column_kwargs={'server_default': func.now()}, nullable=False
    )
