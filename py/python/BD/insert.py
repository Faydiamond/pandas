#comentario

import sqlite3
#enlace a la bd

connect = sqlite3.connect("informs.db")
#permitir ejecutar consultas
cursor = connect.cursor()
#EJECUTAR QUERY
query = cursor.execute("INSERT INTO PERSONS (NAME,LAST_NAME, EDAD) VALUES ('FABIAN','BARBON',26)")

connect.commit()

connect.close()


