palabra = "anana"
# Para frases hay que eliminar los espacios en blanco, pero solo pide para palabras
def es_palindromo(palabra):
    j = len(palabra)-1
    contador = 0
    for i in range(len(palabra)):
        if palabra[i] == palabra[j]:
            j -= 1
        else:
            j -= 1
            contador += 1
    if contador == 0:
        return True
    else:
        return False

print(es_palindromo(palabra))

