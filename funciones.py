# comando def (declaracion de funciones)
# def miFuncion(a):
#     print(a)


# miFuncion('mi 1era funcion')
# miFuncion('creo que esta facil la vaina')

# def imprimeDato(*argumento1):
#     print('el cometa rojo siempre sera', argumento1[0], 'no el falso', argumento1[1])


# imprimeDato('Char Aznable', 'Full Frontal', 'Anabel Gato')

# def nombreCompleto(apellido, nombre):
#     print(nombre,apellido)

# nombreCompleto(nombre='Char', apellido='Aznable')


# def nombreCompleto2(**kwargs):
#     print(kwargs['nombre'], kwargs['apellido'])


# nombreCompleto2(nombre='Char', apellido='Aznable')

def miFuncion2(argumento = 'Char Aznable'):
    print(argumento)

# miFuncion2('Amuro Ray')
# miFuncion2()

def miFuncionLista(lista):
    for el in lista:
        print(el)


# miFuncionLista(['Char Aznable', 'Full Frontal', 'Anabel Gato'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i


# nombres = concatenaNombres(['Char', 'Aznable'])
# print(nombres) 

def recursion(i):
    if(i<1):
        return i
    print(i)
    recursion(i-1)

recursion(6)