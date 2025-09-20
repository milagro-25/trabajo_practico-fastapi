from fastapi import FastAPI
from . import models
from . import database
from .routers import miembros, personal, membresias, pagos, asistencias, progreso, reportes

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=database.engine)

# Inicializar aplicación FastAPI
app = FastAPI(
    title="Gestión de Gimnasio",
    description="API para gestionar membresías, pagos, asistencias, progreso y personal de un gimnasio",
    version="1.0.0"
)

# Incluir routers
app.include_router(miembros.router, prefix="/miembros", tags=["Miembros"])
app.include_router(personal.router, prefix="/personal", tags=["Personal"])
app.include_router(membresias.router, prefix="/membresias", tags=["Membresías"])
app.include_router(pagos.router, prefix="/pagos", tags=["Pagos"])
app.include_router(asistencias.router, prefix="/asistencias", tags=["Asistencias"])
app.include_router(progreso.router, prefix="/progreso", tags=["Progreso"])
app.include_router(reportes.router, prefix="/reportes", tags=["Reportes"])

# Ruta de prueba
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de Gestión de Gimnasio"}