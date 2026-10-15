from sqlmodel import SQLModel, Field, Relationship

#----Proveedor

class ProveedorBase(SQLModel):
    nombre: str
    numero: str

class Proveedor(ProveedorBase, table=True):
    id: int | None = Field(primary_key=True, default=None)
    articulos: list["Articulo"] = Relationship(back_populates="proveedor")

class ProveedorPublic(ProveedorBase):
    id: int    

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorNested(ProveedorPublic):
    articulos: list["Articulo"] | None = []


#-----Articulo


class ArticuloBase(SQLModel):
    nombre: str = Field(index=True)
    precio: float
    activo: bool
    imagen: str | None = None
    proveedor_id: int | None = Field(default=None, foreign_key="proveedor.id")

class Articulo(ArticuloBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    proveedor: Proveedor | None = Relationship(back_populates="articulos")
    

class ArticuloCreate(ArticuloBase):
    pass

class ArticuloPublic(ArticuloBase):
    id: int


class ArticuloNested(ArticuloPublic):
    proveedor: Proveedor | None = None


