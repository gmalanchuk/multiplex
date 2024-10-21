from datetime import datetime, date
from enum import Enum
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from starlette import status


class AgeCategory(int, Enum):
    zero = 0
    six = 6
    twelve = 12
    sixteen = 16
    eighteen = 18


class BaseMovieSchema(BaseModel):
    @field_validator('release_year', check_fields=False)
    def validate_release_year(cls, release_year: int):
        current_year = datetime.now().year
        if release_year > current_year:
            raise HTTPException(
                detail='Release year cannot be greater than the current year', status_code=status.HTTP_400_BAD_REQUEST
            )
        return release_year

    class Config:
        use_enum_values = True


class MovieCreateRequestSchema(BaseMovieSchema):
    name: str
    description: str
    age_category: AgeCategory
    release_year: int
    rental_start_date: date
    rental_end_date: date
    duration: int


class MovieUpdateRequestSchema(BaseMovieSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    age_category: Optional[AgeCategory] = None
    release_year: Optional[int] = None
    rental_start_date: Optional[date] = None
    rental_end_date: Optional[date] = None
    duration: Optional[int] = None


class MovieResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    age_category: int
    release_year: int
    rental_start_date: date
    rental_end_date: date
    duration: int
