from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.dtos.order import OrderDTO
from src.application.interfaces.repositories import OrdersProtocol
from src.application.use_cases.create_order_in_db import OrderPersister
from src.domain.value_objects.order_status import OrderStatusEnum
from src.infrastructure.db.models import OrderORM


class Orders:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, order: OrderDTO):
        await self.session.execute(
            insert(OrderORM).values(
                id=order.id,
                item_id=order.item_id,
                quantity=order.quantity,
                status=OrderStatusEnum.NEW,
                created_at=order.created_at,
                update_at=order.update_at,
            ),
        )
