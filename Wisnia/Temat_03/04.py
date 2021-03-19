import math


def fun(lista):
    return sorted(lista, key=lambda x: math.dist(x, (0, 0)))


lista = [(2.0, 4.0), (5.0, 7.0), (0.0, 0.5)]
print(fun(lista))
