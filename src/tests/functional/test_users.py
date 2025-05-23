from starlette.testclient import TestClient

from tests.common import fake


class TestUsers:
    def test_user_flow(self, client: TestClient):
        payload = {
            'name': fake.name(),
            'email': fake.email(),
        }

        response = client.post('/users/', json=payload)
        assert response.status_code == 201, response.text
        response = client.get(f'/users/{response.json()["id"]}')
        json_response = response.json()

        assert response.status_code == 200, response.text
        assert json_response['id'] == 1
        assert json_response['name'] == payload['name']
        assert json_response['email'] == payload['email']
        assert json_response['created_at']
        assert json_response['updated_at']
        assert json_response['deleted_at'] is None
