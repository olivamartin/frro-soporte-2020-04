from datetime import *
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


    def generar_dni(self):
        dni = ''
        for i in range(8):
            x = random.randint(0, 9)
            dni = dni + str(x)
        self.dni = dni



class Estudiante(Persona):
    nombre_carrera = ''
    fecha_ingreso = ''
    cant_materias = ''
    cant_aprobadas = ''

    def __init__(self,nombre, edad, sexo, peso, altura, nombre_carrera, fecha_ingreso, cant_materias, cant_aprobadas):
       super().__init__(nombre, edad, sexo, peso, altura)
       self.nombre_carrera = nombre_carrera
       self.fecha_ingreso = fecha_ingreso
       self.cant_materias = cant_materias
       self.cant_aprobadas = cant_aprobadas


    def avance(self):
        return (self.cant_aprobadas / self.cant_materias) * 100

    def edad_ingreso(self):
        if (datetime.now().day < self.fecha_ingreso.day ) and (datetime.now().month <  self.fecha_ingreso.month):
            return self.edad - (datetime.now().year - self.fecha_ingreso.year -1)
        else:
            return self.edad - (datetime.now().year - self.fecha_ingreso.year)


e = Estudiante('Martin', 22, 'H',70, 1.70,'Ing en sistemas',datetime(2017,3,15), 36, 26 )

print('{}{}'.format(e.edad_ingreso(),'\n'))
print('{}{}'.format(e.avance(),'%'))



