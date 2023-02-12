import sqlite3

conn=sqlite3.connect('tienda.db')
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE TASA_CAMBIOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRECIO_VENTA VARCHAR(200),
    PRECIO_COMPRA VARCHAR(200),
    FECHA TIMESTAMP NOT NULL
    )"""
)
conn.commit()
conn.close()