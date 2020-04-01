def operacion(a,b,multiplicar):
    return a*b if multiplicar else a/b

try:
    print(operacion(2,0,False))

except:
    print('No es posible dividir por 0')