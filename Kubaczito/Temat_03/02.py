import math


class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.dist([self.x, self.y], [other.x, other.y])


class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def dist(self, other):
        return math.dist([self.x, self.y, self.z], [other.x, other.y, other.z])
