from fastapi import APIRouter
from ..services import menu_service
from ..models.menu import MenuItem

router = APIRouter()

@router.get("/", response_model=list[MenuItem])
def get_menu():
    return menu_service.get_menu()

@router.post("/", response_model=MenuItem)
def add_menu_item(item: MenuItem):
    return menu_service.add_menu_item(item)
