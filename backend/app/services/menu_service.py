import json
from pathlib import Path
from typing import List
from ..models.menu import MenuItem

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "menu_sample.json"

_menu_cache: List[MenuItem] = []

def _load_menu():
    global _menu_cache
    if not _menu_cache:
        items = json.loads(Path(DATA_PATH).read_text(encoding="utf-8"))
        _menu_cache = [MenuItem(**i) for i in items]
    return _menu_cache

def get_menu() -> List[MenuItem]:
    return _load_menu()

def add_menu_item(item: MenuItem) -> MenuItem:
    menu = _load_menu()
    menu.append(item)
    # Persist for demo
    Path(DATA_PATH).write_text(json.dumps([i.dict() for i in menu], indent=2), encoding="utf-8")
    return item

def find_item(item_id: str) -> MenuItem | None:
    for i in _load_menu():
        if i.id == item_id:
            return i
    return None

def find_by_name_or_alias(name: str) -> MenuItem | None:
    name = name.lower()
    for i in _load_menu():
        if i.name.lower() == name or name in [a.lower() for a in (i.aliases or [])]:
            return i
    return None
