from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import ResumeSubmission


class ResumeSubmissionManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        super().__init__(model=ResumeSubmission, session=session)
