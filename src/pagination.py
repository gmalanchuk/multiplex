import importlib

from fastapi import Query
from sqlalchemy import select, func

from src.database.session import async_session


async def get_pagination_params(
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=10)
):
    return page, size


async def paginate_response(items: list, page: int, size: int, service) -> dict:
    """
    Paginates the response for a given list of items.

    Args:
        items (list): The list of items to paginate.
        page (int): The current page number.
        size (int): The number of items per page.
        service: The service instance used to determine the model.

    Returns:
        dict: A dictionary containing paginated response data including items, total count, current page, page size, and total pages.
    """
    model_name = service.__class__.__name__.replace('Service', '')
    model_module = importlib.import_module(f'src.database.models')
    model = getattr(model_module, model_name)

    async with async_session() as session:
        result = await session.execute(select(func.count()).select_from(model))
        total = result.scalar()

    return {
        "items": items,
        "total": total,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size
    }
