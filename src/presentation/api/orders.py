from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends


from src.container import Container


from src.application.dtos.order import OrderCreateDTO, OrderDTO
from src.infrastructure.http.http_clients import CreateOrderAPI

router = APIRouter()


@router.post("/orders", status_code=201, response_model=OrderDTO)
@inject
async def create_order(
    order: OrderCreateDTO,
    uc: CreateOrderAPI = Depends(Provide[Container.application.create_order_in_db]),
):
    result = await uc.create(item_id=order.item_id, quantity=order.quantity)
    return result
