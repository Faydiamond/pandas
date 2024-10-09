
class divisas():
    def __init__(self):
        #create dictionary
        self.my_divisas = dict()
        self.my_divisas = {'Dolar':'$', 'Pesos':'$', 'Euros':'€','Dolar Canadiense':'C$'}
        #print(self.my_divisas)

    def exist_divisa(self):
        #type divisa?
        self.type_divisas = input(' Ingrese su divisa ')
        for k,v in self.my_divisas.items():
            if(self.type_divisas==k):
                print ('la divisa es',k, 'y su respectivo simbolo es:',v)
            else:
                print('No exíste la divisa en la b.d')
                break

    def add_divisas(self):
        self.Name_Divisa = input(' Digite el nombre de la divisa que quiere agregar')
        self.Valor_Divisa = input(' Digite el simbolo de la divisa')
        self.my_divisas.setdefault(self.Name_Divisa,self.Valor_Divisa)

    def show_divisas(self):
        for k,v in self.my_divisas.items():
            print ('Divisa:', k, 'y su simbolo es:',v)

    def delete_divisa(self):
        self.valu = input ('Por favor digite la divisa que quiere eliminar')
        self.my_divisas.pop(self.valu)


d=divisas()
#d.exist_divisa()
#d.add_divisas()

#4d.delete_divisa()
d.show_divisas()