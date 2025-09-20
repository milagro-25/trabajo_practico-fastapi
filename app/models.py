from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Miembro(Base):
    _tablename_ = "miembros"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    edad = Column(Integer)
    email = Column(String, unique=True, index=True)

    membresias = relationship("Membresia", back_populates="miembro")
    asistencias = relationship("Asistencia", back_populates="miembro")
    progresos = relationship("Progreso", back_populates="miembro")

class Personal(Base):
    _tablename_ = "personal"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    puesto = Column(String)

class Membresia(Base):
    _tablename_ = "membresias"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    costo = Column(Float)
    miembro_id = Column(Integer, ForeignKey("miembros.id"))

    miembro = relationship("Miembro", back_populates="membresias")
    pagos = relationship("Pago", back_populates="membresia")

class Pago(Base):
    _tablename_ = "pagos"
    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float)
    fecha = Column(Date)
    membresia_id = Column(Integer, ForeignKey("membresias.id"))

    membresia = relationship("Membresia", back_populates="pagos")

class Asistencia(Base):
    _tablename_ = "asistencias"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    miembro_id = Column(Integer, ForeignKey("miembros.id"))

    miembro = relationship("Miembro", back_populates="asistencias")

class Progreso(Base):
    _tablename_ = "progresos"
    id = Column(Integer, primary_key=True, index=True)
    peso = Column(Float)
    grasa_corporal = Column(Float)
    fecha_registro = Column(Date)
    miembro_id = Column(Integer, ForeignKey("miembros.id"))

    miembro = relationship("Miembro", back_populates="progresos")