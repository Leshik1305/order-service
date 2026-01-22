from typing import Protocol, Optional, Dict, Any
from uuid import UUID


class CatalogServiceAPIProtocol(Protocol):

    async def check_available_qty(self, item_id: UUID, quantity) -> bool:
        pass
