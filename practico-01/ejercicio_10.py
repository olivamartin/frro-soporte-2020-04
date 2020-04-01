lista1 = ['a', 5, 9]
lista2 = ['a', 7, 8]

def superposicion_x(lista1, lista2):

    check = False
    for x in lista1:
        for y in lista2:
            if x == y:
             check = True
    return check

print(superposicion_x(lista1, lista2))

