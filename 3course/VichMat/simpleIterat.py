from matrix import *
from math import log, log10, cos, pi
class Method:
	def __init__(self, func, change_matrix = True, w = 1):
		self.func = func
		self.ch = change_matrix
		self.w = w

# matrix = [
# 	[2.2,4,-3,1.5,0.6,2,0.7],
# 	[4,3.2,1.5,-0.7,-0.8,3,1],
# 	[-3,1.5,1.8,0.9,3,2,2],
# 	[1.5,-0.7,0.9,2.2,4,3,1],
# 	[0.6,-0.8,3,4,3.2,0.6,0.7],
# 	[2,3,2,3,0.6,2.2,4],
# 	[0.7,1,2,1,0.7,4,3.2]
# ]
# b = [3.2, 4.3, 0.1, 3.5, 5.3, 9, 3.7]

# matrix = [
# 	[16, 2, 1, -2],
# 	[4, 20, 1, 5],
# 	[2, 1, 10, 3],
# 	[-4, 7, 4, 32]
# ]
# b = [-13,24,7,2]
# matrix = [
# 	[10,2,1],
# 	[1,10,2],
# 	[1,1,10]
# ]
# b = [10,12,8]

# matrix = [
# 	[2 , 1  , 1],
# 	[1 , 2.5, 1],
# 	[1 , 1  , 3],
# ]

matrix = [[1.111, 1.222, 0.333],
  [1.222, 1.444, 0.555],
  [0.333, 0.555, 1.666]]

b = [1, 1, 1]

# matrix = [
# 	[2, 1],
# 	[1, 2]
# ]

# b = [4, 5]

matrix = [[10, 1., 0.5, 2.],
                  [1., 10, 2., 1.],
                  [0.5, 2, 10, 1.6],
                  [2., 1., 1.6, 10]]
b=  [1, 1, 1,1]

def simple_iter_calculate_x(alpha,beta,x,w):
	return plus(beta,mul(tranвspose(dot(alpha,x))[0],-1))

def zaiendal_calculate_x(alpha,beta,x,w):
	x = x[:]
	for i in range(len(x)):
		x[i] = beta[i]
		for j in range(len(x)):
			if(j != i):
				x[i] -= alpha[i][j]*x[j]
	return x

def relax_calculate_x(alpha,beta,x,w):
	x = x[:]
	for i in range(len(x)):
		x[i] = (1- w)*x[i] + w*beta[i]
		for j in range(len(x)):
			if(j != i):
				x[i] -= w*alpha[i][j]*x[j]
	return x

def grad_spusk(alpha, beta, x, w):
	r = plus(b, mul(transpose(dot(matrix,x))[0], -1))
	# print(F)
	delta = dot(r,r)[0][0]
	delta /= dot(r, transpose(dot(matrix,r))[0])[0][0]
	# print(delta)
	new_x = plus(x, mul(r, delta))
	return new_x

def Richardson(alpha, beta, x, n):
	
	lambdas = self_mean_method_sim(alpha, 11)
	# print(int(log10(eps)))
	new_x = x[:]
	lmax = max(lambdas)
	lmin = min(lambdas)

	tau_z = 2/(lmin + lmax)
	eta = lmin/lmax
	ro = (1 - eta)/(1 + eta)

	ro_one = (1 - eta**0.5)/(1 + eta**0.5)
	for k in range(1, n+1):

		nu = cos((2*k-1)*pi/2/n)
		tau = tau_z/(1 + ro * nu)
		new_x = plus(mul(plus(beta, transpose(mul(dot(alpha, new_x), -1))[0]),tau),new_x)

	return new_x
		

def solve(matrix, b, epsilon, meth):
	x_prev = [0 for i in range(len(matrix))]

	if(meth.ch):

		alpha = [ [matrix[i][j]/matrix[i][i] for j in range(len(matrix))] for i in range(len(matrix))]
		for i in range(len(matrix)):
			alpha[i][i] = 0
		beta = [b[i]/matrix[i][i] for i in range(len(b))]
	else:
		alpha = [ r[:] for r in matrix]
		beta = b[:]

	count = 1
	x = meth.func(alpha, beta, x_prev, meth.w)
	while(abs(sum([abs(i) for i in plus(mul(x,-1), x_prev)])) >= epsilon):
		x_prev = x
		x = meth.func(alpha,beta,x_prev, meth.w)
		# print(count,x)
		# print(count,x)
		count +=1
	print('Count:',count)
	return x

eps = 1e-3

grad = Method(grad_spusk, False)
simpl = Method(simple_iter_calculate_x)
zedal = Method(zaiendal_calculate_x)
relax = Method(relax_calculate_x, w = 1)
richard = Method(Richardson,False, w = 7)

# x = solve(matrix, b, eps, zedal)

x = solve(matrix, b, eps, richard)
print('X', x)
check_x(matrix,b,x)