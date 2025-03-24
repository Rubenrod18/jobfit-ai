from faker import Faker
from sqlalchemy import orm

Session = orm.scoped_session(orm.sessionmaker())

fake = Faker()
