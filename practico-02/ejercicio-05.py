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

    def __init__(self, nombre, edad, sexo, peso, altura, nombre_carrerra, fecha_ingreso, cant_materias, cant_aprobadas):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.nombre_carrera = nombre_carrerra
        self.fecha_ingreso = fecha_ingreso
        self.cant_materias = cant_materias
        self.cant_aprobadas = cant_aprobadas


e1 = Estudiante('Martin', 22, 'H', 70, 1.70, 'Ingenieria en sistemas', datetime(2017, 3, 15), 36, 26)
e2 = Estudiante('Laura', 23, 'H', 70, 1.80, 'Ingenieria mecanica', datetime(2017, 3, 15), 36, 26)
e3 = Estudiante('Tomas', 22, 'H', 70, 1.85, 'Ingenieria Quimica', datetime(2017, 3, 15), 35, 23)
e4 = Estudiante('Jorge', 22, 'H', 70, 1.85, 'Ingenieria Electrica', datetime(2017, 3, 15), 35, 23)
e5 = Estudiante('Diego', 22, 'H', 70, 1.85, 'Ingenieria Electrica', datetime(2017, 3, 15), 35, 23)

estudiantes = [e1, e2, e3, e4, e5]

contISI = 0
contMec = 0
contQ = 0
contEl = 0

for e in estudiantes:
    if e.nombre_carrera == 'Ingenieria en sistemas':
        contISI += 1
    elif e.nombre_carrera == 'Ingenieria mecanica':
            contMec += 1
    elif e.nombre_carrera == 'Ingenieria Electrica':
        contEl += 1
    else:
        contQ += 1

for i in range(len(estudiantes)):
    if i == 0:
        if (estudiantes[i].nombre_carrera == 'Ingenieria en sistemas'):
            d1 = {estudiantes[i].nombre_carrera: contISI}
        elif (estudiantes[i].nombre_carrera == 'Ingenieria mecanica'):
            d1 = {estudiantes[i].nombre_carrera: contMec}
        elif (estudiantes[i].nombre_carrera == 'Ingenieria Quimica'):
            d1 = {estudiantes[i].nombre_carrera: contQ}
        else:
            d1 = {estudiantes[i].nombre_carrera: contEl}
    elif estudiantes[i].nombre_carrera not in d1:
        if (estudiantes[i].nombre_carrera == 'Ingenieria en sistemas'):
            d2 = {estudiantes[i].nombre_carrera: contISI}
            d1.update(d2)
        elif (estudiantes[i].nombre_carrera == 'Ingenieria mecanica'):
            d2 = {estudiantes[i].nombre_carrera: contMec}
            d1.update(d2)
        elif (estudiantes[i].nombre_carrera == 'Ingenieria Quimica'):
            d2 = {estudiantes[i].nombre_carrera: contQ}
            d1.update(d2)
        else:
            d2 = {estudiantes[i].nombre_carrera: contEl}
            d1.update(d2)

print(d1)
