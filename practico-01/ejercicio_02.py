nros1 = [1,10,5]
nros2 = [4,9,18]

def maximo_de_tres(nros):
    maximo = nros[0]
    for i in nros:
        maximo = max(maximo,i)
    return maximo


assert maximo_de_tres(nros1) == 10
assert maximo_de_tres(nros2) == 18
