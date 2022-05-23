from matrix import *
import numpy.linalg
matrix = [
	[2 , 1  , 1],
	[1 , 2.5, 1],
	[1 , 1  , 3],
]
# matrix = [
# 	[2 , 1],
# 	[1 , 2]
# ]

def sgn(num):
	return 1 if num > 0 else -1

def find_max_nd_ind(matrix):
	mi, mj = 0,1
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i != j and abs(matrix[i][j]) > abs(matrix[mi][mj])):
				mi, mj = i, j
	return [mi, mj]

def find_max_diag_ind(matrix):
	mi = 0
	for i in range(1, len(matrix)):
		if(matrix[i][i] > matrix[mi][mi]):
			mi = i
	return mi

def self_mean_method_sim(matrix, p):
	tau = [10**(-(i+1)) for i in range(p)]

	matrix = [r[:] for r in matrix]
	counter = 0
	print(tau)
	for p in tau:
		i, j = find_max_nd_ind(matrix)

		diag_i = find_max_diag_ind(matrix)
		while(abs(matrix[i][j]) >= p): #abs(matrix[diag_i][diag_i])**0.5 * 
			d = ((matrix[i][i] - matrix[j][j])**2 + 4*(matrix[i][j])**2)**0.5
			c = (0.5*( 1 + abs(matrix[i][i] - matrix[j][j])/d))**0.5
			s = sgn(matrix[i][j]*(matrix[i][i] - matrix[j][j])) * (0.5*(1 - abs(matrix[i][i] - matrix[j][j])/d))**0.5

			new_m = [ r[:] for r in matrix]

			new_m[i][j], new_m[j][i] = 0, 0

			for k in range(len(matrix)):
				if(k == i or k == j):
					continue
				new_m[i][k] = c * matrix[k][i] + s* matrix[k][j]
				new_m[k][i] = new_m[i][k]

				new_m[j][k] = -s * matrix[k][i] + c* matrix[k][j]
				new_m[k][j] = new_m[j][k]
			
			new_m[i][i] = c *  c * matrix[i][i] + 2 * c*s * matrix[i][j] + s*s *matrix[j][j]

			new_m[j][j] = s * s * matrix[i][i] - 2 * c * s * matrix[i][j] + c * c * matrix[j][j]

			matrix = new_m

			i, j = find_max_nd_ind(matrix)
			diag_i = find_max_diag_ind(matrix)
			counter += 1
	# print(counter)
	return [matrix[i][i] for i in range(len(matrix))]

m = self_mean_method_sim(matrix, 8)
print("Answer")
e = ones(len(matrix))
for i in range(len(matrix)):
	e[i][i] *= m[i]

new_matrix = plus(matrix, mul(e,-1))
print(m)
print(numpy.linalg.eig(matrix)[0])