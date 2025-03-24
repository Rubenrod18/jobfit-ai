from httpx import AsyncClient

from app.database.factories.user_factory import UserFactory
from tests.common import fake


def test_create_user(client: AsyncClient):
    payload = {
        'name': fake.name(),
        'email': fake.email(),
    }

    response = client.post('/users/', json=payload)
    json_response = response.json()

    assert response.status_code == 201, response.text
    assert json_response['name'] == payload['name']
    assert json_response['email'] == payload['email']


def test_get_user(client):
    user = UserFactory()

    response = client.get(f'/users/{user.id}')
    json_response = response.json()

    assert response.status_code == 200, response.text
    assert json_response['name'] == user.name
    assert json_response['email'] == user.email
