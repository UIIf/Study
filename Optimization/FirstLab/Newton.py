import numpy as np
import random

n = 3

def transpose(m):
	if(type(m[0]) == list):
		if(len(m[0]) == 1):
			temp = [[r[0] for r in m]]
		else:
			temp = [[ 0 for i in range(len(m))] for j in range(len(m[0]))]
			for i in range(len(m)):
				for j in range(len(m[0])):
					temp[j][i] = m[i][j]
	else:
		temp = [[i] for i in m]

	return temp

def dot(a,b):

	if(type(a[0]) != list):
		a = [a]
		if(type(b[0]) != list and len(b) == 1):
			transpose(a)

	if(type(b[0]) != list):
		b = [b]
		if(len(a[0]) == 1):
			transpose(b)

	if(len(a[0]) == len(b)):
		temp = [[0 for j in range(len(b[0]))] for i in range(len(a))]
		for i in range(len(a)):
			for j in range(len(b[0])):
				temp[i][j] = sum([a[i][k] * b[k][j] for k in range(len(b))])
		if(len(temp) == 1 and len(temp[0]) == 1):
			temp = temp[0][0]
		return temp
	else:
		return None

def det(a):
	if(len(a) == len(a[0])):
		if(len(a) == 3):
			sum = 0
			for i in range(len(a)):
				p,m = 1,1
				for j in range(len(a)):
					p *= a[(i+j)%len(a)][j]
					m *= a[(i+j)%len(a)][len(a) - 1 - j]
				print(p,m)
				sum = sum + p - m
			return sum
		elif(len(a) == 2):
			return a[0][0] *a[1][1] - a[0][1]*a[1][0]
		else:
			sum = 0
			for i in range(len(a)):
				m = a[1:]
				#m = HELP 
				sum += a[0][i] * det()
	else:
		return None

def mul(m,a):
	temp = [r[:] for r in m]
	for i in range(len(temp)):
		for j in range(len(temp[0])):
			temp[i][j] *= a
	return temp

def plus(a,b):
	if(len(a) == len(b) and len(a[0]) == len(b[0])):
		temp = [[0 for j in range(len(a[0]))] for i in range(len(a))]

	for i in range(len(a)):
		for j in range(len(a[0])):
			temp[i][j] = a[i][j] + b[i][j]

	return temp

def inv(a):
	return mul(transpose(a),1/det(a))

def pre_generate():
	l = [ [0 for i in range(n)] for j in range(n)]
	for i in range(n):
		l[i][i] = random.randint(1,10)

	for i in range(1, n):
		for j in range(i):
			l[i][j] = random.randint(-10,10)
	a = dot(l, transpose(l))

	b = [[random.randint(-10,10) for i in range(n)]]
	return [a,b]

def func(x,a,b):
	return 0.5 * dot(dot(transpose(x),a),x) + dot(b,x)

def dfunc(x,a,b):
	return transpose(plus(transpose(dot(a,x)),b))

def ddfunc(x,a,b):
	return a

def newtons_method(x,a,b):
	return plus(x, mul(dot(inv(ddfunc(x,a,b)), dfunc(x,a,b)) ,-1))
	

a, b = pre_generate()

# one = transpose(a)
# two = np.transpose(a)
# # print(one, two)
# for i in one:
# 	print(i)
# print("")
# for i in two:
# 	print(i)
for i in a:
	print(i)
print(det(a))

# x = [[0] for i in range(n)]

# print(func(x,a,b))

# get = newtons_method(x,a,b)

# for i in get:
# 	print(i)
