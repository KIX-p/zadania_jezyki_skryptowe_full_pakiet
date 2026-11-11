import pickle
from pathlib import Path

plik = Path(__file__).with_name("imiona.pkl")
wyjatki = {"Kosma", "Barnaba", "Bonawentura", "Jarema", "Kuba"}
try:
    with plik.open("rb") as uchwyt:
        dane = pickle.load(uchwyt)
    zenskie = dane["zenskie"]
    meskie = dane["meskie"]
    if not isinstance(zenskie, list) or not isinstance(meskie, list):
        raise ValueError("W pliku oczekiwano dwóch list.")
except FileNotFoundError:
    zenskie, meskie = [], []
    print("Brak imiona.pkl - zaczynam od pustych list.")
except (pickle.UnpicklingError, EOFError, KeyError, TypeError, ValueError):
    raise SystemExit("Błędny format imiona.pkl. Plik nie został nadpisany.")
while True:
    imie = input("Podaj imię lub wpisz koniec: ").strip()
    if imie.casefold() == "koniec":
        break
    if not imie.isalpha():
        print("Imię musi zawierać wyłącznie litery.")
        continue
    imie = imie.capitalize()
    if imie in zenskie or imie in meskie:
        print("To imię jest już na liście.")
        continue
    if imie.endswith("a") and imie not in wyjatki:
        zenskie.append(imie)
    else:
        meskie.append(imie)
zenskie.sort()
meskie.sort()
print("Imiona żeńskie:", zenskie)
print("Imiona męskie:", meskie)
with plik.open("wb") as uchwyt:
    pickle.dump({"zenskie": zenskie, "meskie": meskie}, uchwyt)
