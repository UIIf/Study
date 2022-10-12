from help import *
from math import log2, ceil


class hash_table:
	def __init__(self, hash_func, f_name = None):
		self.func = hash_func
		self.table = None
		self.offset = 0

		if not(f_name is None):
			self.read_from_file(f_name)

	def read_from_file(self, f_name):
		f = open(f_name, mode ='r', encoding = 'utf-8')

		f_lines = f.readlines()

		f_lines = [line[:-1].split(',') for line in f_lines]
		f.close()

		self.fit(f_lines)


	def fit(self, matrix):
		hashes = [self.func(line) for line in matrix]
		self.offset = min(hashes)

		self.table = [[] for i in range(self.offset, max(hashes) + 1)]

		for i in range(len(hashes)):
			self.table[hashes[i] - self.offset] += [matrix[i]]


	def find_by_hash(self, hash):
		return self.table[hash - self.offset][:]


	def add(self, new_val):
		hash_val = self.func(new_val)
		if(hash_val < self.offset):
			self.table = [[] for i in range(self.offset - hash_val)] + self.table
			self.offset = hash_val
		elif (hash_val > self.offset + len(self.table) - 1):
			self.table = self.table + [[] for i in range(hash_val - (self.offset + len(self.table) - 1))]
		self.table[hash_val - self.offset] += [new_val]

	def delete(self, val):
		ind = self.func(val) - self.offset
		try:
			self.table[ind].remove(val)
		except:
			pass

	def to_str(self):
		ret = ''
		for row in self.table:
			if(len(row) > 0):
				ret += '\n'.join([','.join(el) for el in row]) + '\n'
		return ret


class bintree:
	def __init__(self, func, file_name = None):
		self.bintree = None
		self.func = func
		self.janrs = None
		if not(file_name is None):
			self.read_from_file(file_name)

	def create_bt(self, data):
		tree = [[]]*len(data)
		indexes = self.ltr(range(len(data)))
		for i in range(len(indexes)):
			tree[indexes[i]] = data[i]
		return tree

	def read_from_file(self, f_name):
		f = open(f_name, mode ='r', encoding = 'utf-8')

		f_lines = f.readlines()

		f_lines = [line[:-1].split(',') for line in f_lines]

		all_janres = [self.func(line) for line in f_lines]

		janrs = []

		for janr in all_janres:
			if not(janr in janrs):
				janrs +=[janr]

		self.janrs = self.create_bt(q_sort(janrs, lambda x: x))

		f.close()

		self.fit(f_lines)


	def find_ind_in_bintree(self, val, cur_ind = 0):

		if cur_ind >= len(self.janrs):
			return None

		if(val == self.janrs[cur_ind]):
			return cur_ind
		elif (val < self.janrs[cur_ind]):
			return self.find_ind_in_bintree(val, cur_ind*2 + 1)
		else:
			return self.find_ind_in_bintree(val, cur_ind*2 + 2)

	def ltr(self, arr, ind = 0):
		if(ind >= len(arr)):
			return []
		return self.ltr(arr, ind*2 + 1) + [arr[ind]] +  self.ltr(arr, ind*2 + 2)


	def fit(self, matrix):
		self.bintree = [[] for i in self.janrs]
		for i in matrix:
			ind = self.find_ind_in_bintree(self.func(i))
			if not(ind is None):
				self.bintree[ind] += [i]

	
	def add(self, new_val):
		jr = self.func(new_val)
		jr_ind = self.find_ind_in_bintree(jr)
		# Если нет такого жанра
		if(jr_ind is None):
			
			janrs = self.create_bt(q_sort(self.janrs + [jr], lambda x: x))
			bt = []
			for janr in janrs:
				jr_ind = self.find_ind_in_bintree(janr)
				if(jr_ind is None):
					bt +=[[new_val]]
				else:
					bt += [self.bintree[jr_ind]]
			self.bintree = bt
			self.janrs = janrs
		
		else:
			self.bintree[jr_ind] += [new_val]
			

	def delete(self, val):
		jr = self.func(val)
		jr_ind = self.find_ind_in_bintree(jr)
		if(jr_ind is None):
			return None
		else:
			
			self.bintree[jr_ind].remove(val)

			if(len(self.bintree[jr_ind]) <= 0):
				
				del self.bintree[jr_ind]
				del self.janrs[jr_ind]

				janrs = self.janrs[:]

				self.janrs = self.create_bt(q_sort(self.janrs, lambda x: x))
				bt = []
				# print(janrs)

				# for i in range(len(self.janrs)):
				# 	print(self.janrs[i], len(self.bintree[i]))
				for janr in janrs:
					if(janr in self.janrs):
						jr_ind = self.find_ind_in_bintree(janr)
						bt += [self.bintree[jr_ind]]

				self.bintree = bt
				self.janrs = janrs
		return True


	def to_str(self):
		ret = ''
		for row in self.bintree:
			ret += '\n'.join([','.join(el) for el in row]) + '\n'
		return ret


class Cartoteca:

	def __init__(self, file_client, file_music):
		self.ht = hash_table(lambda x: int(x[1]), file_client) 
		self.bt = bintree(lambda x: x[3], file_music)

	def rewrite_files(file_client, file_music):
		f1 = open(file_client, mode ='w', encoding = 'utf-8')
		f2 = open(file_music, mode ='w', encoding = 'utf-8')

		f1.write(self.ht.to_str())
		f2.write(self.bintree.to_str())

		f1.close()
		f2.close()

	def find(self, age, janr):
		in_age = self.ht.find_by_hash(age)[:]
		names = [i[0] for i in in_age]
		ind = self.bt.find_ind_in_bintree(janr)
		if not(ind is None):
			in_janr = self.bt.bintree[ind]
			return [i for i in in_janr if i[0] in names]
		return None
