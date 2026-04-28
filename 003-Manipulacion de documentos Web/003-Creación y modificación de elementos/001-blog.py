from flask import Flask, render_template
from datetime import datetime


ahora = datetime.now()

app = Flask(__name__)


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
