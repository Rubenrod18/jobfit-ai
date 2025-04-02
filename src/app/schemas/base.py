from datetime import datetime


class TimestampMixin:
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
