app = Flask(__name__)											

@app.get("/")																							
def inicio():														
	conexion = sqlite3.connect("portafolio.db")		
	conexion.row_factory = sqlite3.Row 			
	cursor = conexion.cursor()							
	cursor.execute("SELECT * FROM piezas")
	piezas = cursor.fetchall()					
	
	lista = []															
 
	for pieza in piezas:										
		lista.append(dict(pieza))   						

	print(lista)														

	
	return render_template("portafolio.html",datos=lista)	

if __name__ == "__main__":								
	app.run(debug=True)										
