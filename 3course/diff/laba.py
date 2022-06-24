from math import sin, cos, pi,exp
from matplotlib import pyplot as plt

def f(t):
	return exp(-(t*t))/t

def int_cos(t,w):
	return cos(2 * pi*w*t)

def int_sin(t,w):
	return sin(2 * pi*w*t)

def integral(f, x, func, w):
	return(sum([ f(i)*func(i, w)*(x[-1] - x[0])/len(x) for i in x]))

b = 3

h1 = 1000
h2 = 1000

a = 3/h1	
find_m = int(3e+6)

x = [ (i/h1)*(b-a) + a for i in range(h1) ]

m = 1
new_x = [i/h2*m  for i in range(h2)]
new_y = [ [integral(f, x, int_cos, i), integral(f, x, int_sin, i)] for i in new_x]

plt.plot(new_x, new_y)
plt.legend('cos','sin')
plt.show()