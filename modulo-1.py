# import modulos as model

# print(model.pilotos)
# model.saludo('Char')

from modulos import saludo, pilotos
from camelcase import CamelCase

c = CamelCase()

s = 'esta oracion necesita camelcase'

cc = c.hump(s)

# print(model.pilotos)
# saludo('Char')

print (cc)

