from src.database.models.base import TimeStampMixin, Base


class Payment(Base, TimeStampMixin):
    __tablename__ = "payments"

    pass
