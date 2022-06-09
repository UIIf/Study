from matrix import *
import numpy.linalg

A = [	
		[2.2, 1., 0.5, 2.],
      	[1., 1.3, 2., 1.],
      	[0.5, 2, 0.5, 1.6],
      	[2., 1., 1.6, 2.]
    ]

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

	return [u,l]

#LU_END__________________________________
def find_max_nd_ind(matrix):
	mi, mj = 0,1
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i != j and abs(matrix[i][j]) > abs(matrix[mi][mj])):
				mi, mj = i, j
	return [mi, mj]

#NP----------------------------------------
print("np", numpy.linalg.eig(A)[0])

#QR----------------------------------------
qrA = [r[:] for r in A]
ind = find_max_nd_ind(qrA)
while(qrA[ind[0]][ind[1]] > 0.01):
	Q,R = qr_razloj(qrA)
	qrA = dot(R,Q)
	ind = find_max_nd_ind(qrA)

qr_self = [qrA[i][i] for i in range(len(qrA))]
qr_self.sort()
qr_self.reverse()
print("QR", qr_self)

#LU----------------------------------------
luA = [r[:] for r in A]
ind = find_max_nd_ind(luA)
for i in range(50):
	U,L = qr_razloj(luA)
	luA = dot(U,L)
	ind = find_max_nd_ind(luA)

# lu_self = [luA[i][i] for i in range(len(luA))]
# lu_self.sort()
# lu_self.reverse()
# print("LU", lu_self)

print("LU")
for i in luA:
	print(i)