from starlette.testclient import TestClient

from app.database.factories.user_factory import UserFactory
from tests.common import fake


class TestCreateUserRouter:
    def test_create_user(self, client: TestClient):
        payload = {
            'name': fake.name(),
            'email': fake.email(),
        }

        response = client.post('/users/', json=payload)
        json_response = response.json()

        assert response.status_code == 201, response.text
        assert json_response['id'] == 1
        assert json_response['name'] == payload['name']
        assert json_response['email'] == payload['email']
        assert json_response['created_at']
        assert json_response['created_at']
        assert json_response['deleted_at'] is None


class TestGetUserRouter:
    def test_get_user(self, client: TestClient):
        user = UserFactory(deleted_at=None)

        response = client.get(f'/users/{user.id}')
        json_response = response.json()

        assert response.status_code == 200, response.text
        assert json_response['id'] == user.id
        assert json_response['name'] == user.name
        assert json_response['email'] == user.email
        assert json_response['created_at']
        assert json_response['created_at']
        assert json_response['deleted_at'] is None
