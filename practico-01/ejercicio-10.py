lista1 = [2, 5, 9]
lista2 = [2, 7, 8]

def superposicion_x(lista1, lista2):
    contador = 0
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                contador +=1
    if contador != 0:
        return True
    else:
        return False

print(superposicion_x(lista1, lista2))

