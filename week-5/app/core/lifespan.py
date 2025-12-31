from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from .database import async_session, Base, engine

async def init_db() -> None:
    """Initialize database tables if they don't exist."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI, create_tables: bool = False) -> AsyncGenerator[None, None]:
    """Manage application startup and shutdown events.
    
    Args:
        app: The FastAPI application instance
        create_tables: Whether to create database tables on startup
    """
    if create_tables:
        await init_db()
    
    yield
    
    # Clean up resources on shutdown if needed
    await engine.dispose()
