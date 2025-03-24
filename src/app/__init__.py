from fastapi import FastAPI

from app.models.mongodb.job_analysis import JobAnalysis
from app.models.mongodb.resume_analysis import ResumeAnalysis
from app.routers import ROUTERS


def _register_routers(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)


def _init_python_dependency_injector(app: FastAPI) -> None:
    from app.di_container import ServiceDIContainer

    container = ServiceDIContainer()
    app.container = container


def create_app() -> FastAPI:
    app = FastAPI()

    _init_python_dependency_injector(app)
    _register_routers(app)

    return app
