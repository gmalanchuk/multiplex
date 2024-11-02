from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from src.api.schemas.movie import AgeCategory
from src.database.models import Movie


class MovieFilter(Filter):
    age_category: Optional[AgeCategory] = None
    release_year: Optional[int] = None
    # todo genre

    class Constants(Filter.Constants):
        model = Movie
