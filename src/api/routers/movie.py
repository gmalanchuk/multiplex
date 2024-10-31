from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from starlette import status

from src.api.schemas.movie import MovieResponseSchema, MovieCreateRequestSchema, MovieUpdateRequestSchema

from src.services.movie import MovieService

movie_router = APIRouter(prefix="/v1/movies", tags=["Movies"])


@movie_router.get(path="/", response_model=Page[MovieResponseSchema])
async def get_movies(
        movie_service: Annotated[MovieService, Depends()],
):
    movies = await movie_service.get_movies()
    return paginate(movies)


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
