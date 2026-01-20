from src.application.dtos.order import OrderDTO
from src.application.interfaces.uow import UnitOfWork
from src.domain.entities.order import OrderEntity


class OrderPersister:
    def __init__(
        self,
        uow: UnitOfWork,
    ):
        self.uow = uow

    async def create(self, order: OrderDTO) -> None:
        async with self.uow.init() as repo:
            await repo.orders.create(order)
