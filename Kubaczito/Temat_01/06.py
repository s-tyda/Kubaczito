from functools import reduce
print(reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (int(input("Ile liczb Fibonacciego wyświetlić?\n")) - 2), [0, 1]))
