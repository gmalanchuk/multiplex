from fastapi import HTTPException
from starlette import status

from src.api.schemas.movie import MovieCreateRequestSchema, MovieUpdateRequestSchema
from src.repositories.movie import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    async def get_movies(self):
        # todo фильтрация, пагинация
        return await self.movie_repository.get_all()

    async def create_movie(self, movie: MovieCreateRequestSchema):
        # todo сделать валидацию, что такой фильм уже есть
        return await self.movie_repository.add_one(data=movie.model_dump())

    async def get_movie(self, movie_id: int):
        movie = await self.movie_repository.get_one(id=movie_id)
        if movie is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")  # todo временное решение
        return movie

    async def update_movie(self, movie_id: int, movie: MovieUpdateRequestSchema):
        # todo сделать валидацию, что такой фильм уже есть
        update_data = {k: v for k, v in movie.model_dump().items() if
                       v is not None}  # todo скорее всего тоже временное решение
        movie = await self.movie_repository.update_one(obj_id=movie_id, data=update_data)
        if movie is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")  # todo временное решение
        return movie

    async def delete_movie(self, movie_id: int):
        movie = await self.movie_repository.delete_one(id=movie_id)
        if movie is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")  # todo временное решение
        return None
