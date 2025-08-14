from fastapi import APIRouter
from pydantic import BaseModel
from ..models.nlu import NLUResult, Entity
from ..services import menu_service
import re

router = APIRouter()

class NLUInput(BaseModel):
    text: str

@router.post("/parse", response_model=NLUResult)
def nlu_parse(inp: NLUInput):
    return parse_text(inp.text)

# ---- simple parser for demo ----
SIZE_WORDS = {"small","regular","medium","large","xl","extra large"}

def parse_text(text: str) -> NLUResult:
    lowered = text.lower()
    # intent detection (very naive, for demo)
    intent = "order_item" if any(w in lowered for w in ["order","get","i'll have","i want","give me"]) or any(mi.name.lower() in lowered for mi in menu_service.get_menu()) else "unknown"

    entities = []
    # quantity
    m_qty = re.search(r"(?:^|\s)(\d+)\s", lowered)
    if m_qty:
        entities.append(Entity(type="quantity", value=int(m_qty.group(1))))

    # size
    for s in SIZE_WORDS:
        if s in lowered:
            entities.append(Entity(type="size", value="medium" if s=="regular" else s))
            break

    # menu item by alias or name
    for mi in menu_service.get_menu():
        names = [mi.name.lower()] + [a.lower() for a in (mi.aliases or [])]
        for n in names:
            if n in lowered:
                entities.append(Entity(type="menu_item", value=mi.id))
                break

    # modifiers (simple keywords)
    if "no pickle" in lowered or "no pickles" in lowered:
        entities.append(Entity(type="modifier", value="no_pickles"))
    if "extra cheese" in lowered:
        entities.append(Entity(type="modifier", value="extra_cheese"))
    if "diet" in lowered:
        entities.append(Entity(type="flavor", value="diet"))

    return NLUResult(intent=intent, entities=entities, text=text, confidence=0.75 if intent=="order_item" else 0.4)
