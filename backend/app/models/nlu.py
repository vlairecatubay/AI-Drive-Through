from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class Entity(BaseModel):
    type: str
    value: Any

class NLUResult(BaseModel):
    intent: str
    entities: List[Entity]
    text: str
    confidence: float = 0.9
