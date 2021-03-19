import math

print((lambda a, b, c: "Brak" if (delta := b ** 2 - 4 * a * c) < 0 else (-b/(2 * a) if delta == 0 else [(-b - (sqr := math.sqrt(delta))) / (2 * a), (-b + sqr) / (2 * a)]))(1, 6, 8))
