from fastapi import APIRouter, HTTPException
from typing import List
from modelos.modelo_menu import Menu, MenuCreate
from servicios.servicios_menu import menu_service

router = APIRouter(prefix="/menus", tags=["menus"])

@router.get("/", response_model=List[Menu])
def get_menus():
    return menu_service.listar_menus()

@router.get("/{menu_id}", response_model=Menu)
def get_menu(menu_id: int):
    menu = menu_service.obtener_menu(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menú no encontrado")
    return menu

@router.post("/", response_model=Menu, status_code=201)
def create_menu(menu: MenuCreate):
    return menu_service.crear_menu(menu)

@router.put("/{menu_id}", response_model=Menu)
def update_menu(menu_id: int, menu: MenuCreate):
    updated = menu_service.actualizar_menu(menu_id, menu)
    if not updated:
        raise HTTPException(status_code=404, detail="Menú no encontrado")
    return updated

@router.delete("/{menu_id}", response_model=Menu)
def delete_menu(menu_id: int):
    deleted = menu_service.eliminar_menu(menu_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Menú no encontrado")
    return deleted