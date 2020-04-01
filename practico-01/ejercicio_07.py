lista = [3,'b',9,5,7,7,'d','c']

def numero_al_final(lista):

    for i in lista *2:
        if str(i).isdigit():
            lista.remove(i)
            elemento = i
            lista.append(elemento)

    return lista

print(numero_al_final(lista))
