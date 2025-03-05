from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import Job
from database import AsyncSessionLocal


class JobManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        session = session or AsyncSessionLocal
        super().__init__(model=Job, session=session)
