import sqlite3 

conexion = sqlite3.connect("clientes.db")
cursor = conexion.cursor() 

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall() 	
print(clientes)							

conexion.close()
