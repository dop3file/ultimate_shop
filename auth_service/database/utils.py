from sqlalchemy.ext.asyncio import AsyncSession, async_session

from .database import SessionLocal


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session