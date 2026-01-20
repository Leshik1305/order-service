from typing import Protocol, Optional, Dict, Any
from uuid import UUID


class CreateOrderAPIProtocol(Protocol):

    async def create_order(self, item_id: UUID, quantity: int):
        pass


class CatalogServiceAPIProtocol(Protocol):
    async def get_item_by_id(self, item_id: UUID):
        pass

    async def check_available_qty(self, item_id: UUID, quantity) -> bool:
        pass
