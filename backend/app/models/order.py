from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class OrderItem(BaseModel):
    item_id: str
    qty: int = 1
    size: Optional[str] = None
    mods: Optional[List[str]] = None
    notes: Optional[str] = None

class Money(BaseModel):
    subtotal: float = 0.0
    tax: float = 0.0
    total: float = 0.0

class Order(BaseModel):
    id: str
    lane: str = "DT-1"
    items: List[OrderItem]
    amounts: Money = Field(default_factory=Money)
    status: str = "created"
