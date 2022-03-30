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

matrix = [
	[0.411,  0.421, -0.333,  0.313, -0.141, -0.381 , 0.245],
	[0.241,  0.705,  0.139, -0.409,  0.321,  0.0625, 0.101],
	[0.123, -0.239,  0.502,  0.901,  0.243,  0.819 , 0.321],
	[0.413,  0.309,  0.801,  0.865,  0.423,  0.118 , 0.183],
	[0.241, -0.221, -0.243,  0.134,  1.274,  0.712 , 0.423],
	[0.281,  0.525,  0.719,  0.118, -0.974,  0.808 , 0.923],
	[0.246, -0.301,  0.231,  0.813, -0.702,  1.223 , 1.105]
]

b = [0.096, 1.252, 1.024, 1.023, 1.155, 1.937, 1.673]

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

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

def find_result(l,u,b):
	y = [0 for i in u]
	#Для каждой строки
	for i in range(len(u)):
		y[i] = b[i] - sum([l[i][p]*y[p] for p in range(i)])

	x = y[:]
	n = len(u) - 1

	for i in range(len(u)):
		x[n - i] = (y[n-i] - sum([u[n-i][n-p]*x[n-p] for p in range(i)]))/u[n - i][n - i]
	return x

def check_x(matrix,b,x):
	print("Check")
	for index in range(len(matrix)):
		temp = 0
		for cel_index in range(len(matrix[index])):
			temp += x[cel_index] * matrix[index][cel_index]
		print("D", abs(temp - b[index]))

u, l = generate_l_u(matrix)

print("A")
for i in matrix:
	print(i)
print("L")
for i in l:
	print(i)
print("U")
for i in u:
	print(i)
print("X")
x = find_result(l,u,b)
print(x)

check_x(matrix,b,x)