# comando input (ingresa datos a una variable)
# dato = input('ingrese date: ')

# # print(dato)

# lista = ['Hola','char','como estas hoy?','todo bien?','adios...']

# if lista.count(dato) > 0:
#     print('el dato existe', dato)
# else:
#     print('el dato no existe :(',dato)

# comado o funcion int (convierte en un entero los datos suministrado por un input)
# primero = input('ingrese 1er numero: ')

# try:
#     primero = int(primero)
# except:
#     primero = 'hola'

# segundo = input('ingrese 2do numero: ')

# try:
#     segundo = int(segundo)
# except:
#     segundo = 'hola'

# if primero == 'hola' or segundo == 'hola':
#     print('esta ingresando mal los datos para el ejercicio, prueba solo con numeros...')

# else:
#     suma = primero + segundo
#     print(suma) 


# primero = input('ingrese 1er numero: ')

# try:
#     primero = int(primero)
# except:
#     primero = 'hola'

# if primero == 'hola':
#     print('el valor ingresado no es un entero')
#     exit()

# segundo = input('ingrese 2do numero: ')

# try:
#     segundo = int(segundo)
# except:
#     segundo = 'hola'

# if segundo == 'hola':
#     print('el valor ingresado no es un entero')
#     exit()

# suma = primero + segundo
# print(suma) 

primero = input('ingrese 1er numero: ')

try:
    primero = int(primero)
except:
    primero = 'hola'

if primero == 'hola':
    print('el valor ingresado no es un entero')
    exit()

segundo = input('ingrese 2do numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'hola'

if segundo == 'hola':
    print('el valor ingresado no es un entero')
    exit()

simbolo = input('ingresa operacion: ')

if simbolo == '+':
    operacion = primero + segundo
    print('Suma: ', operacion) 
elif simbolo == '-':
    operacion = primero - segundo
    print('Resta: ', operacion) 
elif simbolo == '*':
    operacion = primero * segundo
    print('Multiplicacion: ', operacion) 
elif simbolo == '/':
    operacion = primero / segundo
    print('Division: ', operacion) 
else:
    print('el simbolo ingresado no es valido')

