import numpy as np
class Circulo():

 def __init__(self, radio):
    self.radio = radio

 def area(self):
    area = np.pi * pow(self.radio,2)
    return area

 def perimetro(self):
     return 2 * np.pi * self.radio

cir = Circulo(10)
print(cir.area())
print(cir.perimetro())