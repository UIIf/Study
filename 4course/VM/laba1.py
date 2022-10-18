# y_prev = p_prev*y + q_prev

# p = (c)/(a*p_prev + b)
# q = (a*q_prev - f)/(b - a*p_prev)

# p1 = c1/b1
# q1 = -f1/b1


# y_n = (f_n - q_prev*a)/(-b + p_prev*a)

# y_div2 = (y_prev - 2 * y + y_next)/h**2

import numpy as np

#Task
# y'' + p(x)y' + q(x)y = f(x)
# a_0*y(x_0) + b_0y'(x_0) = g_0
# a_n*y(x_n) + b_ny'(x_n) = g_1

# p = 2*sqrt(x + 1)
# q = -1/(sqrt(x + 1))
# f = -ln(x + 1)/(sqrt(x + 1)) + 2

# a0 = 1
# b0 = 0
# g0 = 0

# aN = 1
# bN = 0
# g1 = 0.98025

# y_target = sqrt(x + 1) * ln(x + 1)

h = 0.1
r = [0,1]

count = (r[1] - r[0])/h
print(count)

y = np.zeros([int(count)])
f = np.zeros([int(count)])
y0 = 10
y1 = 20
y[0] = y0
y[-1] = y1
print(y)

matrix = np.zeros([int(count),int(count)])
print(matrix)