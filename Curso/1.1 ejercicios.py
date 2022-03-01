# dato = input('Ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
    # print('El dato existe:', dato)
# else:
    # print('El dato no existe :(', dato)

primero = input('Ingrese primer número: ')

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operación: ')

if simbolo == '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('El símbolo ingresado no es válido')

