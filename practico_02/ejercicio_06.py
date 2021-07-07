from datetime import *
class Persona():

    def __init__(self, nacimiento):
        self.nacimiento = nacimiento


    def edad(self):
        if datetime.now().day < self.nacimiento.day and datetime.now().month < self.nacimiento.month:
            return datetime.now().year - self.nacimiento.year

        return datetime.now().year - self.nacimiento.year - 1

p = Persona(datetime(1997, 12, 28))
print(p.edad())