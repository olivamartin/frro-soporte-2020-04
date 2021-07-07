temp = input('Introducir temperatura en Fahrenheit:\n')
fahr = float(temp)

def convertir(fahr):
     return (fahr - 32) * 5 / 9


print(f'{convertir(fahr)}{" grados Celcius"}')
