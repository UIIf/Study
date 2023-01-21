# v5(v15)
import numpy as np

import matplotlib.pyplot as plt


def target(x):
    return np.sqrt(x + 1) * np.log(x + 1)


def P(x):
    return 2 * np.sqrt(x + 1)


def Q(x):
    return -1 / np.sqrt(x + 1)


def F(x):
    return -np.log(x + 1) / np.sqrt(x + 1) + 2


def Sweep(a, b, g0, gN, h):

    signs = [-1, 1, -1, 1]

    M = [[0, 1, 0, g0]]

    M += [
        [
            (1 / h**2) - (P(x) / (2 * h)),
            (-2 / h**2) + Q(x),
            (1 / h**2) + (P(x) / (2 * h)),
            F(x),
        ]
        for x in np.arange(a + h, b, h)
    ]

    M += [[0, 1, 0, gN]]

    M = np.array(M)

    diff = M[1:, 1].copy()

    for i in range(len(M[0])):
        M[1:, i] /= diff

    M *= signs

    for i in range(2, len(M)):

        M[i - 1, -1] += M[i - 1, 0] * M[i - 2, -1]
        M[i, 1] -= M[i, 0] * M[i - 1, 2]

        diff = M[i, 1]

        for j in range(len(M[i])):
            M[i, j] /= diff

    for i in range(len(M) - 1, 0, -1):

        M[i - 1, 3] += M[i, 3] * M[i - 1, 2]

    return M[:, 3]


g0 = 0
gN = 0.98025

a, b, h = 0, 1, 0.05

x = np.linspace(a, b, int(np.ceil((b - a) / h)) + 1)

y = Sweep(a, b, g0, gN, h)

yt = target(x)

plt.plot(x, y, label="pred")
plt.plot(x, yt, label="target")

plt.legend()
plt.show()
