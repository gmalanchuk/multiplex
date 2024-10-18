from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.api.schemas.movie import MovieResponseSchema, MovieRequestSchema
from src.database.models import Movie

from src.database.session import get_async_session
from src.services.movie import MovieService

movie_router = APIRouter(prefix="/v1/movies", tags=["Movies"])


@movie_router.get(path="/", response_model=list[MovieResponseSchema])
async def get_movies(session: AsyncSession = Depends(get_async_session)): # todo сделать фильтрацию
    # todo удалить тогда сессию. чтобы она не создавалась в файле session.py
    result = await session.execute(select(Movie))
    movies = result.scalars().all()
    return movies


@movie_router.post(path="/", response_model=MovieResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_movie(
        request_movie: MovieRequestSchema,
        movie_service: Annotated[MovieService, Depends()],
):
    return await movie_service.create_movie(request_movie)
