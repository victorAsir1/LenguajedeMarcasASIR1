import os
import json
from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURACIÓN AUTOMÁTICA DE ARCHIVOS Y RUTAS ---
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_JSON = os.path.join(DIRECTORIO_ACTUAL, "curriculum.json")
CARPETA_TEMPLATES = os.path.join(DIRECTORIO_ACTUAL, "templates")
RUTA_HTML = os.path.join(CARPETA_TEMPLATES, "for.html")

# 1. Creamos tu estructura de datos reales en el archivo JSON si no existe
mi_json_datos = {
    "datos_personales": {
        "nombre": "Victor Jose",
        "apellidos": "Ureña Renau",
        "email": "victorrenau@gmail.com"
    },
    "formacion": [
        {
            "centro": "Aula Campus",
            "periodo": "2023-2025",
            "estudios": "Sistemas Microinformáticos en Red (SMR)"
        },
        {
            "centro": "CEAC",
            "periodo": "2025-2026",
            "estudios": "Administración de Sistemas Informáticos en Red (ASIR)"
        }
    ],
    "experiencia": []
}

with open(RUTA_JSON, "w", encoding="utf-8") as f:
    json.dump(mi_json_datos, f, indent=2, ensure_ascii=False)

# 2. Creamos la plantilla HTML (for.html) automáticamente con el bucle Jinja2
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Currículum de {{ contenido.datos_personales.nombre }}</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f7f6; color: #333; }
        .cv-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
        h1 { color: #2c3e50; margin-bottom: 5px; }
        h3 { border-bottom: 2px solid #3498db; padding-bottom: 5px; color: #2980b9; margin-top: 25px; }
        ul { list-style: none; padding: 0; }
        li { background: #ecf0f1; margin-bottom: 10px; padding: 10px; border-radius: 5px; border-left: 5px solid #3498db; }
        .periodo { font-weight: bold; color: #e67e22; }
    </style>
</head>
<body>
    <div class="cv-card">
        <h1>{{ contenido.datos_personales.nombre }} {{ contenido.datos_personales.apellidos }}</h1>
        <p><strong>Email:</strong> {{ contenido.datos_personales.email }}</p>
        
        <h3>Formación Académica</h3>
        <ul>
            {% for estudio in contenido.formacion %}
            <li>
                <span class="periodo">[{{ estudio.periodo }}]</span> - <strong>{{ estudio.estudios }}</strong><br>
                <small style="color: #7f8c8d;">{{ estudio.centro }}</small>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

if not os.path.exists(CARPETA_TEMPLATES):
    os.makedirs(CARPETA_TEMPLATES)

with open(RUTA_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)
# ---------------------------------------------------

@app.get("/") 
def inicio():
    # Usamos 'with' para abrir el archivo; se cierra solo automáticamente al salir del bloque
    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)
  
    # Enviamos los datos hacia for.html tal y como pide tu ejercicio
    return render_template("for.html", contenido=contenido)

if __name__ == "__main__":                
    app.run(debug=True)