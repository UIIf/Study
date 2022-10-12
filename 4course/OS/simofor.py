# Импортируем зависимости
from time import sleep
import random
from threading import Thread

# Создание класса семафора
class Semaphore():

	# Инициализация
	def __init__(self, count = 5):
		# При неверном количестве ставится стандартное значение
		if(count<=0):
			self.count = 5
		else:
			self. count = count

	# Освобождение 
	def m(self):
		while(self. count <= 0):
			...
		self. count -= 1
		return self.count > 0

	# Захват
	def p(self):
		self.count += 1

# Создание общего семафора
sem = Semaphore(5)

# Создание семафора для печати
print_sim = Semaphore(1)

# Функция для проверки
def show(text):
	# Захват общего семафора
	sem.m()
	print_sim.m()
	print("Show start", text)
	print_sim.p()
	
	sleep(5)
	
	print_sim.m()
	print("Show end", text )
	print_sim.p()
	sem.p()

th1 = Thread(target = show, args = ('Thread1',))
th2 = Thread(target = show, args = ('Thread2',))
th3 = Thread(target = show, args = ('Thread3',))
th4 = Thread(target = show, args = ('Thread4',))
th5 = Thread(target = show, args = ('Thread5',))
th6 = Thread(target = show, args = ('Thread6',))


th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()

