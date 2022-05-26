from matrix import ones, dot, transpose, mul, euq_len, vector_norm_1, sgn, plus, inv_rec
import numpy.linalg

matrix = [[2.2, 1., 0.5, 2.],
                  [1., 1.3, 2., 1.],
                  [0.5, 2, 0.5, 1.6],
                  [2., 1., 1.6, 2.]]

def find_max_self(matrix, eps):
	counter = 1
	x = [[1] for i in range(len(matrix))] # Столбец
	y = transpose(dot(matrix, x)) #Строка
	lam = dot(y,x)[0][0] # Число
	new_x =  transpose(mul(y, 1/euq_len(y[0])))

	while(vector_norm_1(plus(mul(new_x, -sgn(lam)), x)) > eps):
		x = new_x
		y = transpose(dot(matrix, x))
		lam = dot(y,x)[0][0]
		new_x =  transpose(mul(y, 1/euq_len(y[0])))
		counter += 1
	print('Iters', counter, )
	return lam
	
def find_min_self(matrix, eps):
	invt = inv_rec(matrix)
	x = [1]*len(matrix)

	l_p = 0
	l = 1
	counter = 0
	while(abs(l - l_p) >= eps):
		l_p = l
		x = transpose(dot(invt, mul(x,l)))[0]
		l = 1/max([abs(i) for i in x])
		counter += 1
	print('Iters', counter, )
	return l


print(find_max_self(matrix, 1e-4))
print(max(numpy.linalg.eig(matrix)[0]))
print("REv")
print(find_min_self(matrix, 1e-8))
print(min(abs(i) for i in numpy.linalg.eig(matrix)[0]))