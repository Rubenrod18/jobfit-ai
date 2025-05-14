import pytest
from sqlalchemy.orm import scoped_session
from sqlmodel.main import SQLModelMetaclass

from app.managers.postgresql.resume_submission_manager import ResumeSubmissionManager
from app.models.postgresql import ResumeSubmission
from tests.common import session


@pytest.fixture
def resume_submission_manager():
    return ResumeSubmissionManager(session=session)


def test_resume_submission_manager_attributes(resume_submission_manager):
    assert type(resume_submission_manager.model) is SQLModelMetaclass
    assert isinstance(resume_submission_manager.model(), ResumeSubmission)
    assert isinstance(resume_submission_manager.session, scoped_session)
