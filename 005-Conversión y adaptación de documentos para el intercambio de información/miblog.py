import sqlite3 														
from flask import Flask,render_template		

app = Flask(__name__)											
@app.get("/")																					
def inicio():														
	conexion = sqlite3.connect("blog.db")		
	conexion.row_factory = sqlite3.Row 		
	cursor = conexion.cursor()							
	cursor.execute("SELECT * FROM entradas")
	clientes = cursor.fetchall()						
	
	lista = []															
 
	for fila in clientes:										
		lista.append(dict(fila))   						

	print(lista)														

	
	return render_template("blog.html",datos=lista)	

if __name__ == "__main__":								
	app.run(debug=True)	
