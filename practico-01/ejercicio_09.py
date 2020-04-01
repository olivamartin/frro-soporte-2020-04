palabra = "Arriba la birra"

def es_palindromo(palabra):
    palabra_limpia = palabra[0:].replace(' ', '').lower()
    palabraAlReves = ''.join(reversed((palabra_limpia)))
    return palabraAlReves == palabra_limpia


print((es_palindromo(palabra)))


