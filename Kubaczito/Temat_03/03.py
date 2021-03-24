import math


class Liczba:
    def __init__(self, number):
        self.digits = [x for x in str(number)]

    def __str__(self):
        return "".join(self.digits)

    def __mul__(self, other):
        if isinstance(other, int):
            this = int(self.__str__())
            return Liczba(this * other)
        elif isinstance(other, Liczba):
            this = int(self.__str__())
            other = int(other.__str__())
            return Liczba(this * other)

    @staticmethod
    def factorial(n):
        return math.factorial(n)
