import factory
from faker import Faker

from tests.common import session

faker = Faker()


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'commit'
