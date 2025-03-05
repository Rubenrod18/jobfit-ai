import factory
from faker import Faker
from sqlalchemy.orm import Session

from database import engine

faker = Faker()

session = Session(engine)


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'
