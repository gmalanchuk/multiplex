from enum import Enum

from sqlalchemy import Enum as SqlEnum, DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import TimeStampMixin, Base


class TicketStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"


class Ticket(Base, TimeStampMixin):
    __tablename__ = "tickets"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    screening_id: Mapped[int] = mapped_column(ForeignKey("screenings.id"), nullable=False)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"), nullable=False)
    status: Mapped[TicketStatus] = mapped_column(SqlEnum(TicketStatus), default=TicketStatus.PENDING, nullable=False)
    price: Mapped[DECIMAL] = mapped_column(DECIMAL(5, 2), nullable=False)
