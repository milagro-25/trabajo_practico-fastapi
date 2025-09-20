from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

# ------------------------- MIEMBROS -------------------------

def crear_miembro(db: Session, miembro: schemas.MiembroCrear) -> models.Miembro:
    nuevo = models.Miembro(**miembro.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_miembro(db: Session, miembro_id: int) -> Optional[models.Miembro]:
    return db.query(models.Miembro).filter(models.Miembro.id == miembro_id).first()

def obtener_miembros(db: Session, skip: int = 0, limit: int = 100) -> List[models.Miembro]:
    return db.query(models.Miembro).offset(skip).limit(limit).all()

def actualizar_miembro(db: Session, miembro_id: int, datos: Dict) -> Optional[models.Miembro]:
    miembro = obtener_miembro(db, miembro_id)
    if not miembro:
        return None
    for k, v in datos.items():
        if hasattr(miembro, k):
            setattr(miembro, k, v)
    db.add(miembro)
    db.commit()
    db.refresh(miembro)
    return miembro

def eliminar_miembro(db: Session, miembro_id: int) -> bool:
    miembro = obtener_miembro(db, miembro_id)
    if not miembro:
        return False
    db.delete(miembro)
    db.commit()
    return True


# ------------------------- PERSONAL -------------------------

def crear_personal(db: Session, personal: schemas.PersonalCrear) -> models.Personal:
    nuevo = models.Personal(**personal.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_personal(db: Session, skip: int = 0, limit: int = 100) -> List[models.Personal]:
    return db.query(models.Personal).offset(skip).limit(limit).all()

def obtener_personal_por_id(db: Session, personal_id: int) -> Optional[models.Personal]:
    return db.query(models.Personal).filter(models.Personal.id == personal_id).first()

def actualizar_personal(db: Session, personal_id: int, datos: Dict) -> Optional[models.Personal]:
    p = obtener_personal_por_id(db, personal_id)
    if not p:
        return None
    for k, v in datos.items():
        if hasattr(p, k):
            setattr(p, k, v)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def eliminar_personal(db: Session, personal_id: int) -> bool:
    p = obtener_personal_por_id(db, personal_id)
    if not p:
        return False
    db.delete(p)
    db.commit()
    return True


# ------------------------- MEMBRESÍAS -------------------------

def crear_membresia(db: Session, membresia: schemas.MembresiaCrear) -> models.Membresia:
    nueva = models.Membresia(**membresia.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_membresias(db: Session, skip: int = 0, limit: int = 100) -> List[models.Membresia]:
    return db.query(models.Membresia).offset(skip).limit(limit).all()

def obtener_membresia(db: Session, membresia_id: int) -> Optional[models.Membresia]:
    return db.query(models.Membresia).filter(models.Membresia.id == membresia_id).first()

def eliminar_membresia(db: Session, membresia_id: int) -> bool:
    m = obtener_membresia(db, membresia_id)
    if not m:
        return False
    db.delete(m)
    db.commit()
    return True


# ------------------------- PAGOS -------------------------

def registrar_pago(db: Session, pago: schemas.PagoCrear) -> models.Pago:
    nuevo = models.Pago(**pago.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_pagos(db: Session, skip: int = 0, limit: int = 200) -> List[models.Pago]:
    return db.query(models.Pago).offset(skip).limit(limit).all()

def ingresos_por_mes(db: Session, anio: int, mes: int) -> float:
    suma = db.query(func.coalesce(func.sum(models.Pago.monto), 0)).filter(
        func.strftime("%Y", models.Pago.fecha) == str(anio),
        func.strftime("%m", models.Pago.fecha) == f"{mes:02d}"
    ).scalar()
    return float(suma or 0.0)

def ingresos_periodo(db: Session, fecha_inicio, fecha_fin) -> float:
    suma = db.query(func.coalesce(func.sum(models.Pago.monto), 0)).filter(
        models.Pago.fecha >= fecha_inicio,
        models.Pago.fecha <= fecha_fin
    ).scalar()
    return float(suma or 0.0)


# ------------------------- ASISTENCIAS -------------------------

def registrar_asistencia(db: Session, asistencia: schemas.AsistenciaCrear) -> models.Asistencia:
    nueva = models.Asistencia(**asistencia.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_asistencias(db: Session, skip: int = 0, limit: int = 200) -> List[models.Asistencia]:
    return db.query(models.Asistencia).offset(skip).limit(limit).all()

def conteo_asistencias_por_dia(db: Session, fecha) -> int:
    total = db.query(func.count(models.Asistencia.id)).filter(models.Asistencia.fecha == fecha).scalar()
    return int(total or 0)

def conteo_asistencias_periodo(db: Session, fecha_inicio, fecha_fin) -> Dict[str, int]:
    filas = db.query(models.Asistencia).filter(
        models.Asistencia.fecha >= fecha_inicio,
        models.Asistencia.fecha <= fecha_fin
    ).all()
    conteo: Dict[str, int] = {}
    for a in filas:
        clave = a.fecha.isoformat()
        conteo[clave] = conteo.get(clave, 0) + 1
    return conteo


# ------------------------- PROGRESO -------------------------

def registrar_progreso(db: Session, progreso: schemas.ProgresoCrear) -> models.Progreso:
    nuevo = models.Progreso(**progreso.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_progresos_por_miembro(db: Session, miembro_id: int) -> List[models.Progreso]:
    return db.query(models.Progreso).filter(models.Progreso.miembro_id == miembro_id).order_by(models.Progreso.fecha_registro).all()

def progreso_periodo(db: Session, miembro_id: int, fecha_inicio, fecha_fin) -> List[models.Progreso]:
    return db.query(models.Progreso).filter(
        models.Progreso.miembro_id == miembro_id,
        models.Progreso.fecha_registro >= fecha_inicio,
        models.Progreso.fecha_registro <= fecha_fin
    ).order_by(models.Progreso.fecha_registro).all()

def resumen_progreso(db: Session, miembro_id: int, fecha_inicio=None, fecha_fin=None) -> Dict:
    query = db.query(models.Progreso).filter(models.Progreso.miembro_id == miembro_id)
    if fecha_inicio:
        query = query.filter(models.Progreso.fecha_registro >= fecha_inicio)
    if fecha_fin:
        query = query.filter(models.Progreso.fecha_registro <= fecha_fin)
    entradas = query.order_by(models.Progreso.fecha_registro).all()

    lista = []
    peso_inicial = peso_final = None
    grasa_inicial = grasa_final = None
    for e in entradas:
        lista.append({
            "fecha": e.fecha_registro.isoformat(),
            "peso_kg": e.peso,
            "porcentaje_grasa": e.grasa_corporal
        })
        if e.peso is not None:
            if peso_inicial is None:
                peso_inicial = e.peso
            peso_final = e.peso
        if e.grasa_corporal is not None:
            if grasa_inicial is None:
                grasa_inicial = e.grasa_corporal
            grasa_final = e.grasa_corporal

    delta = {}
    if peso_inicial is not None and peso_final is not None:
        delta["peso_kg"] = round(peso_final - peso_inicial, 2)
    if grasa_inicial is not None and grasa_final is not None:
        delta["porcentaje_grasa"] = round(grasa_final - grasa_inicial, 2)

    return {"miembro_id": miembro_id, "entradas": lista, "cambios": delta}


# ------------------------- UTILIDADES -------------------------

def ingresos_mensuales_por_anio(db: Session, anio: int) -> List[Dict]:
    resultado = []
    for mes in range(1, 13):
        total = ingresos_por_mes(db, anio, mes)
        resultado.append({"mes": mes, "total": round(total, 2)})
    return resultado