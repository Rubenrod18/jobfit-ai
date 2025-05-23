from datetime import datetime

import pytest
from sqlalchemy.orm import scoped_session
from sqlmodel.main import SQLModelMetaclass

from app.database.factories.job_factory import JobFactory
from app.database.factories.resume_submission_factory import ResumeSubmissionFactory
from app.database.factories.user_factory import UserFactory
from app.managers.postgresql.resume_submission_manager import ResumeSubmissionManager
from app.models.postgresql import ResumeSubmission
from tests.common import session


@pytest.fixture
def resume_submission_manager():
    return ResumeSubmissionManager(session=session)


@pytest.fixture
def resume_submission():
    return ResumeSubmissionFactory(deleted_at=None)


class TestResumeSubmissionManager:
    def test_resume_submission_manager_attributes(self, resume_submission_manager):
        assert type(resume_submission_manager.model) is SQLModelMetaclass
        assert isinstance(resume_submission_manager.model(), ResumeSubmission)
        assert isinstance(resume_submission_manager.session, scoped_session)

    def test_create_resume_submission(self, resume_submission_manager):
        data = ResumeSubmissionFactory.build_dict(
            exclude={'id', 'created_at', 'updated_at', 'deleted_at', 'job', 'user'}
        )
        data['job_id'] = JobFactory().id
        data['user_id'] = UserFactory().id

        record_created = resume_submission_manager.create(**data)

        assert isinstance(record_created.id, int)
        assert record_created.user_id == data['user_id']
        assert record_created.job_id == data['job_id']
        assert record_created.resume_text == data['resume_text']
        assert isinstance(record_created.created_at, datetime)
        assert isinstance(record_created.updated_at, datetime)
        assert record_created.deleted_at is None

    def test_find_resume_submission(self, resume_submission, resume_submission_manager):
        record_found = resume_submission_manager.find(resume_submission.id)

        assert record_found.id == resume_submission.id
        assert record_found.user_id == resume_submission.user_id
        assert record_found.job_id == resume_submission.job_id
        assert record_found.resume_text == resume_submission.resume_text
        assert isinstance(record_found.created_at, datetime)
        assert isinstance(record_found.updated_at, datetime)
        assert record_found.deleted_at is None

    def test_find_resume_submission_with_condition(self, resume_submission, resume_submission_manager):
        record_found = resume_submission_manager.find(
            resume_submission.id,
            resume_submission_manager.model.resume_text == resume_submission.resume_text,
        )

        assert record_found.id == resume_submission.id
        assert record_found.user_id == resume_submission.user_id
        assert record_found.job_id == resume_submission.job_id
        assert record_found.resume_text == resume_submission.resume_text
        assert isinstance(record_found.created_at, datetime)
        assert isinstance(record_found.updated_at, datetime)
        assert record_found.deleted_at is None

    def test_find_resume_submission_with_condition_not_found(self, resume_submission, resume_submission_manager):
        record_found = resume_submission_manager.find(
            resume_submission.id,
            resume_submission_manager.model.resume_text == 'not found',
        )

        assert record_found is None
