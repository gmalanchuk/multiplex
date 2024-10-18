from src.api.schemas.movie import MovieRequestSchema
from src.repositories.movie import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    async def get_movies(self):
        # todo фильтрация, пагинация
        return await self.movie_repository.get_all()

    async def create_movie(self, movie: MovieRequestSchema):
        # todo сделать валидацию, что такой фильм уже есть
        return await self.movie_repository.add_one(movie.model_dump())
