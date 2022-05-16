def check_x(matrix,b,x):
	print("Check")
	for index in range(len(matrix)):
		temp = 0
		for cel_index in range(len(matrix[index])):
			temp += x[cel_index] * matrix[index][cel_index]
		print("D", abs(temp - b[index]))

def transpose(m):

	if(type(m[0]) != list):
		temp = [[i for i in m]]

	else:
		if(len(m[0]) == 1):
			temp = [[r[0] for r in m]]
		else:
			temp = [[ 0 for i in range(len(m))] for j in range(len(m[0]))]
			for i in range(len(m)):
				for j in range(len(m[0])):
					temp[j][i] = m[i][j]

	return temp

def dot(A,B = None):
	a,b = None, None
	if(B == None):
		B = A

	if(type(A) != list and type(B) != list):
		return A*B

	if(type(A) != list or type(B) != list):
		if(type(A) != list):
			return mul(B,A)
		else:
			return mul(A,B)

	if(type(A[0]) != list and type(B[0]) != list):
		a = transpose(A)
		b = transpose(transpose(B))

	elif(type(A[0]) != list):
		if(len(A) == len(B)):
			a = transpose(A)
		elif(len(B) == 1):
			a = transpose(transpose(A))
		else:
			return None

	elif(type(B[0]) != list):
		if(len(A[0]) == len(B)):
			b = transpose(transpose(B))
		elif(len(A[0]) == 1):
			b = transpose(B)
		else:
			return None

	if(a == None):
		a = [r[:] for r in A]
	if(b == None):
		b = [r[:] for r in B]

	if(len(a[0]) == len(b)):
		temp = [[0 for j in range(len(b[0]))] for i in range(len(a))]
		for i in range(len(a)):
			for j in range(len(b[0])):
				temp[i][j] = sum([a[i][k] * b[k][j] for k in range(len(b))])
		# if(len(temp) == 1 and len(temp[0]) == 1):
		# 	temp = temp[0][0]
		return temp
	else:
		print("lens not eq", len(a[0]), len(b))
		return None

def det(a):
	if(type(a[0]) != list or len(a) != len(a[0])):
		return None
	if(len(a) == 2):
		return a[0][0] * a[1][1] - a[0][1]*a[1][0]
	elif(len(a) == 3):
		sum = 0
		for i in range(3):
			p = 1
			m = 1
			for j in range(3):
				p *= a[(i + j)%3][j]
				m *= a[(i + j)%3][2-j]
			sum += p
			sum -= m
		return sum
	else:
		sum = 0
		for i in range(len(a)):
			sum += (-1)**i * a[0][i]*det(minor(a,i,0))
		return sum

def minor(a,x,y):
	to_ret = []
	for r in a:
		temp = r[:]
		temp.pop(x)
		to_ret += [temp]
	to_ret.pop(y)
	return to_ret

def main_minor(a,x):
	if(len(a) >= x and len(a[0]) >= x):
		return [ [a[i][j] for j in range(x)] for i in range(x)]
	return None


def mul(m,a):
	if(type(m) != list):
		return None

	if(type(m) == list and type(m[0]) != list):
		temp = [r*a for r in m]

	elif(type(m[0][0]) != list):
		temp = [r[:] for r in m]
		for i in range(len(temp)):
			for j in range(len(temp[0])):
				temp[i][j] *= a

	return temp

def plus(a,b):
	if(type(a) != list or type(b) != list or (type(a[0]) != list and type(b[0]) == list) or (type(a[0]) == list and type(b[0]) != list)):
		return None

	if(type(a[0]) == list and type(b[0]) == list):
		if(len(a) == len(b) and len(a[0]) == len(b[0])):
			temp = [[0 for j in range(len(a[0]))] for i in range(len(a))]

		for i in range(len(a)):
			for j in range(len(a[0])):
				temp[i][j] = a[i][j] + b[i][j]
	elif(len(a) == len(b)):
		temp = a[:]
		for i in range(len(a)):
			temp[i] = a[i]+b[i]

	return temp

def inv(a):
	c = [r[:] for r in a]
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[i][j] = (-1)**(i + j)*det(minor(a,j,i))
	return mul(transpose(c),1/det(a))

def inv_rec(matrix):
	prev_inv = [[1/matrix[0][0]]]
	counter = 1
	while(len(prev_inv) < len(matrix)):
		counter += 1
		temp_m = main_minor(matrix,counter)
		v = [temp_m[counter-1][:-1]]
		u = [ [temp_m[i][counter-1]] for i in range(counter-1)]

		alpha = 1/(temp_m[counter-1][counter-1] - dot(dot(v,prev_inv),u)[0][0])
		Pn = plus(prev_inv,mul(dot(dot(dot(prev_inv,u),v),prev_inv),alpha))
		rn = mul(dot(prev_inv,u), -alpha)
		qn = mul(dot(v,prev_inv), -alpha)

		prev_inv = Pn
		for i in range(len(rn)):
			prev_inv[i].append(rn[i][0])
		qn[0].append(alpha)
		prev_inv.append(qn[0])
	return prev_inv

def ones(s):
	I = [[0]*s for i in range(s)]
	for i in range(s):
		I[i][i] = 1
	return I

def solve_triangle(A,B):
	if(len(A) != len(B)):
		return None
	a = [a[:] for a in A]
	a.reverse()
	[r.reverse() for r in a]
	b = B[:]
	b.reverse()
	x = ([0]*len(b))
	x.reverse()
	for i in range(len(a)):
		for j in range(i):
			b[i] -= a[i][j]*x[j]
		x[i] = b[i]/a[i][i]
		# print("x", x)
	x.reverse()
	return x 

def vector_norm_1(vec):
	if(len(vec) == 2):
		if(len(vec[0]) == 1):
			vec = [i[0] for i in vec]
		else:
			vec = vec[0]
	return sum([abs(x) for x in vec])



	#---------------------------------------------------------------------
	#Собственные значения матрицы

def sgn(num):
	return 1 if num > 0 else -1

def find_max_nd_ind(matrix):
	mi, mj = 0,1
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if(i != j and abs(matrix[i][j]) > abs(matrix[mi][mj])):
				mi, mj = i, j
	return [mi, mj]

def find_max_diag_ind(matrix):
	mi = 0
	for i in range(1, len(matrix)):
		if(matrix[i][i] > matrix[mi][mi]):
			mi = i
	return mi

def self_mean_method_sim(matrix, p):
	tau = [10**(-(i+1)) for i in range(p)]

	matrix = [r[:] for r in matrix]
	counter = 0
	for p in tau:
		i, j = find_max_nd_ind(matrix)

		diag_i = find_max_diag_ind(matrix)
		while(abs(matrix[i][j]) >= p): #abs(matrix[diag_i][diag_i])**0.5 * 
			d = ((matrix[i][i] - matrix[j][j])**2 + 4*(matrix[i][j])**2)**0.5
			c = (0.5*( 1 + abs(matrix[i][i] - matrix[j][j])/d))**0.5
			s = sgn(matrix[i][j]*(matrix[i][i] - matrix[j][j])) * (0.5*(1 - abs(matrix[i][i] - matrix[j][j])/d))**0.5

			new_m = [ r[:] for r in matrix]

			new_m[i][j], new_m[j][i] = 0, 0

			for k in range(len(matrix)):
				if(k == i or k == j):
					continue
				new_m[i][k] = c * matrix[k][i] + s* matrix[k][j]
				new_m[k][i] = new_m[i][k]

				new_m[j][k] = -s * matrix[k][i] + c* matrix[k][j]
				new_m[k][j] = new_m[j][k]
			
			new_m[i][i] = c *  c * matrix[i][i] + 2 * c*s * matrix[i][j] + s*s *matrix[j][j]

			new_m[j][j] = s * s * matrix[i][i] - 2 * c * s * matrix[i][j] + c * c * matrix[j][j]

			matrix = new_m

			i, j = find_max_nd_ind(matrix)
			diag_i = find_max_diag_ind(matrix)
			counter += 1
	# print(counter)
	return [matrix[i][i] for i in range(len(matrix))]

	#/Собственные значения матрицы
	#---------------------------------------------------------------------