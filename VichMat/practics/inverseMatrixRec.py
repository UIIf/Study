import matrix

def inverseRec(matrix):
	if len(matrix) == 1 and len(matrix[0]) == 1:
		return [[1/matrix[0][0]]]

	