from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimeStampMixin, Base, str256, str16, str64


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    username: Mapped[str16] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    full_name: Mapped[str256]
    hashed_password: Mapped[str64] = mapped_column(nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False, default=False)
