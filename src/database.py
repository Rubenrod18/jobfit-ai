import logging
from collections.abc import Callable
from contextlib import AbstractContextManager, contextmanager

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session, sessionmaker

from app import JobAnalysis, ResumeAnalysis
from config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

engine = create_engine(settings.SYNC_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

client = AsyncIOMotorClient(settings.MONGODB_URI)
database = client.get_database(settings.MONGODB_NAME)


async def mongo_init_db():
    await init_beanie(database, document_models=[JobAnalysis, ResumeAnalysis])


class SQLDatabase:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._sessionmaker = orm.sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine, expire_on_commit=False
        )
        self._session_factory = orm.scoped_session(self._sessionmaker)

    @property
    def sessionmaker(self) -> orm.sessionmaker:
        return self._sessionmaker

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            logger.exception('Session rollback because of exception')
            session.rollback()
            raise
        finally:
            session.close()
