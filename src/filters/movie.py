from typing import Optional

from src.api.schemas.movie import AgeCategory
from src.filters.base import BaseFilter


class MovieFilter(BaseFilter):
    def __init__(
        self,
        age_category: Optional[AgeCategory] = None,
        release_year: Optional[int] = None
    ):
        self.age_category = age_category
        self.release_year = release_year
        # todo genres