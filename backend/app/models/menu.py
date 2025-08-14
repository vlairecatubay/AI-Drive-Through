from pydantic import BaseModel
from typing import Optional, List, Dict

class Modifier(BaseModel):
    id: str
    type: str  # 'add' | 'remove' | 'swap'
    label: str
    price: Optional[float] = 0.0

class MenuItem(BaseModel):
    id: str
    name: str
    aliases: List[str] = []
    base_price: float
    sizes: Optional[List[str]] = None
    size_price_deltas: Optional[Dict[str, float]] = None
    modifiers: Optional[List[Modifier]] = None
    tags: Optional[List[str]] = None
    availability: Optional[dict] = None
