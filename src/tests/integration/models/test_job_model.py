from app.database.factories.job_factory import JobFactory
from tests.common import fake, session


class TestJobModel:
    def test_create_job(self):
        data = {
            'title': fake.job(),
            'description': fake.text(),
            'required_skills': fake.words(nb=3),
            'company': fake.company(),
            'posted_at': fake.date_time_between(start_date='-3y', end_date='now'),
            'deleted_at': None,
        }

        job = JobFactory(**data)
        session.add(job)
        session.flush()

        assert job.title == data['title']
        assert job.description == data['description']
        assert job.required_skills == data['required_skills']
        assert job.company == data['company']
        assert job.posted_at == data['posted_at']
        assert job.created_at
        assert job.updated_at
        assert job.deleted_at is None
