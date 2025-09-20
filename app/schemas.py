from pydantic import BaseModel
from datetime import date

class MiembroBase(BaseModel):
    nombre: str
    edad: int
    email: str

class MiembroCrear(MiembroBase):
    pass

class MiembroRespuesta(MiembroBase):
    id: int
    class Config:
        orm_mode = True

class PersonalBase(BaseModel):
    nombre: str
    puesto: str

class PersonalCrear(PersonalBase):
    pass

class PersonalRespuesta(PersonalBase):
    id: int
    class Config:
        orm_mode = True

class MembresiaBase(BaseModel):
    tipo: str
    costo: float
    miembro_id: int

class MembresiaCrear(MembresiaBase):
    pass

class MembresiaRespuesta(MembresiaBase):
    id: int
    class Config:
        orm_mode = True

class PagoBase(BaseModel):
    monto: float
    fecha: date
    membresia_id: int

class PagoCrear(PagoBase):
    pass

class PagoRespuesta(PagoBase):
    id: int
    class Config:
        orm_mode = True

class AsistenciaBase(BaseModel):
    fecha: date
    miembro_id: int

class AsistenciaCrear(AsistenciaBase):
    pass

class AsistenciaRespuesta(AsistenciaBase):
    id: int
    class Config:
        orm_mode = True

class ProgresoBase(BaseModel):
    peso: float
    grasa_corporal: float
    fecha_registro: date
    miembro_id: int

class ProgresoCrear(ProgresoBase):
    pass

class ProgresoRespuesta(ProgresoBase):
    id: int
    class Config:
        orm_mode = True