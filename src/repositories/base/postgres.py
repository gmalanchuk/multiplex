from sqlalchemy import select

from src.database.models.base import Base
from src.database.session import async_session
from src.filters.movie import BaseFilter
from src.repositories.base.abstract import AbstractRepository


class PostgresRepository(AbstractRepository):
    model = type[Base]

    async def get_all(self, page: int, size: int, filters: BaseFilter):
        async with async_session() as session:
            query = select(self.model).offset((page - 1) * size).limit(size).order_by(self.model.id)
            filters = filters.to_dict()
            if filters:
                for key, value in filters.items():
                    if key == 'genres' and isinstance(value, list):
                        for genre in value:
                            query = query.filter(self.model.genres.contains([genre]))
                    else:
                        query = query.filter(getattr(self.model, key) == value)
            result = await session.execute(query)
            return result.scalars().all()

    async def add_one(self, data: dict):
        async with async_session() as session:
            obj = self.model(**data)
            session.add(obj)
            await session.commit()
            return obj

    async def get_one(self, **kwargs):
        async with async_session() as session:
            query = select(self.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def update_one(self, obj_id: int, data: dict):
        obj = await self.get_one(id=obj_id)
        if obj is None:
            return None
        for key, value in data.items():
            setattr(obj, key, value)
        async with async_session() as session:
            session.add(obj)
            await session.commit()
        return obj

    async def delete_one(self, **kwargs):
        obj = await self.get_one(**kwargs)
        if obj is None:
            return None
        async with async_session() as session:
            await session.delete(obj)
            await session.commit()
        return obj
