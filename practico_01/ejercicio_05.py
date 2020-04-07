letra = input("Ingrese letra\n")


def es_vocal(letra):
    return letra.lower() in 'aeiou'



print(es_vocal(letra))
