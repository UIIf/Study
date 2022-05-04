from matrix import *

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

matrix = [
	[16, 2, 1, -2],
	[4, 20, 1, 5],
	[2, 1, 10, 3],
	[-4, 7, 4, 32]
]
b = [-13,24,7,2]
# matrix = [
# 	[10,2,1],
# 	[1,10,2],
# 	[1,1,10]
# ]
# b = [10,12,8]

def simple_iter_calculate_x(alpha,beta,x,w):
	return plus(beta,mul(transpose(dot(alpha,x))[0],-1))

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
	# return new_x

def solve(matrix, b, epsilon, func = simple_iter_calculate_x, w = 1):
	x_prev = [0 for i in range(len(matrix))]
	alpha = [ [matrix[i][j]/matrix[i][i] for j in range(len(matrix))] for i in range(len(matrix))]
	for i in range(len(matrix)):
		alpha[i][i] = 0
	beta = [b[i]/matrix[i][i] for i in range(len(b))]
	count = 1
	x = func(alpha,beta,x_prev,w)
	# print("B", beta)
	# print("A")
	# for i in alpha:
	# 	print(i)
	print()
	while(vector_norm_1(plus(mul(x,-1), x_prev)) >= epsilon):
		x_prev = x
		x = func(alpha,beta,x_prev,w)
		# print(count,x)
		count +=1
	print(count)
	return x

# x = solve(matrix,b,10**(-10), simple_iter_calculate_x)
# print(x)
# check_x(matrix,b,x)
# x = solve(matrix,b,10**(-10), zaiendal_calculate_x)
# print(x)
# check_x(matrix,b,x)
# x = solve(matrix,b,10**(-10), relax_calculate_x, 0.95)
# print(x)
# check_x(matrix,b,x)
# for i in range(0, 20):
# 	solve(matrix,b,10**(-10), relax_calculate_x, i/10)

print(grad_spusk(matrix,b,[0 for i in b], 0))
x = solve(matrix,b,10**(-3), grad_spusk)
print(x)
check_x(matrix,b,x)