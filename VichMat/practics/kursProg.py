from matrix import *
import numpy as np
import numpy.linalg
import random

# A = [	
# 		[ 4, 1, -2,  2],
#       	[ 1, 2,  0,  1],
#       	[-2, 0,  3, -2],
#       	[ 2, 1, -2, -1]
#     ]
# A = [
# 		[ 5, 6,  3],
# 	 	[-1, 0,  1],
# 	 	[ 1, 2, -1]
# ]

# A = [
# 		[-40, 1,   2,  2],
#       	[  1, 2,   0, 1],
#       	[  2, 0,   3, 2],
#       	[  2, 1, 0.1, 1]
# ]

# A = [
# 		[ 1,  2,  3,  4,  5],
#       	[ 6, 13, 18, 24, 30],
#       	[ 7, 15, 22, 29, 36],
#       	[ 8, 18, 23, 34, 42],
#       	[ 9, 21, 20, 33, 48]
# ]

def generate_matrix(n):
	to_ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			to_ret[i][j] = random.randrange(20)

	for i in range(n):
		to_ret[i][i] = sum([abs(to_ret[i][j]) for j in range(n)]) 
	return to_ret
#QR_START________________________________

#как sign только в 0 возвращает 1
def deta(a):
	return -1 if a < 0 else 1

#Создание 
def generate_P(p):
	I = ones(len(p))
	# print(I)
	newp = [p]
	a = -2/dot(p)[0][0]
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
		akk = (sum([r[l][k]**2 for l in range(k, n)]))**0.5

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

#QR_END__________________________________



#LU_START________________________________

def generate_l_u(matrix):
	u = [[0]*len(r) for r in matrix]
	l = [[0]*len(r) for r in matrix]

	#Пустая матрица U
	u[0] = matrix[0][:]

	#Первая строка матрицы l делится на первый элемент
	for i in range(len(matrix)):
		l[i][0] = matrix[i][0]/matrix[0][0]

	#Для итерации
	for i in range(1, len(matrix)):
		#не помню
		for j in range(i, len(matrix)):
			#Произведение строки l на столбец u
			temp = [l[i][k] * u[k][j] for k in range(i)]
			#Заполняем u
			u[i][j] = matrix[i][j] - sum(temp)
			#Произведение строки l на столбец u
			temp = [l[j][k] * u[k][i] for k in range(i)]
			#Заполняем l

			l[j][i] = (matrix[j][i] - sum(temp))/u[i][i]

	return [l, u]

#LU_END__________________________________

#HOUSEHOLDER_START_______________________

def hessel_rot(matrix):
	matrix = [ r[:] for r in matrix] 

	for j in range(len(matrix)):
		for i in range(j+2, len(matrix)):
			if(j > len(matrix) - i + 1):
				break
			
			c = matrix[j + 1][j]/(matrix[j + 1][j]**2 + matrix[i][j]**2)**0.5
			s = matrix[i][j]    /(matrix[j + 1][j]**2 + matrix[i][j]**2)**0.5

			T = ones(len(matrix))

			T[i][i] = c
			T[j + 1][j + 1] = c
			T[i][j+1] = s
			T[j+1][i] = -s

			matrix = dot(dot(transpose(T),matrix),T)
	return matrix
#HOUSEHOLDER_END_________________________


#QR----------------------------------------
def find_self(A,func_of_razl, eps = 1e-6):
	A = [r[:] for r in hessel_rot(A)]
	counter = 0
	old_self = [np.inf]*len(A)
	self_z = [A[i][i] for i in range(len(A))]

	while(vector_norm_1(plus(old_self, mul(self_z, -1))) > eps):
		counter+=1
		old_self = self_z[:]
		B,C = func_of_razl(A)
		A = dot(C,B)
		self_z = [A[i][i] for i in range(len(A))]

	self_z.sort()
	self_z.reverse()
	print("Iters", counter)
	
	return self_z

#LU----------------------------------------

def find_self_lu(A,eps = 1e-6):
	luA = [r[:] for r in hessel_rot(A)]
	counter = 0
	old_self_lu = [np.inf]*len(luA)
	lu_self = [luA[i][i] for i in range(len(luA))]

	# for i in range(50):

	while(vector_norm_1(plus(old_self_lu, mul(lu_self, -1))) > eps):
		counter+=1
		old_self_lu = lu_self[:]
		L,U = generate_l_u(luA)
		luA = dot(U,L)
		lu_self = [luA[i][i] for i in range(len(luA))]

	lu_self.sort()
	lu_self.reverse()
	print("Iters", counter)
	

	return lu_self

#MAIN--------------------------------------

A = generate_matrix(3)
print("A")
for i in A:
	print(i)

temp_arr = numpy.linalg.eig(A)[0].tolist()
temp_arr.sort()
temp_arr.reverse()
print("Собственное значение через numpy", temp_arr)

print("Число итераций")
qr_self = find_self_qr(A, eps = 1e-10)
print("Собственное значение через QR",qr_self)
print("Разница", [ abs(temp_arr[i]- qr_self[i]) for i in range(len(qr_self))])

print("Число итераций")
lu_self = find_self_lu(A, eps = 1e-10)
print("Собственное значение через LU",lu_self)
print("Разница",[ abs(temp_arr[i]- lu_self[i]) for i in range(len(lu_self))])

