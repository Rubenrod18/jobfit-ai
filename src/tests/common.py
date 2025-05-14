import os
from io import BytesIO

from faker import Faker
from reportlab.pdfgen import canvas
from sqlalchemy import orm

from database import SQLDatabase

sql_db = SQLDatabase(db_url=os.getenv('SQLALCHEMY_DATABASE_URI'))
session = orm.scoped_session(sql_db.sessionmaker)

fake = Faker()


def generate_pdf_bytes(text: str = None) -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, text)
    pdf.save()
    buffer.seek(0)
    return buffer.read()
