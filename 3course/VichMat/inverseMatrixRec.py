from matrix import *

matrix = [
	[2.2,4,-3,1.5,0.6,2,0.7],
	[4,3.2,1.5,-0.7,-0.8,3,1],
	[-3,1.5,1.8,0.9,3,2,2],
	[1.5,-0.7,0.9,2.2,4,3,1],
	[0.6,-0.8,3,4,3.2,0.6,0.7],
	[2,3,2,3,0.6,2.2,4],
	[0.7,1,2,1,0.7,4,3.2]
]
b = [3.2, 4.3, 0.1, 3.5, 5.3, 9, 3.7]

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
temp = dot(matrix,rev)
for i in temp:
	print([int(j*1000)/1000 for j in i])
x = [i[0] for i in dot(rev,b)]
print(x)
check_x(matrix,b,x)