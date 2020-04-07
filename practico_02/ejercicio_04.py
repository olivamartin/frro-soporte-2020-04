from datetime import *
import ejercicio_03 as e3

class Estudiante(e3.Persona):


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


if __name__ == "__main__":
    e = Estudiante('Martin', 22, 'H',70, 1.70,'Ing en sistemas',datetime(2017,3,15), 36, 26 )
    print(e.edad_ingreso())
    print('{}{}'.format(e.avance(),'%'))



