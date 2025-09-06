from modelos.modelo_menu import MenuCreate
from repositorios.repositorio_menu import menu_repository

def listar_menus():
    return menu_repository.get_all_menus()

def obtener_menu(menu_id: int):
    return menu_repository.get_menu_by_id(menu_id)

def crear_menu(menu: MenuCreate):
    return menu_repository.create_menu(menu)

def actualizar_menu(menu_id: int, menu: MenuCreate):
    return menu_repository.update_menu(menu_id, menu)

def eliminar_menu(menu_id: int):
    return menu_repository.delete_menu(menu_id) 