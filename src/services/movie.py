from src.api.schemas.movie import MovieCreateRequestSchema, MovieUpdateRequestSchema
from src.exceptions import NotFoundException, MovieAlreadyExistsException
from src.repositories.movie import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MovieRepository()

    async def get_movies(self):
        # todo фильтрация, пагинация
        return await self.movie_repository.get_all()

    async def create_movie(self, movie: MovieCreateRequestSchema):
        existing_movie = await self.movie_repository.get_one(name=movie.name)  # todo сделать для этого специальный валидатор
        if existing_movie is not None:
            raise MovieAlreadyExistsException
        return await self.movie_repository.add_one(data=movie.model_dump())

    async def get_movie(self, movie_id: int):
        movie = await self.movie_repository.get_one(id=movie_id)
        if movie is None:
            raise NotFoundException
        return movie

    async def update_movie(self, movie_id: int, movie: MovieUpdateRequestSchema):
        existing_movie = await self.movie_repository.get_one(name=movie.name)  # todo сделать для этого специальный валидатор
        if existing_movie is not None and existing_movie.id != movie_id:
            raise MovieAlreadyExistsException
        update_data = {k: v for k, v in movie.model_dump().items() if v is not None}  # todo временное решение
        movie = await self.movie_repository.update_one(obj_id=movie_id, data=update_data)
        if movie is None:
            raise NotFoundException
        return movie

    async def delete_movie(self, movie_id: int):
        movie = await self.movie_repository.delete_one(id=movie_id)
        if movie is None:
            raise NotFoundException
        return None
