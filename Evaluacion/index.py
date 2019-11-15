import sqlite3
conexion = sqlite3.connect('estudiantes.db')
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE estudiantes (id INT PRIMARY KEY , nombre VARCHAR(100), apellido VARCHAR(100), cedula INT(200), telefono INT(100))")



#cursor.execute("INSERT INTO estudiantes VALUES (12, 'mary', 'colorado', 5564646, 9451965)")
#cursor.execute("SELECT * FROM estudiantes")
#estudiantes = cursor.fetchone()
#print(estudiantes[1])
#estudiantes = [
    #(1, 'leonardo', 'toro', 84465, 7946551),
    #(2, 'pepe', 'cortes', 848416, 51168468),
    #(3, 'rodrigo', 'alvarez', 611684, 11981989),
#]


#cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?,?)", estudiantes)

#cursor.execute("SELECT * FROM estudiantes")

#estudiantes = cursor.fetchall()

#for estudiantes in estudiantes:
 #   print(estudiantes)
#cursor.execute("UPDATE estudiantes SET  nombre = 'camilo' WHERE id=45")

#cursor.execute("DELETE FROM estudiantes")

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()

