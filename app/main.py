from fastapi import FastAPI

from app.database import engine, Base
from app.routes import ingredient_routes, menu_routes, dish_routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title = "Restaurant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(ingredient_routes.router)
app.include_router(dish_routes.router)
app.include_router(menu_routes.router)