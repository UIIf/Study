# Finite difference method
# phi = (x - x_{i-1})/h if x in range(x_{i-1}, x_i)
# phi = -(x - x_{i+1})/h if x in range(x, x_{+1})
# phi = 0 if not x in range(x_{i-1}, x_{i+1})

# Galerkin


# if u(a) = u(b) = 0:
#     phi(0) = 0, phi(i) = (1 - x^(2*i))

# V5
# u'' - u' - 2u = -3e^(-x)
# u'(0) = 1 => u(0) = 0
# u(1) + 2u'(1) = 0
# u_p(x) = (x + 1)e^(-x)

# u(x) = (x + 1)e^(-x)

from sympy import Symbol, Piecewise, lambdify, init_printing
import scipy as sc
from scipy.integrate import quad
import numpy as np

import matplotlib.pyplot as plt

# u(x) = Sum(C_i*phi_i(x))

# a = 0
# b = 1

# N = 10
# h = (b - a) / N
# x_i = np.arange(a, b + h, h)


# def P(x):
#     return -1


# def Q(x):
#     return -2


# def F(x):
#     return -3 * np.exp(-x)


a = -1
b = 1

N = 4
h = 0.5
x_i = [-1, -0.5, 0, 0.5, 1]


def P(x):
    return 0


def Q(x):
    return 1 + x**2


def F(x):
    return -1


def create_phi(x_i, h):
    x = Symbol("x")

    phi = []
    phi_d = []
    for i in range(1, len(x_i) - 1):
        # print(x_i[i - 1], x_i[i], x_i[i + 1])
        cur_phi = Piecewise(
            (0, x < x_i[i - 1]),
            ((x - x_i[i - 1]) / h, x <= x_i[i]),
            (-(x - x_i[i + 1]) / h, x <= x_i[i + 1]),
            (0, x > x_i[i + 1]),
        )
        phi += [lambdify(x, cur_phi)]
        phi_d += [lambdify(x, cur_phi.diff(x))]
    return phi, phi_d


def component_a(x, i, j):
    return (
        -phi_d[j](x) * phi_d[i](x)
        + P(x) * phi_d[j](x) * phi[i](x)
        + Q(x) * phi[j](x) * phi[i](x)
    )


def component_d(x, i):
    return phi[i](x) * F(x)


phi, phi_d = create_phi(x_i, h)

A = np.zeros((N - 1, N - 1))

for i in range(N - 1):
    for j in range(N - 1):
        for ind in range(N):
            A[i, j] += quad(component_a, x_i[ind], x_i[ind + 1], args=(i, j))[0]

d = np.zeros((N - 1, 1))
for i in range(N - 1):
    for ind in range(N):
        d[i] += quad(component_d, x_i[ind], x_i[ind + 1], args=(i))[0]

C = np.linalg.solve(A, d)


show_N = 100
show_h = (b - a) / show_N

show_x = np.arange(a, b, show_h)


def calc_final(x, phi, C):
    ret = 0

    for i in range(len(phi)):
        ret += phi[i](x) * C[i][0]

    return ret


def calc_semi(x, phi, C):
    ret = []
    for i in range(len(phi)):
        ret += [phi[i](x) * C[i][0]]
    return ret


# real = (show_x + 1) * np.exp(-show_x)
# plt.plot(show_x, real)
plt.plot(show_x, calc_final(show_x, phi, C))
semi = calc_semi(show_x, phi, C)

for s in semi:
    plt.plot(show_x, s)
plt.show()
