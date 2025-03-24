from sqlalchemy.orm import Session

from app.managers.base import BaseSQLManager
from app.models.postgresql import User


class UserManager(BaseSQLManager):
    def __init__(self, session: type[Session]):
        super().__init__(model=User, session=session)
