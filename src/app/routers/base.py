import sqlalchemy as sa
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException

import database as db
from app.di_container import ServiceDIContainer
from database import SQLDatabase

router = APIRouter()


@router.get('/')
def welcome_route():
    return {'Hello': 'World'}


@router.get('/health')
@inject
def health_check(sql_db: SQLDatabase = Depends(Provide[ServiceDIContainer.sql_db])):
    try:
        with sql_db.session() as session:
            session.execute(sa.text('SELECT 1'))
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
