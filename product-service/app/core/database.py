import os
from sys import modules

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlmodel.ext.asyncio.session import AsyncSession
from dotenv import load_dotenv
import os


database_uri = os.getenv('DATABASE_URI')
if "pytest" in modules:
    database_uri = database_uri

async_engine = create_async_engine(
    database_uri,
    echo=True,
    future=True
)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
