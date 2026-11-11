folder = fileparts(mfilename('fullpath'));
plik = fullfile(folder, 'wig20.csv');
fid = fopen(plik, 'rt');
if fid == -1
    error('Brak wig20.csv. Uruchom pobierz_dane.py albo pobierz CSV ze Stooq.');
endif
naglowek = fgetl(fid);
nazwy = strsplit(strtrim(naglowek), ',');
kol_data = find(strcmpi(nazwy, 'Date') | strcmpi(nazwy, 'Data'));
kol_close = find(strcmpi(nazwy, 'Close') | strcmpi(nazwy, 'Zamkniecie'));
if numel(kol_data) != 1 || numel(kol_close) != 1
    fclose(fid);
    error('Niepoprawny naglowek CSV: wymagane Date/Data i Close/Zamkniecie.');
endif
format = repmat('%s', 1, numel(nazwy));
dane = textscan(fid, format, 'Delimiter', ',', 'EmptyValue', NaN);
fclose(fid);
if isempty(dane{kol_data})
    error('Plik CSV nie zawiera notowan.');
endif
daty = datenum(char(dane{kol_data}), 'yyyy-mm-dd');
zamkniecie = str2double(dane{kol_close});
if numel(daty) != numel(zamkniecie) || any(!isfinite(zamkniecie))
    error('Niepoprawne dane. Zadna sesja nie zostala automatycznie pominieta.');
endif
if any(daty < datenum(2025, 1, 1) | daty > datenum(2025, 12, 31))
    error('Oczekiwano danych od 2025-01-01 do 2025-12-31.');
endif
[daty, kolejnosc] = sort(daty);
zamkniecie = zamkniecie(kolejnosc);
if any(diff(daty) == 0)
    error('CSV zawiera powtorzone daty. Sprawdz plik zrodlowy.');
endif
stopien = 3;
if numel(daty) <= stopien
    error('Za malo notowan do aproksymacji stopnia 3.');
endif
t = daty - daty(1);
[p, S, mu] = polyfit(t, zamkniecie, stopien);
aproksymacja = polyval(p, t, [], mu);
blad_rmse = sqrt(mean((zamkniecie - aproksymacja).^2));
figure(1);
plot(daty, zamkniecie, 'b-', 'LineWidth', 1);
datetick('x', 'yyyy-mm', 'keeplimits');
xlabel('Data sesji'); ylabel('WIG20 [pkt]');
title('WIG20 - ceny zamkniecia w 2025 roku'); grid on;
print(fullfile(folder, 'wig20_2025.png'), '-dpng', '-r150');
figure(2);
plot(daty, zamkniecie, 'b-', daty, aproksymacja, 'r-', 'LineWidth', 1.2);
datetick('x', 'yyyy-mm', 'keeplimits');
xlabel('Data sesji'); ylabel('WIG20 [pkt]');
legend('Zamkniecie', 'Wielomian stopnia 3', 'Location', 'northwest');
title('WIG20 2025 - aproksymacja wielomianowa'); grid on;
print(fullfile(folder, 'wig20_2025_aproksymacja.png'), '-dpng', '-r150');
fprintf('Liczba sesji: %d\nRMSE: %.4f pkt\n', numel(daty), blad_rmse);
disp('Wspolczynniki przy kolejnych potegach z = (t - mu(1)) / mu(2):');
disp(p); disp('mu ='); disp(mu);
