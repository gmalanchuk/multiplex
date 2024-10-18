from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base, TimeStampMixin, str256


class Cinema(Base, TimeStampMixin):
    __tablename__ = "cinemas"

    name: Mapped[str256] = mapped_column(nullable=False)
    address: Mapped[str256] = mapped_column(nullable=False)
    city: Mapped[str256] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
