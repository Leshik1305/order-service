from uuid import UUID

from src.application.use_cases.check_available_qty import CheckAvailabilityUseCase
from src.application.use_cases.create_order_in_db import OrderPersister
from src.application.use_cases.post_order import PostOrderService


class CreateOrderUseCase:
    def __init__(
        self,
        validator: CheckAvailabilityUseCase,
        service: PostOrderService,
        db: OrderPersister,
    ):
        self.validator = validator
        self.service = service
        self.db = db

    async def execute(self, item_id: UUID, quantity: int):

        item_data = await self.validator.check_available_qty(item_id, quantity)

        response = await self.service.create(item_id, quantity)

        return await self.db.create(response)
