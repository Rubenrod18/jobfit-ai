from datetime import datetime, UTC

from sqlalchemy import func
from sqlmodel import Field, SQLModel


class BaseMixin(SQLModel):
    __abstract__ = True
    id: int = Field(primary_key=True)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC), sa_column_kwargs={'server_default': func.now()}, nullable=False
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_column_kwargs={'server_default': func.now(), 'onupdate': func.now()},
        nullable=False,
    )
    deleted_at: datetime = Field(nullable=True)


class TimestampedModel(BaseMixin):
    __abstract__ = True
