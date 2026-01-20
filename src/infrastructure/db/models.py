import enum

from decimal import Decimal
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Enum, Numeric, DateTime, func, UUID, Integer, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.infrastructure.db import Base


class OrderStatusEnum(str, enum.Enum):
    NEW = "NEW"
    PAID = "PAID"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"


class OrderORM(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    item_id: Mapped[UUID] = mapped_column(UUID, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[OrderStatusEnum] = mapped_column(
        Enum(OrderStatusEnum), default=OrderStatusEnum.NEW
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    update_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"Order number {id}"
