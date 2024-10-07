from enum import Enum

from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database.models.base import Base, str256, TimeStampMixin


class AgeRestrictionsEnum(Enum):
    ZERO = 0
    SIX = 6
    TWELVE = 12
    SIXTEEN = 16
    EIGHTEEN = 18


class Movie(Base, TimeStampMixin):
    __tablename__ = "movies"

    name: Mapped[str256] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    age_restrictions: Mapped[AgeRestrictionsEnum] = mapped_column(SqlEnum(AgeRestrictionsEnum), nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)  # todo не больше текущего года
    rating: Mapped[float] = mapped_column(nullable=True)  # todo от 0 до 10
    duration: Mapped[int] = mapped_column(nullable=False)
