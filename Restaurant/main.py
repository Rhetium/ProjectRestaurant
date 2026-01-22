from fastapi import FastAPI
from routers import ingredients, updateIngredient

app = FastAPI()

app.include_router(ingredients.router)
app.include_router(updateIngredient.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Restaurant Ingredient API"}
