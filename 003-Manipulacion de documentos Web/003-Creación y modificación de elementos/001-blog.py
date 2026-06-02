from flask import Flask, render_template
from datetime import datetime
import os

ahora = datetime.now()

app = Flask(__name__)

# --- CONFIGURACIÓN AUTOMÁTICA DE RUTAS Y ARCHIVOS ---
# Esto detecta exactamente dónde está guardado este archivo .py
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
CARPETA_TEMPLATES = os.path.join(DIRECTORIO_ACTUAL, 'templates')
RUTA_HTML = os.path.join(CARPETA_TEMPLATES, 'calendario.html')

# Contenido del HTML de la plantilla
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendario Anual</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; margin: 30px; }
        h1 { color: #2c3e50; }
        .info-servidor { background: #e2e8f0; padding: 10px; border-radius: 5px; margin-bottom: 20px; font-size: 0.9em; }
        .temporada { background: white; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .temporada h2 { margin-top: 0; color: #3498db; border-bottom: 2px solid #ecf0f1; padding-bottom: 5px; }
        ul { list-style: none; padding: 0; }
        li { margin-bottom: 10px; padding: 8px; background: #fafafa; border-left: 4px solid #3498db; }
        strong { color: #e74c3c; }
    </style>
</head>
<body>

    <h1>Calendario de Eventos</h1>
    
    <div class="info-servidor">
        <p><strong>Año actual:</strong> {{ datos.info_servidor.anio_actual }}</p>
        <p><strong>Última actualización:</strong> {{ datos.info_servidor.ultima_actualizacion }}</p>
    </div>

    {% for temporada, eventos in datos.temporadas.items() %}
        <div class="temporada">
            <h2>{{ temporada }}</h2>
            <ul>
                {% for item in eventos %}
                    <li>
                        <strong>{{ item.fecha }}</strong> - <span>{{ item.evento }}</span>: 
                        <em>{{ item.descripcion }}</em>
                    </li>
                {% endfor %}
            </ul>
        </div>
    {% endfor %}

</body>
</html>
"""

# Creamos la carpeta 'templates' si no existe al lado del script
if not os.path.exists(CARPETA_TEMPLATES):
    os.makedirs(CARPETA_TEMPLATES)

# Escribimos el archivo HTML automáticamente en su sitio correcto
with open(RUTA_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)
# -----------------------------------------------------------------


calendario_anual = {
    'info_servidor': {
        'anio_actual': ahora.year,
        'ultima_actualizacion': ahora.strftime("%d/%m/%Y %H:%M")
    },
    'temporadas': {
        'Invierno': [
            {'evento': 'Año Nuevo', 'fecha': '01-01', 'descripcion': 'Celebración del inicio del año civil.'},
            {'evento': 'Reyes Magos', 'fecha': '06-01', 'descripcion': 'Tradición de entrega de regalos.'}
        ],
        'Primavera': [
            {'evento': 'Semana Santa', 'fecha': 'Variable', 'descripcion': 'Festividad religiosa y primera pausa primaveral.'},
            {'evento': 'Día del Trabajo', 'fecha': '01-05', 'descripcion': 'Festivo nacional e internacional.'}
        ],
        'Verano': [
            {'evento': 'Noche de San Juan', 'fecha': '24-06', 'descripcion': 'Celebración del solsticio de verano con hogueras.'},
            {'evento': 'Vacaciones de Agosto', 'fecha': 'Agosto', 'descripcion': 'Periodo de máximo descanso estival.'}
        ],
        'Otoño': [
            {'evento': 'Halloween / Todos los Santos', 'fecha': '01-11', 'descripcion': 'Tradiciones de recuerdo a los difuntos.'},
            {'evento': 'Día de la Constitución', 'fecha': '06-12', 'descripcion': 'Celebración nacional.'}
        ],
        'Navidad': [
            {'evento': 'Nochebuena', 'fecha': '24-12', 'descripcion': 'Cena familiar principal.'},
            {'evento': 'Navidad', 'fecha': '25-12', 'descripcion': 'Nacimiento y festividad central.'},
            {'evento': 'Nochevieja', 'fecha': '31-12', 'descripcion': 'Cierre del año.'}
        ]
    }
}

@app.get("/")
def mostrar_calendario():
    return render_template("calendario.html", datos=calendario_anual)

if __name__ == "__main__":
    app.run(debug=True)