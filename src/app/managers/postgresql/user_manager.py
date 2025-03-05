from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import User
from database import AsyncSessionLocal


class UserManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        session = session or AsyncSessionLocal
        super().__init__(model=User, session=session)
