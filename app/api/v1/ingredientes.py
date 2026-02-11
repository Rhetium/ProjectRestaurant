from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List

from app.models.ingredientes import IngredienteCreate, Ingrediente, RegistroCosto, ActualizarCostoIngrediente
from app.storage import memory


router = APIRouter(prefix="/ingredientes", tags=["ingredientes"])

@router.post("/", response_model=Ingrediente, status_code=status.HTTP_201_CREATED)
async def crear_ingrediente(ingrediente: IngredienteCreate):
    for ing in memory.ingredientes:
        if ing.nombre.lower() == ingrediente.nombre.lower():
            raise HTTPException(status_code=400, detail="El ingrediente ya existe")
    
    global_id = memory.next_ingrediente_id
    ingrediente = Ingrediente(
        id = global_id,
        nombre=ingrediente.nombre,
        unidad=ingrediente.unidad,
        costo_actual=ingrediente.costo_actual,
        )
    memory.ingredientes.append(ingrediente)
    memory.next_ingrediente_id += 1

    registro =  RegistroCosto(
        ingrediente_id=ingrediente.id,
        fecha_semana=date.today(),
        costo_por_unidad=ingrediente.costo_actual
    )
    memory.registros_costos.append(registro)

    return ingrediente

@router.get("/", response_model=List[Ingrediente])
async def listar_ingredientes():
    return memory.ingredientes

@router.post("/{ingrediente_id}/costo", status_code=status.HTTP_200_OK)
async def actualizar_costo_ingrediente(ingrediente_id: int, datos_costo: ActualizarCostoIngrediente):
    ingrediente = next((ing for ing in memory.ingredientes if ing.id == ingrediente_id), None)
    if not ingrediente:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    
    ingrediente.costo_actual = datos_costo.costo_actual

    registro = RegistroCosto(
        ingrediente_id=ingrediente_id,
        fecha_semana=datos_costo.fecha_semana or date.today(),
        costo_por_unidad=datos_costo.costo_actual
    )
    memory.registros_costos.append(registro)

    return {"message": "Costo actualizado correctamente"}