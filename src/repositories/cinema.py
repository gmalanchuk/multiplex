from src.database.models import Cinema
from src.repositories.base.postgres import PostgresRepository


class CinemaRepository(PostgresRepository):
    model = Cinema
