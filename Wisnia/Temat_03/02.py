def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


lista = list(fib(int(input())))
print(lista)
