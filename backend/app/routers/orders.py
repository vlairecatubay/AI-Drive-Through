from fastapi import APIRouter, HTTPException
from ..models.order import OrderItem, Order
from ..services import order_service, recommender, kitchen
import uuid

router = APIRouter()

@router.post("/preview")
def preview_order(items: list[OrderItem]):
    amounts = order_service.build_amounts(items)
    upsells = recommender.suggest_upsell(items)
    return {"amounts": amounts.dict(), "upsells": upsells}

@router.post("/confirm", response_model=Order)
def confirm_order(items: list[OrderItem]):
    order_id = f"ORD-{uuid.uuid4().hex[:8]}"
    try:
        order = order_service.create_order(order_id, items)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # fire to KDS
    kds = kitchen.fire_to_kitchen(order.dict())
    order.status = "kitchen_fired"
    return order
