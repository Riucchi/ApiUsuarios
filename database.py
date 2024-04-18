from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Product # Asegúrate de importar Base y tus modelos desde models.py

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()