import sqlite3 

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor() 


cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT
)
""")


cursor.execute("""
INSERT INTO clientes (nombre, email, telefono)
VALUES ("Manolo Lama", "Manol.Lamine@gmail.com", "600123456");
""")

conexion.commit()


conexion.close()
