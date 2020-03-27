lista = [2, 2, 3, 4]

def multiplicar(lista):
    total = 0
    for i in range(4):
        if i == 0:
            total = lista[0]
        else:
            total = total * lista[i]

    return total

print(multiplicar(lista))
