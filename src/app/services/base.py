from abc import ABC

from app.managers.base import BaseSQLManager


class BaseService(ABC):
    def __init__(self, manager: BaseSQLManager):
        self.manager = manager
