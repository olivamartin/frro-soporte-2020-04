class rectangulo:
 base = ''
 altura = ''

 def __init__(self,base,altura):
     self.base = base
     self.altura = altura

 def area(self, a, b):
     area = a * b
     return area


rec = rectangulo(10, 3)
print(rec.area(rec.base,rec.altura))


