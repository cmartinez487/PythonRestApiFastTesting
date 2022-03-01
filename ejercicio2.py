# ejercicio 1 - Multiplicar 2 numeros sin usar el simbolo de multiplicacion
# a = 4
# b = 8
# resultado1 = 0
# resultado2 = 0

# for x in range(a):
#     resultado1 += b


# for x in range(b):
#     resultado2 += a

# print(resultado1)
# print(resultado2)

# ejercicio 2 - ingresar un nombre y apellido e imprimirlos al revez
# nombre = input('ingresa el nombre: ')
# apellido = input('ingresa ingrese el apellido: ')

# concatenacion = nombre + ' '+ apellido

# print(concatenacion[::-1])

# ejercicio 3 - escribir una funcion que encuentre el elemento menor de una lista

# lista = [1,2,3,4,5,6,7,88,-187,-87]
# menor = 'init'

# for x in lista:
#     if menor == 'init':
#         menor = x
#     else:
#         menor = x if x < menor else menor

# print('menor: ',menor)

# ejercicio 4 - escribir una funcion que devuelva el volumen de una esfera por su radio 4/3 * pi * r ** 3 (** elevar a la potencia)

# def calcularVolumen(r):
#     return 4/3 * 3.14 * r ** 3

# resueltado = calcularVolumen(6)

# print('resultado del calculo: ', resueltado)

# ejercicio 5 - escribir una funcion que indique si el usuario es mayor de edad

# def esMayor(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self, edad):
#         self.edad = edad

# usuario = Usuario(15)
# usuario2 = Usuario(27)

# resultado1 = esMayor(usuario)
# resultado2 = esMayor(usuario2)

# print(resultado1)
# print(resultado2)

# ejercicio 6 - escribir una funcion que indique si el numero ingresado es par o impar

# def esPar(n):
#     return n % 2 == 0

# resultado = esPar(11)

# print(resultado)

# ejercicio 7 - escriba una funcion que indique el numero de vocales que tiene una palabra

# palabra = 'paralelepipedo'
# vocales = 0

# for x in palabra:
#     y = x.lower()
#     vocales += 1 if y =='a' or y =='e' or y =='i' or y =='o' or y =='u' else 0

# print('numero de vocales = ', vocales)

# ejercicio 8 - escriba una aplicacion que reciba cantidad infinita de numeros hasta decir basta
# y luego devuelva la suma de los numeros ingresados

# lista = []
# print('ingrese numeros, para salir escriba "basta"')

# while True: 
#     valor = input('ingrese valor: ')
#     if valor == 'basta':
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print('dato invalido')
#             exit()

# resultado = 0

# for x in lista:
#     resultado += x

# print(resultado)

# ejercicio 9 - escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo 

def agregaNombreaArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a') 
    c.write(nombre + ' ' + apellido + '\n')
    c.close()


agregaNombreaArchivo('Char', 'Aznable')
agregaNombreaArchivo('Amuro', 'Ray')
agregaNombreaArchivo('Ryu', 'Jose')

#  