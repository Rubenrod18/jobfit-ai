"""Module for managing dependency injections."""

import os

from dependency_injector import containers, providers
from dotenv import load_dotenv

from app.managers.postgresql.user_manager import UserManager
from app.services.user_service import UserService
from config import get_settings
from database import SQLDatabase

settings = get_settings()
load_dotenv()


class ServiceDIContainer(containers.DeclarativeContainer):
    """Service Dependency Injection Container."""

    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=[
            '.routers.base',
            '.routers.users',
        ]
    )
    # OPTIMIZE: Load all env vars on this config
    config.from_dict({'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI')})

    # Database
    sql_db = providers.Singleton(SQLDatabase, db_url=config.SQLALCHEMY_DATABASE_URI)

    user_manager = providers.Factory(
        UserManager,
        session=sql_db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_manager=user_manager,
    )
