from typing import Protocol
from uuid import UUID

from ..dtos.order import OrderCreateDTO


class Orders(Protocol):
    async def check_idempotency_key(self, idempotency_key: UUID): ...

    async def create(self, order: OrderCreateDTO, key: UUID): ...


class Repository(Protocol):
    orders: Orders
