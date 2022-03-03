matrix = [
	[1,2,1,4,13],
	[2,0,4,3,28],
	[4,2,2,1,20],
	[-3,1,3,2,6]
]

# matrix = [
# 	[2.1,-4.5,-2.0,19.07],
# 	[3.,2.5,4.3,3.21],
# 	[-6,3.5,2.5,-18.25]
# ]

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

def gaus(matrix):

	if(len(matrix) != len(matrix[0]) - 1):
		return []
	
	m = [i[:] for i in matrix]

	N = [i for i in range(len(m))]#Индексы не использованных столбцов
	diag_matrix = []
	ret_x = [0 for i in range(len(m))]

	while(len(N) > 0):
		x = N[0]
		y = 0
		matrix_max = m[y][x]

		for i in N:

			col = [abs(m[j][i]) for j in range(len(m))]
			temp_max = max(col)

			if(temp_max == 0):
				print(cringe)
				return []

			if(matrix_max < temp_max):
				matrix_max = temp_max
				x = i
				y = col.index(temp_max)

		temp_row = m.pop(y)
		temp_row =[j/temp_row[x] for j in temp_row]
		for row in m:
			mult = row[x]
			for j in range(len(row)):
				row[j] -= temp_row[j] * mult 

		diag_matrix.append([temp_row,x])
		N.remove(x)
	
	diag_matrix.reverse()

	for row in diag_matrix:
		temp_x = row[0][-1]
		for col_index in N:
			temp_x -= row[0][col_index] * ret_x[col_index]
		N.append(row[1])
		ret_x[row[1]] = temp_x

	return ret_x


def check_x(matrix,x):
	print("Check")
	for row in matrix:
		temp = 0
		for cel_index in range(len(row)-1):
			temp += x[cel_index] * row[cel_index]
		print(temp, row[-1])

x = gaus(matrix)
check_x(matrix,x)