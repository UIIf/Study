from math import sin, cos, pi
from matplotlib import pyplot as plt

def f(t):
	return sin(t)

def int_cos(t,w):
	return cos(2 * pi*w*t)

def int_sin(t,w):
	return sin(2 * pi*w*t)

def integral(f, x, func, w):
	return(sum([ f(i)*func(i, w)*(x[-1] - x[0])/len(x) for i in x]))

a = 0
b = pi

h1 = 100
h2 = 2000

m = 10
find_m = int(3e+6)

x = [ (i/h1)*(b-a) + a for i in range(h1 + 1) ]
ox = [((i - h2/2)/h2)*(2*b)  for i in range(h2 + 1)]
y = [ [integral(f, x, int_cos, i), integral(f, x, int_sin, i)] for i in ox]

step = 0.00001
eps = 0.00001
for i in range(1, find_m):
	if(
		abs(integral(f,x,int_cos,i*step) - integral(f,x,int_cos, -i*step)) < eps
		and
		abs(integral(f,x,int_sin,i*step) - integral(f,x,int_sin, -i*step)) < eps
		):
		print(
			abs(integral(f,x,int_cos,i*step) - integral(f,x,int_cos, -i*step)),
			abs(integral(f,x,int_sin,i*step) - integral(f,x,int_sin, -i*step))
			)
		m = i*step
		break
print(m)
new_x = [((i - h2/2)/h2)*(2*m)  for i in range(h2 + 1)]
new_y = [ [integral(f, x, int_cos, i), integral(f, x, int_sin, i)] for i in new_x]

plt.plot(new_x, new_y)
plt.show()