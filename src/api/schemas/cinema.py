from pydantic import BaseModel

from src.api.schemas.pagination import PaginatedResponse


class CinemaCreateRequestSchema(BaseModel):
    name: str
    address: str
    city: str
    phone: str


class CinemaResponseSchema(BaseModel):
    id: int
    name: str
    address: str
    city: str
    phone: str


PaginatedCinemaResponseSchema = PaginatedResponse[CinemaResponseSchema]
