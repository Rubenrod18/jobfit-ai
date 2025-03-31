from sqlmodel import SQLModel

from app.managers.postgresql.user_manager import UserManager
from app.services.base import BaseService


class UserService(BaseService):
    def __init__(self, manager: UserManager) -> None:
        super().__init__(manager=manager)

    def get_user_by_id(self, user_id: int) -> SQLModel:
        return self.manager.find(user_id)

    def create_user(self, user_data: dict) -> SQLModel:
        return self.manager.create(**user_data)
