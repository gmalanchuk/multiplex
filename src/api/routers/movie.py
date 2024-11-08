from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from starlette import status

from src.api.schemas.movie import MovieResponseSchema, MovieCreateRequestSchema, MovieUpdateRequestSchema, \
    PaginatedMovieResponseSchema
from src.filters.movie import MovieFilter
from src.pagination import get_pagination_params, paginate_response

from src.services.movie import MovieService

movie_router = APIRouter(prefix="/v1/movies", tags=["Movies"])


@movie_router.get(path="/", response_model=PaginatedMovieResponseSchema)
async def get_movies(
        movie_service: Annotated[MovieService, Depends()],
        pagination: tuple[int, int] = Depends(get_pagination_params),
        filters: MovieFilter = FilterDepends(MovieFilter),
):
    page, size = pagination
    movies = await movie_service.get_movies(page, size, filters)
    return await paginate_response(movies, page, size, movie_service)


@movie_router.post(path="/", response_model=MovieResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_movie(
        request_movie: MovieCreateRequestSchema,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.create_movie(request_movie)


@movie_router.get(path="/{movie_id}/", response_model=MovieResponseSchema)
async def get_movie(
        movie_id: int,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.get_movie(movie_id)


@movie_router.patch(path="/{movie_id}/", response_model=MovieResponseSchema)
async def update_movie(
        movie_id: int,
        request_movie: MovieUpdateRequestSchema,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.update_movie(movie_id, request_movie)


@movie_router.delete(path="/{movie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(
        movie_id: int,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.delete_movie(movie_id)
