import sqlalchemy as sa
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db

router = APIRouter()


@router.get('/')
async def welcome_route():
    return {'Hello': 'World'}


@router.get('/health')
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(sa.text('SELECT 1'))
        return {'message': 'Connected to PostgreSQL'}
    except Exception as e:
        return {'error': str(e)}
