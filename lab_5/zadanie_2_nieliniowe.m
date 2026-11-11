F = @(v) [v(1)^2 + 2*v(1)*v(2)^2 - 40;
          2*v(1)^2 - 3*v(2)^2 + 19];
opcje = optimset('TolX', 1e-10, 'TolFun', 1e-10);
starty = [1, 1; 2, -2];
rozwiazania = zeros(2, 2);
for k = 1:columns(starty)
    [v, reszta, info] = fsolve(F, starty(:, k), opcje);
    if info <= 0 || norm(reszta, Inf) > 1e-8
        error('Nie uzyskano poprawnego rozwiazania dla startu %d.', k);
    endif
    rozwiazania(:, k) = v;
    fprintf('Rozwiazanie %d: x = %.10f, y = %.10f\n', k, v(1), v(2));
    fprintf('Maksymalny blad: %.3e\n', norm(reszta, Inf));
endfor
assert(norm(rozwiazania - [2, 2; 3, -3], Inf) < 1e-7);
