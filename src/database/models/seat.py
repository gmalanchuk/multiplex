from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimeStampMixin, Base


class Seat(Base, TimeStampMixin):
    __tablename__ = "seats"

    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id"), nullable=False)
    seat_number: Mapped[int] = mapped_column(nullable=False)
