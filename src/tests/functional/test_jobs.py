from starlette.testclient import TestClient

from app.database.factories.base_factory import faker


class TestJobs:
    def test_create_and_get_job_flow(self, client: TestClient):
        payload = {
            'title': faker.job(),
            'description': faker.text(),
            'required_skills': faker.sentence(nb_words=3),
            'company': faker.company(),
        }

        response = client.post('/jobs/', json=payload)
        assert response.status_code == 201, response.text
        response = client.get(f'/jobs/{response.json()["id"]}')
        json_response = response.json()

        assert response.status_code == 200, response.text
        assert json_response['id'] == 1
        assert json_response['title'] == payload['title']
        assert json_response['description'] == payload['description']
        assert json_response['required_skills'] == payload['required_skills']
        assert json_response['company'] == payload['company']
        assert json_response['created_at']
        assert json_response['updated_at']
        assert json_response['deleted_at'] is None
