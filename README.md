# Trabajo Práctico - FastAPI

Este proyecto es una aplicación desarrollada con **[FastAPI](https://fastapi.tiangolo.com/)** como parte de un trabajo práctico.

#Requisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

#Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/milagro-25/trabajo_practico-fastapi.git
   cd trabajo_practico-fastapi
2_crear y activar un entorno virtual(opcional pero recomendado)
   python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
3_instalar dependencias
pip install -r 
requirements.txt
4_ejecucion del servidor
con uvicorn:
uvicorn app.main:app --reload
#Esquema:
fastapi_menu_secundario/
│── app/
|   |-- __init__.
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── api/
│   │   └── rutas_menu.py    # Endpoints relacionados al menú
│   ├── modelos/
│   │   └── menu.py           # Modelos Pydantic
│   ├── repositories/
│   │   └── menu_repositorio.py # CRUD en memoria
│   ├── servicios/
│   │   └── menu_servicio.py   # Lógica de negocio
