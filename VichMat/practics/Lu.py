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

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 0]
]

b = [5, 8, 2]

# matrix = [
# 	[1,-1,5],
# 	[2,1,-7]
# ]

def generate_l_u(matrix):
	u = [[0]*len(r) for r in matrix]
	l = [[0]*len(r) for r in matrix]

	u[0] = matrix[0][:]

	for i in range(len(matrix)):
		l[i][0] = matrix[i][0]/matrix[0][0]

	

	for i in range(1, len(matrix)):
		for j in range(i, len(matrix)):
			
			temp = [l[i][k] * u[k][j] for k in range(i)]
			print("u", matrix[i][j],temp)
			u[i][j] = matrix[i][j] - sum(temp)

			temp = [l[j][k] * u[k][i] for k in range(i)]
			print("l",i,j,matrix[j][i],temp)
			l[j][i] = (matrix[j][i] - sum(temp))/u[i][i]


	return [u,l]

u, l = generate_l_u(matrix)

for i in u:
	print(i)
print("")
for i in l:
	print(i)