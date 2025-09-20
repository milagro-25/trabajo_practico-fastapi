from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/miembros", tags=["Miembros"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MiembroRespuesta)
def crear_miembro(miembro: schemas.MiembroCrear, db: Session = Depends(get_db)):
    return crud.crear_miembro(db, miembro)

@router.get("/", response_model=list[schemas.MiembroRespuesta])
def listar_miembros(db: Session = Depends(get_db)):
    return crud.obtener_miembros(db)