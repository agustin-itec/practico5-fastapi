from sqlmodel import Session, SQLModel, select
from database import engine
from models.articulos_models import Articulo

def poblar_base_datos():
    # Asegura que las tablas existan antes de insertar
    SQLModel.metadata.create_all(engine)

    articulos_semilla = [
        Articulo(nombre="Leña (bolsa 6kg)", precio=2600.0, activo=True),
        Articulo(nombre="Carbón (bolsa 3kg)", precio=2700.0, activo=True),
        Articulo(nombre="Bolsa de astillas para encendido", precio=1200.0, activo=True),
        Articulo(nombre="Pack leña quebracho colorado (10kg)", precio=4500.0, activo=True),
    ]

    with Session(engine) as session:
        # Evita duplicar registros si ya existen artículos en la tabla
        existentes = session.exec(select(Articulo)).first()
        if existentes:
            print("ℹ️ La base de datos ya contiene registros. No se agregaron duplicados.")
            return

        for art in articulos_semilla:
            session.add(art)

        session.commit()
        print("✅ Registros cargados con éxito en db_lenera_sqlmodel.db")

if __name__ == "__main__":
    poblar_base_datos()