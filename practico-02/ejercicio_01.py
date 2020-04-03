class rectangulo:

 def __init__(self,base,altura):
     self.base = base
     self.altura = altura

 def area(self):
    return self.base * self.altura


rec = rectangulo(10, 3)
print(rec.area())


