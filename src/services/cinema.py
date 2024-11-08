from src.repositories.cinema import CinemaRepository


class CinemaService:
    def __init__(self):
        self.cinema_repository = CinemaRepository()

    async def get_cinemas(self, page: int, size: int):
        return await self.cinema_repository.get_all(page, size)

    async def create_cinema(self, cinema):
        return await self.cinema_repository.add_one(data=cinema.model_dump())
