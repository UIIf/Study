# matrix = [
# 	[1,2,1,4,13],
# 	[2,0,4,3,28],
# 	[4,2,2,1,20],
# 	[-3,1,3,2,6]
# ]

matrix = [
	[2.1,-4.5,-2.0,19.07],
	[3.,2.5,4.3,3.21],
	[-6,3.5,2.5,-18.25]
]

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


def check_x(matrix,x):
	print("Check")
	for row in matrix:
		temp = 0
		for cel_index in range(len(row)-1):
			temp += x[cel_index] * row[cel_index]
		print(temp, row[-1])

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
	# [print(i) for i in m]
	# print("\n")

	for step in range(len(matrix)):
		for sub_step in range(step):
			subtract_rows(m[step], m[sub_step], sub_step)
		devide_row(m[step],m[step][step])

		for sub_step in range(step):
			subtract_rows(m[sub_step], m[step], step)
		# [print(i) for i in m]
		# print("\n")
	x = [i[-1] for i in m]
	return x



temp = rect_method(matrix)

check_x(matrix,temp)

