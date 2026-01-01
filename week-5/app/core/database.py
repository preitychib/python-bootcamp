from typing import AsyncGenerator, cast

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base

from .config import settings

DATABASE_URI = cast(str, settings.DATABASE_URI)
engine = create_async_engine(
    DATABASE_URI,
    echo=True,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

