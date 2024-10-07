from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database.models.base import Base, str256, TimeStampMixin


class Movie(Base, TimeStampMixin):
    __tablename__ = "movies"

    name: Mapped[str256] = mapped_column(nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    age_restrictions: Mapped[int] = mapped_column(nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False) # todo не больше текущего года
    rating: Mapped[float] = mapped_column(nullable=True) # todo от 0 до 10
    duration: Mapped[int] = mapped_column(nullable=False)
