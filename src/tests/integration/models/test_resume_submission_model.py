from app.database.factories.job_factory import JobFactory
from app.database.factories.resume_submission_factory import ResumeSubmissionFactory
from app.database.factories.user_factory import UserFactory
from tests.common import fake, session


class TestResumeSubmissionModel:
    def test_create_resume_submission(self):
        job = JobFactory()
        user = UserFactory()
        data = {
            'job': job,
            'user': user,
            'resume_text': fake.paragraph(),
            'score': fake.pyfloat(min_value=0.0, max_value=100.0),
        }

        resume_submission = ResumeSubmissionFactory(**data, deleted_at=None)
        session.add(resume_submission)
        session.flush()

        assert resume_submission.job_id == data['job'].id
        assert resume_submission.user_id == data['user'].id
        assert resume_submission.resume_text == data['resume_text']
        assert resume_submission.score == data['score']
        assert resume_submission.submission_date
        assert resume_submission.created_at
        assert resume_submission.updated_at
        assert resume_submission.deleted_at is None
