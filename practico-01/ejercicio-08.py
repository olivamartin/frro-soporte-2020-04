palabra = "holas"

def mitad(palabra):
    if len(palabra) % 2 == 0:
        return palabra[int(len(palabra)/2):]
    else:
       return palabra[int(round(len(palabra))/2):]

print(mitad(palabra))
