def filter(fun, lista):
    return [x for x in lista if fun(x)]


print(filter(lambda x: not bool(x % 2), [1, 2, 3, 4, 5]))
