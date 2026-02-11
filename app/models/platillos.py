from pydantic import BaseModel


class PlatilloBase(BaseModel):
    nombre: str


class PlatilloCreate(PlatilloBase):
    pass


class Platillo(PlatilloBase):
    id: int


class PlatilloIngrediente(BaseModel):
    platillo_id: int
    ingrediente_id: int
    cantidad: float
