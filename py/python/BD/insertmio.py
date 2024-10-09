#importo el modulo sqlite3
import sqlite3
#connect
connect = sqlite3.connect("informs.db")
#creo variable pa querys
cursor = connect.cursor()
#Query y ejecucion
query = cursor.execute("INSERT INTO PERSONS (NAME,LAST_NAME,EDAD) values ('Juan','Sanchez',22),('Juanita','Sanchez',23),('Juan','Lopez',22)")

connect.commit()

connect.close()


