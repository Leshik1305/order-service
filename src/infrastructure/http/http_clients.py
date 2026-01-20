from typing import Optional
from uuid import UUID, uuid4

import httpx

from src.application.dtos.item import ItemDTO
from src.application.dtos.order import OrderDTO
from src.application.exceptions import (
    ItemNotFoundError,
    IdempotencyConflictError,
    IsAvailableQtyError,
)
from src.application.interfaces.http_clients import (
    CatalogServiceAPIProtocol,
    CreateOrderAPIProtocol,
)


class CatalogServiceAPI(CatalogServiceAPIProtocol):

    def __init__(self, base_url: str, api_key: str):
        self._base_url = base_url
        self._api_key = api_key
        self._client = httpx.AsyncClient()

    async def get_item_by_id(self, item_id: UUID) -> Optional[ItemDTO]:
        response = await self._client.get(
            f"{self._base_url}/api/catalog/items/{item_id}",
            headers={"X-API-Key": self._api_key},
        )
        if response.status_code == 404:
            raise ItemNotFoundError
        response.raise_for_status()
        data = response.json()
        item = ItemDTO(**data)
        return item

    async def check_available_qty(self, item_id: UUID, quantity: int) -> bool:
        item = await self.get_item_by_id(item_id)
        if not item:
            return False
        return item.available_qty >= quantity


class CreateOrderAPI(CreateOrderAPIProtocol):
    def __init__(
        self, base_url: str, api_key: str, catalog_service: CatalogServiceAPIProtocol
    ):
        self._base_url = base_url
        self._api_key = api_key
        self._catalog_service = catalog_service
        self._client = httpx.AsyncClient()

    async def create(self, item_id: UUID, quantity: int):
        is_available = await self._catalog_service.check_available_qty(
            item_id, quantity
        )

        if not is_available:
            raise IsAvailableQtyError(
                f"Item does not have enough quantity ({quantity})"
            )
        key = uuid4()
        payload = {
            "quantity": quantity,
            "item_id": str(item_id),
            "idempotency_key": str(key),
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self._base_url}/api/orders",
                    json=payload,
                    headers={"X-API-Key": self._api_key},
                )
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 409:
                    raise IdempotencyConflictError(
                        f"Idempotency conflict for key {key}. "
                        f"Server response: {e.response.text}"
                    )
                raise e
            except httpx.RequestError as e:

                raise Exception(f"Network error: {str(e)}")

            else:
                data = response.json()
                order = OrderDTO(**data)
                return order
