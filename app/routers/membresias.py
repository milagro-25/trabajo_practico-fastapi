from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import SessionLocal

router = APIRouter(prefix="/membresias", tags=["Membresías"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MembresiaRespuesta)
def crear_membresia(membresia: schemas.MembresiaCrear, db: Session = Depends(get_db)):
    nueva = models.Membresia(**membresia.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=list[schemas.MembresiaRespuesta])
def listar_membresias(db: Session = Depends(get_db)):
    return db.query(models.Membresia).all()