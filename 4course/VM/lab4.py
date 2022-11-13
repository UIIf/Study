import numpy as np
import matplotlib.pyplot as plt

import time

np.set_printoptions(linewidth=1000)
np.set_printoptions(precision=3, floatmode='fixed')

def g(x, t):
	return 0

def phi(x):
	return 0

def psi(x):
	return 0

def gamma_0(t):
	return t*(t-1)

def gamma_1(t):
	return 3*t*t

M = 100
N = 100

L = 1
T = 1

a = 1

h = L/M
tau = T/N

# M - col
# N - row
U = np.zeros([N,M])



def FillXLim():
	U[0,:] = phi(np.linspace(0, L, M))

def FillTLim():
	U[:, 0] = gamma_0(np.linspace(0, T, N))
	U[:, -1] = gamma_1(np.linspace(0, T, N))


def CalcM1():
	U[1, 1:-2] = tau*psi(np.linspace(0, L, M)[1:-2]) +U[0, 1:-2] 


def CalcMN():

	s_tau = tau*tau
	s_a = a*a
	s_h = h*h

	all_m_x = np.linspace(0, L, M)[1:-2]
	all_m = np.arange(1, M-2)

	for n in range(2, N):
		U[n, all_m] = s_tau*(s_a/s_h*(U[n - 1, all_m - 1] - 2 * U[n-1, all_m ]  +  U[n - 1,all_m + 1]) + g(all_m_x, n*tau)) - U[n - 2, all_m] + 2*U[n - 1, all_m]

FillXLim()
FillTLim()
CalcM1()
CalcMN()


for n in range(N):
	plt.plot(np.linspace(0, L, M), U[n,:])
plt.show()
