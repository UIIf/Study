def new_a_b(matrix,j,kp):
	temp = matrix[kp][kp] - sum([matrix[i][kp] * matrix[kp][i] for i in range(kp - 1)])
	for i in range(kp-1):
		matrix[kp][j] = matrix[kp][j] - sum([matrix[i][j] * matrix[kp][i] for i in range(kp - 1)])/temp
	matrix[kp][-1] = matrix[kp][-1] - sum([matrix[i][-1] * matrix[kp][i] for i in range(kp-1)])/temp