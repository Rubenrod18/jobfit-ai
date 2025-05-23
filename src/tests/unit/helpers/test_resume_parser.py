import io

from fastapi import UploadFile

from app.helpers.resume_parser import parse_resume
from tests.common import fake, generate_pdf_bytes


class TestResumeParser:
    def test_resume_parser_with_a_pdf_file(self):
        text = fake.paragraph()
        file = UploadFile(
            filename='test_file.pdf',
            file=io.BytesIO(generate_pdf_bytes(text)),
        )

        pdf_content = parse_resume(file)

        assert pdf_content == text

    def test_resume_parser_with_a_pdf_file_empty(self):
        text = ''
        file = UploadFile(
            filename='test_file.pdf',
            file=io.BytesIO(generate_pdf_bytes(text)),
        )

        pdf_content = parse_resume(file)

        assert pdf_content == text

    def test_resume_parser_with_a_text_file(self):
        buffer = io.BytesIO()
        buffer.write(fake.paragraph().encode('utf-8'))
        buffer.seek(0)
        buffer.read()
        file = UploadFile(
            filename='test_file.txt',
            file=buffer,
        )

        txt_content = parse_resume(file)

        assert txt_content == ''
