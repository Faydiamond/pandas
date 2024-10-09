class createtable:

    def __init__(self):
        #nombre tabla
        print("hgere")




    def show_table(self):
        print(self.table)

    def add_campesTable (self):
        self.table = input("por favor digite el nombre de la tabla")
        self.my_divisas = dict()
        try:
            self.cantidad_campos = int (input("Digite la cantidad de campos de la bd"))
            self.i=0
            while self.i <=self.cantidad_campos:
                self.clave = input("por favor digite el nombre del campo ")
                self.valor = input("por favor digite el valor del campo ")
                self.my_divisas.setdefault(self.clave,self.valor)
                self.i +=1
        except ValueError:
            print ("por favor digite un número")
        except:
            print ("Por favor verifique que esta digitando un número")


    def parameters_send (self):
        print(self.my_divisas)
        """
        self.field = str(self.my_divisas).replace(':',' ').replace("'","").replace('}',')').replace('{','(');
        self.my_query ="CREATE TABLE "+ self.table +" {}".format(self.field)
        print("mysqry: " ,self.my_query)
        import sqlite3
        try:
            print("aqui")
            self.con = sqlite3.connect("dfgfsdggf.db")
            self.cursor = self.con.cursor()
            self.cursor.execute (self.my_query)
            self.con.commit()
            self.con.close()
        except Exception:
            print("Errorerror", Exception)


        #cursor ejecuta sentencias sql en py"""


c = createtable()

c.add_campesTable()
c.parameters_send()