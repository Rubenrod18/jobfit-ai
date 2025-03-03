from fastapi import FastAPI

from app.routers import ROUTERS


def _register_routers(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI()

    _register_routers(app)

    return app
