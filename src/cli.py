"""CLI module for managing custom commands of the application."""

import typer

from app.cli.seeder_cli import SeederCli
from database import SessionLocal

app = typer.Typer()


@app.command(name='seed', help='Fill database with fake data.')
def seeds() -> None:
    """Command line script for filling database with fake data."""
    seeder_cli = SeederCli(session=SessionLocal())
    seeder_cli.run_command()


if __name__ == '__main__':
    app()
