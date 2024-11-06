
my_dict = {'Семен': 1999, 'Вадим': 2004, 'Карл': 2010, 'Ирина': 1975}
print('Dict:', my_dict)
print('Existing value:', my_dict['Вадим'])
print('Not existing value:', my_dict.get('Костя'))
my_dict['Клава'] = 1989
my_dict['Сима'] = 2005
print('Deleted value:', my_dict.pop('Карл'))
print('Modified dict:', my_dict)

my_set = {3, 3, 5, 'Бобик', '23', 23, 17, 17, (1, 2, 3), 23, 17, 'лист'}
print('Set:', my_set)
my_set.add(8)
my_set.add('прима')
my_set.discard(17)
print('Modified set:', my_set)
