import sqlalchemy as sa
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import database as db

router = APIRouter()


@router.get('/')
async def welcome_route():
    return {'Hello': 'World'}


@router.get('/health')
async def health_check(db: AsyncSession = Depends(db.get_db)):
    try:
        await db.execute(sa.text('SELECT 1'))
        return {'message': 'Connected to PostgreSQL'}
    except Exception as e:
        return {'error': str(e)}


@router.get('/mongo-health')
async def mongo_health_check():
    try:
        await db.database.command('ping')
        return {'status': 'Connected to MongoDB'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'MongoDB connection error: {str(e)}')
