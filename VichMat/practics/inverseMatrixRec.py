from matrix import *

matrix = [
	[10,2,1],
	[1,10,2],
	[1,1,10]
]
b = [10,12,8]

def inv_rec(matrix):
	prev_inv = [[1/matrix[0][0]]]
	counter = 1
	while(len(prev_inv) < len(matrix)):
		counter += 1
		temp_m = main_minor(matrix,counter)
		v = [temp_m[counter-1][:-1]]
		u = [ [temp_m[i][counter-1]] for i in range(counter-1)]
		# print('counter',counter)

		alpha = 1/(temp_m[counter-1][counter-1] - dot(dot(v,prev_inv),u)[0][0])
		Pn = plus(prev_inv,mul(dot(dot(dot(prev_inv,u),v),prev_inv),alpha))
		rn = mul(dot(prev_inv,u), -alpha)
		qn = mul(dot(v,prev_inv), -alpha)
		# print('Pn',Pn)
		# print('rn', rn)
		# print('qn', qn)
		prev_inv = Pn
		for i in range(len(rn)):
			prev_inv[i].append(rn[i][0])
		qn[0].append(alpha)
		prev_inv.append(qn[0])
	return prev_inv


rev = inv_rec(matrix)
x = [i[0] for i in dot(rev,b)]
print(x)
check_x(matrix,b,x)