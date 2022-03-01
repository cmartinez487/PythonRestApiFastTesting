#aca hay un comentario, de los que no les gusta a los ineptos de efecty
if 3 > 5:
    print('esto no se va a cumplir/imprimir')
    

#aca hay un comentario, de los que no les gusta a los ineptos de efecty
#if 6 > 3:
    #print('Hola Carlos, estas progresando')

x = 4
y = ' esta aprendiendo, aprendiendo!!'

#print(x, y)

#Variables multiples
nombre_user,email_usuario,edad_usuario = 'char','cmartinez487@gmail.com','33'

Mensaje_nombre = 'Usuario: '
Mensaje_correo = 'Correo: '
Mensaje_edad = 'Edad: '

#print(Mensaje_nombre + nombre_user + ', ',Mensaje_correo + email_usuario +', ',Mensaje_edad + edad_usuario)
v1 = v2 = v3 = 'Error!!'

#print(v1, v2, v3)

#tipo de datos 
oracion = 'Hola Carlos!' #string
oracion_cd = "Hola Char" #sting
entero = 4 #int
flotante = 4.2 #float
complejo = 1j

#print(oracion,oracion_cd,entero,flotante,complejo)

#listas
lista1 = ['Hola','Char','como estas?']
lista2 = lista1.copy()

#comando append (agrega elemanetos a la lista)
lista1.append('Recuerda, un paso a la vez')

#comando clear (elimina los elementos de la lista)
#lista1.clear()

#print(lista1, lista2)

#comando count (cuenta elemento determinado en una lista)  
#print(#lista.count('hola'))

#comando len (cuenta los elementos que existen en la lista)
#print(len(lista1), len(lista2))

largoLista = len(lista1)
largoLista2 = len(lista2)

#print(largoLista,largoLista2)

#print(lista1[0],lista1[1],lista1[2])

#comando pop (elimina el ultimo elementos de una lista)
#lista1.pop()

#comando remove (elimina valor de una lista, dependiendo del elemento seleccionado)
#lista1.remove('Hola')

#comando reverse(invierte el orden de la lista)
lista1.reverse()

#comando sort (ordena la lista, nota: solo puede ser usado cuando se tiene el mismo tipo de datos en la lista)
lista1.sort()

#print(lista1)

tupla = ('hola','mundo','soy una tupla')

#print(tupla)

#comando count - funciona igual que en las listas
#print(tupla.count('hola'))

#comando index (busca la posicion de un valor en la tupla)
#print(tupla.index('hola'))

#comando list (convierte la tupla en una lista)  
ListaDeTupla = list(tupla)
ListaDeTupla.append('chanchito')

#print(ListaDeTupla)

rango = range(6)

#print(rango)

# crear diccionario
diccionario = {
    "nombre": "chanchito feliz",
    "raza": "persa",
    "edad": 5
}

print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))

diccionario['nombre'] = 'Jako'

# print(diccionario.get('nombre'))
# print(len(diccionario))

diccionario['ronronea'] = 'si'

# print(diccionario)

#comandos pop, del y popitem (pop y del eliminar valores de diccionario, popitem elimina el ultimo del borra el item seleccionado del diccionario)
# diccionario.pop('ronronea')
# diccionario.popitem()
# del diccionario['ronronea']

# comando copy (copia el diccionario creado anteriormente)
copiadiccionario = diccionario.copy()
diccionario.popitem()
# print(diccionario, copiadiccionario)

# comando clear (elimina todos los items de un diccionario)
diccionario.clear()

# constructor dict (otra forma de copiar un diccionario, tambien es usado para crear un diccionarios, eso esta mas abajo)
CopiaDeCopia = dict(copiadiccionario)

# print(diccionario, copiadiccionario, CopiaDeCopia)

#diccionarios anidados (Forma 1)
#dicPerros = {
#    "Dante":{
#        "nombre": "Dante",
#        "edad": 1
#    },
#    "Gaia":{
#        "nombre": "Gaia",
#        "edad": 1
#    }
#} 

#diccionarios anidados (Forma 2)

Dante = {
        "nombre" : "Dante",
        "edad" : 2
    }

Gaia = {
        "nombre" : "Gaia",
        "edad" : 1
    }

dicPerros = {
    "Dante":Dante,
    "Gaia":Gaia,
}

# print(dicPerros)

# constructor dict (funcion para crear diccionarios)
Perros = dict(nombre="Pandora", edad = 9)
dicPerros['Pandora'] = Perros 

# print(dicPerros)
# print(dicPerros['Dante'])
# print(dicPerros['Gaia'])
# print(dicPerros['Pandora'])

# valores Boolean
verdadero = True
falso = False

#print(verdadero,falso)