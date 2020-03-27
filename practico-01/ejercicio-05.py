letra = input("Ingrese letra\n")


def es_vocal(letra):
    if letra.lower() in 'aeiou':
        return True
    else:
        return False


print(es_vocal(letra))
