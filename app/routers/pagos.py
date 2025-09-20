from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix="/pagos", tags=["Pagos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PagoRespuesta)
def registrar_pago(pago: schemas.PagoCrear, db: Session = Depends(get_db)):
    nuevo = models.Pago(**pago.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[schemas.PagoRespuesta])
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(models.Pago).all()