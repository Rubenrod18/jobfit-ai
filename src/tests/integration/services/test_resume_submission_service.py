from datetime import datetime

import pytest

from app.database.factories.job_factory import JobFactory
from app.database.factories.resume_submission_factory import ResumeSubmissionFactory
from app.database.factories.user_factory import UserFactory
from app.managers.postgresql.resume_submission_manager import ResumeSubmissionManager
from app.services.resume_submission_service import ResumeSubmissionService
from tests.common import session


@pytest.fixture
def resume_submission_manager():
    return ResumeSubmissionManager(session=session)


@pytest.fixture
def resume_submission_service(resume_submission_manager):
    return ResumeSubmissionService(manager=resume_submission_manager)


def test_create_resume_submission_service(resume_submission_service):
    data = ResumeSubmissionFactory.build_dict(exclude={'id', 'created_at', 'updated_at', 'deleted_at', 'job', 'user'})
    data['job_id'] = JobFactory().id
    data['user_id'] = UserFactory().id

    resume_submission = resume_submission_service.create_resume_submission(data)

    assert isinstance(resume_submission.id, int)
    assert resume_submission.user_id == data['user_id']
    assert resume_submission.job_id == data['job_id']
    assert resume_submission.resume_text == data['resume_text']
    assert isinstance(resume_submission.created_at, datetime)
    assert isinstance(resume_submission.updated_at, datetime)
    assert resume_submission.deleted_at is None


def test_find_resume_submission_service(resume_submission_service):
    resume_submission = ResumeSubmissionFactory(deleted_at=None)

    resume_submission = resume_submission_service.get_resume_submission_by_id(resume_submission.id)

    assert resume_submission.id == resume_submission.id
    assert resume_submission.user_id == resume_submission.user_id
    assert resume_submission.job_id == resume_submission.job_id
    assert resume_submission.resume_text == resume_submission.resume_text
    assert isinstance(resume_submission.created_at, datetime)
    assert isinstance(resume_submission.updated_at, datetime)
    assert resume_submission.deleted_at is None


def test_find_resume_submission_service_with_condition(resume_submission_service):
    resume_submission = ResumeSubmissionFactory(deleted_at=None)

    resume_submission = resume_submission_service.get_resume_submission_by_id(
        resume_submission.id,
        resume_submission_service.manager.model.resume_text == resume_submission.resume_text,
    )

    assert resume_submission.id == resume_submission.id
    assert resume_submission.user_id == resume_submission.user_id
    assert resume_submission.job_id == resume_submission.job_id
    assert resume_submission.resume_text == resume_submission.resume_text
    assert isinstance(resume_submission.created_at, datetime)
    assert isinstance(resume_submission.updated_at, datetime)
    assert resume_submission.deleted_at is None


def test_find_resume_submission_service_with_condition_not_found(resume_submission_service):
    resume_submission = ResumeSubmissionFactory(deleted_at=None)

    resume_submission = resume_submission_service.get_resume_submission_by_id(
        resume_submission.id,
        resume_submission_service.manager.model.resume_text == 'not found',
    )

    assert resume_submission is None
