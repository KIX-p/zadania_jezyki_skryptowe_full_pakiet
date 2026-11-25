import math
from Punkt import Punkt


class Kolo(Punkt):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.r = r

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r**2

    def __str__(self):
        return f"Kolo({self.x}, {self.y}, {self.r})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.r})"

    def przesun(self, wektor):
        self.x += wektor[0]
        self.y += wektor[1]

    def cz_wsp(self, other):
        return self.dystans(other) > self.r + other.r
