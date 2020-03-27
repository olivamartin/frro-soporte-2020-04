from datetime import *
class Persona():
    nombre = ''
    nacimiento = ''
    sexo = ''
    peso = ''
    altura = ''
    dni = ''

    def __init__(self, nacimiento):
        self.nacimiento = nacimiento


    def edad(self):
     if datetime.now().day < self.nacimiento.day and datetime.now().month < self.nacimiento.month:
         return datetime.now().year - self.nacimiento.year - 1
     else:
         return datetime.now().year - self.nacimiento.year

p = Persona(datetime(1997, 12, 28))
print(p.edad())