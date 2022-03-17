from matrix import *
from math import sqrt

# matrix = [
# 	[1,2,1,4],
# 	[2,0,4,3],
# 	[4,2,2,1],
# 	[-3,1,3,2]
# ]
# b = [13,28,20,6]

# matrix = [
# 	[2.1,-4.5,-2.0,19.07],
# 	[3.,2.5,4.3,3.21],
# 	[-6,3.5,2.5,-18.25]
# ]

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 0]
]

b = [5, 8, 2]

# matrix = [
# 	[0.411,  0.421, -0.333,  0.313, -0.141, -0.381 , 0.245],
# 	[0.241,  0.705,  0.139, -0.409,  0.321,  0.0625, 0.101],
# 	[0.123, -0.239,  0.502,  0.901,  0.243,  0.819 , 0.321],
# 	[0.413,  0.309,  0.801,  0.865,  0.423,  0.118 , 0.183],
# 	[0.241, -0.221, -0.243,  0.134,  1.274,  0.712 , 0.423],
# 	[0.281,  0.525,  0.719,  0.118, -0.974,  0.808 , 0.923],
# 	[0.246, -0.301,  0.231,  0.813, -0.702,  1.223 , 1.105]
# ]

# b = [0.096, 1.252, 1.024, 1.023, 1.155, 1.937, 1.673]

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

def deta(a):
	return -1 if a < 0 else 1

def generate_P(p):
	I = ones(len(p))
	# print(I)
	a = -2/dot(p)
	m = dot(transpose(transpose(p)), transpose(p))
	P = mul(m,a)
	P = plus(I,P)
	return P

def qr_razloj(matrix):
	if(len(matrix) != len(matrix[0])):
		return None
	r = [m[:] for m in matrix]
	n = len(r)
	q = ones(len(matrix))


	for k in range(0,len(r) - 1):
		p = [0]*len(r)
		akk = sqrt(sum([r[l][k]**2 for l in range(k, n)]))
		p[k] = r[k][k] + deta(akk)*akk
		for i in range(k+1,n):
			p[i] = r[i][k]
		q = dot(q,generate_P(p))
		pp = sum([p[i]*p[i] for i in range(k, n)])
		for j in range(k,n):
			px = sum([p[l]*r[l][j] for l in range(0, n)])
			for i in range(k,n):
				r[i][j] -=2*p[i]/pp*px 

	for i in dot(q,r):
		print(i)
	return [q,r]

def solve(Q,R,B):
	q = transpose(Q)
	b = dot(Q,transpose(transpose(B)))
	return solve_triangle(R,b)


for i in matrix:
	print(i)
print()

q,r = qr_razloj(matrix)
solve(q,r,b)
# x = solve(q,r,b)
# print(x)