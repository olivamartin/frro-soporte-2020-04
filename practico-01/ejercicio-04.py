temp = input('Introducir temperatura en Fahrenheit:\n')
fahr = float(temp)


def convertir(fahr):
    celcius = (fahr - 32) * 5 / 9
    return celcius


print(f'{convertir(fahr)}{" grados Celcius"}')
