from typing import Dict, List
from . import menu_service
from ..models.order import Order, OrderItem, Money
from ..models.menu import MenuItem

TAX_RATE = 0.12  # 12% VAT demo

def price_item(menu_item: MenuItem, order_item: OrderItem) -> float:
    price = menu_item.base_price
    if order_item.size and menu_item.size_price_deltas:
        price += menu_item.size_price_deltas.get(order_item.size, 0.0)
    # Mods
    if order_item.mods and menu_item.modifiers:
        mod_map = {m.id: m for m in menu_item.modifiers}
        for mod in order_item.mods:
            if mod in mod_map:
                price += float(mod_map[mod].price or 0.0)
    return price * order_item.qty

def build_amounts(items: List[OrderItem]) -> Money:
    subtotal = 0.0
    for oi in items:
        mi = menu_service.find_item(oi.item_id)
        if not mi:
            continue
        subtotal += price_item(mi, oi)
    tax = round(subtotal * TAX_RATE, 2)
    total = round(subtotal + tax, 2)
    return Money(subtotal=round(subtotal, 2), tax=tax, total=total)

def validate_items(items: List[OrderItem]) -> List[str]:
    errors = []
    for oi in items:
        mi = menu_service.find_item(oi.item_id)
        if not mi:
            errors.append(f"Unknown item_id: {oi.item_id}")
            continue
        if oi.size and mi.sizes and oi.size not in mi.sizes:
            errors.append(f"Invalid size '{oi.size}' for {mi.name}")
    return errors

def create_order(order_id: str, items: List[OrderItem], lane: str = "DT-1") -> Order:
    errs = validate_items(items)
    if errs:
        raise ValueError("; ".join(errs))
    amounts = build_amounts(items)
    return Order(id=order_id, items=items, lane=lane, amounts=amounts, status="kitchen_fired")
