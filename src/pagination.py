from fastapi import Query

async def paginate(
        page: int = Query(ge=1, default=1),
        size: int = Query(ge=1, le=100, default=10)
):
    return page, size
