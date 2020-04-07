palabra = "Arriba la birra"

def es_palindromo(palabra):
    palabra_limpia = palabra[0:].replace(' ', '').lower()
    palabraAlReves = palabra_limpia[::-1]
    return palabraAlReves == palabra_limpia


print((es_palindromo(palabra)))


