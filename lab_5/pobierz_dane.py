import csv
import io
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

adresy = [
    "https://stooq.pl/q/d/l/?s=wig20&d1=20250101&d2=20251231&i=d",
    "https://stooq.pl/q/d/l/?s=%5Ewig20&d1=20250101&d2=20251231&i=d",
    "https://stooq.com/q/d/l/?s=%5Ewig20&d1=20250101&d2=20251231&i=d",
]
plik = Path(__file__).with_name("wig20.csv")
for adres in adresy:
    try:
        zapytanie = Request(adres, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(zapytanie, timeout=30) as odpowiedz:
            tekst = odpowiedz.read().decode("utf-8-sig")
        wiersze = list(csv.DictReader(io.StringIO(tekst)))
        if not wiersze or not ({"Date", "Data"} & wiersze[0].keys()):
            print("Adres nie zwrócił CSV:", adres)
            continue
        pole_daty = "Date" if "Date" in wiersze[0] else "Data"
        pole_ceny = "Close" if "Close" in wiersze[0] else "Zamkniecie"
        daty = [wiersz[pole_daty] for wiersz in wiersze]
        if any(not "2025-01-01" <= data <= "2025-12-31" for data in daty):
            raise ValueError("Otrzymano daty spoza 2025 roku.")
        if len(set(daty)) != len(daty):
            raise ValueError("Otrzymano powtórzone daty.")
        for wiersz in wiersze:
            float(wiersz[pole_ceny])
        plik.write_text(tekst, encoding="utf-8")
        print(f"Zapisano {len(wiersze)} sesji do {plik}.")
        break
    except (HTTPError, URLError, TimeoutError, UnicodeError, ValueError, KeyError) as blad:
        print("Nie udało się pobrać danych:", blad)
else:
    raise SystemExit("Pobierz dzienny CSV WIG20 za 2025 ze Stooq i zapisz obok skryptu jako wig20.csv.")
