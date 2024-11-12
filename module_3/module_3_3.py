def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [23, 'boss', (12, 23.45, 'cheat')]
values_dict = {'a': 34, 'b': 'Phillip', 'c': [1, 2, 5]}

values_list2 = [56.17, 'John']


print_params()
print_params(a=12)
print_params(a=True, b=17)
print_params(a=45.34, b='cdr', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)

