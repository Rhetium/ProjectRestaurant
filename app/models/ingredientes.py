from datetime import datetime, date
from typing import Optional

from sqlmodel import SQLModel, Field


class IngredienteBase(SQLModel):
    nombre: str = Field(index=True)
    unidad_base: str  # "ml", "g", "unidad", etc.


class Ingrediente(IngredienteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    costo_actual_por_unidad: float


class RegistroCosto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ingrediente_id: int = Field(foreign_key="ingrediente.id")
    fecha_semana: datetime  # ahora datetime
    precio_paquete: float
    cantidad_paquete: float
    unidad_base: str
    costo_por_unidad_calculado: float


class IngredienteCreate(SQLModel):
    nombre: str
    unidad_base: str
    precio_paquete: float
    cantidad_paquete: float


class ActualizarCostoIngrediente(SQLModel):
    precio_paquete: float
    cantidad_paquete: float
    fecha_semana: Optional[datetime] = None


class IngredienteConPrecio(SQLModel):
    id: int
    nombre: str
    unidad_base: str
    costo_actual_por_unidad: float
    precio_paquete_actual: Optional[float] = None
    cantidad_paquete_actual: Optional[float] = None
