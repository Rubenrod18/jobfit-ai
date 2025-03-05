from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import ResumeSubmission
from database import AsyncSessionLocal


class ResumeSubmissionManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        session = session or AsyncSessionLocal
        super().__init__(model=ResumeSubmission, session=session)
