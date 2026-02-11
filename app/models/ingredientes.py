from datetime import date
from pydantic import BaseModel


class IngredienteBase(BaseModel):
    nombre: str
    unidad: str


class IngredienteCreate(IngredienteBase):
    costo_actual: float


class Ingrediente(IngredienteBase):
    id: int
    costo_actual: float


class RegistroCosto(BaseModel):
    ingrediente_id: int
    fecha_semana: date
    costo_por_unidad: float

class ActualizarCostoIngrediente(BaseModel):
    costo_actual: float
    fecha_semana: date | None = None