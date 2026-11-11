import pickle
from pathlib import Path

folder = Path(__file__).resolve().parent
wyjatki = {"Kosma", "Barnaba", "Bonawentura", "Jarema", "Kuba"}
zenskie = []
meskie = []

def dodaj_imie(imie):
    if not imie.isalpha():
        print("Pominięto niepoprawne imię:", repr(imie))
        return
    imie = imie.capitalize()
    if imie in zenskie or imie in meskie:
        print("To imię jest już na liście:", imie)
        return
    if imie.endswith("a") and imie not in wyjatki:
        zenskie.append(imie)
    else:
        meskie.append(imie)

try:
    with (folder / "imiona.txt").open("r", encoding="utf-8") as uchwyt:
        for wiersz in uchwyt:
            dodaj_imie(wiersz.strip())
except FileNotFoundError:
    print("Brak imiona.txt - zaczynam od pustych list.")
while True:
    imie = input("Podaj imię lub wpisz koniec: ").strip()
    if imie.casefold() == "koniec":
        break
    dodaj_imie(imie)
zenskie.sort()
meskie.sort()
print("Imiona żeńskie:", zenskie)
print("Imiona męskie:", meskie)
with (folder / "imiona.pkl").open("wb") as uchwyt:
    pickle.dump({"zenskie": zenskie, "meskie": meskie}, uchwyt)
