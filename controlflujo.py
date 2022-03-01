# if 3 < 2:
#     print("esta condicion en la vida se va a complir")

#     # a == b
#     # a != b
#     # a < b
#     # a > b
#     # a <= b
#     # a => b

# if 2 == 2:
#     print("claro que 2 es igual a 2, sorete...")

# if 3 != 2:
#     print("es que eres bien sorete!!! claro que 3 es diferente de 2")

# if y elif (condiciones multiples)
# if 2 > 5:
#     print('5 es mayor a 2')
# elif 2 > 5:
#     print('2 es menor a 5 - 1er elif')
# elif 2 < 5:
#     print('2 es menor a 5 - 2d elif')
# else:
#     print('yo me imprimo solo si los anteriores casos son falsos')

# if 2 > 5:
#     print('5 es mayor a 2')
# else:
#     print('yo me imprimo solo si los anteriores casos son falsos - 2')

# operadores ternarios - 1era forma
# if 2<5: print("ejecuta un if en una linea")

# operadores ternarios - 2da forma
# print('cuando devuelve true') if 5>2 else print('cuando devuelve false')

if 2 < 5 and 5 > 2:
    print('esto si se va a ejecutar porque ambas devuelven true') 

if 2 > 5 and 5 > 2:
    print('hay una falsa, esto no se mostrara') 

if 2 > 5 or 5 > 2:
    print('hay una falsa, pero como se evalua en un or, esto se mostrara') 

if 2 > 5 or 5 < 2:
    print('hay 2 falsa, esto no se mostrara') 