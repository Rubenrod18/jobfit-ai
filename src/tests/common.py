import os

from faker import Faker
from sqlalchemy import orm

from database import SQLDatabase

sql_db = SQLDatabase(db_url=os.getenv('SQLALCHEMY_DATABASE_URI'))
session = orm.scoped_session(sql_db.sessionmaker)

fake = Faker()
