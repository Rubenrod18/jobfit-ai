"""Module for managing dependency injections."""

import os

from dependency_injector import containers, providers
from dotenv import load_dotenv

from app.managers.postgresql.job_manager import JobManager
from app.managers.postgresql.resume_submission_manager import ResumeSubmissionManager
from app.managers.postgresql.user_manager import UserManager
from app.services.job_service import JobService
from app.services.resume_submission_service import ResumeSubmissionService
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
            '.routers.jobs',
            '.routers.users',
            '.routers.resume_submissions',
            '.schemas.resume_submission',
        ]
    )
    # OPTIMIZE: Load all env vars on this config
    config.from_dict({'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI')})

    # Database
    sql_db = providers.Singleton(SQLDatabase, db_url=config.SQLALCHEMY_DATABASE_URI)

    # Managers
    job_manager = providers.Factory(JobManager, session=sql_db.provided.session)
    resume_submission_manager = providers.Factory(ResumeSubmissionManager, session=sql_db.provided.session)
    user_manager = providers.Factory(UserManager, session=sql_db.provided.session)

    # Services
    user_service = providers.Factory(UserService, manager=user_manager)
    job_service = providers.Factory(JobService, manager=job_manager)
    resume_submission_service = providers.Factory(ResumeSubmissionService, manager=resume_submission_manager)
