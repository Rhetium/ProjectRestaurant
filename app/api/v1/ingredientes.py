from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db import get_session
from app.models.ingredientes import (
    IngredienteCreate,
    Ingrediente,
    RegistroCosto,
    ActualizarCostoIngrediente,
    IngredienteConPrecio,
)

router = APIRouter(prefix="/ingredientes", tags=["ingredientes"])


@router.post(
    "/",
    response_model=Ingrediente,
    status_code=status.HTTP_201_CREATED,
)
async def crear_ingrediente(
    ingrediente_in: IngredienteCreate,
    session: Session = Depends(get_session),
):
    # Validar nombre único
    statement = select(Ingrediente).where(
        Ingrediente.nombre == ingrediente_in.nombre
    )
    existente = session.exec(statement).first()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un ingrediente con ese nombre",
        )

    if ingrediente_in.cantidad_paquete <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La cantidad del paquete debe ser mayor a cero",
        )

    costo_por_unidad = (
        ingrediente_in.precio_paquete / ingrediente_in.cantidad_paquete
        if ingrediente_in.cantidad_paquete > 0
        else 0.0
    )

    ingrediente = Ingrediente(
        nombre=ingrediente_in.nombre,
        unidad_base=ingrediente_in.unidad_base,
        costo_actual_por_unidad=costo_por_unidad,
    )
    session.add(ingrediente)
    session.commit()
    session.refresh(ingrediente)

    # Registrar historial de costo
    registro = RegistroCosto(
        ingrediente_id=ingrediente.id,
        fecha_semana=datetime.today(),
        precio_paquete=ingrediente_in.precio_paquete,
        cantidad_paquete=ingrediente_in.cantidad_paquete,
        unidad_base=ingrediente_in.unidad_base,
        costo_por_unidad_calculado=costo_por_unidad,
    )
    session.add(registro)
    session.commit()

    return ingrediente


@router.post(
    "/{ingrediente_id}/costos",
    response_model=Ingrediente,
    status_code=status.HTTP_200_OK,
)
async def actualizar_costo_ingrediente(
    ingrediente_id: int,
    datos_costo: ActualizarCostoIngrediente,
    session: Session = Depends(get_session),
):
    # Buscar ingrediente
    ingrediente = session.get(Ingrediente, ingrediente_id)
    if not ingrediente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ingrediente no encontrado",
        )

    if datos_costo.cantidad_paquete <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La cantidad del paquete debe ser mayor a cero",
        )

    fecha_semana = datos_costo.fecha_semana or datetime.today()

    costo_por_unidad = (
        datos_costo.precio_paquete / datos_costo.cantidad_paquete
        if datos_costo.cantidad_paquete > 0
        else 0.0
    )

    ingrediente.costo_actual_por_unidad = costo_por_unidad
    session.add(ingrediente)

    registro = RegistroCosto(
        ingrediente_id=ingrediente.id,
        fecha_semana=fecha_semana,
        precio_paquete=datos_costo.precio_paquete,
        cantidad_paquete=datos_costo.cantidad_paquete,
        unidad_base=ingrediente.unidad_base,
        costo_por_unidad_calculado=costo_por_unidad,
    )
    session.add(registro)
    session.commit()
    session.refresh(ingrediente)

    return ingrediente


@router.get(
    "/{ingrediente_id}/costos",
    response_model=List[RegistroCosto],
)
def listar_costos_ingrediente(
    ingrediente_id: int,
    session: Session = Depends(get_session),
):
    statement = select(RegistroCosto).where(
        RegistroCosto.ingrediente_id == ingrediente_id
    )
    return session.exec(statement).all()


@router.get("/", response_model=List[IngredienteConPrecio])
async def listar_ingredientes(session: Session = Depends(get_session)):
    ingredientes = session.exec(select(Ingrediente)).all()
    respuesta: List[IngredienteConPrecio] = []

    for ing in ingredientes:
        stmt = (
            select(RegistroCosto)
            .where(RegistroCosto.ingrediente_id == ing.id)
            .order_by(RegistroCosto.fecha_semana.desc(), RegistroCosto.id.desc())
        )
        ultimo_registro = session.exec(stmt).first()

        item = IngredienteConPrecio(
            id=ing.id,
            nombre=ing.nombre,
            unidad_base=ing.unidad_base,
            costo_actual_por_unidad=ing.costo_actual_por_unidad,
            precio_paquete_actual=ultimo_registro.precio_paquete if ultimo_registro else None,
            cantidad_paquete_actual=ultimo_registro.cantidad_paquete if ultimo_registro else None,
        )

        respuesta.append(item)

    return respuesta
