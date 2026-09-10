from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Articulo(Base):
    __tablename__ = "articulo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)
    activo = Column(Boolean)
    imagen = Column(String)