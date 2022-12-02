# y_prev = p_prev*y + q_prev

	# => y = (y_prev - q_prqv)/p_prev


# p = (c)/(a*p_prev + b)
# q = (a*q_prev - f)/(b - a*p_prev)

# p1 = c1/b1
# q1 = -f1/b1


# y_n = (f_n - q_prev*a)/(-b + p_prev*a)

# y_div2 = (y_prev - 2 * y + y_next)/h**2

import numpy as np
from numpy.linalg import solve

#Task
# y'' + p(x)y' + q(x)y = f(x)
# a_1*y(x_0) + b_1y'(x_0) = g_1
# a_n*y(x_n) + b_ny'(x_n) = g_n

# p = 2*sqrt(x + 1)
# q = -1/(sqrt(x + 1))
# f = -ln(x + 1)/(sqrt(x + 1)) + 2

# a1 = 1
# b1 = 0
# g1 = 0
	# => y(x_0) = 0 => y(0) = 0

# aN = 1
# bN = 0
# gN = 0.98025
	# => y(x_1) = 0.98025 => y(1) = 0.98025

# y_target = sqrt(x + 1) * ln(x + 1) = 0.98025

def a(h, p):
	return 1 - h/2*p

def b(h,q):
	return h**2*q - 2

def c(h, p):
	return 1 + h/2*p

def y_t(x):
	return np.sqrt(x + 1) * np.log(x + 1)

h = 0.1
r = [0,1]

count = int((r[1] - r[0])/h + 1)

x = np.arange(r[0],r[1] + h,h)
p = 2 * np.sqrt(x + 1)
q = -1/np.sqrt(x+1)
f = -np.log(x + 1)/np.sqrt(x + 1) + 2

y = np.zeros([int(count)])
y0 = 10
y1 = 20
y[0] = y0
y[-1] = y1


matrix = np.zeros([int(count),int(count)]) 
for i in range(count):
	if(i - 1 >= 0):
		matrix[i][i - 1] = a(h,p[i])
	matrix[i][i] = b(h,q[i])
	if(i + 1 < count):
		matrix[i][i + 1] = c(h,p[i])
# print(matrix)
print(solve(matrix, f))
print(y_t(x))