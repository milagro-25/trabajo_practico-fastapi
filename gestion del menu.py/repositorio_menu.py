from modelo_menu import Menu, MenuCreate

# Base de datos en memoria
db_menus = []
id_counter = 1

def get_all_menus():
    return db_menus

def get_menu_by_id(menu_id: int):
    return next((menu for menu in db_menus if menu.id == menu_id), "menu")

def create_menu(menu: MenuCreate):
    global id_counter
    new_menu = Menu(id=id_counter, **menu.dict())
    db_menus.append(new_menu)
    id_counter += 1
    return new_menu

def update_menu(menu_id: int, menu_data: MenuCreate):
    menu = get_menu_by_id(menu_id)
    if menu:
        menu.dia = menu_data.dia
        menu.principal = menu_data.principal
        menu.guarnicion = menu_data.guarnicion
        menu.bebida = menu_data.bebida
        menu.postre = menu_data.postre
    return menu

def delete_menu(menu_id: int):
    global db_menus
    menu = get_menu_by_id(menu_id)
    if menu:
        db_menus = [m for m in db_menus if m.id != menu_id]
    return menu