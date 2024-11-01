from src.api.schemas.movie import MovieCreateRequestSchema, MovieUpdateRequestSchema
from src.exceptions import NotFoundException
from src.repositories.movie import MovieRepository
from src.validators.movie import MovieValidator


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()
        self.movie_validator = MovieValidator()

    async def get_movies(self, page: int, size: int):
        # todo сделать фильтрацию
        return await self.movie_repository.get_all(page, size)

    async def create_movie(self, movie: MovieCreateRequestSchema):
        await self.movie_validator.movie_already_exists(movie_name=movie.name)
        return await self.movie_repository.add_one(data=movie.model_dump())

    async def get_movie(self, movie_id: int):
        movie = await self.movie_repository.get_one(id=movie_id)
        if movie is None:
            raise NotFoundException
        return movie

    async def update_movie(self, movie_id: int, movie: MovieUpdateRequestSchema):
        await self.movie_validator.movie_already_exists(movie_name=movie.name, movie_id=movie_id)
        update_data = movie.model_dump(exclude_none=True)
        movie = await self.movie_repository.update_one(obj_id=movie_id, data=update_data)
        if movie is None:
            raise NotFoundException
        return movie

    async def delete_movie(self, movie_id: int):
        movie = await self.movie_repository.delete_one(id=movie_id)
        if movie is None:
            raise NotFoundException
        return None
