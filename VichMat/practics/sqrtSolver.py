from matrix import *
import math

def generate_s(matrix):
	s = [[0]*len(r) for r in matrix]

	# #Первая формула
	# s[0][0] = math.sqrt(matrix[0][0])

	# #Вторая формула
	# for i in range(len(s)):
	# 	s[0][i] = matrix[0][i]/s[0][0]

	for i in range(len(s)):
		#Третья формула
		s[i][i] = math.sqrt(matrix[i][i] - sum([s[k][i]**2 for k in range(i)]))
		#Четвертая формула
		for j in range(i, len(s)):
			s[i][j] = (matrix[i][j] - sum([s[k][i]*s[k][j] for k in range(i)]))/s[i][i]
