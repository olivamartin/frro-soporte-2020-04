import random

class Persona():

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.dni = self.generar_dni()
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        return self.edad >= 18


    def print_data(self):
        return print(self.nombre, self.edad, self.sexo, self.sexo, self.altura, self.dni)

    def generar_dni(self):
        dni = ''
        for i in range(8):
            x = random.randint(0, 9)
            dni += str(x)
        return dni

if __name__ == "__main__":
    p = Persona('Martin', 17, 1.70, 'H', 70)
    print(p.es_mayor_edad())
    p.print_data()