import pdfplumber
from fastapi import UploadFile


def parse_resume(file: UploadFile) -> str:
    """Extracts text from PDF files.

    Parameters
    ----------
        file : UploadFile
            Uploaded PDF.

    Returns
    -------
    Text from PDF file.

    """

    filename = file.filename.lower()

    if filename.endswith('.pdf'):
        with pdfplumber.open(file.file) as doc:
            text = '\n'.join([page.extract_text() for page in doc.pages if page.extract_text()])
    else:
        text = ''

    return text.strip()
