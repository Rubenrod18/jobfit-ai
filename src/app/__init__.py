import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.models.mongodb.job_analysis import JobAnalysis
from app.models.mongodb.resume_analysis import ResumeAnalysis
from app.routers import ROUTERS
from database import client, mongo_init_db


def _register_routers(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)


def _init_python_dependency_injector(app: FastAPI) -> None:
    from app.di_container import ServiceDIContainer

    container = ServiceDIContainer()
    app.container = container


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(_: FastAPI):
        logging.info('Connecting to MongoDB...')

        await mongo_init_db()

        logging.info('MongoDB initialized successfully!')

        yield

        logging.info('Closing MongoDB connection...')
        client.close()

    app = FastAPI(lifespan=lifespan)

    _init_python_dependency_injector(app)
    _register_routers(app)

    return app
