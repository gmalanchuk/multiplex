from datetime import datetime

from sqlalchemy import DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimeStampMixin, Base


class Screening(Base, TimeStampMixin):
    __tablename__ = "screenings"

    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), nullable=False)
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime] = mapped_column(nullable=False)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 2), nullable=False)
