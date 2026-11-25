from Punkt import Punkt
from Kolo import Kolo


if __name__ == "__main__":
    print("Zadanie 1")
    p1 = Punkt(3, 4)
    p2 = Punkt(6, 8)
    print(p1)
    print(p2)
    print(repr(p1))
    print("Punkt domyslny:", Punkt())
    print("Odleglosc:", p1.odleglosc())
    print("Dystans:", p1.dystans(p2))

    print("\nZadanie 2")
    k1 = Kolo()
    k2 = Kolo(3, 4, 2)
    print(k1)
    print(k2)

    print("\nZadanie 3")
    print("Obwod:", k2.obwod())
    print("Pole:", k2.pole())
    print(str(k2))
    print(repr(k2))

    print("\nZadanie 4")
    k1 = Kolo(2, 0, 1)
    print(k1)
    k1.przesun((1, 2))
    print(k1)
    k1.przesun([-1, -1])
    print(k1)

    print("\nZadanie 5")
    k1 = Kolo(0, 0, 2)
    k2 = Kolo(8, 0, 2)
    k3 = Kolo(2, 0, 2)
    print(k1.cz_wsp(k2))
    print(k1.cz_wsp(k3))
