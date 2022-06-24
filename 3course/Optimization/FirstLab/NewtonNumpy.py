import numpy as np
import random

n = 6

def pre_generate():
	l = np.zeros((n,n))
	for i in range(n):
		l[i][i] = random.randint(1, 100)
	for i in range(1,n):
		for j in range(i):
			l[i][j] = random.randint(-100, 100)
	b = np.array([random.randint(-100, 100) for i in range(n)])
	a = np.dot(l, np.transpose(l))
	return [a, b]

def func(x, a, b):
	return 0.5 * np.dot(np.dot(np.transpose(x),a),x) + np.dot(b,x)

def dfunc(x, a, b):
	return np.dot(a,x) + b

def newtons_method(x,a,b):
	return x - dot(inv(a), dfunc(x,a,b))

a,b = pre_generate()

x = np.zeros(n)

print(newtons_method(x,a,b))