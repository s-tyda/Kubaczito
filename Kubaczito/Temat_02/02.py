# Co za głupi pomysł mi wpadł do głowy, ale działa, jest w jednej linijce i jest list comprehension :D
print((fun := lambda n, lista: lista + [lista.append(lista[x-1] + lista[x-2]) for x in range(3, n)][:0])(int(input()), [0, 1, 1]))
