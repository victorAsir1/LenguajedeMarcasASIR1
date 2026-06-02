import sqlite3
import os

# 1. Aseguramos que la base de datos se cree en la misma carpeta que el script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "mi_empresa.db")

# 2. Conectamos a la base de datos (si no existe, Python la crea automáticamente)
conexion = sqlite3.connect(RUTA_BD)

# 3. Creamos el "cursor" para poder ejecutar comandos SQL
cursor = conexion.cursor()

# 4. Creamos una tabla (por ejemplo, de empleados) si no existe ya
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puesto TEXT NOT NULL,
    salario_bruto REAL NOT NULL
)
""")
print("Tabla 'empleados' verificada/creada correctamente.")

# 5. Insertamos un registro de prueba
# Usamos '?' para evitar problemas de seguridad (Inyección SQL)
cursor.execute("""
INSERT INTO empleados (nombre, puesto, salario_bruto) 
VALUES (?, ?, ?)
""", ("Victor Jose", "Desarrollador", 2500.0))

# 6. CRUCIAL: Guardamos los cambios en el archivo
conexion.commit()
print("¡Registro insertado con éxito!")

# 7. Cerramos la conexión por buena práctica
conexion.close()