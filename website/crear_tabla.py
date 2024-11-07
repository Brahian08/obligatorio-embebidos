import sqlite3

# Conectamos o creamos la base de datos
connection = sqlite3.connect('datos.db')
cursor = connection.cursor()

# Creamos una tabla de ejemplo
cursor.execute('''
CREATE TABLE datos (
    id INTEGET PRIMARY KEY,
    ts DATETIME DEFAULT CURRENT_TIMESTAMP,
    frecuencia FLOAT NOT NULL,
    luz INTEGER NOT NULL
)
''')

# Insertamos algunos datos
cursor.execute('INSERT INTO datos (frecuencia, luz) VALUES (?, ?)', (40.05, 132))
cursor.execute('INSERT INTO datos (frecuencia, luz) VALUES (?, ?)', (47.43, 234))
cursor.execute('INSERT INTO datos (frecuencia, luz) VALUES (?, ?)', (55.76, 405))

# Guardamos los cambios y cerramos la conexión
connection.commit()
connection.close()