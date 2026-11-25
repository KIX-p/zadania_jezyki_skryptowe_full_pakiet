import math


class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def odleglosc(self):
        return math.hypot(self.x, self.y)

    def dystans(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"
