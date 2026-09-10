from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



sqlite_url = "sqlite:///./db_lenera.db"

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db   #return que no corta el flujo de la funcion (porque siempre se tiene que cerrar la session)
    finally:
        db.close()