from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from src.database.models.base import TimeStampMixin, Base, str256


class Hall(Base, TimeStampMixin):
    __tablename__ = "halls"

    cinema_id: Mapped[int] = mapped_column(ForeignKey("cinemas.id"), nullable=False)
    name: Mapped[str256] = mapped_column(nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
