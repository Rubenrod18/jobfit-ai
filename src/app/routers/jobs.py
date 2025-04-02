from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status

from app.di_container import ServiceDIContainer
from app.schemas import job as job_schema
from app.services.job_service import JobService

router = APIRouter(prefix='/jobs', tags=['jobs'])


@router.post('/', response_model=job_schema.JobResponse, status_code=status.HTTP_201_CREATED)
@inject
def create_job_route(
    user_data: job_schema.JobCreate,
    job_service: Annotated[JobService, Depends(Provide[ServiceDIContainer.job_service])],
):
    return job_service.create_job(user_data.model_dump())


@router.get('/{job_id}', response_model=job_schema.JobResponse)
@inject
def get_job_route(job_id: int, job_service: Annotated[JobService, Depends(Provide[ServiceDIContainer.job_service])]):
    return job_service.get_job_by_id(job_id)
