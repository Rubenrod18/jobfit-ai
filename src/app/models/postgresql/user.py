import typing as t
from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Field, Relationship

from app.models.base import TimestampedModel

if t.TYPE_CHECKING:
    from app.models.postgresql import Job


class User(TimestampedModel, table=True):
    __tablename__ = 'users'

    name: str
    email: str = Field(sa.String, unique=True)
    resume_submissions: t.Optional['ResumeSubmission'] = Relationship(back_populates='user')


class ResumeSubmission(TimestampedModel, table=True):
    __tablename__ = 'resume_submissions'

    user_id: int | None = Field(default=None, foreign_key='users.id')
    user: t.Optional['User'] = Relationship(back_populates='resume_submissions')

    job_id: int | None = Field(default=None, foreign_key='jobs.id')
    job: t.Optional['Job'] = Relationship(back_populates='resume_submissions')

    resume_text: str | None = None
    submission_date: datetime | None = Field(default=None)
    score: float | None = None
