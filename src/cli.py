"""CLI module for managing custom commands of the application."""

import typer

from app.cli import CreateDatabaseCli, SeederCli
from database import SessionLocal, settings

app = typer.Typer()


@app.command(name='create_db', help='Create database.')
def create_database() -> None:
    """Command line script for creating the database."""
    seeder_cli = CreateDatabaseCli(db_uri=settings.SYNC_DATABASE_URL)
    seeder_cli.run_command()


@app.command(name='seed', help='Fill database with fake data.')
def seeds() -> None:
    """Command line script for filling database with fake data."""
    seeder_cli = SeederCli(session=SessionLocal())
    seeder_cli.run_command()


if __name__ == '__main__':
    app()
