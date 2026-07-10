from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Declaracion de la base de datos
DATABASE_URL = "sqlite:///./restaurant.db"

engine =  create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()