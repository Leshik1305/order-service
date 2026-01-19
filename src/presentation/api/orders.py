import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, HTTPException
from pydantic import BaseModel

from src.application.use_cases.post_order import PostOrderService
from src.container import Container
from src.controller.api import auth
from src.entity import Notification, NotificationId, OwnerId

from src.application.dtos.order import OrderCreateDTO, OrderDTO

router = APIRouter()


@router.post("/orders", status_code=201, response_model=OrderDTO)
@inject
async def create_order(
    order: OrderCreateDTO,
    uc: PostOrderService = Depends(Provide[Container.infrastructure.create_order_api]),
):
    status_code, result = await uc.execute(
        user_id=item.user_id,
        item_id=item.item_id,
        quantity=item.quantity,
        key=item.idempotency_key,
    )

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result)

    return result
