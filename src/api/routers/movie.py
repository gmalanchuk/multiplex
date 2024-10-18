from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from src.api.schemas.movie import MovieResponseSchema, MovieRequestSchema

from src.services.movie import MovieService

movie_router = APIRouter(prefix="/v1/movies", tags=["Movies"])


@movie_router.get(path="/", response_model=list[MovieResponseSchema])
async def get_movies(
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.get_movies()


@movie_router.post(path="/", response_model=MovieResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_movie(
        request_movie: MovieRequestSchema,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.create_movie(request_movie)


@movie_router.get(path="/{movie_id}/", response_model=MovieResponseSchema)
async def get_movie(
        movie_id: int,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.get_movie(movie_id)
