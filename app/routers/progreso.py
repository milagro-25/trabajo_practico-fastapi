from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix="/progresos", tags=["Progresos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProgresoRespuesta)
def registrar_progreso(progreso: schemas.ProgresoCrear, db: Session = Depends(get_db)):
    nuevo = models.Progreso(**progreso.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[schemas.ProgresoRespuesta])
def listar_progresos(db: Session = Depends(get_db)):
    return db.query(models.Progreso).all()