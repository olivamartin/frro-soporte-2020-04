lista = [3,7,9,6,'b','d','c']


def numero_al_final(lista):
    lista2 = lista[0:]
    j = 0

    for i in range(len(lista)):
        if str(lista[i]).isalpha():
            lista2[j] = lista[i]
            j = j + 1
    
    for k in range(len(lista)):
        if str(lista[k]).isdigit():
            lista2[j] = lista[k]
            j = j + 1


    return lista2


print(numero_al_final(lista))
