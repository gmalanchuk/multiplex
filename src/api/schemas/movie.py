from enum import  Enum

from pydantic import BaseModel


class AgeCategory(int, Enum):
    zero = 0
    six = 6
    twelve = 12
    sixteen = 16
    eighteen = 18


class MovieRequestSchema(BaseModel):
    name: str
    description: str
    age_category: AgeCategory
    release_year: int
    duration: int

    class Config:
        use_enum_values = True


class MovieResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    age_category: int
    release_year: int
    rating: float | None
    duration: int
