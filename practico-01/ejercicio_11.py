import math

num = 8

def es_primo(num):

    if (num % 2 == 0 and num > 2) or num == 1 :
        return False
    return all(num % i for i in range(3, int(math.sqrt(num)) + 1, 2))

print(es_primo(num))
