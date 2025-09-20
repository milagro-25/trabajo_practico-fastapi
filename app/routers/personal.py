from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(prefix="/personal", tags=["Personal"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PersonalRespuesta)
def crear_personal(personal: schemas.PersonalCrear, db: Session = Depends(get_db)):
    return crud.crear_personal(db, personal)

@router.get("/", response_model=list[schemas.PersonalRespuesta])
def listar_personal(db: Session = Depends(get_db)):
    return crud.obtener_personal(db)