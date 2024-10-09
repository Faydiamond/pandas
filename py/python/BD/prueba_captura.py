cantidad_campos = int (input("Digite la cantidad de campos de la bd"))
my_divisas = dict()
i = 0
while i <=cantidad_campos:
    clave = input("por favor digite el nombre del campo")
    valor = input("por favor digite el valor del campo")
    my_divisas.setdefault(clave,valor)
    i +=1
for k,v in my_divisas.items():
    print (k, ' ', v,)