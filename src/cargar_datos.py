import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('db_lenera.db')
cursor = conn.cursor()

# Insertar el primer registro
cursor.execute("""
    INSERT INTO articulo (nombre, precio, activo, imagen) 
    VALUES ('Leña (bolsa 6kg)', 2600.0, 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7svZcUJPdEdxpolnznz3owj-Ca1GOYQ6oSprBcmT76i0zLUp1')
""")

# Insertar el segundo registro
cursor.execute("""
    INSERT INTO articulo (nombre, precio, activo, imagen) 
    VALUES ('Carbón (bolsa 3kg)', 2700.0, 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNjoF3OGTmnFRtlIS6OZzHnpvTO0DMijNOoA&s')
""")

# Guardar los cambios y cerrar
conn.commit()
conn.close()

print("¡Los 2 registros fueron insertados con éxito!")