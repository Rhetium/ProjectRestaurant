from fastapi import FastAPI

from app.database import engine, Base
from app.routes import ingredient_routes

app = FastAPI(title = "Restaurant API")

Base.metadata.create_all(bind=engine)

app.include_router(ingredient_routes.router)