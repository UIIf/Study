import numpy as np

def create_jard(matrix,x,x_0):

	W = np.copy(matrix)

	dif = (x - x_0).reshape((1, x.shape[0]))
	W = np.append(W, dif,axis = 0)

	dif = np.append(dif, 0)
	dif = dif.reshape((dif.shape[0],1))
	W = np.append(W, dif, axis = 1)
	
	return W

def function(matrix, b, x):
	return (1/2 * x.T @ matrix @ x + b @ x)[0]

matrix = [
	[ 20, -18, -4,  6],
	[-18,   8,  4,  2],
	[ -4,   4, 20, -6],
	[  6,   2, -6, 12]
]

f = [[9, 3, 8, 10]]



x_prev = np.zeros((len(f[0])))
x_0 = np.array([2, 7, -3, 8])
x = np.copy(x_0) 

A = np.array(matrix)

B = np.array(f)

print(A)
print()
print(B)

new_x = x - create_jard(A,x,x_0)