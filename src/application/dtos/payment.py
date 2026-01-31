from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PaymentDTO(BaseModel):
    order_id: UUID
    amount: str
    idempotency_key: str


class PaymentCreateDTO(PaymentDTO):
    pass


class PaymentReadDTO(PaymentDTO):
    id: str
    user_id: str
    status: str
    idempotency_key: str
    created_at: datetime


class PaymentCallbackDTO(BaseModel):
    payment_id: UUID
    order_id: UUID
    status: str
    amount: Decimal
    error_message: Optional[str] = None
