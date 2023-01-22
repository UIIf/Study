# V5

import numpy as np
import matplotlib.pyplot as plt
import sympy as syp

x = syp.Symbol("x")

n = 3
h = 0.1
a = 0
b = 1


def basis(i):
    return 1 - x ** (2 * i)


def P(x):
    return -1


def Q(x):
    return -2


def F(x):
    return -3 * syp.exp(-x)


def equation(u, du, ddu):
    return ddu + P(x) * du + Q(x) * u - F(x)


def for_ritz(u, du):
    return P(x) * du**2 - Q(x) * u**2 + 2 * F(x) * u


def target(x):
    return (x + 1) * np.exp(-x)


def create_coef_basis():

    return [
        [syp.Symbol("C" + str(i)) for i in range(n)],  # C
        [basis(i) for i in range(n)],  # Basis
    ]


def calc_u(C, basis_arr):

    u_x = [0] * n
    u_x[0] = sum([syp.Add(syp.Mul(C[i], basis_arr[i])) for i in range(n)])

    for i in range(1, n):
        u_x[i] = syp.diff(u_x[i - 1], x)
    return u_x


def solution(method):
    def wrapper():
        C, basis_arr = create_coef_basis()
        u_x = calc_u(C, basis_arr)

        C_answer = method(C, u_x)

        solution_met = syp.lambdify(C, u_x[0])(*tuple(*C_answer))

        return syp.lambdify(x, solution_met, "numpy")

    return wrapper


@solution
def colocation_method(C, u_x):

    eq_c = syp.simplify(equation(u_x[0], u_x[1], u_x[2]))

    return syp.linsolve(
        [
            syp.lambdify(x, eq_c)(np.random.uniform(a + 0.1, b - 0.1))
            for i in range(n - 1)
        ],
        C,
    )


@solution
def ritz_method(C, u_x):

    return syp.linsolve(
        [
            syp.integrate(
                syp.diff(
                    for_ritz(
                        u_x[0],
                        u_x[1],
                    ),
                    C[i],
                ),
                (x, a, b),
            )
            for i in range(1, n)
        ],
        C,
    )


colocation = colocation_method()
ritz = ritz_method()
x_axis = np.linspace(a, b + h, int((b + h - a) / h))

plt.plot(x_axis, target(x_axis), label="target")
plt.plot(x_axis, colocation(x_axis), label="colocation")
plt.plot(x_axis, ritz(x_axis), label="Ritz")

plt.legend()
plt.show()
