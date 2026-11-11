from math import hypot, isfinite, pi

class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def odleglosc(self):
        return hypot(self.x, self.y)

    def dystans(self, inny):
        return hypot(self.x - inny.x, self.y - inny.y)

    def __str__(self):
        return f"Punkt({self.x:g}, {self.y:g})"

    def __repr__(self):
        return f"({self.x:g}, {self.y:g})"

class Kolo(Punkt):
    def __init__(self, x=0, y=0, r=1):
        if not isfinite(r) or r < 0:
            raise ValueError("Promień musi być skończony i nieujemny.")
        super().__init__(x, y)
        self.r = r

    def obwod(self):
        return 2 * pi * self.r

    def pole(self):
        return pi * self.r ** 2

    def __str__(self):
        return f"Kolo({self.x:g}, {self.y:g}, {self.r:g})"

    def __repr__(self):
        return f"({self.x:g}, {self.y:g}, {self.r:g})"

    def przesun(self, wektor):
        dx, dy = wektor
        self.x += dx
        self.y += dy

    def cz_wsp(self, inne):
        return self.dystans(inne) > self.r + inne.r

if __name__ == "__main__":
    p0 = Punkt()
    p1 = Punkt(1.2, 2)
    p2 = Punkt(3, 4)
    print("Punkt domyślny:", p0)
    print("str(p1):", str(p1), "repr(p1):", repr(p1))
    print("Odległość p2 od (0, 0):", p2.odleglosc())
    print("Dystans p0-p2:", p0.dystans(p2))
    k0 = Kolo()
    k1 = Kolo(2, 0, 1)
    print("Koło domyślne:", k0, "repr:", repr(k0))
    print("Obwód:", k0.obwod(), "Pole:", k0.pole())
    k1.przesun((1, 2))
    print("Po przesunięciu krotką:", repr(k1))
    k1.przesun([-1, -1])
    print("Po przesunięciu listą:", repr(k1))
    przypadki = [("rozłączne", Kolo(3, 0)), ("styczne", Kolo(2, 0)),
                 ("zachodzące", Kolo(1, 0)), ("zawarte", Kolo(0, 0, 0.5))]
    for opis, inne in przypadki:
        print(opis, "- brak części wspólnej:", k0.cz_wsp(inne))
