import sqlite3
conn = sqlite3.connect('db_lenera.db')
columnas = conn.execute("PRAGMA table_info(articulo);").fetchall()
print(columnas)