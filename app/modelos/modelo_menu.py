from pydantic import BaseModel

class MenuBase(BaseModel):
    id: int
    dia: str
    principal: str
    guarnicion: str
    bebida: str
    postre: str

class MenuCreate(MenuBase):
    Lista=[{
    "id": 1,
    "dia": "Lunes",
    "principal": "Milanesa con puré",
    "guarnicion": "Ensalada de tomate",
    "bebida": "Agua",
    "postre": "Fruta"}]

class Menu(MenuBase):
    id: int