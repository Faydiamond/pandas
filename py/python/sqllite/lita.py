cantidad = int( input("Por favor digite la cantidad de frutas que desea agregar a la lista "))
frutas   = []

i = 0

while i <= cantidad :
    fruta= input("Por favor digite el nombre de la fruta ")
    frutas.append(fruta)
    i+=1

for f in frutas:
    print(f)