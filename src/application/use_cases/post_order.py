from uuid import UUID, uuid4

from src.application.dtos.order import OrderDTO
from src.application.interfaces.http_clients import CreateOrderAPIProtocol


class PostOrderService:
    def __init__(self, client: CreateOrderAPIProtocol):
        self.client = client

    async def create(self, item_id: UUID, quantity: int) -> OrderDTO:

        response = await self.client.create_order(item_id, quantity)

        return response
