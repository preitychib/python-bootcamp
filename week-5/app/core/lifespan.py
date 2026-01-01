import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .database import Base, engine

logger = logging.getLogger(__name__)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI, create_tables: bool = False) -> AsyncGenerator[None, None]:
    if create_tables:
        logger.info("Initializing database tables")
        await init_db()

    yield

    logger.info("Disposing database engine")
    await engine.dispose()

