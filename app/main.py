from fastapi import FastAPI
from app.api.v1 import ingredientes, platillos

app = FastAPI()

app.include_router(ingredientes.router, prefix="/api/v1", tags=["ingredientes"])
app.include_router(platillos.router, prefix="/api/v1", tags=["platillos"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de recetas de cocina"}