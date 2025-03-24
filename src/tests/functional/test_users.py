from starlette.testclient import TestClient

from tests.common import fake


def test_user_flow(client: TestClient):
    payload = {
        'name': fake.name(),
        'email': fake.email(),
    }

    response = client.post('/users/', json=payload)
    assert response.status_code == 201, response.text
    user_id = response.json()['id']

    response = client.get(f'/users/{user_id}')
    json_response = response.json()

    assert response.status_code == 200, response.text
    assert json_response['name'] == payload['name']
    assert json_response['email'] == payload['email']
