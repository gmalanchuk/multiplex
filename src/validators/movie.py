from typing import NoReturn

from src.exceptions import MovieAlreadyExistsException
from src.repositories.movie import MovieRepository


class MovieValidator:
    def __init__(self):
        self.movie_repository = MovieRepository()

    async def movie_already_exists(self, movie_name: str, movie_id: int = None) -> None or NoReturn:
        existing_movie = await self.movie_repository.get_one(name=movie_name)
        if existing_movie is not None and (movie_id is None or existing_movie.id != movie_id):
            raise MovieAlreadyExistsException
