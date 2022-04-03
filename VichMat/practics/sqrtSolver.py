from matrix import *
import math

matrix = [
	[2.2,4,-3,1.5,0.6,2,0.7],
	[4,3.2,1.5,-0.7,-0.8,3,1],
	[-3,1.5,1.8,0.9,3,2,2],
	[1.5,-0.7,0.9,2.2,4,3,1],
	[0.6,-0.8,3,4,3.2,0.6,0.7],
	[2,3,2,3,0.6,2.2,4],
	[0.7,1,2,1,0.7,4,3.2]
]
b = [3.2, 4.3, 0.1, 3.5, 5.3, 9, 3.7]

def generate_s(matrix):
	s = [[0]*len(r) for r in matrix]
	y = s[0][:]

	for i in range(len(s)):
		s[i][i] = (matrix[i][i] - sum([s[k][i]**2 for k in range(i)]))**0.5
		for j in range(i, len(s)):
			s[i][j] = (matrix[i][j] - sum([s[k][i]*s[k][j] for k in range(i)]))/s[i][i]
	return s

def find_y(s,b):
	y = [0]*len(s)
	for i in range(len(s)):
		y[i] = (b[i] - sum([s[k][i]*y[k] for k in range(i)]))/s[i][i]
	return y



s = generate_s(matrix)
y = find_y(s,b)
x = solve_triangle(s, y)
check_x(matrix,b,x)
