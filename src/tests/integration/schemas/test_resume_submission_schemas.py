import io
from unittest.mock import Mock

import pytest
from fastapi import UploadFile

from app.database.factories.job_factory import JobFactory
from app.database.factories.user_factory import UserFactory
from app.exceptions import NotFoundException
from app.managers.postgresql.job_manager import JobManager
from app.managers.postgresql.user_manager import UserManager
from app.schemas import resume_submission as rs_schema
from tests.common import generate_pdf_bytes


def test_resume_submission_create_success(app):
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    file = UploadFile(
        filename='test_file.pdf',
        file=io.BytesIO(generate_pdf_bytes(text)),
    )
    job = JobFactory()
    user = UserFactory()

    job_manager_mock = Mock(spec=JobManager)
    job_manager_mock.find.return_value = [job]
    user_manager_mock = Mock(spec=UserManager)
    user_manager_mock.find.return_value = [user]

    with (
        app.container.user_manager.override(job_manager_mock),
        app.container.user_manager.override(user_manager_mock),
    ):
        payload = rs_schema.ResumeSubmissionCreate(user_id=user.id, job_id=job.id)
        resume_text = rs_schema.ResumeSubmissionCreate.get_resume_text(file)

    validated_data = payload.model_dump()
    validated_data['resume_text'] = resume_text

    assert validated_data == {'resume_text': text, 'user_id': user.id, 'job_id': job.id}


def test_resume_submission_create_user_not_found(app):
    job = JobFactory()
    user_id = 1

    job_manager_mock = Mock(spec=JobManager)
    job_manager_mock.find.return_value = [job]
    user_manager_mock = Mock(spec=UserManager)
    user_manager_mock.find.return_value = []

    with pytest.raises(NotFoundException, match='User "1" not found'):
        with (
            app.container.user_manager.override(job_manager_mock),
            app.container.user_manager.override(user_manager_mock),
        ):
            rs_schema.ResumeSubmissionCreate(user_id=user_id, job_id=job.id)


def test_resume_submission_create_job_not_found(app):
    job_id = 1
    user = UserFactory()

    job_manager_mock = Mock(spec=JobManager)
    job_manager_mock.find.return_value = []
    user_manager_mock = Mock(spec=UserManager)
    user_manager_mock.find.return_value = [user]

    with pytest.raises(NotFoundException, match='Job "1" not found'):
        with (
            app.container.user_manager.override(job_manager_mock),
            app.container.user_manager.override(user_manager_mock),
        ):
            rs_schema.ResumeSubmissionCreate(user_id=user.id, job_id=job_id)


def test_resume_submission_create_file_not_valid(app):
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    buffer = io.BytesIO()
    buffer.write(text.encode('utf-8'))
    buffer.seek(0)
    buffer.read()

    file = UploadFile(
        filename='test_file.txt',
        file=buffer,
    )

    with pytest.raises(NotFoundException, match='Resume text or file must be provided'):
        rs_schema.ResumeSubmissionCreate.get_resume_text(file)
