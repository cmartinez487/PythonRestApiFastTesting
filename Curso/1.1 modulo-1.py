import modulos as xs
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
