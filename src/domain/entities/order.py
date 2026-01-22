from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from ..value_objects.order_status import OrderStatusEnum


class OrderEntity(BaseModel):
    id: UUID
    item_id: UUID
    quantity: int
    amount: Decimal
    status: OrderStatusEnum = OrderStatusEnum.NEW
    created_at: datetime
    update_at: datetime
