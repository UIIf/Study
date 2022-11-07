# дифференциальный метод прогонки
import numpy as np
from colorama import Fore


def solution(x):
    return 1 / (x + 1)


def P(x):
    return -x + 1


def q(x):
    return -1


def F(x):
    return 2 / (x + 1) ** 3


def progonka(y0, yn, a, b, h):
    print(Fore.YELLOW + "Начало прогонки" + Fore.BLUE)
    M = [[0, 1, 0, y0]]
    for x in np.arange(a + h, b, h):
        M.append([])
        M[-1].append((1 / h ** 2) - (P(x) / (2 * h)))
        M[-1].append((-2 / h ** 2) + q(x))
        M[-1].append((1 / h ** 2) + (P(x) / (2 * h)))
        M[-1].append(F(x))
    M.append([0, 1, 0, yn])
    M = np.array(M)
    print(M)
    for i in range(1, len(M)):
        diff = M[i, 1]
        for j in range(len(M[i])):
            M[i, j] /= diff
            if j == 0 or j == 2:
                M[i, j] *= -1
    print(M)
    for i in range(1, len(M) - 1):
        M[i, -1] -= M[i, 0] * M[i - 1, -1] * -1
        M[i + 1, 1] += M[i + 1, 0] * M[i, 2] * -1
        diff = M[i + 1, 1]
        for j in range(len(M[i + 1])):
            M[i + 1, j] /= diff
    print(M)
    for i in range(len(M) - 2, -1, -1):
        M[i, -1] += M[i + 1, -1] * M[i, 2]
    print(M)
    print(Fore.YELLOW + "Конец прогонки")
    return M[:, -1]


def review(a, b, h):
    yS = []
    xS = []
    for x in np.arange(a, b + h, h):
        yS.append(solution(x))
        xS.append(x)
    return yS, xS


def printResult(y, yS, xS):
    print(Fore.GREEN + "X  |  YS  |  Y" + Fore.YELLOW)
    for i in range(len(y)):
        print(str(round(xS[i], 3)) + " | " + str(round(yS[i], 3)) + " | " + str(round(y[i], 3)))


def main():
    # a0, b0, c0, an, bn, cn = 1, 0, 1, 1, 0, 0.5
    y0 = 1
    yn = 0.5
    a, b, h = 0, 1, 0.1
    y = progonka(y0, yn, a, b, h)
    # yS, xS = review(a, b, h)
    # printResult(y, yS, xS)


if __name__ == '__main__':
    main()