from pydantic import BaseModel


class MovieRequestSchema(BaseModel):
    name: str
    description: str
    age_restrictions: int
    release_year: int
    rating: float
    duration: int


class MovieResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    age_restrictions: int
    release_year: int
    rating: float
    duration: int
