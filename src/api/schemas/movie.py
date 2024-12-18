from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from src.api.schemas.pagination import PaginatedResponse


class AgeCategory(int, Enum):
    zero = 0
    six = 6
    twelve = 12
    sixteen = 16
    eighteen = 18


class MovieCreateRequestSchema(BaseModel):
    name: str
    description: str
    age_category: AgeCategory
    release_year: int
    rental_start_date: date
    rental_end_date: date
    genres: list[str]
    duration: int

    class Config:
        use_enum_values = True


class MovieUpdateRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    age_category: Optional[AgeCategory] = None
    release_year: Optional[int] = None
    rental_start_date: Optional[date] = None
    rental_end_date: Optional[date] = None
    genres: Optional[list[str]] = None
    duration: Optional[int] = None

    class Config:
        use_enum_values = True


class MovieResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    age_category: int
    release_year: int
    rental_start_date: date
    rental_end_date: date
    genres: list[str]
    duration: int


PaginatedMovieResponseSchema = PaginatedResponse[MovieResponseSchema]
