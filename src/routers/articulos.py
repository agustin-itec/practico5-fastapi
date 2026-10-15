from typing import Annotated
from fastapi import HTTPException, Path, Query, APIRouter, Depends
from database import get_db
from models.articulos_models import Articulo, ArticuloBase, ArticuloCreate, ArticuloPublic, Proveedor, ProveedorBase, ProveedorPublic, ProveedorCreate, ArticuloNested
from sqlmodel import Session, select

articulos_routers = APIRouter()

DICT_NOT_FOUND: dict = {
    404: {
        "description": "Si el artículo no se encuentra en la lista",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Articulo no encontrado"
                }
            }
        }
        }
    }

##########################
# METODOS GET
##########################

@articulos_routers.get("/", response_model=list[ArticuloPublic])
async def get_articulos( db: Session = Depends(get_db)):
    return db.exec(select(Articulo)).all()

@articulos_routers.get(
        "/{id}",
        responses=DICT_NOT_FOUND,
        response_model=ArticuloNested
        ) 
async def get_articulos_id(id: Annotated[int, Path(gt=0, description="El ID debe ser mayor a cero")], db: Session = Depends(get_db)):
    articulo_obtenido = db.get(Articulo, id) # envio tabla e ID
    if not articulo_obtenido:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return articulo_obtenido
    


##########################
# METODO POST 
##########################

@articulos_routers.post(
        "/",
        response_model=ArticuloNested)
async def agregar_articulo(nuevo_articulo:ArticuloCreate, db: Session = Depends(get_db)):

    articulo_db = Articulo.model_validate(nuevo_articulo)

    db.add(articulo_db)
    db.commit()
    db.refresh(articulo_db)

    return articulo_db
    
##########################
# METODOS PUT
##########################

@articulos_routers.put("/{id}",responses=DICT_NOT_FOUND, response_model=ArticuloPublic)
async def actualizar_articulo(
    id:Annotated[int,Path(gt=0)],
    articulo_editar:ArticuloCreate,
    db: Session = Depends(get_db)
    ): 

    articulo_obtenido = db.get(Articulo, id)

    if not articulo_obtenido:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")

    articulo_obtenido.nombre = articulo_editar.nombre
    articulo_obtenido.precio = articulo_editar.precio
    articulo_obtenido.activo = articulo_editar.activo
    articulo_obtenido.imagen = articulo_editar.imagen

    db.commit()
    db.refresh(articulo_obtenido)

    return articulo_obtenido


##########################
# METODO DELETE
##########################

@articulos_routers.delete(
    "/{id}",
    responses=DICT_NOT_FOUND,
    response_model=ArticuloPublic,
)
async def eliminar_articulo(
    id: Annotated[int, Path(gt=0)],
    logico: Annotated[bool, Query(description="Indica si se debe eliminar un artículo o no")] = True,
    db: Session = Depends(get_db)
): 
    articulo_obtenido = db.get(Articulo, id)
    if articulo_obtenido is None:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")
    
    if logico:
        articulo_obtenido.activo = False
        db.commit()
        db.refresh(articulo_obtenido)
        return articulo_obtenido
    else:
        db.delete(articulo_obtenido)
        db.commit()
        return articulo_obtenido






@articulos_routers.post("/proveedor", tags=["Proveedor"], response_model=ProveedorPublic)
async def add_proveedor(proveedor:ProveedorCreate, db: Session = Depends(get_db)):

    nuevo_proveedor = Proveedor.model_validate(proveedor)

    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)

    return nuevo_proveedor