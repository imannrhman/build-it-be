

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from dotenv import load_dotenv
import os

load_dotenv()

database_uri = os.getenv('DATABASE_URI')

async_engine = create_async_engine(
    "postgresql+asyncpg://auth_admin:auth_admin@auth-db/auth_db_dev",
    echo=True,
    future=True
)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
