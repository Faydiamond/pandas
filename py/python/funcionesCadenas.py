message = ''' Hey this message
is for you, so i have a good memories about you! '''

print (message)

print('cantidad de caracteres en la cadena: ',len (message))


message_upper = ''' Hey this message
is for you, so i have a good memories about you! '''

print(message_upper.upper())


#convertir a mayusculas

zen = 'este es tu mensaje!'

zen2 = zen.upper()

print (zen2)

#a minusculas lower

zen3 = zen2.lower()

print (zen3)


#palabras split

worlds = message.split()

print (worlds)

print (type(worlds))

for w in worlds:
    print ('in the for ',w)

list_string = 'verdes,azules,cafes,negros'
print(list_string)
list_string.split(',')

print (list_string)

name = input ('Digite su nombre')
age = int(input('Digite su edad'))

print('Hola {}, tu edad es {}'.format(name,age))

d = 50/12

print ('el resultado de la division es: {x}'.format(x=d))

#formatear de manera abreviada

print (f"Hola {name}, tu edad es {age}")