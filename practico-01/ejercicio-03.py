def operacion(a, b, multiplicar):
    if multiplicar:
        total = a * b
        return total
    else:
        total = a / b
        return total


print(operacion(9, 5, False))
