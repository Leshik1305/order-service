import typing
from uuid import UUID

from src.application.dtos.order import OrderCreateDTO, OrderDTO
from src.application.interfaces.http_clients import CreateOrderAPIProtocol
from src.application.interfaces.uow import UnitOfWork
from src.application.use_cases.check_available_qty import CheckAvailabilityUseCase


class CreateOrderUseCase:
    def __init__(
        self,
        uow: UnitOfWork,
        catalog: CreateOrderAPIProtocol,
        available_qty: CheckAvailabilityUseCase,
    ):
        self.uow = uow
        self.catalog = catalog
        self.available_qty = available_qty

    async def create_order(self, item_id: UUID, quantity: int):
        if await self.available_qty(item_id, quantity):

        request_body = {
            "item_id": str(item_id),
            "quantity": quantity,
            "idempotency_key": str(idempotency_key)
        }

        external_data = await self.catalog.initialize_remote_order(request_body)


        async with self.uow:
            # Проверка на дубликат по ключу идемпотентности перед записью
            existing = await self.uow.orders.get_by_idempotency_key(idempotency_key)
            if existing:
                return existing

            # Создаем доменную модель, используя данные из ответа внешней системы
            order = Order(
                user_id=user_id,
                item_id=item_id,
                quantity=quantity,
                idempotency_key=idempotency_key,
                status=OrderStatus.NEW
                # Здесь можно добавить поля из external_data, например:
                # remote_reference=external_data["remote_id"]
            )

            await self.uow.orders.add(order)
            await self.uow.commit()

            return order
