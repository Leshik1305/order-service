from typing import Protocol

from src.application.dtos.order import OrderDTO


class OrdersProtocol(Protocol):
    async def create(self, order: OrderDTO): ...


class Repository(Protocol):
    orders: OrdersProtocol
