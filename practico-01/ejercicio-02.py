def maximo_de_tres(a, b, c):
    max1 = max(a, b)
    max2 = max(a, c)
    if max1 > max2:
        return max1
    else:
        return max2


print(maximo_de_tres(1, 3, 2))
