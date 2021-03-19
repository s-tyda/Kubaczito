# Zakres jako zakres indeksów
print(sorted([int(x) for x in input("Podaj liczbę oddzielone spacją.\n").split()], reverse=bool(input("Podaj 1 żeby posortować malejąco, 0 żeby rosnąco.\n")))[int(input("Od którego indeksu wyświetlić?\n")):int(input("Do którego indeksu włącznie wyświetlić?\n")) + 1])
# Zakres jako zakres wartości
[print(j) for j in (lambda a, b: [i for i in sorted([int(x) for x in input("Podaj liczbę oddzielone spacją.\n").split()], reverse=bool(input("Podaj 1 żeby posortować malejąco, 0 żeby rosnąco.\n"))) if a <= i <= b])(int(input("Od jakiej wartości wyświetlić?\n")), int(input("Do jakiej wartości wyświetlić?\n")))]
