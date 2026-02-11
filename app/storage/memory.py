from typing import List

from app.models.ingredientes import Ingrediente, RegistroCosto
from app.models.platillos import Platillo, PlatilloIngrediente

ingredientes: List[Ingrediente] = []
registros_costos: List[RegistroCosto] = []
platillos: List[Platillo] = []
platillo_ingredientes: List[PlatilloIngrediente] = []

next_ingrediente_id = 1
next_platillo_id = 1
