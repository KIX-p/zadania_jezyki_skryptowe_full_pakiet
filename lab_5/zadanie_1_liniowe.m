A = [2, 1, -1; 3, -2, 1; 1, -1, -1];
b = [-3; 9; 0];
wynik = A \ b;
fprintf('x = %.10f\ny = %.10f\nz = %.10f\n', wynik);
reszta = A * wynik - b;
fprintf('Maksymalny blad: %.3e\n', norm(reszta, Inf));
assert(norm(reszta, Inf) < 1e-10);
