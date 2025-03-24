from datetime import datetime, UTC

from sqlalchemy.orm import Session
from sqlmodel import SQLModel


class BaseSQLManager:
    def __init__(self, model: type[SQLModel], session: type[Session]):
        self.model = model
        self.session = session

    def create(self, **kwargs) -> SQLModel:
        with self.session() as session:
            current_date = datetime.now(UTC)
            kwargs.update({'created_at': current_date, 'updated_at': current_date})
            user = self.model(**kwargs)
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def find(self, record_id: int, *args) -> SQLModel | None:
        with self.session() as session:
            query = session.query(self.model).filter(self.model.id == record_id)

            for arg in args:
                query = query.filter(arg)

            return query.first()
