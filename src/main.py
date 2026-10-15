from fastapi import FastAPI, HTTPException, Body, Path, Query
from typing import Annotated
from pydantic import BaseModel, Field
from routers.articulos import articulos_routers
from fastapi.middleware.cors import CORSMiddleware
from database import SQLModel, engine
from models.articulos_models import (
    ArticuloBase,
    Articulo,
    ArticuloCreate,
    ArticuloPublic
)

# SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.title = "LEÑERA"

app.version = "1.0"

app.include_router(articulos_routers, tags=["Articulos"], prefix="/articulos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)