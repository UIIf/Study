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
	[10,2,1],
	[1,10,2],
	[1,1,10]
]
b = [10,12,8]

def simple_iter_calculate_x(alpha,beta,x):
	return plus(beta,mul(transpose(dot(alpha,x))[0],-1))

def zaenbal_calculate_x(alpha,beta,x):
	x = x[:]
	for i in range(len(x)):
		x[i] = beta[i]
		for j in range(len(x)):
			if(j != i):
				x[i] -= alpha[i][j]*x[j]
	return x

def solve(matrix, b, epsilon, func = simple_iter_calculate_x):
	x_prev = [0 for i in range(len(matrix))]
	alpha = [ [matrix[i][j]/matrix[i][i] for j in range(len(matrix))] for i in range(len(matrix))]
	for i in range(len(matrix)):
		alpha[i][i] = 0
	beta = [b[i]/matrix[i][i] for i in range(len(b))]
	count = 1
	x = func(alpha,beta,x_prev)
	print("B", beta)
	print("A")
	for i in alpha:
		print(i)
	print()
	while(vector_norm_1(plus(mul(x,-1), x_prev)) >= epsilon):
		x_prev = x
		x = func(alpha,beta,x_prev)
		print(x)
		count +=1
	print(count)
	return x

x = solve(matrix,b,0.0001, zaenbal_calculate_x)
print(x)
check_x(matrix,b,x)