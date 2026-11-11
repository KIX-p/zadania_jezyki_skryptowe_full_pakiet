imiona = []
for numer in range(1, 11):
    imie = input(f"Imię {numer}/10: ").strip()
    if not imie.isalpha():
        print("Imię musi zawierać wyłącznie litery.")
        continue
    imie = imie.capitalize()
    if imie in imiona:
        print("To imię jest już na liście.")
    else:
        imiona.append(imie)
print("Zapisane imiona:", imiona)
