import math


def fun(lista, point):
    return [(math.dist(i, point), i) for i in sorted(lista, key=lambda x: math.dist(x, point))]
