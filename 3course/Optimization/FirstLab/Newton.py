import random

n = 4

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

def dot(A,B = None):
	a,b = None, None
	if(B == None):
		B = A

	if(type(A) != list or type(B) != list):
		print("Not list")
		return None

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
		if(len(temp) == 1 and len(temp[0]) == 1):
			temp = temp[0][0]
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
		l[i][i] = random.randint(1,5)

	for i in range(1, n):
		for j in range(i):
			l[i][j] = random.randint(-5,5)
	a = dot(l, transpose(l))

	b = [[random.randint(-5,5) for i in range(n)]]
	return [a,b]

def func(x,a,b):
	return 0.5 * dot(dot(transpose(x),a),x) + dot(b,x)

def dfunc(x,a,b):
	return transpose(plus(transpose(dot(a,x)),b))

def ddfunc(x,a,b):
	return a

def newtons_method(x,a,b):
	return plus(x, mul(dot(inv(ddfunc(x,a,b)), dfunc(x,a,b)) ,-1))

def grad_method(x,a,b,step = 0.1):
	iters = 0
	xn = [r[:] for r in x]
	while(step > 0.001):
		iters += 1
		start = func(xn,a,b)
		d = dfunc(xn,a,b)
		right  = mul(d ,-step)
		xn = plus(xn, right)
		end = func(xn,a,b)
		if(start < end):
			step /= 10
	print(iters)
	return xn

a, b = pre_generate()

# a = [
# 	[49, -56, 28],
# 	[-56, 164, 18],
# 	[28, 18, 122]
# ]
# b = [[-8, 1, 3]]
print("A")
for i in a:
	print(i)
print()
print("B",b)
print()

print("Newton")
xn = [[0] for i in range(n)]
print("x",xn)
min_of_func_n = func(xn, a, b)
print("f",min_of_func_n)
xn = newtons_method(xn, a, b)
print("Newton x",xn)
min_of_func_n = func(xn, a, b)
print("Newton f",min_of_func_n)
print()

print("Grad from zero")
xg = [[0] for i in range(n)]
print("x",xg)
min_of_func_g = func(xg, a, b)
print("f",min_of_func_g)
xg = grad_method(xg, a, b)
print("Grad x",xg)
min_of_func_g = func(xg, a, b)
print("Grad f",min_of_func_g)
print()

print("Grad from rand")
xr = [[random.randint(-100, 100)]for i in range(n)]
print("x",xr)
min_of_func_r = func(xr, a, b)
print("f",min_of_func_r)
xr = grad_method(xr , a, b)
print("Grad rand x",xg)
min_of_func_g = func(xg, a, b)
print("Grad rand f",min_of_func_g)
print()
