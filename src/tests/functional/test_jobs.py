from starlette.testclient import TestClient

from app.database.factories.base_factory import faker


def test_job_flow(client: TestClient):
    payload = {
        'title': faker.job(),
        'description': faker.text(),
        'required_skills': faker.sentence(nb_words=3),
        'company': faker.company(),
    }

    response = client.post('/jobs/', json=payload)
    assert response.status_code == 201, response.text
    job_id = response.json()['id']

    response = client.get(f'/jobs/{job_id}')
    json_response = response.json()

    assert response.status_code == 200, response.text
    assert json_response['title'] == payload['title']
    assert json_response['description'] == payload['description']
    assert json_response['required_skills'] == payload['required_skills']
    assert json_response['company'] == payload['company']
