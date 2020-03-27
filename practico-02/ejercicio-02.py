import numpy as np
class Circulo():
 radio = ''

 def __init__(self, radio):
    self.radio = radio

 def area(self, radio):
    area = np.pi * pow(radio,2)
    return area

 def perimetro(self, radio):
    per = 2 * np.pi * radio
    return per



cir = Circulo(10)
print(cir.area(cir.radio))
print(cir.perimetro(cir.radio))