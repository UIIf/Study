import numpy as np


def target_u(x,t):
	return np.exp(-np.pi*t)*np.sin(np.sin(np.pi*x/4))

a = 4/np.pi
L = 4
T = 0.1

N = 10
M = 10

U = np.zeros([N,M])

def fill_bor