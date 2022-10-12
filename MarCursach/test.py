import music_finder
from help import validate

# ht, bintree, janr_matrix = music_finder.init('file1.csv', 'file2.csv')
# ht, bt = music_finder.init('file1.csv', 'file2.csv')

# login = 'admin'
# password = '123'

ct = music_finder.Cartoteca('file1.csv', 'file2.csv')

# #Сохраняет файлы
# music_finder.rewrite_files(ct,'file1.csv', 'file2.csv')

# ct.ht.add(['Valerchik','16','0'])
# ct.ht.delete(['Valerchik','16','0'])

# ct.bt.add(['ABKdw','BIeh','smt','Блюз'])# Добавить в бинарное дерево
# print(ct.bt.to_str())

# ct.bt.delete(['ABKdw','BIeh','smt','Блюз'])
# print(ct.bt.to_str())


# ct.bt.add_list([
# 						['ABKdw','BIeh','smt','AE'],
# 						['Chpok','BIeh','smt','AYE']
# 					])# Добавить в бинарное дерево

# print(['ABKdw','BIeh','YZm','AE'] in ct.find(29, 'AE'))
# ct.bt.delete(['ABKdw','BIeh','YZm','Aboba'])# Удалить из бинарного дерева
# print(['ABKdw','BIeh','YZm','AE'] in ct.find(29, 'AE'))
print(ct.find(23, 'Детские песни'))

# print(validate(''))
# print(validate(' '))
# print(validate(' Jora'))
# print(validate('Jora'))
# print(validate('Jora1'))

# print(ct.bt.ltr(ct.bt.janrs))