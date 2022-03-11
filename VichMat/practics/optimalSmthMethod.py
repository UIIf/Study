# matrix = [
# 	[1,2,1,4,13],
# 	[2,0,4,3,28],
# 	[4,2,2,1,20],
# 	[-3,1,3,2,6]
# ]

# matrix = [
# 	[2.1,-4.5,-2.0,19.07],
# 	[3.,2.5,4.3,3.21],
# 	[-6,3.5,2.5,-18.25]
# ]

# matrix = [
# 	[5, 2, 3, 3],
# 	[1, 6, 1, 5],
# 	[3, -4, -2, 8]
# ]

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

# matrix = [
# 	[1, 2, 3, 5],
# 	[4, 5, 6, 8],
# 	[7, 8, 0, 2]
# ]

# l = [
# 	[1, 0, 0],
# 	[4,1,0],
# 	[7,2,1]
# ]
# u = [
# 	[1,2,3],
# 	[0,-3,-6],
# 	[0,0,-9]
# ]

matrix = [
	[0.411,  0.421, -0.333,  0.313, -0.141, -0.381 , 0.245, 0.096],
	[0.241,  0.705,  0.139, -0.409,  0.321,  0.0625, 0.101, 1.252],
	[0.123, -0.239,  0.502,  0.901,  0.243,  0.819 , 0.321, 1.024],
	[0.413,  0.309,  0.801,  0.865,  0.423,  0.118 , 0.183, 1.023],
	[0.241, -0.221, -0.243,  0.134,  1.274,  0.712 , 0.423, 1.155],
	[0.281,  0.525,  0.719,  0.118, -0.974,  0.808 , 0.923, 1.937],
	[0.246, -0.301,  0.231,  0.813, -0.702,  1.223 , 1.105, 1.673]
]


def check_x(matrix,x):
	print("Check")
	for row in matrix:
		temp = 0
		for cel_index in range(len(row)-1):
			temp += x[cel_index] * row[cel_index]
		print("D", abs(temp - row[-1]))

def subtract_rows(a,b,index):
	mul = a[index]
	for i in range(len(a)):
		a[i] -= b[i]*mul

def devide_row(row, mul):
	for i in range(len(row)):
		row[i] /= mul

def rect_method(matrix):
	if(len(matrix) != len(matrix[0]) - 1):
		return []
	
	m = [i[:] for i in matrix]
	[print(i) for i in m]
	print("\n")

	for step in range(len(matrix)):
		for sub_step in range(step):
			subtract_rows(m[step], m[sub_step], sub_step)
		devide_row(m[step],m[step][step])

		for sub_step in range(step):
			subtract_rows(m[sub_step], m[step], step)
		[print(i) for i in m]
		print("\n")
	x = [i[-1] for i in m]
	return x



temp = rect_method(matrix)
print(temp)
check_x(matrix,temp)

