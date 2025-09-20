from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from .. import models
from ..database import SessionLocal

router = APIRouter(prefix="/reportes", tags=["Reportes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ingresos_mensuales")
def ingresos_mensuales(anio: int, mes: int, db: Session = Depends(get_db)):
    ingresos = db.query(func.sum(models.Pago.monto)).filter(
        func.strftime("%Y", models.Pago.fecha) == str(anio),
        func.strftime("%m", models.Pago.fecha) == f"{mes:02d}"
    ).scalar()
    return {"anio": anio, "mes": mes, "ingresos": ingresos or 0}

@router.get("/asistencias_diarias")
def asistencias_diarias(fecha: date, db: Session = Depends(get_db)):
    total = db.query(func.count(models.Asistencia.id)).filter(models.Asistencia.fecha == fecha).scalar()
    return {"fecha": fecha, "total_asistencias": total}

@router.get("/progreso_periodo")
def progreso_periodo(miembro_id: int, fecha_inicio: date, fecha_fin: date, db: Session = Depends(get_db)):
    progresos = db.query(models.Progreso).filter(
        models.Progreso.miembro_id == miembro_id,
        models.Progreso.fecha_registro.between(fecha_inicio, fecha_fin)
    ).all()
    return progresos