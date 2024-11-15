from datetime import date

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database.models.base import Base, str256, TimeStampMixin


class Movie(Base, TimeStampMixin):
    __tablename__ = "movies"

    name: Mapped[str256] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    age_category: Mapped[int] = mapped_column(nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)
    rental_start_date: Mapped[date] = mapped_column(nullable=False)
    rental_end_date: Mapped[date] = mapped_column(nullable=False)
    # todo рейтинг зрителей
    # todo рейтинг критиков
    genres: Mapped[list[str]] = mapped_column(JSONB, nullable=False)
    # todo какого числа станет доступен в прокате
    duration: Mapped[int] = mapped_column(nullable=False)
