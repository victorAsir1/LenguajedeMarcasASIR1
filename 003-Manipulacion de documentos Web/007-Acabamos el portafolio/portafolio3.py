import sqlite3                                                     
from flask import Flask, render_template     
import os
from datetime import datetime

app = Flask(__name__)                                           

# --- SOLUCIÓN AUTOMÁTICA DE RUTAS Y BASE DE DATOS ---
# Forzamos a Python a localizar la carpeta exacta de este archivo .py
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "portafolio.db")
CARPETA_TEMPLATES = os.path.join(DIRECTORIO_ACTUAL, 'templates')
RUTA_HTML = os.path.join(CARPETA_TEMPLATES, 'portafolio.html')

# Contenido del HTML integrado para evitar el error TemplateNotFound
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Victor Ureña - Portafolio Técnico</title>
</head>
<body style="font-family: sans-serif; margin: 40px; background: #f4f4f9;">

<header>
    <h1>Victor Ureña</h1>
    <h2>Técnico de Redes</h2>
    <p>Año de consulta: {{ datos.anio }}</p>
</header>

<main>
    <section id="sobremi">
        <h3>Sobre mí</h3>
        <p>Soy un técnico de redes con conocimientos en instalación, configuración y mantenimiento de sistemas informáticos...</p>
    </section>

    <section id="blog">
        <h3>Blog Técnico (Datos desde SQLite)</h3>
        <div id="contenedor-blog">
            {% for articulo in datos.articulos %}
            <div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; border-radius: 5px; background: #fff;">
                <h4>{{ articulo.titulo }}</h4>
                <p><small>Publicado el: {{ articulo.fecha }}</small></p>
                <p>{{ articulo.texto }}</p>
            </div>
            {% else %}
            <p>No se encontraron artículos en la tabla 'piezas'.</p>
            {% endfor %}
        </div>
    </section>
</main>

<footer>
    <p>&copy; {{ datos.anio }} Victor Ureña - Todos los derechos reservados</p>
</footer>

</body>
</html>
"""

# Creamos la carpeta templates e inyectamos el HTML automáticamente si no existen
if not os.path.exists(CARPETA_TEMPLATES):
    os.makedirs(CARPETA_TEMPLATES)

with open(RUTA_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

def inicializar_base_datos():
    """Crea la tabla piezas e introduce registros iniciales si no existen."""
    conexion = sqlite3.connect(RUTA_BD)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        fecha TEXT NOT NULL,
        texto TEXT NOT NULL
    )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM piezas")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
        INSERT INTO piezas (titulo, fecha, texto) 
        VALUES (?, ?, ?)
        """, ("Instalación de Servidores en Rack", "02/06/2026", "Configuración de infraestructura física de red para centros de datos."))
        
        cursor.execute("""
        INSERT INTO piezas (titulo, fecha, texto) 
        VALUES (?, ?, ?)
        """, ("Segmentación de VLANs", "01/06/2026", "Aislamiento y optimización del tráfico de red local."))
        conexion.commit()
    conexion.close()
# -----------------------------------------------------------------

@app.get("/")                                                                           
def inicio():                                                                           
    conexion = sqlite3.connect(RUTA_BD)     
    conexion.row_factory = sqlite3.Row          
    cursor = conexion.cursor()                                          
    
    # Consultamos la tabla 'piezas' de la base de datos
    cursor.execute("SELECT * FROM piezas")
    resultados = cursor.fetchall()                                      
    
    lista_piezas = []                                                                                                   
    for fila in resultados:                                       
        lista_piezas.append(dict(fila))                                

    # Diccionario estructurado para que Jinja2 reciba los parámetros requeridos
    datos_para_web = {
        "anio": datetime.now().year,
        "articulos": lista_piezas
    }
    
    return render_template("portafolio.html", datos=datos_para_web)   

if __name__ == "__main__":                                              
    inicializar_base_datos()
    app.run(debug=True)