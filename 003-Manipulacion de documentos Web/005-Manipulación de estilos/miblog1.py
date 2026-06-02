import sqlite3                                                   
from flask import Flask, render_template     
import os

app = Flask(__name__)                                            

# --- CONFIGURACIÓN AUTOMÁTICA DE RUTAS Y BASE DE DATOS ---
# Detectamos la carpeta exacta donde está guardado este archivo .py
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "blog.db")
CARPETA_TEMPLATES = os.path.join(DIRECTORIO_ACTUAL, 'templates')
RUTA_HTML = os.path.join(CARPETA_TEMPLATES, 'blog.html')

# Contenido del HTML para el blog (evita el error TemplateNotFound)
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Blog Personal</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f4f9; }
        .post { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        h2 { color: #3498db; margin-top: 0; }
    </style>
</head>
<body>
    <h1>Entradas del Blog</h1>
    {% for entrada in datos %}
        <div class="post">
            <h2>{{ entrada.titulo }}</h2>
            <p>{{ entrada.contenido }}</p>
        </div>
    {% endfor %}
</body>
</html>
"""

# Aseguramos que la carpeta templates exista y creamos el HTML automáticamente
if not os.path.exists(CARPETA_TEMPLATES):
    os.makedirs(CARPETA_TEMPLATES)

with open(RUTA_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Inicializamos la base de datos asegurándonos de que la tabla tenga datos
def inicializar_bd():
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entradas (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        titulo TEXT NOT NULL, 
        contenido TEXT NOT NULL
    )
    """)
    cursor.execute("SELECT COUNT(*) FROM entradas")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO entradas (titulo, contenido) VALUES (?, ?)", 
                       ("Mi Primera Entrada", "¡Hola! Este es el contenido de prueba leido desde la base de datos SQLite."))
        conexion.commit()
    conexion.close()
# -----------------------------------------------------------------

@app.get("/")                                                                                                                                                                                                               
def inicio():                                                               
    conexion = sqlite3.connect(RUTA_BD)       
    conexion.row_factory = sqlite3.Row      
    cursor = conexion.cursor()                                  
    
    cursor.execute("SELECT * FROM entradas")
    clientes = cursor.fetchall()                                
    
    lista = []                                                                                                                          
    for fila in clientes:                                       
        lista.append(dict(fila))                                

    print(lista)                                                                                                                        
    return render_template("blog.html", datos=lista) 

if __name__ == "__main__": 
    inicializar_bd() # Crea la tabla y los datos antes de arrancar la web                              
    app.run(debug=True)