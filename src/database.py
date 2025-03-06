from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app import JobAnalysis, ResumeAnalysis
from config import get_settings

settings = get_settings()

async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

engine = create_engine(settings.SYNC_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


client = AsyncIOMotorClient(settings.MONGODB_URI)
database = client.get_database(settings.MONGODB_NAME)


async def mongo_init_beanie():
    await init_beanie(database, document_models=[JobAnalysis, ResumeAnalysis])


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
