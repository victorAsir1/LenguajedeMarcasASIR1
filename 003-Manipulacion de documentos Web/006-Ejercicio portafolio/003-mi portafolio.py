from flask import Flask, render_template  # <--- ¡Importación corregida!
import os

app = Flask(__name__)

# Configuración de rutas automáticas por si usas archivos externos en el futuro
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def inicio():
    # De momento devolvemos texto directo para comprobar que el servidor arranca bien
    return "<h1>¡Mi Portafolio con Flask funciona correctamente!</h1><p>Servidor activo en Python 3.13.</p>"

if __name__ == "__main__":
    # Arrancamos el servidor en modo depuración
    app.run(debug=True)