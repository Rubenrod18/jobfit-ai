from datetime import datetime, UTC

from sqlalchemy.orm import Session
from sqlmodel import SQLModel


class BaseSQLManager:
    def __init__(self, model: type[SQLModel], session: type[Session]):
        self.model = model
        self.session = session

    def create(self, **kwargs) -> SQLModel:
        current_date = datetime.now(UTC)
        kwargs.update({'created_at': current_date, 'updated_at': current_date})
        return self.model(**kwargs)

    def save(self, record_id: int, **kwargs) -> SQLModel:
        record = self.session.query(self.model).filter_by(id=record_id).first()

        for key, value in kwargs.items():
            setattr(record, key, value)

        return record

    def get(self, **kwargs) -> dict:
        page = int(kwargs.get('page_number', 1)) - 1
        items_per_page = int(kwargs.get('items_per_page', 10))

        query = self.session.query(self.model)
        records_total = self.session.query(self.model).count()

        query = query.offset(page * items_per_page).limit(items_per_page)

        return {
            'query': query,
            'records_total': records_total,
            'records_filtered': query.count(),
        }

    def delete(self, record_id: int) -> SQLModel:
        record = self.find(record_id)
        record.deleted_at = datetime.now(UTC)
        return record

    def find(self, record_id: int, *args) -> SQLModel | None:
        query = self.session.query(self.model).filter(self.model.id == record_id)

        for arg in args:
            query = query.filter(arg)

        return query.first()
