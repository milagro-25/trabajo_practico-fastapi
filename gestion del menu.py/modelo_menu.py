from pydantic import BaseModel
# from typing import List

class MenuBase(BaseModel):
    dia: str
    principal: str
    guarnicion: str
    bebida: str
    postre: str

class MenuCreate(MenuBase):
    lista=[
  {
    "id": 1,
    "dia": "Lunes",
    "principal": "Milanesa con puré",
    "guarnicion": "Ensalada de tomate",
    "bebida": "Agua",
    "postre": "Fruta"}]

class Menu(MenuBase):
    id: int