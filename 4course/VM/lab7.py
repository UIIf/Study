import numpy as np
import matplotlib.pyplot as plt

from sympy import (
    symbols,
    series,
    integrate,
    Matrix,
    linsolve,
    lambdify,
    exp,
)
from sympy.polys.polytools import Poly


def get_functions(func, n, fx):
    ser = Poly(series(func, x, n=n).removeO(), x, s)

    a_i = []

    b_i = []

    for i in range(1, len(ser.as_list())):
        coeff = ser.as_expr().coeff(x**i)
        if coeff != 0:
            b_i += [coeff]
            a_i += [ser.as_expr().coeff(coeff)]

    c_i = symbols(f"c1:{len(a_i) + 1}")

    u = sum([c_i[i] * a_i[i] for i in range(len(a_i))]) + fx

    return a_i, b_i, c_i, u


def create_f_i(bet, fs, a, b):
    f_i = []
    for i in range(len(bet)):
        f_i += [integrate(bet[i] * fs.subs(x, s), (s, a, b))]

    return f_i


def create_Aii(alp, bet, a, b):
    return [
        [integrate(alp[j].subs(x, s) * bet[i], (s, a, b)) for j in range(len(alp))]
        for i in range(len(bet))
    ]


def create_Sys(alp, bet, fs, ci, a, b):
    Aii = create_Aii(alp, bet, a, b)
    f_i = create_f_i(bet, fs, a, b)
    C_i = []

    for i in range(len(f_i)):
        sum_CA_ij = [(ci[j] * Aii[i][j]).subs(ci[j], 1) for j in range(len(Aii[i]))]
        sum_CA_ij[i] = ((ci[i] * Aii[i][i] - ci[i])).subs(ci[i], 1)

        sum_CA_ij += [f_i[i]]
        C_i += [sum_CA_ij]

    return C_i


def solve(u, alp, bet, fs, ci, a, b):

    M = Matrix(create_Sys(alp, bet, fs, ci, a, b))

    u = u.subs(ci, linsolve(M, ci).args[0])
    return u


x, s, y = symbols("x s y")
n = 4

kernel = (1 + s) * (exp(0.2 * x * s) - 1)
fx = exp(-x)

a_i, b_i, c_i, ux = get_functions(kernel, n, fx)

ux = solve(u=ux, alp=a_i, bet=b_i, fs=fx, ci=c_i, a=0, b=1)
left_side = lambdify(x, ux - integrate(kernel * ux.subs(x, s), (s, 0, 1)), "numpy")

x_lin = np.linspace(0, 1, 101)
print("MAE", np.abs((left_side(x_lin) - np.exp(-x_lin))).mean())

# plt.plot(x_lin, np.exp(-x_lin) - left_side(x_lin), "red")
plt.plot(x_lin, left_side(x_lin), "red")
plt.plot(x_lin, np.exp(-x_lin), "blue")
plt.show()
