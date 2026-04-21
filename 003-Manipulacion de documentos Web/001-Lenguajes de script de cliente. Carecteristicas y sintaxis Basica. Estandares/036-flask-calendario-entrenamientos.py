from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    cadena = '''
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f7f4;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        h1 {
            color: #2c3e50;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        .calendario {
            max-width: 600px;
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            text-align: center;
        }
        .dia {
            width: 60px;
            height: 60px;
            border: none;
            display: inline-block;
            text-align: center;
            line-height: 60px;
            margin: 5px;
            background-color: #e8f4fd;
            color: #3498db;
            font-weight: bold;
            border-radius: 10px;
            transition: transform 0.2s, background-color 0.2s;
            cursor: pointer;
        }
        .dia:hover {
            background-color: #3498db;
            color: white;
            transform: scale(1.1);
        }
        .especial {
            background-color: #ffeaa7;
            color: #d35400;
        }
    </style>
    <div class="calendario">
        <h1>🐣 Planificador de Vacaciones de Pascua 🐰</h1>
        <p>Haz clic en los días para planificar tus actividades</p>
    '''
    
    for dia in range(1, 31):
        clase_extra = " especial" if dia in [10, 11, 12, 13] else ""
        cadena += f'<div class="dia{clase_extra}">{dia}</div>'
    
    cadena += '</div>'
    return cadena

if __name__ == "__main__":
    app.run(debug=True)
