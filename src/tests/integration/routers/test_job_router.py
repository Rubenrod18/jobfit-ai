from starlette.testclient import TestClient

from app.database.factories.base_factory import faker
from app.database.factories.job_factory import JobFactory


class TestCreateJobRouter:
    def test_create_job(self, client: TestClient):
        payload = {
            'title': faker.job(),
            'description': faker.text(),
            'required_skills': faker.sentence(nb_words=3),
            'company': faker.company(),
        }

        response = client.post('/jobs/', json=payload)
        json_response = response.json()

        assert response.status_code == 201, response.text
        assert json_response['title'] == payload['title']
        assert json_response['description'] == payload['description']
        assert json_response['required_skills'] == payload['required_skills']
        assert json_response['company'] == payload['company']
        assert json_response['posted_at']
        assert json_response['created_at']
        assert json_response['updated_at']
        assert json_response['deleted_at'] is None


class TestGetJobRouter:
    def test_get_job(self, client: TestClient):
        job = JobFactory(deleted_at=None)

        response = client.get(f'/jobs/{job.id}')
        json_response = response.json()

        assert response.status_code == 200, response.text
        assert json_response['title'] == job.title
        assert json_response['description'] == job.description
        assert json_response['required_skills'] == job.required_skills
        assert json_response['company'] == job.company
        assert json_response['posted_at'] == job.posted_at.isoformat()
        assert json_response['created_at'] == job.created_at.isoformat()
        assert json_response['updated_at'] == job.updated_at.isoformat()
        assert json_response['deleted_at'] is None
