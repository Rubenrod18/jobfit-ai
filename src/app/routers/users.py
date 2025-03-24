import logging
from typing import Annotated

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status

from app.di_container import ServiceDIContainer
from app.schemas import user as user_schema
from app.services.user_service import UserService

router = APIRouter(prefix='/users', tags=['users'])
logging.basicConfig(level=logging.DEBUG)


@router.post('/', response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
@inject
def create_user(
    user_data: user_schema.UserCreate,
    user_service: Annotated[UserService, Depends(Provide[ServiceDIContainer.user_service])],
):
    """Create a new user."""
    return user_service.create_user(user_data.model_dump())


@router.get('/{user_id}', response_model=user_schema.UserResponse)
@inject
def get_user_api(user_id: int, user_service: Annotated[UserService, Depends(Provide[ServiceDIContainer.user_service])]):
    return user_service.get_user_by_id(user_id)


""" TODO: HERE
@router.put("/users/{user_id}", response_model=UserUpdateSchema)
async def update_user(user_id: int, user_data: UserUpdateSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update user fields
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    await session.commit()
    await session.refresh(user)  # Refresh to get the latest data

    return user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await session.delete(user)
    await session.commit()

    return {"message": "User deleted successfully"}
"""
