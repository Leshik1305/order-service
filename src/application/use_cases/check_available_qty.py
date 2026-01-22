from uuid import UUID

from src.application.interfaces.http_clients import CatalogServiceAPIProtocol


class CheckAvailabilityUseCase:
    def __init__(self, catalog: CatalogServiceAPIProtocol):
        self._catalog = catalog

    async def execute(self, item_id: UUID, quantity: int) -> bool:

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        return await self._catalog.check_available_qty(item_id, quantity)
