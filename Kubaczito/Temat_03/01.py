class LiczbaZespolona:
    def __init__(self, real, imag):
        self.z = complex(real, imag)

    def modul(self):
        return abs(self.z)

    def __add__(self, other):
        z = self.z + other.z
        return LiczbaZespolona(z.real, z.imag)

    def __str__(self):
        return str(self.z)

    def __mul__(self, other):
        z = self.z * other.z
        return LiczbaZespolona(z.real, z.imag)

    def __truediv__(self, other):
        z = self.z / other.z
        return LiczbaZespolona(z.real, z.imag)

    def __sub__(self, other):
        z = self.z - other.z
        return LiczbaZespolona(z.real, z.imag)

    def __lt__(self, other):
        return self.modul() < other.modul()

    def __le__(self, other):
        return self.modul() <= other.modul()

    def __eq__(self, other):
        return self.modul() == other.modul()

    def __ne__(self, other):
        return self.modul() != other.modul()

    def __gt__(self, other):
        return self.modul() > other.modul()

    def __ge__(self, other):
        return self.modul() >= other.modul()
