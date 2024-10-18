from src.database.models import Movie
from src.repositories.base.postgres import PostgresRepository


class MovieRepository(PostgresRepository):
    model = Movie
