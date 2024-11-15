from typing import Optional

from fastapi import Query

from src.api.schemas.movie import AgeCategory
from src.filters.base import BaseFilter


class MovieFilter(BaseFilter):
    def __init__(
        self,
        age_category: Optional[AgeCategory] = Query(default=None),
        release_year: Optional[int] = Query(default=None),
        genres: Optional[list[str]] = Query(default=None),
    ):
        self.age_category = age_category
        self.release_year = release_year
        self.genres = genres
