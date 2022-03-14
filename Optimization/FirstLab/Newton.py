import random

n = 6

def transpose(m):

	if(type(m[0]) != list):
		temp = [[i] for i in m]

	else:
		if(len(m[0]) == 1):
			temp = [[r[0] for r in m]]
		else:
			temp = [[ 0 for i in range(len(m))] for j in range(len(m[0]))]
			for i in range(len(m)):
				for j in range(len(m[0])):
					temp[j][i] = m[i][j]

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
	c = [r[:] for r in a]
	for i in range(len(a)):
		for j in range(len(a[0])):
			c[i][j] = (-1)**(i + j)*det(minor(a,j,i))
	return mul(transpose(c),1/det(a))

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

for i in a:
	print(i)
print(" ")
print(b)
print()
x = newtons_method([[0] for i in range(n)], a, b)
print(x)
min_of_func = func(x, a, b)
print(min_of_func)
#Near
print("near point")
x = plus(x, [[0.001] for i in range(n)])
other_func = func(x, a, b)
print(other_func)
print("is min:",other_func > min_of_func)