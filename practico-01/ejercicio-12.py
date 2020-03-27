num = input('Ingrese numero\n')
numero = int(num)

def suma(numero):
 contador = 0
 for i in range(numero+1):
         contador += i

 return contador

print(suma(numero))