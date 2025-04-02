from sqlmodel import SQLModel

from app.managers.postgresql.job_manager import JobManager
from app.services.base import BaseService


class JobService(BaseService):
    def __init__(self, manager: JobManager) -> None:
        super().__init__(manager=manager)

    def get_job_by_id(self, job_id: int) -> SQLModel:
        return self.manager.find(job_id)

    def create_job(self, job_data: dict) -> SQLModel:
        return self.manager.create(**job_data)
