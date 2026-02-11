from app.storage import memory


def calcular_costo_platillo(platillo_id: int) -> float:
    costo_total = 0.0
    for pi in memory.platillo_ingredientes:
        if pi.platillo_id == platillo_id:
            ingrediente = next(
                (ing for ing in memory.ingredientes if ing.id == pi.ingrediente_id),
                None,
            )
            if ingrediente:
                costo_total += pi.cantidad * ingrediente.costo_actual
    return costo_total
