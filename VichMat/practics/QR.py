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

# matrix = [
# 	[1, 2, 3],
# 	[4, 5, 6],
# 	[7, 8, 0]
# ]

# b = [5, 8, 2]

# matrix = [
# 	[0.411,  0.421, -0.333,  0.313, -0.141, -0.381 , 0.245],
# 	[0.241,  0.705,  0.139, -0.409,  0.321,  0.0625, 0.101],
# 	[0.123, -0.239,  0.502,  0.901,  0.243,  0.819 , 0.321],
# 	[0.413,  0.309,  0.801,  0.865,  0.423,  0.118 , 0.183],
# 	[0.241, -0.221, -0.243,  0.134,  1.274,  0.712 , 0.423],
# 	[0.281,  0.525,  0.719,  0.118, -0.974,  0.808 , 0.923],
# 	[0.246, -0.301,  0.231,  0.813, -0.702,  1.223 , 1.105]
# ]

b = [0.096, 1.252, 1.024, 1.023, 1.155, 1.937, 1.673]

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

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

#как sign только в 0 возвращает 1
def deta(a):
	return -1 if a < 0 else 1

#Создание 
def generate_P(p):
	I = ones(len(p))
	# print(I)
	newp = [p]
	a = -2/dot(p)
	m = dot(transpose(newp), newp)
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
		#Вектор нормали
		p = [0]*len(r)
		#Находим а^(k+1)
		akk = sqrt(sum([r[l][k]**2 for l in range(k, n)]))

		p[k] = r[k][k] + deta(akk)*akk

		for i in range(k+1,n):
			p[i] = r[i][k]

		q = dot(q,generate_P(p))
		pp = sum([p[i]**2 for i in range(k, n)])
		for j in range(k,n):
			px = sum([p[l]*r[l][j] for l in range(0, n)])
			for i in range(k,n):
				r[i][j] -=2*p[i]/pp*px 

	return [q,r]

def solve(Q,R,B):
	q = transpose(Q)
	b = dot(q,B)
	b = [t[0] for t in b]
	return solve_triangle(R,b)

q,r = qr_razloj(matrix)
x = solve(q,r,b)
print("x",x)
check_x(matrix,b,x)