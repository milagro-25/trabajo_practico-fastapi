from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AsistenciaRespuesta)
def registrar_asistencia(asistencia: schemas.AsistenciaCrear, db: Session = Depends(get_db)):
    nueva = models.Asistencia(**asistencia.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=list[schemas.AsistenciaRespuesta])
def listar_asistencias(db: Session = Depends(get_db)):
    return db.query(models.Asistencia).all()