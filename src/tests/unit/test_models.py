from app.database.factories.base_factory import faker
from app.database.factories.job_factory import JobFactory
from app.database.factories.resume_submission_factory import ResumeSubmissionFactory
from app.database.factories.user_factory import UserFactory
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


def test_create_resume_submission():
    job = JobFactory()
    user = UserFactory()
    data = {
        'job': job,
        'user': user,
        'resume_text': faker.paragraph(),
        'score': faker.pyfloat(min_value=0.0, max_value=100.0),
    }

    resume_submission = ResumeSubmissionFactory(**data, deleted_at=None)

    assert resume_submission.job_id == data['job'].id
    assert resume_submission.user_id == data['user'].id
    assert resume_submission.resume_text == data['resume_text']
    assert resume_submission.score == data['score']
    assert resume_submission.submission_date
    assert resume_submission.created_at
    assert resume_submission.updated_at
    assert resume_submission.deleted_at is None
