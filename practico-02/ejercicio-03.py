import random

class Persona():
    nombre = ''
    edad = ''
    sexo = ''
    peso = ''
    altura = ''
    dni = ''

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def print_data(self):
        return print(self.nombre, self.edad, self.sexo, self.sexo, self.altura, self.dni)

    def generar_dni(self):
        dni = ''
        for i in range(8):
            x = random.randint(0, 9)
            dni = dni + str(x)
            self.dni = dni

p = Persona('Martin', 21, 1.70, 'H', 70)

print(p.es_mayor_edad())
p.generar_dni()
p.print_data()