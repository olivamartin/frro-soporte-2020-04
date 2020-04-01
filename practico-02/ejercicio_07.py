from datetime import *
import numpy as np
class Ejercicio:

    def Inicio(self, fecha):
        if fecha.month >= 7 :
            return datetime(fecha.year , 7, 1)
        if fecha.month < 7:
            return datetime(fecha.year -1 , 7, 1)


    def Fin(self, fecha):
        if fecha.month <=6:
            return datetime(fecha.year , 6, 30)
        elif fecha.month > 6:
           return datetime(fecha.year + 1 , 6, 30)

    def Semana(self, fecha):
        fec = self.Fin(fecha)
        dias = str(datetime.now() - fec)
        dias2 = int(dias[0:3])
        semanas = int(np.trunc(dias2 / 7))
        return semanas


e = Ejercicio()
print(e.Inicio(datetime(2017, 3, 15)))
print(e.Fin(datetime(2017, 2, 1)))
print(e.Semana(datetime(2017, 2, 1)))
