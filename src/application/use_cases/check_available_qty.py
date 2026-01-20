from uuid import UUID

from src.application.exceptions import ItemNotFoundError
from src.application.interfaces.http_clients import CatalogServiceAPIProtocol


class CheckAvailabilityUseCase:
    def __init__(self, catalog: CatalogServiceAPIProtocol):
        self.catalog = catalog

    async def check_available_qty(self, item_id: UUID, quantity: int) -> bool:
        item = await self.catalog.get_item_by_id(item_id)
        if not item:
            raise ItemNotFoundError(f"Item {item_id} does not exist")

        if item.available_qty < quantity:
            raise ValueError("Insufficient quantity")
        else:
            return True
