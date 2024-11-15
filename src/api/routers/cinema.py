from fastapi import APIRouter, Depends
from starlette import status

from src.api.schemas.cinema import CinemaResponseSchema, CinemaCreateRequestSchema, PaginatedCinemaResponseSchema
from src.pagination import get_pagination_params, paginate_response

from src.services.cinema import CinemaService

cinema_router = APIRouter(prefix="/v1/cinemas", tags=["Cinemas"])


@cinema_router.get(path="/", response_model=PaginatedCinemaResponseSchema)
async def get_cinemas(
        cinema_service: CinemaService = Depends(),
        pagination: tuple[int, int] = Depends(get_pagination_params),
):
    page, size = pagination
    cinemas = await cinema_service.get_cinemas(page, size)
    return await paginate_response(cinemas, page, size, cinema_service)


@cinema_router.post(path="/", response_model=CinemaResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_cinema(
        request_cinema: CinemaCreateRequestSchema,
        cinema_service: CinemaService = Depends(),
):
    return await cinema_service.create_cinema(request_cinema)
