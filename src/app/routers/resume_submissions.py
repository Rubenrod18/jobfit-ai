from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, File, Form, status, UploadFile

from app.di_container import ServiceDIContainer
from app.schemas import resume_submission as rs_schema
from app.services.resume_submission_service import ResumeSubmissionService

router = APIRouter(prefix='/resume_submissions', tags=['resume_submissions'])


@router.post('/', response_model=rs_schema.ResumeSubmissionResponse, status_code=status.HTTP_201_CREATED)
@inject
def submit_resume(
    resume_submission_service: Annotated[
        ResumeSubmissionService, Depends(Provide[ServiceDIContainer.resume_submission_service])
    ],
    file: UploadFile = File(...),
    user_id: int = Form(),
    job_id: int = Form(),
):
    """Uploads a resume PDF and extracts text."""
    payload = rs_schema.ResumeSubmissionCreate(user_id=user_id, job_id=job_id)
    resume_text = rs_schema.ResumeSubmissionCreate.get_resume_text(file)

    validated_data = payload.model_dump()
    validated_data['resume_text'] = resume_text
    return resume_submission_service.create_resume_submission(validated_data)
