from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import Job


class JobManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        super().__init__(model=Job, session=session)
