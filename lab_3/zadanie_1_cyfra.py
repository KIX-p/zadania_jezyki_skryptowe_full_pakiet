slownie = {
    "0": "zero", "1": "jeden", "2": "dwa",
    "3": "trzy", "4": "cztery", "5": "pięć",
    "6": "sześć", "7": "siedem", "8": "osiem",
    "9": "dziewięć",
}
cyfra = input("Podaj jedną cyfrę od 0 do 9: ").strip()
if cyfra in slownie:
    print(slownie[cyfra])
else:
    print("Błąd: wpisz dokładnie jedną cyfrę od 0 do 9.")
