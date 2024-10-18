from datetime import datetime
from typing import Annotated

from sqlalchemy import func, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


str16 = Annotated[int, 16]
str64 = Annotated[int, 64]
str256 = Annotated[int, 256]


class Base(DeclarativeBase):
    """Base model class from which other models inherit"""
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    type_annotation_map = {
        str16: String(16),
        str64: String(64),
        str256: String(256),
    }


class TimeStampMixin:
    """Mixin class for adding timestamps to a model"""
    created_at: Mapped[datetime] = mapped_column(index=True, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), server_onupdate=func.now(), nullable=False)
