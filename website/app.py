from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta principal que muestra los datos de la base de datos
@app.route('/')
def index():
    # Conexión a la base de datos
    connection = sqlite3.connect('datos.db')
    cursor = connection.cursor()

    # Obtenemos todos los datos de la tabla "users"
    cursor.execute('SELECT * FROM datos')
    datos = cursor.fetchall()

    # Cerramos la conexión
    connection.close()

    # Pasamos los datos a la plantilla
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)