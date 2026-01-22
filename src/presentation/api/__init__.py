import fastapi

from src.presentation.api import orders
from src.presentation.api import new_orders

router = fastapi.APIRouter(prefix="/api")
router.include_router(orders.router)
