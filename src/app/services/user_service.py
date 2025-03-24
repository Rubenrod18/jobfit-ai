from sqlmodel import SQLModel

from app.managers.postgresql.user_manager import UserManager


class UserService:
    def __init__(self, user_manager: UserManager) -> None:
        self._manager = user_manager

    def get_user_by_id(self, user_id: int) -> SQLModel:
        return self._manager.find(user_id)

    def create_user(self, user_data: dict) -> SQLModel:
        return self._manager.create(**user_data)
