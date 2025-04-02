from app.database.factories.base_factory import faker
from app.models.postgresql import Job, User
from tests.common import fake


def test_create_user():
    data = {
        'name': fake.name(),
        'email': fake.email(),
    }

    user = User(**data)

    assert user.name == data['name']
    assert user.email == data['email']


def test_create_job():
    data = {
        'title': faker.job(),
        'description': faker.text(),
        'required_skills': faker.words(nb=3),
        'company': faker.company(),
        'posted_at': faker.date_time_between(start_date='-3y', end_date='now'),
    }

    job = Job(**data)

    assert job.title == data['title']
    assert job.description == data['description']
    assert job.required_skills == data['required_skills']
    assert job.company == data['company']
    assert job.posted_at == data['posted_at']
    assert job.created_at
    assert job.updated_at
    assert job.deleted_at is None
