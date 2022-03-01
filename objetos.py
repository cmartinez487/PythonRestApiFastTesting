class Usuario:
    # palabra reservada init (solicita parametros para poder ejecutar la clase)
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola! mi nombre es", self.nombre,self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo', self.nombre, 'y soy el comandante de la White Base')


# usuario = Usuario('Char', 'Aznable')
# # usuario2 = Usuario('Full','Frontal')

# # print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# usuario.saludo()
# usuario.nombre = 'Amuro'
# usuario.apellido = 'Ray'
# usuario.saludo()

# # del usuario.nombre
# # del usuario
# # print(usuario)

# admin = Admin('Brith','Noa')
# admin.superSaludo()

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo,' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self,nombre,onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('instanciando un perro')


class Canario(Animal):
    tipo = 'canario'

gato = Gato('Patan', 'maullido') 
gato.saludo()

perro = Perro('Lindo Pulgoso', 'ladrido') 
perro.saludo()

canario = Canario('Twity', 'silvido') 
canario.saludo()