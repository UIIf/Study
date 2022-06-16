import numpy as np
import matplotlib.pyplot as plt

n = 6
maxI = 10000000
eps = 1e-6


def f(x):
    return (0.5*np.reshape(x, (1, n))).dot(A).dot(np.reshape(x, (n, 1))) + b.dot(x)

def grad(x):
    return np.reshape(A.dot(x), (1, n)) + b

def H(x):
    return A

def Hinv(x):
    return np.linalg.inv(A)

A = np.random.randn(n, n)*10

b = np.random.rand(n)

x = np.zeros((n,1))
x0 = x

i = 0

while np.linalg.norm(grad(x)) > eps:
    x = x - Hinv(x).dot(np.reshape(grad(x), (n, 1)))
    i += 1
    if (i >= maxI):
        print("Ошибка")
        break

print("Безусловный минимум методом Ньютона")
print(x)

r = np.random.rand(1, 1)
c = np.reshape((x - x0), (1, n)).dot(x - x0)

while c - r*r <= 0:
    r = np.random.rand(1, 1)

print("Число r")
print(r)
print("Проверим, что для безусловного минимума не выполнено условие (x - x0)*(x - x0) -r*r <= 0")
print("(x - x0)*(x - x0) -r*r = ", str(c - r*r))

M = A
col = [0. for i in range(0,n)]
col[0] = float(c)
col = np.array(col, dtype=np.float64)
M = np.column_stack((M, np.reshape(col, (n, 1))))
c1 = np.append(x-x0, 0)
M = np.vstack((M, c1))
B = np.append(-b, r*r)
Y = np.linalg.inv(M.astype('float')).dot(B)
x = Y[0:n]
print("Условный минимум")
print(x)
print("Проверка")
x = np.reshape(x, (n, 1))
print(np.reshape((x - x0), (1, n)).dot(x - x0) - r*r)
