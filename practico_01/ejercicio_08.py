palabra = "holap"

def mitad(palabra):
    if len(palabra) % 2 == 0:
        return palabra[len(palabra)//2:]

    return palabra[round(len(palabra)//2):]

print(mitad(palabra))
