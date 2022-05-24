from matrix import ones, dot, transpose, mul, euq_len, vector_norm_1, sgn, plus
import numpy.linalg

matrix = [
	[2 , 1  , 1],
	[1 , 2.5, 1],
	[1 , 1  , 3],
]

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
	

print(find_max_self(matrix, 1e-4))
print(max(numpy.linalg.eig(matrix)[0]))