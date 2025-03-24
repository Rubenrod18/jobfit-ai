import os
import uuid

import pytest
from dotenv import find_dotenv, load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text

from app import create_app
from app.cli import CreateDatabaseCli
from app.models.base import BaseMixin
from database import settings
from tests.common import Session


def pytest_configure():
    """Load .env.test before running tests"""
    load_dotenv(find_dotenv('.env.test'), override=True)


@pytest.fixture(scope='function', autouse=True)
def setup_database():
    db_uri = f'{settings.SYNC_DATABASE_URL}_{uuid.uuid4().hex}'
    engine = create_engine(db_uri)
    Session.configure(bind=engine)
    os.environ['SQLALCHEMY_DATABASE_URI'] = db_uri

    def create_db():
        seeder_cli = CreateDatabaseCli(db_uri=db_uri)
        seeder_cli.run_command()

        with engine.begin() as conn:
            BaseMixin.metadata.create_all(conn)

    def drop_db():
        db_name_to_drop = db_uri.rsplit('/', 1)[1]
        neutral_engine_url = engine.url.set(database='postgres')
        neutral_engine = create_engine(neutral_engine_url, echo=True)

        try:
            with neutral_engine.connect() as conn:
                conn.execution_options(isolation_level='AUTOCOMMIT')
                conn.execute(
                    text(f"""
                    SELECT pg_terminate_backend(pid)
                    FROM pg_stat_activity
                    WHERE datname = '{db_name_to_drop}';
                """)
                )
                conn.execute(text(f'DROP DATABASE IF EXISTS "{db_name_to_drop}"'))
                print(f"Database '{db_name_to_drop}' dropped successfully.")  # noqa
        finally:
            neutral_engine.dispose()

    create_db()
    yield db_uri
    drop_db()


@pytest.fixture
def client(setup_database):
    app = create_app()
    app.container.config.from_dict({'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI')})
    yield TestClient(app)
