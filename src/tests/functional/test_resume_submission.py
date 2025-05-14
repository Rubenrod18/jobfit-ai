import io

from starlette.testclient import TestClient

from app.database.factories.job_factory import JobFactory
from app.database.factories.user_factory import UserFactory
from tests.common import generate_pdf_bytes


def test_create_resume_submission(client: TestClient):
    user = UserFactory()
    job = JobFactory()
    payload = {
        'user_id': user.id,
        'job_id': job.id,
    }
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    file = io.BytesIO(generate_pdf_bytes(text=text))

    response = client.post(
        '/resume_submissions/',
        data=payload,
        files={'file': ('resume.pdf', file, 'application/pdf')},
    )
    json_response = response.json()

    assert response.status_code == 201, response.text
    assert json_response['user_id'] == payload['user_id']
    assert json_response['job_id'] == payload['job_id']
