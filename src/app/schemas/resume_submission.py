from datetime import datetime

from dependency_injector.wiring import inject, Provide
from fastapi import UploadFile
from pydantic import BaseModel

from app.di_container import ServiceDIContainer
from app.exceptions import NotFoundException
from app.helpers.resume_parser import parse_resume
from app.managers.postgresql.job_manager import JobManager
from app.managers.postgresql.user_manager import UserManager
from app.schemas.core import TimestampMixin


class ResumeSubmissionCreate(BaseModel):
    user_id: int
    job_id: int

    @inject
    def model_post_init(
        self,
        __context,
        job_manager: JobManager = Provide[ServiceDIContainer.job_manager],
        user_manager: UserManager = Provide[ServiceDIContainer.user_manager],
    ):
        if not user_manager.find(record_id=self.user_id):
            raise NotFoundException(f'User "{self.user_id}" not found')

        if not job_manager.find(record_id=self.job_id):
            raise NotFoundException(f'Job "{self.job_id}" not found')

    @staticmethod
    def get_resume_text(file: UploadFile) -> str:
        resume_text = parse_resume(file)

        if not resume_text:
            raise NotFoundException('Resume text or file must be provided')

        return resume_text


class ResumeSubmissionResponse(BaseModel, TimestampMixin):
    id: int
    job_id: int
    user_id: int
    resume_text: str | None
    submission_date: datetime | None
    score: float | None

    class Config:
        from_attributes = True
