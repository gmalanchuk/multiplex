from fastapi import Query
from sqlalchemy import select, func

from src.database.models import Movie
from src.database.session import async_session


async def get_pagination_params(
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=10)
):
    return page, size


async def paginate_response(movies, page, size):
    async with async_session() as session:
        result = await session.execute(select(func.count()).select_from(Movie))
        total = result.scalar()

    return {
        "items": movies,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size
    }
