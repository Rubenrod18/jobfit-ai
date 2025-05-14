from sqlmodel import SQLModel

from app.managers.postgresql.resume_submission_manager import ResumeSubmissionManager
from app.services.base import BaseService


class ResumeSubmissionService(BaseService):
    def __init__(self, manager: ResumeSubmissionManager) -> None:
        super().__init__(manager=manager)

    def get_resume_submission_by_id(self, resume_submission_id: int, *args) -> SQLModel:
        return self.manager.find(resume_submission_id, *args)

    def create_resume_submission(self, resume_submission_data: dict) -> SQLModel:
        return self.manager.create(**resume_submission_data)
