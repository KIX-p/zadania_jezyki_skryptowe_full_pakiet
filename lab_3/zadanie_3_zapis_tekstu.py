from pathlib import Path

plik = Path(__file__).with_name("imiona.txt")
imiona = []
while True:
    imie = input("Podaj imię lub wpisz koniec: ").strip()
    if imie.casefold() == "koniec":
        break
    if not imie.isalpha():
        print("Imię musi zawierać wyłącznie litery.")
        continue
    imie = imie.capitalize()
    if imie in imiona:
        print("To imię jest już na liście.")
    else:
        imiona.append(imie)
imiona.sort()
print("Posortowane imiona:", imiona)
with plik.open("w", encoding="utf-8") as uchwyt:
    for imie in imiona:
        uchwyt.write(imie + "\n")
print("Zapisano do:", plik)
