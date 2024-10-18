from sqlalchemy import select

from src.database.models.base import Base
from src.database.session import async_session
from src.repositories.base.abstract import AbstractRepository


class PostgresRepository(AbstractRepository):
    model = type[Base]

    async def get_all(self):
        async with async_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.scalars().all()

    async def get_one(self, **kwargs):
        async with async_session() as session:
            query = select(self.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def add_one(self, data: dict):
        async with async_session() as session:
            obj = self.model(**data)
            session.add(obj)
            await session.commit()
            return obj
