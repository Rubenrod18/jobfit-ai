from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import Job
from database import SessionLocal


# TODO: Pending to send the session as argument thorugh ServiceDIContainer
class JobManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        session = session or SessionLocal
        super().__init__(model=Job, session=session)
