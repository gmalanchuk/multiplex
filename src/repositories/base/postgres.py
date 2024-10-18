from src.database.models.base import Base
from src.database.session import async_session
from src.repositories.base.abstract import AbstractRepository


class PostgresRepository(AbstractRepository):
    model = type[Base]

    async def get_one(self, model_field: str, value: str):
        pass
    #     async with async_session() as session:
    #         field = getattr(self.model, model_field)
    #         query = select(self.model).where(field == value)
    #         return (await session.execute(query)).scalars().first()


    async def add_one(self, data: dict):
        async with async_session() as session:
            obj = self.model(**data)
            session.add(obj)
            await session.commit()
            return obj
